from django.db import models

# Create your models here.
from uuidfield.fields import UUIDField
from django.core.urlresolvers import reverse


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32, blank=True)

    birthday_date = models.DateField(blank=True, null=True)

    student_card_id = UUIDField(auto=True)
    group = models.ForeignKey('Group', related_name='groups', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return "%s %s. ID=%s" % (str(self.first_name), str(self.surname), str(self.student_card_id))

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'student_id': str(self.id)})

    class Meta:
        ordering = ['surname', 'first_name']


class Group(models.Model):
    title = models.CharField(max_length=32, unique=True)
    praepostor = models.ForeignKey('Student', related_name='praepostor', blank=True, null=True,
                                   on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'group_id': str(self.id)})

    class Meta:
        ordering = ['title']