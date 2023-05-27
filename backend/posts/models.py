from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField()
    email= models.EmailField()
    password= models.CharField()
    first_name = models.CharField()
    last_name= models.CharField()
    profile_description=models.TextField()
    profile_image= models.ImageField()

class BlogPostCategory(models.Model):
    name= models.CharField()

class BlogPostTag(models.Model):
    name= models.CharField()


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    #Added below to avoid making Blog post type model
    blog_post_type= models.CharField()
    expected_read_time= models.CharField()
    unit_of_time= models.CharField()
    post_image= models.ImageField()
    post_image_link= models.CharField()
    post_video= models.FileField()
    post_video_link= models.CharField()
    post_audio=models.FileField()
    post_audio_link= models.CharField()
    content = models.TextField()
    promotion= models.TextField()
    pinned= models.BooleanField()
    notes= models.TextField()
    comments_enabled= models.BooleanField()
    post_preview= models.TextField()
    about_the_author= models.TextField()
    slug= models.TextField()
    status= models.TextField()
    ## need to confirm below feild again
    post_category= models.OneToOneField(BlogPostCategory, on_delete = models.CASCADE, primary_key = True)
   
    post_tag= models.ManyToManyField(BlogPostTag)
    user= models.ForeignKey(User)

class Comment(models.Model):
    content= models.TextField
    # Comment belong to one Post but post can have many comments : This is One to Many Relationship : Django -> Use foreign key 
    post =models.ForeignKey(BlogPost)
    user= models.ForeignKey(User)

class CommentLikes(models.Model):
    comment_id= models.ForeignKey(Comment)
    user_id=models.ForeignKey(User)

class BlogPostLikes(models.Model):
    post= models.ForeignKey(BlogPost)
    user_id=models.ForeignKey(User)
    
class Inquiry(models.Model):
    first_name=models.CharField()
    last_name=models.CharField()
    email= models.EmailField()
    phone= models.PositiveIntegerField()
    company= models.CharField()
    contact_reason= models.TextField()
    message_subject=models.TextField()
    message= models.TextField()
    viewed=models.BooleanField()

class BlogPostFav(models.Model):
    post= models.ForeignKey(BlogPost)
    user_id=models.ForeignKey(User)


## Use Later - 
class SocialMediaPlatform(models.Model):
    name=models.TextField()
    icon=models.TextField()
    description= models.TextField()

class UserSocialMedia(models.Model):
    platform= models.ForeignKey(SocialMediaPlatform)
    link = models.TextField()
    user= models.ForeignKey(User)










