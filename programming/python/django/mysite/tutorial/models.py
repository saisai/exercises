from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    
# Custom manager    
class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().all()
    
    
# Meta inheritance    
    
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)    
    objects = models.Manager()  # The default manager.
    published = StudentManager()  # Our custom manager.
    
    
# Multi-table inheritance
    
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)    
    
    @property
    def get_place(self):
        return self.name
        
    def hello(self):
        return '{0}-{1}'.format(self.name, self.address)
    
    
# Custom field

class CurrencyField(models.IntegerField):
    description = "A field to save dollars as pennies (int) in db, but act like a float"

    def get_db_prep_value(self, value, *args, **kwargs):
        if value is None:
          return None
        return int(round(value * 100))

    def to_python(self, value):
        if value is None or isinstance(value, float):
          return value
        try:
          return float(value) / 100
        except (TypeError, ValueError):
          raise ValidationError("This value must be an integer or a string represents an integer.")

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def formfield(self, **kwargs):
        from django.forms import FloatField
        defaults = {'form_class': FloatField}
        defaults.update(kwargs)
        return super(CurrencyField, self).formfield(**defaults)
        
class House(models.Model):
    currency = CurrencyField()
    name = models.CharField(max_length=100)
    

# Create custom create method
class Book(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        # do something with the book
        return book
        
class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book

class Book2(models.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()        
    
class PersonShirt(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)
    
    
class PersonTest(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Club(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(PersonTest)    
    
    
"""
tom = PersonTest.objects.create(name="Tom", description="A nice guy")
bill = PersonTest.objects.create(name="Bill", description="Good dancer")

nightclub = Club.objects.create(name="The Saturday Night Club")
nightclub.members.add(tom, bill)

for person in nightclub.members.all():
    print(person.name)
    
p = PersonTest.objects.get(pk=1)
p.club_set.all()
    
"""    
        