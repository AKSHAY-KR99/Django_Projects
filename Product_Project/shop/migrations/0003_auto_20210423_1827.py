# Generated by Django 3.1.7 on 2021-04-23 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('despatched', 'despatched'), ('cancelled', 'cancelled'), ('delivered', 'delivered')], default='ordered', max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.mobile')),
            ],
        ),
    ]
