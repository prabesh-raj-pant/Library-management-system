# Generated by Django 5.0.2 on 2024-06-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='Employee_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='Return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
