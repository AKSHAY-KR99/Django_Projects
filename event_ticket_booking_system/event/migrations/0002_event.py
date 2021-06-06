# Generated by Django 3.1.7 on 2021-06-03 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('team', models.CharField(default='No', max_length=100)),
                ('ticket_price', models.IntegerField()),
                ('total_seats', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('img', models.ImageField(upload_to='images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventcategory')),
            ],
        ),
    ]
