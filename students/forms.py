from django import forms
from django.forms.widgets import DateInput

from students.models import Student, Group


__author__ = 'iurii'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['student_card_id']
        widgets = {
            'birthday_date': DateInput(attrs={'class': 'datepicker', 'type': 'date'})
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'