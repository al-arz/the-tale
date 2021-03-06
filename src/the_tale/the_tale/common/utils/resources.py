
import smart_imports

smart_imports.all()


class Resource(old_views.BaseResource):

    ERROR_TEMPLATE = 'error.html'
    DIALOG_ERROR_TEMPLATE = 'dialog_error.html'

    def __init__(self, request, *args, **kwargs):
        super(Resource, self).__init__(request, *args, **kwargs)

        self.account = self.request.user
        if self.account.is_authenticated:
            self.account = accounts_prototypes.AccountPrototype(model=self.account)

    def initialize(self, *args, **kwargs):
        super(Resource, self).initialize(*args, **kwargs)

        if self.account.is_authenticated and self.account.is_update_active_state_needed:
            amqp_environment.environment.workers.accounts_manager.cmd_run_account_method(account_id=self.account.id,
                                                                                         method_name=accounts_prototypes.AccountPrototype.update_active_state.__name__,
                                                                                         data={})

    def validate_account_argument(self, account_id):
        if self.account and self.account.id == int(account_id):
            return self.account

        return accounts_prototypes.AccountPrototype.get_by_id(account_id)
