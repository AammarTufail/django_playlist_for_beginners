from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course_image = models.ImageField(upload_to='images/')
    difficulty_level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    instructor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

