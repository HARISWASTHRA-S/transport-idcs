from django.shortcuts import render, redirect
from .models import BusRoute, BoardingPoint, Driver, BusIncharge, Student, BusApplication
from django.contrib import messages

def home(request):
	routes = BusRoute.objects.all().select_related('driver', 'incharge')
	boarding_points = BoardingPoint.objects.select_related('route')
	context = {
		'routes': routes,
		'boarding_points': boarding_points,
	}
	return render(request, 'home.html', context)

def apply_bus(request):
	if request.method == 'POST':
		regno = request.POST.get('regno')
		name = request.POST.get('name')
		branch = request.POST.get('branch')
		year = request.POST.get('year')
		section = request.POST.get('section')
		mobile = request.POST.get('mobile')
		email = request.POST.get('email')
		address = request.POST.get('address')
		parent_name = request.POST.get('parent_name')
		parent_mobile = request.POST.get('parent_mobile')
		emergency_contact = request.POST.get('emergency_contact')
		route_id = request.POST.get('route')
		point_id = request.POST.get('boarding_point')
		student, created = Student.objects.get_or_create(regno=regno, defaults={'name': name})
		route = BusRoute.objects.get(id=route_id)
		point = BoardingPoint.objects.get(id=point_id)
		BusApplication.objects.create(
			student=student,
			route=route,
			boarding_point=point,
			branch=branch,
			year=year,
			section=section,
			mobile=mobile,
			email=email,
			address=address,
			parent_name=parent_name,
			parent_mobile=parent_mobile,
			emergency_contact=emergency_contact
		)
		routes = BusRoute.objects.all()
		boarding_points = BoardingPoint.objects.all()
		return render(request, 'apply_bus.html', {
			'routes': routes,
			'boarding_points': boarding_points,
			'request': request,
			'messages': ['Applied successfully!']
		})
	routes = BusRoute.objects.all()
	boarding_points = BoardingPoint.objects.all()
	return render(request, 'apply_bus.html', {
		'routes': routes,
		'boarding_points': boarding_points,
		'request': request
	})
