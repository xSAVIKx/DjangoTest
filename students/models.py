from django.db import models

# Create your models here.
from django.dispatch import Signal, receiver
from uuidfield.fields import UUIDField
from django.core.urlresolvers import reverse

model_update_signal = Signal()
model_create_signal = Signal()
model_delete_signal = Signal()


class SignalEvent(models.Model):
    sender = models.CharField(max_length=254)
    event = models.CharField(max_length=254)
    additional_info = models.TextField(max_length=1024)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s : %s" % (str(self.sender), str(self.event), str(self.time_stamp))

    class Meta:
        ordering = ['time_stamp']


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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        is_created = True
        if self.id:
            is_created = False
        super(Student, self).save(force_insert, force_update, using, update_fields)
        if is_created:
            model_create_signal.send(sender=self.__class__,
                                     additional_info='object_id=%d' % self.id)
        else:
            model_update_signal.send(sender=self.__class__, additional_info='object_id=%d' % self.id)

    def delete(self, using=None):
        model_delete_signal.send(sender=self.__class__, additional_info='object_id=%d' % self.id)
        super(Student, self).delete(using)


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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        is_created = True
        if self.id:
            is_created = False
        super(Group, self).save(force_insert, force_update, using, update_fields)
        if is_created:
            model_create_signal.send(sender=self.__class__,
                                     additional_info='object_id=%d' % self.id)
        else:
            model_update_signal.send(sender=self.__class__, additional_info='object_id=%d' % self.id)

    def delete(self, using=None):
        model_delete_signal.send(sender=self.__class__, additional_info='object_id=%d' % self.id)
        super(Group, self).delete(using)


@receiver(model_update_signal)
def model_update(sender, **kwargs):
    SignalEvent.objects.create(sender=sender, event="update", additional_info=kwargs.get('additional_info'))


@receiver(model_create_signal)
def model_create(sender, **kwargs):
    SignalEvent.objects.create(sender=sender, event="create", additional_info=kwargs.get('additional_info'))


@receiver(model_delete_signal)
def model_delete(sender, **kwargs):
    SignalEvent.objects.create(sender=sender, event="delete", additional_info=kwargs.get('additional_info'))