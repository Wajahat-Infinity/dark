from website.models import Project, Blog, Images, WebsiteContent, Services, SocialLinks, Skills
from django.contrib import admin


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'created_at', 'updated_at')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'created_at', 'updated_at')


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'homeImage')


@admin.register(WebsiteContent)
class WebsiteContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'home_title', 'years_exp')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon', 'description')


@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'facebook', 'twitter', 'instagram', 'linkedin')


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_name', 'icon')

