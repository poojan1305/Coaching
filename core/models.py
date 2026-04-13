from django.db import models

BOARD_CHOICES = [
    ('SSC', 'SSC'),
    ('ICSE', 'ICSE'),
]

class StudentResult(models.Model):
    name = models.CharField(max_length=200)
    board = models.CharField(max_length=10, choices=BOARD_CHOICES)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()
    subject = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='toppers/', blank=True, null=True)
    is_topper = models.BooleanField(default=False)
    rank = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-score']

    def __str__(self):
        return f"{self.name} - {self.board} {self.year} ({self.score}%)"


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    board = models.CharField(max_length=10, choices=BOARD_CHOICES)
    year = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.year}"


class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%d %b %Y')}"
