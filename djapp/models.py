from django.db import models

# Create your models here.


class Performer(models.Model):
    name = models.CharField('Исполнитель',max_length=30)
    description = models.CharField('Описание', max_length=50, null=True, blank=True, default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField('Заголовок',max_length=30)
    created_at = models.DateTimeField('Выпущен',auto_now_add=True)
    performer = models.ForeignKey('Performer', verbose_name='Исполнитель', on_delete='CASCADE', related_name='Albums')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр',related_name='Album_by_genre')

    class Meta:
        ordering = ('title',)
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField('Жанр',max_length=30)
    # albums = models.ManyToManyField('Album', related_name='Genres')

    class Meta:
        ordering = ('genre',)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre


class Track(models.Model):
    song = models.CharField('Песня',max_length=30)
    duration = models.DurationField('Длительность', null=True, blank=True)
    album = models.ManyToManyField('Album', verbose_name='Альбом', related_name='tracks')
    published_at = models.DateTimeField(verbose_name='Опубликовано', auto_now_add=True, editable=False)

    class Meta:
        ordering = ('song',)
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return self.song

