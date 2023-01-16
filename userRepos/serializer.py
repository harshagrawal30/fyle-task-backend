from rest_framework import serializers,fields

from .models import user,repositories,languages




class languageSerializer(serializers.ModelSerializer):
    class Meta:
        model = languages
        fields = '__all__'


class reposSerializer(serializers.ModelSerializer):
    repository_language = languageSerializer(many=True,read_only=True)
    class Meta:
        model = repositories
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    user_repositories = reposSerializer(many=True,read_only=True)
    class Meta:
        model = user
        fields = '__all__'
