from django.db import models
from posts.models import Post
from authors.models import Author


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self',  on_delete=models.CASCADE,  null=True,blank=True, related_name='replies' )

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
