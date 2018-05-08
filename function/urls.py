from django.conf.urls import url
from function import views

app_name='function'
urlpatterns= [
	
	url(r'^$',views.homepage,name='home'),
	url(r'^register/$', views.signup, name='signup'),
	url(r'^login/$',views.user_login,name='login'),
	url(r'^logout/$',views.user_logout,name='logout'),
	url(r'^All_Features/$',views.show_feature,name='show_feature'),
	url(r'^profile/$',views.profile,name='profile'),
	url(r'^profile/add_feature/$',views.add_feature,name='add_feature'),
	url(r'^profile/add_company/$',views.add_company,name='add_company'),
]