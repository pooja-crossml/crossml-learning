from django.db import models


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from .validators import validate_file_extension
from django.utils import timezone

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    data = models.FileField(validators=[validate_file_extension], upload_to='media')
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title

