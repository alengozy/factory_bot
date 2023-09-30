from django.db import models
from authentication.models import CustomUser
# Create your models here.
class Messages(models.Model):
    text = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
    
    def __str__(self):
        return f"Message ID: {self.pk} | Posted By: {self.user.username}"