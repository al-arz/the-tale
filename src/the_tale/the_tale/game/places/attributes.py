
import smart_imports

smart_imports.all()


class Attributes(game_attributes.create_attributes_class(relations.ATTRIBUTE)):
    __slots__ = ()

    def sync_size(self, hours):

        self.goods += hours * self.production

        if self.goods >= c.PLACE_GOODS_TO_LEVEL:
            self.size += 1
            if self.size <= c.PLACE_MAX_SIZE:
                self.goods = int(c.PLACE_GOODS_TO_LEVEL * c.PLACE_GOODS_AFTER_LEVEL_UP)
            else:
                self.size = c.PLACE_MAX_SIZE
                self.goods = c.PLACE_GOODS_TO_LEVEL
        elif self.goods <= 0:
            self.size -= 1
            if self.size > 0:
                self.goods = int(c.PLACE_GOODS_TO_LEVEL * c.PLACE_GOODS_AFTER_LEVEL_DOWN)
            else:
                self.size = 1
                self.goods = 0

        self.goods = int(self.goods)

    def sync(self):
        self.modifier_multiplier = f.place_specialization_modifier(self.size)

    def set_power_economic(self, value):
        self.power_economic = value

    def set_tax_size_border(self, value):
        self.tax_size_border = int(value)

    def set_money_economic(self, value):
        self.money_economic = value

    def set_area(self, value):
        self.area = value

    def ui_specializations(self):
        specializations = [record
                           for record in modifiers.CITY_MODIFIERS.records
                           if not record.is_NONE]

        sorted_specializations = [(specialization, getattr(self, specialization.points_attribute.name.lower()))
                                  for specialization in specializations]

        sorted_specializations.sort(key=lambda x: -x[1])

        return sorted_specializations
