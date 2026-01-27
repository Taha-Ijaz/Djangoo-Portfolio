from django.db import models

class Skill(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='General', blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.level})" if self.level else self.name