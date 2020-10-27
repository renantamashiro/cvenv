from django.db import models

from .users import User


class Group(models.Model):
    name = models.CharField('name', max_length=50)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField('name', max_length=50)

    def __str__(self):
        return self.name


class Log(models.Model):
    title = models.CharField('title', max_length=50)
    description = models.TextField('description')
    date_published = models.DateTimeField('date published')
    events = models.IntegerField(default=0)
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING,
        related_name='users'
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.deletion.DO_NOTHING,
        related_name='levels'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.deletion.DO_NOTHING,
        related_name='groups'
    )

    def __str__(self):
        return self.title
