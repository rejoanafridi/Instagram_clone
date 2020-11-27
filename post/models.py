
from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
from django.db.models.signals import post_save
from django.utils.text import slugify




class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    caption = models.TextField(max_length=1500)
    posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()

    def get_absolute_url(self):
        return reversed("post_details", kwargs=[str(self.id)])

    def __str__(self):
        return self.posted


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')


class Stream(models.Model):
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stream_follower')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    date = models.DateTimeField()

    def add_post(sender, instanse, *args, **kwargs):
        post = instanse
        user = post.user
        followers = Follow.objects.all().filter(follwing=user)
        for follower in followers:
            stream = Stream(post=post, user=follower.follower,
                            date=post.posted, following=user)
            stream.save()


post_save.connect(Stream.add_post, sender=Post)
