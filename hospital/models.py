



from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(blank=True, null=True)
    head_of_department=models.CharField(max_length=100,blank=True,null=True)
    established_year=models.IntegerField(blank=True,null=True)
    icon = models.CharField(max_length=50, blank=True)   
    color = models.CharField(max_length=20, blank=True)
    

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.department.name})"

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Booking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name} on {self.date} at {self.time}"


