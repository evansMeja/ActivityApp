from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login,authenticate,logout
from .models import *
from .utils import unique_slug_generator
from django.contrib.auth.decorators import user_passes_test

def user_login(request):
    template_name="activityApp/login.html"
    context={}
    return render(request,template_name,context)

def get_data_endpoint(request):
	data = {}
	for activity_status in ActivityStatus.objects.all():
		data["ok"] = activity_status.status
		members_list = ActivityMembers.objects.filter(activity_user_owner=activity_status)
		l=[]
		for member in members_list:
			member_dict = {}
			member_dict["id"]= member.id
			member_dict["real_name"]= member.real_name
			member_dict["tz"]= member.tz
			l1=[]
			ActivityPeriods_list = ActivityPeriods.objects.filter(activity_period_owner = member)
			for activityperiod in ActivityPeriods_list:
				activity_dict = {}
				activity_dict['start_time'] = activityperiod.start_time
				activity_dict['end_time'] = activityperiod.end_time
				l1.append(activity_dict)
			member_dict["activity_periods"]= l1
			l.append(member_dict)
		data["members"] = l
	return JsonResponse(data)

def save_activity_endpoint(request):
	member_id=int(request.POST.get('member'))
	start_date=request.POST.get('start_date')
	end_date=request.POST.get('end_date')
	ActivityPeriods_Obj = ActivityPeriods()
	ActivityPeriods_Obj.activity_period_owner = ActivityMembers.objects.get(pk=member_id)
	ActivityPeriods_Obj.start_time = start_date
	ActivityPeriods_Obj.end_time = end_date
	ActivityPeriods_Obj.save()
	data = {"msg":"save successfully"}	
	return JsonResponse(data)

def save_new_user_endpoint(request):
	name=request.POST.get('name')
	tz=request.POST.get('tz')
	ActivityMembers_Obj = ActivityMembers()
	ActivityMembers_Obj.activity_user_owner = ActivityStatus.objects.all().first()
	ActivityMembers_Obj.tz = tz
	ActivityMembers_Obj.real_name = name
	ActivityMembers_Obj.save()
	data = {"msg":"save successfully"}	
	return JsonResponse(data)
    
def validatemylogin(request):
	data = {
		'is_logged_in_admin': request.user.is_authenticated and request.user.is_staff
	}	
	if not data['is_logged_in_admin']:
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			if request.user.is_staff:
				data['is_logged_in_admin'] = True
	return JsonResponse(data)

def dashboard(request):
    template_name="activityApp/dashboard.html"
    context={}
    return render(request,template_name,context)

def add_user(request):
    template_name="activityApp/add_user.html"
    context={}
    return render(request,template_name,context)

def add_activity(request):
	template_name="activityApp/add_activity.html"
	ActivityMembers_List = ActivityMembers.objects.all()
	context={"ActivityMembers_List":ActivityMembers_List}
	return render(request,template_name,context)

