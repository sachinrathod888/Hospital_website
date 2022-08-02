from django.db import models

# Create your models here.

class Myuser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length = 100)



class PatientInfoNew(models.Model):
    Patient_name= models.CharField(max_length=100)
    age=models.IntegerField(null=False)
    mobile=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=250,null=True,blank=True,unique=True)
    gender=models.CharField(max_length=10)
    address=models.TextField(max_length=250,blank=True)
    complaint = models.TextField(max_length=250,blank=True)
    pulse=models.CharField(max_length = 3,blank=True)
    bp=models.CharField(max_length=3,blank=True)
    bsl=models.CharField(max_length=3,blank=True)
    temprature=models.CharField(max_length=3,blank=True)
    general_exam = models.CharField(max_length=250,blank=True)
    medicine_type1 = models.CharField(max_length=100,blank=True)
    medicine_name1 = models.CharField(max_length=100,blank=True)
    medicine_units1 = models.CharField(max_length =3,blank=True)
    medicine_detail1 = models.CharField(max_length=50,blank=True)
    medicine_type2 = models.CharField(max_length=100,blank=True,null=True)
    medicine_name2 = models.CharField(max_length=100,blank=True,null=True)
    medicine_units2 = models.CharField(max_length =3,blank=True,null=True)
    medicine_detail2 = models.CharField(max_length=50,blank=True,null=True)
    medicine_type3 = models.CharField(max_length=100,blank=True,null=True)
    medicine_name3 = models.CharField(max_length=100,blank=True,null=True)
    medicine_units3 = models.CharField(max_length =3,blank=True,null=True)
    medicin_detail3 = models.CharField(max_length=50,blank=True,null=True)
    medicine_type4 = models.CharField(max_length=100,blank=True,null=True)
    medicine_name4 = models.CharField(max_length=100,blank=True,null=True)
    medicine_units4 = models.CharField(max_length =3,blank=True,null=True)
    medicine_detail4 = models.CharField(max_length=50,blank=True,null=True)
    medicine_type5 = models.CharField(max_length=100,blank=True,null=True)
    medicine_name5 = models.CharField(max_length=100,blank=True,null=True)
    medicine_units5 = models.CharField(max_length =3,blank=True,null=True)
    medicine_detail5 = models.CharField(max_length=50,blank=True,null=True)
    other_information = models.TextField(max_length=200,blank=True)
    total_bill = models.CharField(max_length = 5,blank=True)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)






    







