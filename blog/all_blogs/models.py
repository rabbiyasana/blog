from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_email_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    blog_type= models.CharField(max_length=50, choices=BLOGS_TYPE)
    image = models.ImageField(upload_to='blogs_media/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f'{self.title} | {str(self.pub_date)}'