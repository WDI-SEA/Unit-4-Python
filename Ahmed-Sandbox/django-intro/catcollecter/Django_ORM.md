1. Retrieve All Cats:
    - Cat.objects.all()

2. Retrieve first row of query:
    Cat.objects.first()

3. Create new Cat:
    - someVariable = Cat(name='', .., ..)

4. Save Changes to an existing queryset
    - catInstance.save()

5. Filter Cats from DB:
    - Cat.objects.filter(name='', ...)
    - Cat..objects.filter(name__contains='...')
    - Cat.objects.filter(age__lte= ...) (Less than or equal to)
    - Cat.objects.filter(age__gte= ...) (Greater than or equal to)

6. Retrieve Cat by property:
    - Cat.objects.get(id=1) (Or any property)

7. Retrieve Cats and order:
    - Cat.objects.order_by('-age')
