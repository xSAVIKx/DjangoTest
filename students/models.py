from django.db import models

# Create your models here.
from uuidfield.fields import UUIDField


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)

    birthday_date = models.DateField()

    student_card_id = UUIDField(auto=True)
    group = models.ForeignKey('Group', related_name='groups')

    def __unicode__(self):
        return "%s %s. ID=%s".format(str(self.first_name), str(self.surname), str(self.student_card_id))

    class Meta:
        ordering = ['surname', 'first_name']


class Group(models.Model):
    title = models.CharField(max_length=32, unique=True)
    praepostor = models.ForeignKey('Student', related_name='praepostor')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']