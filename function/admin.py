from django.contrib import admin
from .models import UserProfile,Feature

class FeatureAdmin(admin.ModelAdmin):
	list_display=['feature_name']

class feature(admin.TabularInline):
	model = Feature
	extra = 1

class user_feature(admin.ModelAdmin):
	inlines = [feature,]

admin.site.register(UserProfile,user_feature)
admin.site.register(Feature,FeatureAdmin)
