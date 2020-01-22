from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Q


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_description = models.TextField()
    cat_order = models.IntegerField()

    def __str__(self):
        return self.cat_name


class Importance(models.Model):
    imp_name = models.CharField(max_length=200)
    imp_description = models.TextField()
    imp_order = models.IntegerField()

    def __str__(self):
        return self.imp_name


class Status(models.Model):
    sta_name = models.CharField(max_length=200)
    sta_description = models.TextField()
    sta_order = models.IntegerField()

    def __str__(self):
        return self.sta_name


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    importance = models.ForeignKey(Importance, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    duedate = models.DateTimeField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    finishdate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str((self.name, self.category, self.status))

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(startdate__lt=F('finishdate')),
                name='startdate_lt_finishdate',
            ),
        ]
