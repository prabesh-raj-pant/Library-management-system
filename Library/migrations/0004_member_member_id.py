# Generated by Django 5.0.2 on 2024-06-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_alter_loan_loan_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Member_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
