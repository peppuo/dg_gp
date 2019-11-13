from django.db import models
from django.db.models import F, Q


class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    notes = models.TextField()
    # Timestamp at creation
    registered = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.email_address


class Log(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    started = models.DateTimeField()
    finished = models.DateTimeField()

    def __str__(self):
        return self.task, self.user, self.started, self.finished

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(started__lt=F('finished')),
                name='started_lt_finished',
            ),
        ]
