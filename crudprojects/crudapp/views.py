from django.shortcuts import render,redirect
from crudapp.models import Bike
from crudapp.forms import BikeForm
def read(request):
	bike=Bike.objects.all()
	return render(request,'apps/result.html',{'b':bike})
def insert(request):
	form=BikeForm()
	if request.method=="POST":
		form=BikeForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/insert.html',{'form':form})
def delete(request,id):
	b=Bike.objects.get(id=id)
	b.delete()
	return redirect('/result')
def update(request,id):
	bike=Bike.objects.get(id=id)
	if request.method=="POST":
		form=BikeForm(request.POST,instance=bike)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'b':bike})
