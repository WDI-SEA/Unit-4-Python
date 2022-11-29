------------- CATS -------------------------

1. Retrieve All Cats:
    - Cat.objects.all()

    Retrieve first row of query:
        - Cat.objects.first()

2. Create a new Cat:
    - catInstance = Cat(name='', .. .. .)

3. Save changes to an exisitng queryset
    - catInstance.save()

4. Filter Cats from DB:
    - Cat.objects.filter(name='.. ...)
    - Cat.objects.filter(name__contains=' .... ..')
    - Cat.objects.filter(age__lte= .. .. .. ) (Less than or equal to)

5. Retrieve Cat by property:
    - Cat.objects.get(id=1) (or any property)

6. Retrieve Cats and order:
    - Cat.objects.order_by('-age')

------------- FEEDING -------------------------

7. Retrieve all Feedings of a Cat (1:M, ForeignKey)
    - c = Cat.objects.get(id=1)
    - c.feeding_set.all()

7. Create a new Feeding for a Cat (1:M, ForeignKey)
    - c = Cat.objects.get(id=1)
    - c.feeding_set.create(.. ..)

8. Another way to create a new Feeding for a Cat (1:M, ForeignKey)
    - c = Cat.objects.get(id=1)
    - newFeeding = Feeding(...., cat=c)
    - newFeeding.save()

9. Another way to create a new Feeding for a Cat (1:M, ForeignKey)
    - c = Cat.objects.get(id=1)
    - Feeding.objects.create(....., cat=c)

------------- TOYS -------------------------

10. Associate a Cat to a Toy (vice versa)
    - my_cat_peaches = Cat.objects.get(name='peaches')
    - rubber_ducky = Toy.objects.first()
    - my_cat_peaches.toys.add(rubber_ducky)
    - (TO REMOVE) my_cat_peaches.toys.remove(rubber_ducky)

    - (TO REMOVE ALL ASSOCIATIONS)
    - for c in Cat.objects.all():
            c.toys.clear() 