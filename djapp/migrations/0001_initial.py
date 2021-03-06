# Generated by Django 2.0.1 on 2018-01-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30, verbose_name='genre')),
                ('albums', models.ManyToManyField(related_name='Genres', to='djapp.Album')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('-genre',),
            },
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='performer')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=30, verbose_name='song')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='duration')),
                ('album', models.ManyToManyField(related_name='Tracks', to='djapp.Album')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
                'ordering': ('-song',),
            },
        ),
        migrations.AddField(
            model_name='album',
            name='performer',
            field=models.ForeignKey(on_delete='CASCADE', related_name='Albums', to='djapp.Performer', verbose_name='Исполнитель'),
        ),
    ]
