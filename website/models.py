from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PostType(models.Model):
    post_type = models.CharField(max_length=50)

    class Meta:
        pass


class Post(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(User, related_name="post")
    summary = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    attachment_link = models.CharField(max_length=255, blank=True, null=True)
    post_type = models.ForeignKey(PostType, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Comment(models.Model):
    """
    Description: Model Description
    """
    post = models.ForeignKey(Post, related_name="comments")
    author = models.ForeignKey(User, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class ElementWord(models.Model):
    """
    Description: Model Description
    """
    author = models.ForeignKey(User, related_name="element_words")
    testimony = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Task(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_kenalan = models.BooleanField(default=False)
    attachment_link = models.CharField(max_length=255, blank=True, null=True)
    expected_amount = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Submission(models.Model):
    """
    Description: Model Description
    """
    user = models.ForeignKey(User, related_name="submissions")
    task = models.ForeignKey(Task, related_name="submissions")
    file_link = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    attachment_link = models.CharField(max_length=255, blank=True, null=True)
    expected_attendee = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Album(models.Model):
    name = models.CharField(max_length=255)
    album_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class TaskStatistic(models.Model):
    task = models.ForeignKey(Task, related_name='statistics')
    expected_amount = models.SmallIntegerField(blank=True, null=True)
    amount = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class EventStatistic(models.Model):
    event = models.ForeignKey(Event)
    attendee = models.SmallIntegerField(default=0)
    on_time = models.SmallIntegerField(default=0)
    late = models.SmallIntegerField(default=0)
    permission = models.SmallIntegerField(default=0)
    absent = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class UserStatistic(models.Model):
    user = models.ForeignKey(User, related_name='user_statistics')
    name = models.CharField(max_length=255)
    expected_amount = models.SmallIntegerField(default=0)
    amount = models.SmallIntegerField(default=0)

    class Meta:
        pass
