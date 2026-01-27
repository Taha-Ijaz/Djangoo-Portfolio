from django.db import models

class Bio(models.Model):
    full_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    languages = models.CharField(max_length=200, blank=True, help_text='Comma separated languages or human readable')
    interests = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bio'
        verbose_name_plural = 'Bios'

    def __str__(self):
        return f"{self.full_name} — {self.job_title}" if self.job_title else self.full_name