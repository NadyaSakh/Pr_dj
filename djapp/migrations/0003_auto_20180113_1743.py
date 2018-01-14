# Generated by Django 2.0.1 on 2018-01-13 07:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0002_auto_20180113_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='performer',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='track',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
