from django.db import models

class Organizing_Committee(models.Model):
	unique_id = models.CharField(primary_key=True, max_length=25, unique=True)
	member_Name = models.CharField(max_length=100)
	member_Role = models.CharField(max_length=100)
	member_Department = models.CharField(max_length=100)
	member_YOG = models.IntegerField()
	member_InstaID = models.URLField(max_length=100)
	member_Pic = models.ImageField(upload_to='member_pics/', null=True, blank=True)
	def __str__(self):
		return self.member_Name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def __str__(self):
        return self.name