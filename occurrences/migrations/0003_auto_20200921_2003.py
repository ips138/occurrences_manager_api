# Generated by Django 3.1.1 on 2020-09-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0002_occurrence_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='created',
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
    ]
