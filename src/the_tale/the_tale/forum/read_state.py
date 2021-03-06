
import smart_imports

smart_imports.all()


class ReadState(object):

    def __init__(self, account):
        self._account = account

        # can not make lazy properties, since some read_infos can be created after this object was constructed
        self.subcategories_read_info = self.get_subcategories_read_info()
        self.threads_read_info = self.get_threads_read_info()

    def get_subcategories_read_info(self):
        if not self._account.is_authenticated:
            return {}

        return prototypes.SubCategoryReadInfoPrototype.get_subcategories_info(account_id=self._account.id)

    def get_threads_read_info(self):
        if not self._account.is_authenticated:
            return {}

        return prototypes.ThreadReadInfoPrototype.get_threads_info(account_id=self._account.id)

    @utils_decorators.lazy_property
    def threads_info(self):
        if not self._account.is_authenticated:
            return {}

        time_barrier = datetime.datetime.now() - datetime.timedelta(seconds=conf.settings.UNREAD_STATE_EXPIRE_TIME)

        return {thread.id: thread for thread in prototypes.ThreadPrototype.from_query(prototypes.ThreadPrototype._db_filter(updated_at__gt=time_barrier))}

    def thread_has_new_messages(self, thread):
        if not self._account.is_authenticated:
            return False

        if thread.updated_at + datetime.timedelta(seconds=conf.settings.UNREAD_STATE_EXPIRE_TIME) < datetime.datetime.now():
            return False

        thread_read_info = self.threads_read_info.get(thread.id)
        read_at = thread_read_info.read_at if thread_read_info else self._account.created_at

        subcategory_read_info = self.subcategories_read_info.get(thread.subcategory_id)

        if subcategory_read_info is not None:
            read_at = max(subcategory_read_info.all_read_at, read_at)

        return thread.updated_at > read_at

    def thread_is_new(self, thread):
        if not self._account.is_authenticated:
            return False

        if thread.author.id == self._account.id:
            return False

        if thread.created_at + datetime.timedelta(seconds=conf.settings.UNREAD_STATE_EXPIRE_TIME) < datetime.datetime.now():
            return False

        thread_read_info = self.threads_read_info.get(thread.id)
        read_at = thread_read_info.read_at if thread_read_info else self._account.created_at

        subcategory_read_info = self.subcategories_read_info.get(thread.subcategory_id)

        if subcategory_read_info is not None:
            read_at = max(subcategory_read_info.read_at, read_at)

        return thread.created_at > read_at

    def subcategory_has_new_messages(self, subcategory):

        if not self._account.is_authenticated:
            return False

        subcategory_read_info = self.subcategories_read_info.get(subcategory.id)

        if subcategory.updated_at + datetime.timedelta(seconds=conf.settings.UNREAD_STATE_EXPIRE_TIME) < datetime.datetime.now():
            return False

        if subcategory_read_info is None:
            return True

        return any(self.thread_has_new_messages(thread)
                   for thread in self.threads_info.values()
                   if thread.subcategory_id == subcategory.id)
