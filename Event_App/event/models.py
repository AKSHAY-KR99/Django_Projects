from django.db import models

# Create your models here.

class EventCategory(models.Model):
    event_category=models.CharField(max_length=50)

    def __str__(self):
        return self.event_category

class Event(models.Model):
    event_name=models.CharField(max_length=100)
    category=models.ForeignKey(EventCategory,on_delete=models.CASCADE)
    team_name=models.CharField(max_length=100,default="No")
    ticket_price=models.IntegerField()
    place=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    total_seats=models.IntegerField()
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return self.event_name


class EventBook(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    user=models.CharField(max_length=100)
    number_of_tickets=models.IntegerField(default=1)
    booking_date=models.DateField(auto_now=True)
    Mobile_number=models.IntegerField()
    choices=[
        ("booked","booked"),
        ("cancel","cancel")
    ]
    status=models.CharField(max_length=10,choices=choices,default="booked")
