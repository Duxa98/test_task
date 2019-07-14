from rest_framework import serializers

from user_list.models import AppUser, Token

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

    def save(self, **kwargs):
        super().save(**kwargs)
        data = {
            'user': AppUser.objects.get(login=self.data['login']).pk,
            'token': f'{self.data["login"]}_token'
        }
        new_token = TokenSerializer(data=data)
        if new_token.is_valid():
            new_token.save()

class TokenSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())

    class Meta:
        model = Token
        fields = '__all__'
        # depth = 1
