from django.db import models

class TodoModel(models.Model):
    TodoText=models.CharField(max_length=200)
    Added_date=models.DateTimeField(auto_now=True)
    Update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.TodoText