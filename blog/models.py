from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    text  = models.TextField()
    date = models.DateTimeField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title
