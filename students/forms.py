from django import forms
from django.forms.widgets import DateInput

from students.models import Student


__author__ = 'iurii'


class StudentForm(forms.ModelForm):
    initial=''
    class Meta:
        model = Student
        exclude = ['student_card_id']
        widgets = {
            'birthday_date': DateInput(attrs={'class': 'datepicker', 'type': 'date'})
        }