from django.contrib import admin
from .models import user,repositories,languages
# Register your models here.
# class userRepoModel(admin.ModelAdmin):
admin.site.register(user)
admin.site.register(repositories)
admin.site.register(languages)