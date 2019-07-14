from rest_framework import serializers

from user_list.models import AppUser, Token

from stories import Failure, Success, arguments, story


class GetToken:

    @story
    @arguments('data')
    def create_token(I):
        I.create_token_data
        I.create_token_object
        I.check_token_object_is_valid
        I.save_token_object

    @story
    def create_token_data(I):
        I.load_user_login
        I.load_user_id
        I.create_token_value
        I.save_token_data

    def load_user_login(self, ctx):
        login = self.get_user_login(ctx.data)
        return Success(login=login)

    def load_user_id(self, ctx):
        user_id = self.get_user_id(ctx.login)
        return Success(user_id=user_id)

    def create_token_value(self, ctx):
        token = f'{ctx.login}_token'
        return Success(token=token)

    def save_token_data(self, ctx):
        token_data = {
            'token': ctx.token,
            'user': ctx.user_id
        }
        return Success(token_data=token_data)

    def create_token_object(self, ctx):
        token_object = TokenSerializer(data=ctx.token_data)
        return Success(token_object=token_object)

    def check_token_object_is_valid(self, ctx):
        if ctx.token_object.is_valid():
            return Success()
        return Failure()

    def save_token_object(self, ctx):
        ctx.token_object.save()
        return Success()

    def __init__(self, get_user_login, get_user_id):
        self.get_user_login = get_user_login
        self.get_user_id = get_user_id


#External dependencies
def get_user_login(data):
    return data['login']
def get_user_id_by_login(login):
    return AppUser.objects.get(login=login).pk


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'



    def save(self, **kwargs):
        super().save(**kwargs)
        get_token = GetToken(get_user_login, get_user_id_by_login)
        get_token.create_token(data=self.data)

        # token = f'{self.data["login"]}_token'
        # # if not Token.objects.filter(token=token).exists():
        # data = {
        #     'user': AppUser.objects.get(login=self.data['login']).pk,
        #     'token': token
        # }
        # new_token = TokenSerializer(data=data)
        # if new_token.is_valid():
        #     new_token.save()


class TokenSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())

    class Meta:
        model = Token
        fields = '__all__'
        # depth = 1
