from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

class Department(models.Model):
    departmentName = models.CharField("Department name", max_length=255)
    cabinetNumber = models.IntegerField("Cabinet number", max_length=4)

    def __str__(self):
        return self.departmentName

    class Meta:
        verbose_name_plural = "Departments"


class Ticket(models.Model):
    problemDescription = models.TextField("Problem description")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Employee", default="")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Department", default="")
    ticketDate = models.DateTimeField(default=datetime.now)
    photo = models.ImageField("Photo", upload_to='problems')
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.problemDescription

    def get_absolute_url(self):
        return reverse('ticketDetails', args=[self.pk])

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Tickets"


'''class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, related_name="comments", on_delete=models.CASCADE)
    commentDateTime = models.DateTimeField(default=datetime.now)
    comment = models.TextField("Add comment")

    def __str__(self):
        return self.comment'''

