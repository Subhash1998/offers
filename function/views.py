from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from .forms import UserForm,FeatureForm,CompanyForm
from .models import UserProfile,Feature
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def homepage(request):
	return render(request,'function/homepage.html',)


def signup(request):
    context=RequestContext(request)
    registered=False
    if request.method=='POST':         
        form=UserForm(data=request.POST)
        if form.is_valid():
				first_name=form.cleaned_data['first_name']
				email=form.cleaned_data['email']
				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				user=form.save()
				user.set_password(user.password)
				user.save()
				registered=True
				return redirect('/function/')
				print "clear"   
        else:
            print form.errors
    else:
        form=UserForm()

    return render_to_response('function/register.html',{'form':form,'registered':registered},context)



def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print password
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                response=False
                login(request,user)
                return HttpResponseRedirect('/function/profile/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username,password)
            response=True
            return render(request,'function/login.html',{'response':response})
           
    else:
        return render_to_response('function/login.html', {}, context)

@login_required
def profile(request):
	args={'user':request.user}
	ob=Feature.objects.all()
	ob2=UserProfile.objects.get(user_id=request.user.id)
	return render(request,'function/profile.html',{'ob':ob,'ob2':ob2},args)

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/function/')

@login_required
def add_feature(request):
	context=RequestContext(request)
	registered=False
	if request.method=='POST':         
		form=FeatureForm(data=request.POST)
		if form.is_valid():
			feature_name=form.cleaned_data['feature_name']
			feature_detail=form.cleaned_data['feature_detail']
			a=Feature()
			a.company_name=request.user.userprofile.company
			a.feature_name=feature_name	
			a.feature_detail=feature_detail
			ob=UserProfile.objects.get(user_id=request.user.id)
			a.feature=ob
			a.save()
			registered=True
			return redirect('/function/profile/')   
		else:
			print form.errors
	else:
		form=FeatureForm()
	return render_to_response('function/add_feature.html',{'form':form,'registered':registered},context)

def add_company(request):
   if request.method=='POST':
      company_form = CompanyForm(request.POST)
      if company_form.is_valid():
         a=UserProfile.objects.get(user_id=request.user.id)
         a.company=request.POST.get('company')
         a.save()
         return redirect('/function/profile/')
   else:
      company_form= CompanyForm()
   return render(request,'function/profile.html',{'company_form':company_form})

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StockSerializer1,StockSerializer2,StockSerializer3

 
class Users_List(APIView):

      def get(self,request):
          stocks = User.objects.all()
          serializer=StockSerializer1(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass


class UserProfile_List(APIView):

      def get(self,request):
          stocks = UserProfile.objects.all()
          serializer=StockSerializer2(stocks,many=True)
          return Response(serializer.data)


      def post(self):
          pass

class Feature_list(APIView):

      def get(self,request):
          stocks = Feature.objects.all()
          serializer=StockSerializer3(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass


