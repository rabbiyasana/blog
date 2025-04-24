from django.db import models
from django.utils import timezone

class Blog(models.Model):
    BLOGS_TYPE=[
        ('food','Food'),
        ('travel','Travel'),
        ('lifestyle','Lifestyle'),
        ('technology','Technology'),
        ('fashion','Fashion'),
        ('fitness','Fitness'),
        ('health','Health'),
        ('education','Education'),
        ('business','Business'),
        ('entertainment','Entertainment')
    ]
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    blog_type= models.CharField(max_length=50, choices=BLOGS_TYPE)
    image = models.ImageField(upload_to='blogs_media/')

    def __str__(self):
        return self.title + ' | ' + str(self.pub_date)