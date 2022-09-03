from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    body = models.TextField()

    #self.self_author_title = str(self.title) + ' : ' + str(self.author)

    def __str__(self):
        return self.title

        


