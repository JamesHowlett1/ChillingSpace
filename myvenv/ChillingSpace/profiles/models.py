from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length = 50, blank=True)
    last_name = models.CharField(max_length = 50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 200, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars')
    nickname = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    friends = models.ManyToManyField(User, blank=True, related_name ='friends')

    def __str__(self):
        return f"{self.nickname}-{self.created.strftime('%d-%m-%y')}"

STATUS_CHOICES=(
    ('send', 'send'),
    ('accepted', 'accepted'),
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'sender')
    receiver = models.ForeignKey(Profile, on_delete = models.CASCADE,related_name = 'receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
