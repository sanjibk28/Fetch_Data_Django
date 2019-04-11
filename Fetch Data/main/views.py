from django.shortcuts import render
from django.http import HttpResponse
from.models import PlayerData
# Create your views here.

def homepage(request):

	return render(request=request,
				  template_name="main/site.html",
				  context={"playerdata":PlayerData.objects.all})
	django_list = list(PlayerData.objects.all())