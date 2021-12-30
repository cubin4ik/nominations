# Generated by Django 3.0.6 on 2021-12-29 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='votes',
            options={'verbose_name_plural': 'votes'},
        ),
        migrations.AlterField(
            model_name='nominations',
            name='title',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='votes',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='votes',
            unique_together={('voter', 'nomination')},
        ),
    ]
