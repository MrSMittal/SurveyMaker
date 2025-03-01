from django.db import models
from django.contrib.auth.models import User

QUESTION_TYPES = [
    ('radio', 'Radio Button'),
    ('dropdown', 'Dropdown'),
    ('checkbox', 'Checkbox'),
    ('number', 'Number'),
    ('text', 'Text'),
    ('textarea', 'Textarea'),
]

class Survey(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.text

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return f"Response by {self.user.username} for {self.question.text}"
