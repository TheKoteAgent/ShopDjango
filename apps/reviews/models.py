from django.db import models
from django.contrib.auth.models import User
from apps.main.models import Lot


class Review(models.Model):
    lot = models.ForeignKey(Lot, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    advantages = models.TextField(blank=True, max_length=100)
    disadvantages = models.TextField(blank=True, max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    helpful_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('lot', 'author')
        ordering = ['-created_at']
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return f"{self.author.username} - {self.title}"