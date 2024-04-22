from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import os



def file_size(value):
    limit= 15000000
    if value.size > limit:
        raise ValidationError('File size should not exceed 15 MB. Try re-uploading.')
        
class Post(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(null=False,blank=False,upload_to='Files', validators=[file_size, FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc', 'docx', 'ppt', 'pptx'])])
	content = models.TextField(max_length=500)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

        
