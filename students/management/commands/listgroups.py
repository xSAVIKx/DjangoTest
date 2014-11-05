from django.core.management.base import NoArgsCommand

from students.models import Group, Student


__author__ = 'Iurii Sergiichuk <i.sergiichuk@samsung.com>'


class Command(NoArgsCommand):
    help = 'Prints groups and groups students.'

    def handle_noargs(self, **options):
        lines = []

        groups = Group.objects.all()
        for group_index, group in enumerate(groups):
            lines.append("%d. Group '%s' students:" % (group_index + 1, str(group)))
            group_students = Student.objects.filter(group=group)
            for student_index, student in enumerate(group_students):
                lines.append("\t%d) %s" % (student_index + 1, str(student)))
        return '\n'.join(lines)