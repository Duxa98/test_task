from rest_framework import serializers

from user_list.models import AppUser, Token


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())

    class Meta:
        model = Token
        fields = '__all__'
        # depth = 1
