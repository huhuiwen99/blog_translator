from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Publish'))

# Model is designed to contain fields of data
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateField(auto_now=True)

    # slug is a method to create a meaningful url
    slug = models.SlugField(max_length=200, unique= True)
    # ForeighKey: get this value from another database table (is this case, a User database table)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE)
    # choose draft or published
    status = models.IntegerField(choices = STATUS, default=0)

    def __str__(self):
        return self.title

