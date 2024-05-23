from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

@receiver(post_migrate)
def create_default_task(sender, **kwargs):
    if sender.name == 'tasks':
        Task.objects.get_or_create(title='Default task', description='This is a default task')