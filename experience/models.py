from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, help_text='Optional human-friendly duration e.g. 2023 - Present')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['-start_date', '-end_date']

    def __str__(self):
        return f"{self.title} — {self.organization}"