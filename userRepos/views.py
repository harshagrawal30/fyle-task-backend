from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializer import userSerializer
# Create your views here.
from django.http import HttpResponse
from .models import user
from rest_framework.response import Response
import requests
import json
# def index(request):
#     def list(self,request):

class Userviewlist(viewsets.ViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
    
    def list(self):
        # print(self)
        print(self,'print')
        queryset = user.objects.all()
        serializer_class = userSerializer(queryset,many=True)
        return Response(serializer_class.data)
        # return queryset
    

    def retrieve(self,request,*args,**kwargs):
        params = kwargs
        # isuser = user.objects.filter()
        # queryset = user.objects.filter(username = params['pk'])
        # if queryset is not None:
        #     serializer_class = userSerializer(queryset,many=True)
        print(params['pk'])
        responseData={}
        fetchurl = 'https://api.github.com/users/'+params['pk']
        data = requests.get(fetchurl)
        print(data.text)
        jsonData = json.loads(data.text)
        if 'repos_url' in jsonData:
            repositories = requests.get(jsonData['repos_url'])
            repos= json.loads(repositories.text)

            reposData = []
            for repo in repos:
                langFetch = requests.get(repo['languages_url'])
                languagedata = json.loads(langFetch.text)
                languages =[]
                for i in languagedata:
                    languages.append(i)
                reposData.append({'id':repo['id'],'name':repo['name'],'description':repo['description'],'repository_language':languages,'repo_url':repo['html_url']})



            responseData = {'status':'success','id':jsonData['id'],'name':jsonData['name'],'username':jsonData['login'],
            'avatar':jsonData['avatar_url'],'location':jsonData['location'],
            'bio':jsonData['bio'],'twitter':jsonData['twitter_username'],
            'user_repositories':reposData
            }


        if 'message' in jsonData:
            print('error')
            return Response([{'status':'notfound','user_repositories':[],'id':None,'name':None,'avatar':None,'bio':None,'location':None,'username':None,'twitter':None}])
        else:
            return Response([responseData])