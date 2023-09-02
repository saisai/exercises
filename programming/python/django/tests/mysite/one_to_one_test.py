
from cgitb import reset
import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

from django.db import IntegrityError, connection, transaction


from one_to_one.models import (
    Bar,
    Director,
    Favorites,
    HiddenPointer,
    ManualPrimaryKey,
    MultiModel,
    Place,
    Pointer,
    RelatedModel,
    Restaurant,
    School,
    Target,
    ToFieldPointer,
    UndergroundBar,
    Waiter,
)

class OneToOneTest:
    
    def __init__(self):      
        
        
        Place.objects.all().delete()
        Restaurant.objects.all().delete()
        Restaurant.objects.all().delete()        
            
        
        
        self.p1 = Place.objects.create(name="Demon Dogs", address="944 W. Fullerton")
        self.p2 = Place.objects.create(name="Ace Hardware", address="1013 N. Ashland")
        self.r1 = Restaurant.objects.create(
                place=self.p1, serves_hot_dogs=True, serves_pizza=False
            )
        self.b1 = Bar.objects.create(place=self.p1, serves_cocktails=False)
        
            
        self.r1 = Restaurant.objects.first()
        self.p1 = Place.objects.first()
        self.p2 = Place.objects.last()
        self.b1 = Bar.objects.first()
         
    
    @classmethod
    def init(cls):      
        cls.p1 = Place.objects.create(name="Demon Dogs", address="944 W. Fullerton")
        cls.p2 = Place.objects.create(name="Ace Hardware", address="1013 N. Ashland")
        cls.r1 = Restaurant.objects.create(
            place=cls.p1, serves_hot_dogs=True, serves_pizza=False
        )
        cls.b1 = Bar.objects.create(place=cls.p1, serves_cocktails=False)
        
    def test_getter(self):
        
        # A Restaurant can access its place.
        #self.assertEqual(repr(self.r1.place), "<Place: Demon Dogs the place>")
        print(repr(self.r1.place))
        print(repr(self.r1.place) == "<Place: Demon Dogs the place>")
        print(repr(self.p1.restaurant) == "<Restaurant: Demon Dogs the restaurant>")
       
       
        try:
            print(self.p2.restaurant)
        except Restaurant.DoesNotExist as e:
            print("Place has no restaurant")
        print(hasattr(self.p2, "restaurant"))
        
    def test_setter(self):
        # Set the place using assignment notation. Because place is the primary
        # key on Restaurant, the save will create a new restaurant
        self.r1.place = self.p2
        self.r1.save()
        print(repr(self.p2.restaurant) == "<Restaurant: Ace Hardware the restaurant>")
        
        print(repr(self.r1.place) == "<Place: Ace Hardware the place>")
        print(self.p2.pk == self.r1.pk)
        # Set the place back again, using assignment in the reverse direction.
        self.p1.restaurant = self.r1
        print(
            repr(self.p1.restaurant)== "<Restaurant: Demon Dogs the restaurant>"
        )
        r = Restaurant.objects.get(pk=self.p1.id)
        print(repr(r.place) == "<Place: Demon Dogs the place>")
        
    def test_manager_all(self):
        # Restaurant.objects.all() just returns the Restaurants, not the Places.
        self.assertSequenceEqual(Restaurant.objects.all(), [self.r1])
        # Place.objects.all() returns all Places, regardless of whether they
        # have Restaurants.
        self.assertSequenceEqual(Place.objects.order_by("name"), [self.p2, self.p1])
        
    def test_manager_get(self):
        def assert_get_restaurant(**params):
            self.assertEqual(
                repr(Restaurant.objects.get(**params)),
                "<Restaurant: Demon Dogs the restaurant>",
            )

        assert_get_restaurant(place__id__exact=self.p1.pk)
        assert_get_restaurant(place__id=self.p1.pk)
        assert_get_restaurant(place__exact=self.p1.pk)
        assert_get_restaurant(place__exact=self.p1)
        assert_get_restaurant(place=self.p1.pk)
        assert_get_restaurant(place=self.p1)
        assert_get_restaurant(pk=self.p1.pk)
        assert_get_restaurant(place__pk__exact=self.p1.pk)
        assert_get_restaurant(place__pk=self.p1.pk)
        assert_get_restaurant(place__name__startswith="Demon")
        
        def assert_get_place(**params):
            self.assertEqual(
                repr(Place.objects.get(**params)), "<Place: Demon Dogs the place>"
            )

        assert_get_place(restaurant__place__exact=self.p1.pk)
        assert_get_place(restaurant__place__exact=self.p1)
        assert_get_place(restaurant__place__pk=self.p1.pk)
        assert_get_place(restaurant__exact=self.p1.pk)
        assert_get_place(restaurant__exact=self.r1)
        assert_get_place(restaurant__pk=self.p1.pk)
        assert_get_place(restaurant=self.p1.pk)
        assert_get_place(restaurant=self.r1)
        assert_get_place(id__exact=self.p1.pk)
        assert_get_place(pk=self.p1.pk)
        
    def test_foreign_key(self):
        # Add a Waiter to the Restaurant.
        w = self.r1.waiter_set.create(name="Joe")
        self.assertEqual(
            repr(w), "<Waiter: Joe the waiter at Demon Dogs the restaurant>"
        )

        # Query the waiters
        def assert_filter_waiters(**params):
            self.assertSequenceEqual(Waiter.objects.filter(**params), [w])

        assert_filter_waiters(restaurant__place__exact=self.p1.pk)
        assert_filter_waiters(restaurant__place__exact=self.p1)
        assert_filter_waiters(restaurant__place__pk=self.p1.pk)
        assert_filter_waiters(restaurant__exact=self.r1.pk)
        assert_filter_waiters(restaurant__exact=self.r1)
        assert_filter_waiters(restaurant__pk=self.r1.pk)
        assert_filter_waiters(restaurant=self.r1.pk)
        assert_filter_waiters(restaurant=self.r1)
        assert_filter_waiters(id__exact=w.pk)
        assert_filter_waiters(pk=w.pk)
        # Delete the restaurant; the waiter should also be removed
        r = Restaurant.objects.get(pk=self.r1.pk)
        r.delete()
        self.assertEqual(Waiter.objects.count(), 0)
        
    def test_multiple_o2o(self):
        # One-to-one fields still work if you create your own primary key
        
        ManualPrimaryKey.objects.all().delete()
        RelatedModel.objects.all().delete()
        MultiModel.objects.all().delete()
        
        o1 = ManualPrimaryKey(primary_key="abc123", name="primary")
        o1.save()
        o2 = RelatedModel(link=o1, name="secondary")
        o2.save()

        # You can have multiple one-to-one fields on a model, too.
        x1 = MultiModel(link1=self.p1, link2=o1, name="x1")
        x1.save()
        self.assertEqual(repr(o1.multimodel), "<MultiModel: Multimodel x1>")
        # This will fail because each one-to-one field must be unique (and
        # link2=o1 was used for x1, above).
        mm = MultiModel(link1=self.p2, link2=o1, name="x1")
        #with self.assertRaises(IntegrityError):
        try:
            with transaction.atomic():
                mm.save()
        except IntegrityError as e:
            print("e ", e)

    def test_unsaved_object(self):
        """
        #10811 -- Assigning an unsaved object to a OneToOneField
        should raise an exception.
        """
        place = Place(name="User", address="London")
        #with self.assertRaises(Restaurant.DoesNotExist):
        #    place.restaurant

        msg = (
            "save() prohibited to prevent data loss due to unsaved related object "
            "'place'."
        )
        msgs = "save() prohibited to prevent data loss due to unsaved related object 'place'."
        #with self.assertRaisesMessage(ValueError, msg):
        try:
            Restaurant.objects.create(
                place=place, serves_hot_dogs=True, serves_pizza=False
            )
        except ValueError as e:
  
            print(msg == str(e))
        # place should not cache restaurant
        #with self.assertRaises(Restaurant.DoesNotExist):
        #    place.restaurant
        
    def test_reverse_relationship_cache_cascade(self):
        """
        Regression test for #9023: accessing the reverse relationship shouldn't
        result in a cascading delete().
        """
        bar = UndergroundBar.objects.create(place=self.p1, serves_cocktails=False)

        # The bug in #9023: if you access the one-to-one relation *before*
        # setting to None and deleting, the cascade happens anyway.
        self.p1.undergroundbar
        bar.place.name = "foo"
        bar.place = None
        bar.save()
        self.p1.delete()

        self.assertEqual(Place.objects.count(), 1)
        self.assertEqual(UndergroundBar.objects.count(), 1)
        
    def test_create_models_m2m(self):
        """
        Models are created via the m2m relation if the remote model has a
        OneToOneField (#1064, #1506).
        """
        print(self.r1)
        Favorites.objects.all().delete()
        f = Favorites(name="Fred")
        f.save()
        f.restaurants.set([self.r1])
        print(f.restaurants.all())
        self.assertSequenceEqual(f.restaurants.all(), [self.r1])
        
    def test_reverse_object_cache(self):
        """
        The name of the cache for the reverse object is correct (#7173).
        """
        self.assertEqual(self.p1.restaurant, self.r1)
        self.assertEqual(self.p1.bar, self.b1)
        
    def test_assign_none_reverse_relation(self):
        p = Place.objects.get(name="Demon Dogs")
        # Assigning None succeeds if field is null=True.
        ug_bar = UndergroundBar.objects.create(place=p, serves_cocktails=False)
        p.undergroundbar = None
        self.assertIsNone(ug_bar.place)
        ug_bar.save()
        ug_bar.refresh_from_db()
        print("ug_bar.place", ug_bar.place)
        self.assertIsNone(ug_bar.place)
        
    def test_assign_none_null_reverse_relation(self):
        p = Place.objects.get(name="Demon Dogs")
        # Assigning None doesn't throw AttributeError if there isn't a related
        # UndergroundBar.
        p.undergroundbar = None

    def test_assign_none_to_null_cached_reverse_relation(self):
        p = Place.objects.get(name="Demon Dogs")
        # Prime the relation's cache with a value of None.
        with self.assertRaises(Place.undergroundbar.RelatedObjectDoesNotExist):
            getattr(p, "undergroundbar")
        # Assigning None works if there isn't a related UndergroundBar and the
        # reverse cache has a value of None.
        p.undergroundbar = None
        
    def test_assign_o2o_id_value(self):
        b = UndergroundBar.objects.create(place=self.p1)
        b.place_id = self.p2.pk
        b.save()
        self.assertEqual(b.place_id, self.p2.pk)
        self.assertFalse(UndergroundBar.place.is_cached(b))
        self.assertEqual(b.place, self.p2)
        self.assertTrue(UndergroundBar.place.is_cached(b))
        # Reassigning the same value doesn't clear a cached instance.
        b.place_id = self.p2.pk
        self.assertTrue(UndergroundBar.place.is_cached(b))
        
    def test_assign_o2o_id_none(self):
        b = UndergroundBar.objects.create(place=self.p1)
        b.place_id = None
        b.save()
        self.assertIsNone(b.place_id)
        self.assertFalse(UndergroundBar.place.is_cached(b))
        self.assertIsNone(b.place)
        self.assertTrue(UndergroundBar.place.is_cached(b))
        
    def test_related_object_cache(self):
        """Regression test for #6886 (the related-object cache)"""

        # Look up the objects again so that we get "fresh" objects
        p = Place.objects.get(name="Demon Dogs")
        r = p.restaurant

        # Accessing the related object again returns the exactly same object
        self.assertIs(p.restaurant, r)

        # But if we kill the cache, we get a new object
        del p._state.fields_cache["restaurant"]
        self.assertIsNot(p.restaurant, r)

        # Reassigning the Restaurant object results in an immediate cache update
        # We can't use a new Restaurant because that'll violate one-to-one, but
        # with a new *instance* the is test below will fail if #6886 regresses.
        r2 = Restaurant.objects.get(pk=r.pk)
        p.restaurant = r2
        self.assertIs(p.restaurant, r2)

        # Assigning None succeeds if field is null=True.
        ug_bar = UndergroundBar.objects.create(place=p, serves_cocktails=False)
        ug_bar.place = None
        self.assertIsNone(ug_bar.place)

        # Assigning None will not fail: Place.restaurant is null=False
        setattr(p, "restaurant", None)

        # You also can't assign an object of the wrong type here
        msg = (
            'Cannot assign "<Place: Demon Dogs the place>": '
            '"Place.restaurant" must be a "Restaurant" instance.'
        )
        with self.assertRaisesMessage(ValueError, msg):
            setattr(p, "restaurant", p)

        # Creation using keyword argument should cache the related object.
        p = Place.objects.get(name="Demon Dogs")
        r = Restaurant(place=p)
        self.assertIs(r.place, p)

        # Creation using keyword argument and unsaved related instance (#8070).
        p = Place()
        r = Restaurant(place=p)
        self.assertIs(r.place, p)

        # Creation using attname keyword argument and an id will cause the related
        # object to be fetched.
        p = Place.objects.get(name="Demon Dogs")
        r = Restaurant(place_id=p.id)
        self.assertIsNot(r.place, p)
        self.assertEqual(r.place, p)


    def assertSequenceEqual(self, a, b):
        print(a == b)
        
    def assertEqual(self, a, b):
        print(a == b)
    
    def assertIsNone(self, obj):
        print(not obj)
        
    def assertFalse(self, obj):
        print( obj)
        
    def assertTrue(self, obj):
        print( obj )
    
        
h = OneToOneTest()
#h.test_getter()
#h.test_setter()
#h.test_manager_all()
#h.test_manager_get()
#h.test_foreign_key()
#h.test_multiple_o2o()
#h.test_unsaved_object()
#h.test_reverse_relationship_cache_cascade()
#h.test_create_models_m2m()
#h.test_reverse_object_cache()
#h.test_assign_none_reverse_relation()
#h.test_assign_none_null_reverse_relation()
#h.test_assign_o2o_id_value()
#h.test_assign_o2o_id_none()
#h.test_related_object_cache()
