# django/myapp/Models/models_csv1.py

from django.db import models

class Ganison_dataset_1(models.Model):
    school_name = models.CharField(max_length=100)
    year = models.IntegerField()
    StudentID = models.CharField(max_length=20)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Year_Level = models.CharField(max_length=10)
    Class_Subject = models.CharField(max_length=100)
    Answers = models.IntegerField()
    Correct_Answers = models.IntegerField()
    Question_Number = models.IntegerField()
    Subject_Contents = models.CharField(max_length=200)
    Assessment_Areas = models.CharField(max_length=100)
    sydney_correct_count_percentage = models.FloatField()
    sydney_average_score = models.FloatField()
    sydney_participants = models.IntegerField()
    student_score = models.FloatField()
    student_total_assessed = models.FloatField()
    student_area_assessed_score = models.FloatField()
    total_area_assessed_score = models.FloatField()
    participant = models.CharField(max_length=100)
    correct_answer_percentage_per_class = models.FloatField()
    average_score = models.FloatField()
    school_percentile = models.FloatField()
    sydney_percentile = models.FloatField()
    strength_status = models.CharField(max_length=50)
    high_distinct_count = models.IntegerField()
    distinct_count = models.IntegerField()
    credit_count = models.IntegerField()
    participant_count = models.IntegerField()
    award = models.CharField(max_length=100)
    
    def __str__(self):
        return self.school_name
