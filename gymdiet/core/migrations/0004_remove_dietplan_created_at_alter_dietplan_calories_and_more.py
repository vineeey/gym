# Generated by Django 5.2.4 on 2025-07-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_dietplan_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dietplan',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='calories',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='meals',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('customer', 'Customer'), ('trainer', 'Trainer')], default='customer', max_length=10),
        ),
    ]
