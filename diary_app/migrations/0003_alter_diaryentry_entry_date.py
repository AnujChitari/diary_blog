# Generated by Django 4.2.3 on 2023-07-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_app', '0002_diaryentry_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryentry',
            name='entry_date',
            field=models.DateTimeField(null=True),
        ),
    ]