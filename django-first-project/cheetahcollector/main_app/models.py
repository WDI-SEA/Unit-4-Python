from django.db import models

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Cheetah(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.TextField(max_length=250)
    def __str__(self):
        return self.name


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,  
        default=MEALS[0][0]  
    )
    # Cat Foreign Key Below
    cheetah = models.ForeignKey(Cheetah, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']