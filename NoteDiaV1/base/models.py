from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField



class Topic(models.Model):
    name = models.CharField(max_length=200)
    MAJOR_CHOICES = [
        ('Computer Science','Computer Science'),
        ('Computer Information Systems','Computer Information Systems'),
        ('Bussiness Information Technology','Bussiness Information Technology'),
        ('Artifical Intelligence','Artifical Intelligence'),
        ('Data Science','Data Science'),
        ('CyberSecurity','CyberSecurity'),
        ('Computer Engineering','Computer Engineering'),
        ('Software Engineering','Software Engineering'),
    ]
    majors = MultiSelectField(max_length=200, choices=MAJOR_CHOICES,null=True)
   

    def __str__(self):
        return self.name
    
class User(AbstractUser):
   
    name =models.CharField(max_length=200,null=True)
    email =models.EmailField(unique=True,null=True)
    bio =models.TextField(null=True)
    avatar =models.ImageField(null=True,default="avatar.svg")
    isProfessor =models.BooleanField(default=False)
    major =models.CharField(max_length=70,
                            choices=[('Computer Science','Computer Science'),
                                     ('Computer Information Systems','Computer Information Systems'),
                                     ('Bussiness Information Technology','Bussiness Information Technology'),
                                     ('Artifical Intelligence','Artifical Intelligence'),
                                     ('Data Science','Data Science'),
                                     ('CyberSecurity','CyberSecurity'),
                                     ('Computer Engineering','Computer Engineering'),
                                     ('Software Engineering','Software Engineering'),],null=True)
    topic = models.ManyToManyField(Topic, through="UserTopic",limit_choices_to={'majors': major})

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =[]

class UserTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    media_file = models.FileField(null=True,upload_to='media/',blank=True)
    rating_stars = models.IntegerField(choices=(
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ), null=True, blank=True)
    rating_count = models.IntegerField(default=0)
    rating_average = models.FloatField(default=0)
    rating_sum= models.FloatField(default=0)
    rating = models.IntegerField(default=0)
    last_rated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='last_rated_room',blank=True)
    isProfessor =models.BooleanField(default=False)
    class Meta:
        ordering= ['-created']

    def __str__(self):
        return self.name 

    def ratingCount(self):
        return self.rating_count + 1
    def averageRating(self):
        return self.rating_sum / self.rating_count
    def ratingSum(self):
        return self.rating_sum + self.rating_average


class Message(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body= models.TextField() 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering= ['-updated','-created']


    def __str__(self):
        return self.body[0:50]
    
