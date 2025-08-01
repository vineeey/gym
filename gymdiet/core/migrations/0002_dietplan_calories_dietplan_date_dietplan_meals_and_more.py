# Generated by Django 5.2.4 on 2025-07-31 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietplan',
            name='calories',
            field=models.PositiveIntegerField(default=0, help_text='Total calories for the day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dietplan',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dietplan',
            name='meals',
            field=models.TextField(default=0, help_text='Describe the meal plan, e.g. Breakfast, Lunch, Dinner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='details',
            field=models.TextField(blank=True, help_text='Any extra notes'),
        ),
    ]
