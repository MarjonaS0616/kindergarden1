from django.db import models

class User(models.Model):
    KIDS = "bolalar"
    TEACHERS = "o'qituvchi"


    ROLES = (
        (KIDS, "bolalar"),
        (TEACHERS, "o'qituvchi")
    )

    user = models.CharField(max_length=200, choices=ROLES)
    full_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.full_name

class Kid(models.Model):
    dads_name = models.CharField(max_length=200)
    mothers_name = models.CharField(max_length=200)
    age = models.IntegerField()
    going = models.IntegerField()
    
    def __str__(self):
        return self.dads_name

class Teacher(models.Model):
    educated = models.CharField(max_length=200)
    experience = models.IntegerField()
    married = models.CharField(max_length=200)

    def __str__(self):
        return self.educated


class GroupOne(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    reception_day = models.DateTimeField(auto_now_add=True)
    until_when = models.DateField()

    def __str__(self):
        return self.user.full_name








