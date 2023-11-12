from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    rollno = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True, unique=True)
    team_member_count = models.PositiveIntegerField()
    team_member_names = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    project_link = models.URLField(max_length=200)

    def str(self):
        return f"Team {self.team_id} - {self.name}"
    