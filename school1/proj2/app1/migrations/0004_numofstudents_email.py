# Generated by Django 3.2.4 on 2021-08-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_attendence_datefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='numofstudents',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=50),
            preserve_default=False,
        ),
    ]