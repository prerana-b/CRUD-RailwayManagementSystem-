# Generated by Django 3.2 on 2021-05-02 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railwaybooking', '0003_auto_20210503_0153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketinfo',
            options={},
        ),
        migrations.RemoveField(
            model_name='ticketinfo',
            name='dor',
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='destination',
            field=models.CharField(default=23.3, max_length=100),
            preserve_default=False,
        ),
    ]
