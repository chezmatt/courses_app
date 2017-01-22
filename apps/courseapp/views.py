from django.shortcuts import render, redirect, HttpResponse
from . import models

# CONTROLLER!!!


def index(request):
	getcourses = models.Course.objects.all()
	print getcourses.query
	print getcourses
	context = {
		'courses': getcourses,
	}
	return render(request, "courseapp/index.html", context)


def edit(request, course_id):
	context = {
		'id': course_id,
		'courses': getcourses,
	}
	return render(request, "courseapp/edit.html", context)


def add(request):
	course_name = request.POST['course_name']
	course_description = request.POST['course_description']
	models.Course.objects.create(name=course_name,description=course_description)
	print course_name
	print course_description

	# process the form here
	return redirect('/')


def delete(request, course_id):
	# process the form here
	return redirect('/')
