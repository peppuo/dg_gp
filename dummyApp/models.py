from django.db import models


# class Department(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()

#     def __str__(self):
#         return self.name


# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()

#     def __str__(self):
#         return self.name


# class Status(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()

#     def __str__(self):
#         return self.name


# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email_address = models.EmailField(max_length=254)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     notes = models.TextField()
#     # Timestamp at creation
#     registered = models.DateTimeField(auto_now_add=True, editable=False)

#     def __str__(self):
#         return self.email_address


# class Email(models.Model):
#     users = models.ManyToManyField(UserInfo)
#     number_emails = models.PositiveIntegerField()
#     sent = models.DateTimeField()

#     def __str__(self):
#         return self.users, self.number_emails


# class Task(models.Model):
#     user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     category = models.CharField
#     votes = models.IntegerField(default=0)
