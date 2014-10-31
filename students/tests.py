# Create your tests here.
import datetime

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from selenium.webdriver.support.select import Select

from students.models import Group, Student


class StudentIntegrationTests(LiveServerTestCase):
    selenium = None

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(StudentIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(StudentIntegrationTests, cls).tearDownClass()

    def setUp(self):
        Group.objects.create(title='Test group 1')
        Group.objects.create(title='Test group 2')

    def test_add_student(self):
        first_name = "Valera"
        middle_name = "Sergiyovich"
        surname = "Petrenko"
        birthday_date = "10/01/2014"
        group = Group.objects.get(title='Test group 1')

        self.selenium.get('%s%s' % (self.live_server_url, '/students/student/new'))
        self.selenium.find_element_by_id('id_first_name').send_keys(first_name)
        self.selenium.find_element_by_id('id_middle_name').send_keys(middle_name)
        self.selenium.find_element_by_id('id_surname').send_keys(surname)
        self.selenium.find_element_by_id('id_birthday_date').send_keys(birthday_date)
        group_select = Select(self.selenium.find_element_by_id('id_group'))
        group_select.select_by_value('1')

        self.selenium.find_element_by_css_selector("button[type='submit']").click()
        students = Student.objects.all()
        self.assertEqual(len(students), 1, "There is not one student!")
        actual_student = students[0]
        self.assertEqual(actual_student.first_name, first_name)
        self.assertEqual(actual_student.middle_name, middle_name)
        self.assertEqual(actual_student.surname, surname)
        self.assertEqual(actual_student.birthday_date, datetime.date(year=2014, month=10, day=01))
        self.assertEqual(actual_student.group, group)