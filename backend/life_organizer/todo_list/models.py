from django.db import models
from django.urls import reverse
import datetime
class Task(models.Model):
    title = models.CharField(max_length=127, default='')
    desciption = models.TextField(default='')
    is_subtask = models.BooleanField(default=False)
    parent = models.ForeignKey("Task", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    duo_date = models.DateField("duo date", default=datetime.date.today())
    whole_day = models.BooleanField(default=True)
    duo_time = models.TimeField("duo time", blank=True)


    

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
