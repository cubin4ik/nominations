# Generated by Django 3.0.6 on 2021-12-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211229_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='color',
            field=models.CharField(choices=[('BLU', '#dce6ff'), ('PNK', '#ffdcf2'), ('BRW', '#ffe8dc'), ('GRN', '#dcffdc'), ('VLT', '#e6dcff'), ('YLW', '#fcffdc')], default='BLU', max_length=3),
        ),
    ]
