from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=20)
    email= models.EmailField()
    password= models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    profile_description=models.TextField()
    profile_image= models.TextField()

class BlogPostCategory(models.Model):
    name= models.CharField(max_length=30)

class BlogPostTag(models.Model):
    name= models.CharField(max_length=30)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    #Added below to avoid making Blog post type model
    blog_post_type= models.CharField(max_length=50)
    expected_read_time= models.CharField(max_length=20)
    unit_of_time= models.CharField(max_length=10)
    post_image= models.ImageField()
    post_image_link= models.TextField()
    post_video= models.FileField()
    post_video_link= models.TextField
    post_audio=models.FileField()
    post_audio_link= models.TextField()
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
    post_category= models.OneToOneField(BlogPostCategory, on_delete = models.DO_NOTHING, primary_key = True)
   
    post_tag= models.ManyToManyField(BlogPostTag)
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Comment(models.Model):
    content= models.TextField
    # Comment belong to one Post but post can have many comments : This is One to Many Relationship : Django -> Use foreign key 
    post =models.ForeignKey(BlogPost,on_delete=models.DO_NOTHING )
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING)

class CommentLikes(models.Model):
    comment_id= models.ForeignKey(Comment, on_delete=models.DO_NOTHING)
    user_id=models.ForeignKey(User, on_delete=models.DO_NOTHING)

class BlogPostLikes(models.Model):
    post= models.ForeignKey(BlogPost, on_delete=models.DO_NOTHING)
    user_id=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
class Inquiry(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email= models.EmailField()
    phone= models.PositiveIntegerField()
    company= models.CharField(max_length=50)
    contact_reason= models.TextField()
    message_subject=models.TextField()
    message= models.TextField()
    viewed=models.BooleanField()

class BlogPostFav(models.Model):
    post= models.ForeignKey(BlogPost, on_delete=models.DO_NOTHING)
    user_id=models.ForeignKey(User, on_delete=models.DO_NOTHING)


## Use Later - 
class SocialMediaPlatform(models.Model):
    name=models.TextField()
    icon=models.TextField()
    description= models.TextField()

class UserSocialMedia(models.Model):
    platform= models.ForeignKey(SocialMediaPlatform, on_delete=models.DO_NOTHING)
    link = models.TextField()
    user= models.ForeignKey(User,on_delete=models.DO_NOTHING)










