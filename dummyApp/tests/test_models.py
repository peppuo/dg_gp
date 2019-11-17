import datetime

from django.test import RequestFactory, TestCase
from django.utils import timezone

from dummyApp.models import Category, Department, Log, Status, Task, User


class LogModelTests(TestCase):

    def setUp(self):
        Category.objects.create(name='dummy_category')
        Department.objects.create(name='dummy_department')
        Status.objects.create(name='dummy_status')
        Task.objects.create(
            name='dummy_task',
            category=Category.objects.get(name='dummy_category'),
            )
        User.objects.create(
            first_name='dummy_user',
            email_address='dummy_email@address.com',
            department=Department.objects.get(name='dummy_department'),
            )

    def test_startdatetime_gt_enddatetime(self):
        """
        create task log with start date time after end date time
        test constrain works not allowing the insertion of the log
        """
        started_datetime = timezone.now()
        finished_datetime = started_datetime - datetime.timedelta(days=1)
        wrong_start_finished_log = Log(
            task=Task.objects.get(name='dummy_task'),
            user=User.objects.get(email_address='dummy_email@address.com'),
            status=Status.objects.get(name='dummy_status'),
            started=started_datetime,
            finished=finished_datetime,
            )

        with self.assertRaises(Exception) as violates_constraint:
            wrong_start_finished_log.save()
        exception_msg = str(violates_constraint.exception)
        error_msg = 'violates check constraint'
        self.assertIn(error_msg, exception_msg)

    def test_startdatetime_lt_enddatetime(self):
        """
        create task log with start date time before end date time
        test 
        """
        started_datetime = timezone.now()
        finished_datetime = started_datetime + datetime.timedelta(days=1)
        correct_start_finished_log = Log(
            task=Task.objects.get(name='dummy_task'),
            user=User.objects.get(email_address='dummy_email@address.com'),
            status=Status.objects.get(name='dummy_status'),
            started=started_datetime,
            finished=finished_datetime,
            )
        try:
            correct_start_finished_log.save()
            msg = 'ok'
        except Exception as e:
            print('Issue with start or finish time in Log object', e)
        self.assertEqual(msg, 'ok')
