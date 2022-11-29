from django.db import models

# Create your models here.
MEALS=(
    ('B','Breakfast'),
    ('L','Lunch'),
    ('D','Dinner')
)

class Finch(models.Model):
    name = models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    age = models.IntegerField()
class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
	 choices=MEALS,
	 default=MEALS[0][0]
  )
  # Create a cat_id FK
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
#     object.all() object.get(id=1)
# object.filter()
# .save()
# .Cat()create