from django.db import models

class TechnicalAchievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(
        max_length=100, 
        default='fas fa-trophy',
        help_text='Font Awesome icon class (e.g., fas fa-code, fas fa-trophy)'
    )
    order = models.IntegerField(default=0, help_text='Order for display (lower numbers appear first)')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Technical Achievement'
        verbose_name_plural = 'Technical Achievements'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
