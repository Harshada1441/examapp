from django.db import models

class Questions(models.Model):

    qid = models.AutoField(primary_key=True)

    qtext = models.CharField(max_length=250)

    op1 = models.CharField(max_length=250)
    op2 = models.CharField(max_length=250)
    op3 = models.CharField(max_length=250)
    op4 = models.CharField(max_length=250)

    correct_ans = models.CharField(max_length=250)

    subject = models.CharField(max_length=250)


class Student_info(models.Model):

    username = models.CharField(max_length=250)

    password = models.CharField(max_length=250)

    mobno = models.BigIntegerField()


class Result(models.Model):

    user = models.ForeignKey(Student_info, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=250)
    score = models.IntegerField()

    