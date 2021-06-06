from django.db import models


# Create your models here.
class EventCategory(models.Model):
    event_category = models.CharField(max_length=50)

    def __str__(self):
        return self.event_category


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    team_or_performer = models.CharField(max_length=100, default="No")
    ticket_price = models.IntegerField()
    total_seats = models.IntegerField()
    avlbl_seats = models.IntegerField(default=0)
    location = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.event_name


class EventBook(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    no_of_tickets = models.IntegerField(default=1)
    booking_date = models.DateField(auto_now=True)
    mobile_number = models.CharField(max_length=12)
    choices = [
        ("booked", "booked"),
        ("cancel", "cancel")
    ]
    status = models.CharField(max_length=10, choices=choices, default="booked")
    total = models.IntegerField()

class Feedback(models.Model):
    user=models.CharField(max_length=100)
    feedback=models.CharField(max_length=1000)
    def __str__(self):
        return self.user

