import datetime

from django.test import RequestFactory, TestCase

from dummyApp.models import Category, Department, Log, Status, Task, User


class LogModelTests(TestCase):

    def setUp(self):
        Category.objects.create(name='dummy_category')
        Department.objects.create(name='dummy_department')
        Status.objects.create(name='dummy_status')

        User.objects.create(first_name='dummy_user',
                            email_address='dummy_email@address.com')
    
    def test_startdatetime_lt_enddatetime(self):
        """
        create task log with start date time after end date time
        """
        started_datetime = datetime.datetime.now()
        finished_datetime = started_datetime - datetime.timedelta(days=1)
        dummy_task = Task(category=Category.objects.all()[0],
                          name='dummy_task', ).save()
        wrong_start_finished_log = Log(task=dummy_task, 
                                       user=User.objects.get(email_address='dummy_email@address.com'
                                       status=Status.objects.all(),
                                       started=started_datetime,
                                       finished=finished_datetime,
                                       )
        res = wrong_start_finished_log.save()
        print('RES:', res)
        error_msg = 'violates check constraint'
        self.assertEqual(res, error_msg)
