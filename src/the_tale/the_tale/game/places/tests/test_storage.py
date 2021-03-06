
import smart_imports

smart_imports.all()


class PlacesStorageTest(utils_testcase.TestCase):

    def setUp(self):
        super(PlacesStorageTest, self).setUp()
        self.p1, self.p2, self.p3 = game_logic.create_test_map()
        self.storage = storage.PlacesStorage()
        self.storage.sync()

    def test_initialization(self):
        _storage = storage.PlacesStorage()
        self.assertEqual(_storage._data, {})
        self.assertEqual(_storage._version, None)

    def test_sync(self):
        self.assertEqual(len(self.storage._data), 3)

        self.assertNotEqual(self.p1.attrs.size, 7)

        place = models.Place.objects.get(id=self.p1.id)
        data = s11n.from_json(place.data)
        data['attributes']['size'] = 7
        place.data = s11n.to_json(data)
        place.save()

        self.storage.sync()
        self.assertNotEqual(self.storage[self.p1.id].attrs.size, 7)

        self.storage.sync(force=True)
        self.assertEqual(self.storage[self.p1.id].attrs.size, 7)

    def test_sync_after_settings_update(self):
        self.assertEqual(len(self.storage._data), 3)

        self.assertNotEqual(self.p1.attrs.size, 7)

        place = models.Place.objects.get(id=self.p1.id)
        data = s11n.from_json(place.data)
        data['attributes']['size'] = 7
        place.data = s11n.to_json(data)
        place.save()

        self.storage.sync()
        self.assertNotEqual(self.storage[self.p1.id].attrs.size, 7)

        global_settings[self.storage.SETTINGS_KEY] = uuid.uuid4().hex

        self.storage.sync()
        self.assertEqual(self.storage[self.p1.id].attrs.size, 7)

    def test_getitem_wrong_id(self):
        self.assertRaises(exceptions.PlacesStorageError, self.storage.__getitem__, 666)

    def test_getitem(self):
        self.assertEqual(self.storage[self.p1.id].id, self.p1.id)

    def test_get(self):
        self.assertEqual(self.storage.get(666, self.p2).id, self.p2.id)
        self.assertEqual(self.storage.get(self.p3.id, self.p1).id, self.p3.id)

    def test_all(self):
        self.assertEqual(len(self.storage.all()), 3)

    def test_contains(self):
        self.assertTrue(self.p1.id in self.storage)
        self.assertFalse(666 in self.storage)

    def test_nearest_places_with_distances(self):
        distances = self.storage.nearest_places_with_distance(self.p1.id)
        self.assertEqual(distances,
                         [(0, self.p1.id),
                          (navigation_logic.manhattan_distance(self.p1.x, self.p1.y, self.p3.x, self.p3.y), self.p3.id),
                          (navigation_logic.manhattan_distance(self.p1.x, self.p1.y, self.p2.x, self.p2.y), self.p2.id)])

        distances = self.storage.nearest_places_with_distance(self.p3.id)
        self.assertEqual(distances,
                         [(0, self.p3.id),
                          (navigation_logic.manhattan_distance(self.p3.x, self.p3.y, self.p1.x, self.p1.y), self.p1.id),
                          (navigation_logic.manhattan_distance(self.p3.x, self.p3.y, self.p2.x, self.p2.y), self.p2.id)])

    def test_nearest_places_with_distances__number(self):
        distances = self.storage.nearest_places_with_distance(self.p1.id, number=2)
        self.assertEqual(distances,
                         [(0, self.p1.id),
                          (navigation_logic.manhattan_distance(self.p1.x, self.p1.y, self.p3.x, self.p3.y), self.p3.id)])

        distances = self.storage.nearest_places_with_distance(self.p3.id, number=2)
        self.assertEqual(distances,
                         [(0, self.p3.id),
                          (navigation_logic.manhattan_distance(self.p3.x, self.p3.y, self.p1.x, self.p1.y), self.p1.id),
                          (navigation_logic.manhattan_distance(self.p3.x, self.p3.y, self.p2.x, self.p2.y), self.p2.id)])

    def test_nearest_places(self):
        distances = self.storage.nearest_places(self.p1.id)
        self.assertEqual(distances, [self.storage[self.p1.id],
                                     self.storage[self.p3.id],
                                     self.storage[self.p2.id]])

        distances = self.storage.nearest_places(self.p1.id, number=2)
        self.assertEqual(distances, [self.storage[self.p1.id],
                                     self.storage[self.p3.id]])

    def test_expected_minimum_quest_distance(self):
        self.assertAlmostEqual(self.storage.expected_minimum_quest_distance(), 6.666666666666667)


class ResourceExchangeStorageTests(utils_testcase.TestCase):

    def setUp(self):
        super(ResourceExchangeStorageTests, self).setUp()
        self.place_1, self.place_2, self.place_3 = game_logic.create_test_map()

        self.resource_1 = random.choice(relations.RESOURCE_EXCHANGE_TYPE.records)
        self.resource_2 = random.choice(relations.RESOURCE_EXCHANGE_TYPE.records)

    def test_create(self):
        self.assertEqual(len(storage.resource_exchanges.all()), 0)

        old_version = storage.resource_exchanges._version

        exchange = prototypes.ResourceExchangePrototype.create(place_1=self.place_1,
                                                               place_2=self.place_2,
                                                               resource_1=self.resource_1,
                                                               resource_2=self.resource_2,
                                                               bill=None)

        self.assertEqual(len(storage.resource_exchanges.all()), 1)

        self.assertEqual(exchange.id, storage.resource_exchanges.all()[0].id)
        self.assertNotEqual(old_version, storage.resource_exchanges._version)

    def test_get_exchanges_for_place__no(self):
        self.assertEqual(storage.resource_exchanges.get_exchanges_for_place(self.place_2), [])

    def test_get_exchanges_for_place__multiple(self):
        exchange_1 = prototypes.ResourceExchangePrototype.create(place_1=self.place_1,
                                                                 place_2=self.place_2,
                                                                 resource_1=self.resource_1,
                                                                 resource_2=self.resource_2,
                                                                 bill=None)

        prototypes.ResourceExchangePrototype.create(place_1=self.place_1,
                                                    place_2=self.place_3,
                                                    resource_1=self.resource_1,
                                                    resource_2=self.resource_2,
                                                    bill=None)

        exchange_3 = prototypes.ResourceExchangePrototype.create(place_1=self.place_2,
                                                                 place_2=self.place_3,
                                                                 resource_1=self.resource_1,
                                                                 resource_2=self.resource_2,
                                                                 bill=None)

        self.assertEqual(set(exchange.id for exchange in storage.resource_exchanges.get_exchanges_for_place(self.place_2)),
                         set((exchange_1.id, exchange_3.id)))

    def test_get_exchanges_for_bill_id_no(self):
        self.assertEqual(storage.resource_exchanges.get_exchange_for_bill_id(666), None)

    def test_get_exchanges_for_bill_id__exists(self):
        account = self.accounts_factory.create_account()

        forum_category = forum_models.Category.objects.create(caption='category-1', slug='category-1')
        forum_models.SubCategory.objects.create(caption=bills_conf.settings.FORUM_CATEGORY_UID + '-caption',
                                                uid=bills_conf.settings.FORUM_CATEGORY_UID,
                                                category=forum_category)

        bill_data = bills_bills.place_renaming.PlaceRenaming(place_id=self.place_1.id, name_forms=game_names.generator().get_test_name('new_name'))
        bill = bills_prototypes.BillPrototype.create(account, 'bill-caption', bill_data, chronicle_on_accepted='chronicle-on-accepted')

        prototypes.ResourceExchangePrototype.create(place_1=self.place_1,
                                                    place_2=self.place_2,
                                                    resource_1=self.resource_1,
                                                    resource_2=self.resource_2,
                                                    bill=None)

        exchange_2 = prototypes.ResourceExchangePrototype.create(place_1=self.place_1,
                                                                 place_2=self.place_3,
                                                                 resource_1=self.resource_1,
                                                                 resource_2=self.resource_2,
                                                                 bill=bill)

        prototypes.ResourceExchangePrototype.create(place_1=self.place_2,
                                                    place_2=self.place_3,
                                                    resource_1=self.resource_1,
                                                    resource_2=self.resource_2,
                                                    bill=None)

        self.assertEqual(exchange_2.id, storage.resource_exchanges.get_exchange_for_bill_id(bill.id).id)


class EffectsStorageTest(utils_testcase.TestCase):

    def setUp(self):

        tt_services.effects.cmd_debug_clear_service()

        super().setUp()

        self.places = game_logic.create_test_map()
        self.storage = storage.EffectsStorage()
        self.storage.sync()

    def test_initialize(self):
        self.assertEqual(self.storage._effects_by_place, {})

    def test_effects_for_place(self):
        effect_1_id = logic.register_effect(place_id=self.places[0].id,
                                            attribute=relations.ATTRIBUTE.CULTURE,
                                            value=0.1,
                                            name='test.effect.1')
        effect_2_id = logic.register_effect(place_id=self.places[0].id,
                                            attribute=relations.ATTRIBUTE.STABILITY,
                                            value=0.2,
                                            name='test.effect.2')
        effect_3_id = logic.register_effect(place_id=self.places[1].id,
                                            attribute=relations.ATTRIBUTE.STABILITY,
                                            value=0.3,
                                            name='test.effect.3')

        self.storage.refresh()

        self.assertEqual({effect.id for effect in self.storage.effects_for_place(self.places[0].id)},
                         {effect_1_id, effect_2_id})
        self.assertEqual({effect.id for effect in self.storage.effects_for_place(self.places[1].id)},
                         {effect_3_id})
        self.assertEqual({effect.id for effect in self.storage.effects_for_place(self.places[2].id)},
                         set())


class ClansRegionsStorageTests(helpers.PlacesTestsMixin,
                               utils_testcase.TestCase):

    def setUp(self):
        tt_services.effects.cmd_debug_clear_service()

        super().setUp()

        self.places = game_logic.create_test_map()

        self.storage = storage.clans_regions

    def test_initialize(self):
        clans_regions = storage.ClansRegionsStorage()

        self.assertEqual(clans_regions._regions, {})

    def test_recalculate__single_none_region(self):
        self.assertEqual(self.storage.region_for_place(self.places[0].id),
                         self.storage.region_for_place(self.places[1].id))

        self.assertEqual(self.storage.region_for_place(self.places[0].id),
                         self.storage.region_for_place(self.places[2].id))

        self.assertEqual(self.storage.region_for_place(self.places[0].id).places_ids,
                         {place.id for place in self.places})

    def test_united_regions(self):
        self.set_protector(self.places[0].id, 1)
        self.set_protector(self.places[1].id, 2)
        self.set_protector(self.places[2].id, 2)

        self.assertNotEqual(self.storage.region_for_place(self.places[0].id),
                            self.storage.region_for_place(self.places[1].id))

        self.assertEqual(self.storage.region_for_place(self.places[1].id),
                         self.storage.region_for_place(self.places[2].id))

        self.assertEqual(self.storage.region_for_place(self.places[0].id).places_ids,
                         {self.places[0].id})

        self.assertEqual(self.storage.region_for_place(self.places[1].id).places_ids,
                         {self.places[1].id, self.places[2].id})

    def test_large_region(self):
        self.set_protector(self.places[0].id, 2)
        self.set_protector(self.places[1].id, 2)
        self.set_protector(self.places[2].id, 2)

        self.assertEqual(self.storage.region_for_place(self.places[0].id),
                         self.storage.region_for_place(self.places[1].id))

        self.assertEqual(self.storage.region_for_place(self.places[1].id),
                         self.storage.region_for_place(self.places[2].id))

        self.assertEqual(self.storage.region_for_place(self.places[1].id).places_ids,
                         {self.places[0].id, self.places[1].id, self.places[2].id})

    def test_broken_regions(self):
        self.set_protector(self.places[0].id, 1)
        self.set_protector(self.places[1].id, 2)
        self.set_protector(self.places[2].id, 1)

        self.assertNotEqual(self.storage.region_for_place(self.places[0].id),
                            self.storage.region_for_place(self.places[1].id))

        self.assertNotEqual(self.storage.region_for_place(self.places[1].id),
                            self.storage.region_for_place(self.places[2].id))

        self.assertNotEqual(self.storage.region_for_place(self.places[0].id),
                            self.storage.region_for_place(self.places[2].id))

        self.assertEqual(self.storage.region_for_place(self.places[0].id).places_ids,
                         {self.places[0].id})

        self.assertEqual(self.storage.region_for_place(self.places[1].id).places_ids,
                         {self.places[1].id})

        self.assertEqual(self.storage.region_for_place(self.places[2].id).places_ids,
                         {self.places[2].id})
