from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=50)
    price=models.IntegerField(default=50)
    pages=models.IntegerField()
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.book_name

# book1=Book(book_name="test1",author='mt',price=250,pages=150,category='fiction')
# book2=Book(book_name="test2",author='omv',price=250,pages=150,category='romance')

# instead of select * from table is >>>>>>  books=Book.objects.all()

# updation in OMR query
#         we have to fetch book object
#             book=Book.objects.get(id=1)



# ORM query for creating an book object
# >>book=Book.(book_name="half girl friend",author="oc")
# book.save()
#
#  fetching corresponding book
#
# book=Book.objects.get(id=1)
# book.delete()

# books=Book.objects.all()
