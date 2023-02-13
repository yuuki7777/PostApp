from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=50, blank=False, null=True)
    content = models.TextField(verbose_name='本文', max_length=800, blank=False, null=True)

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿'
    
    def __str__(self):
        return self.title
        