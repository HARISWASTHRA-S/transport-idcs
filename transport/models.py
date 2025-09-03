from django.db import models

class Driver(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)

class BusIncharge(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)

class BusRoute(models.Model):
	route_name = models.CharField(max_length=100)
	bus_no = models.CharField(max_length=10)
	driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
	incharge = models.ForeignKey(BusIncharge, on_delete=models.CASCADE)

class BoardingPoint(models.Model):
	route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
	point_name = models.CharField(max_length=100)
	timing = models.TimeField()
	fee = models.DecimalField(max_digits=8, decimal_places=2)

class Student(models.Model):
	regno = models.CharField(max_length=20, unique=True)
	name = models.CharField(max_length=100)

class BusApplication(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
	boarding_point = models.ForeignKey(BoardingPoint, on_delete=models.CASCADE)
	branch = models.CharField(max_length=100, default="")
	year = models.CharField(max_length=10, default="")
	section = models.CharField(max_length=10, default="")
	mobile = models.CharField(max_length=15, default="")
	email = models.EmailField(default="")
	address = models.TextField(default="")
	parent_name = models.CharField(max_length=100, default="")
	parent_mobile = models.CharField(max_length=15, default="")
	emergency_contact = models.CharField(max_length=15, default="")
	applied_on = models.DateTimeField(auto_now_add=True)
