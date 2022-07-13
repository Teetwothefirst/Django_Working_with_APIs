#from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class link(models.Model):
    # class a_link:
    #     verbose_name = "link"
    #     verbose_name_plural = "link"
    target_url = models.URLField(max_length = 200)
    #description use models.charfield
    description = models.CharField(max_length= 200)
    #identifier use models.slugfield
    identifier = models.SlugField(max_length = 200, blank = True, unique = True)
    #author this is a foreign key to current user model use Make use of Django’s get_user_model function.
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="link_posts")
    # #created_date : A date-time column, use Django’s models.DateTimeField.
    Created_date = models.DateTimeField()
    # #active :  A boolean (True or False), determining if the shortened URL is publicly accessible. Make use of Django’s BooleanField. The default should be True.
    active = models.BooleanField(default = True)

