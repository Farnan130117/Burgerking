# Generated by Django 3.1.2 on 2020-10-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='deposit_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='return_amount',
            field=models.IntegerField(),
        ),
    ]
