from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
	'''Exam model is for deciding the exam title'''
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title


class Score(models.Model):
	'''socre model is for containg all the users exams scores'''
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
	score = models.IntegerField()
