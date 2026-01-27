from django.db import models

class TechnicalExpertise(models.Model):
    category = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0, help_text='Order for display (lower numbers appear first)')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Technical Expertise'
        verbose_name_plural = 'Technical Expertise'
        ordering = ['order', 'category']

    def __str__(self):
        return self.category
