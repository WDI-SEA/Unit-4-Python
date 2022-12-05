from django.db import models

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# we write the model here & then migrate, that's all
# python manage.py makemigrations
# python manage.py migrate
# migrate looks at the files that had not run yet & runs them
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # there are many other fields like DateField & FileField
    def __str__(self):
        return self.name

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        # if we want default to show nothing we will put default=""
        # [0][0] means the zeroth column & row which will be 'B'
        default=MEALS[0][0]
    )
    # Cat foreign key
    # because the feeding table is the one that has the foreign key then the relation will be one cat to many foods
    # the one that doesn't have the foreign key is the one that is one
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    # __str__ this is called dunder (double underscore) or magic method
    def __str__(self):
        return (f"{self.get_meal_display()} on {self.date}")
    
    class Meta:
        ordering = ['-date']