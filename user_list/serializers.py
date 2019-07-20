# from dependencies import Injector
from rest_framework import serializers

from user_list.models import AppUser, Token


# from stories import Failure, Success, arguments, story


class AppUserSerializer(serializers.ModelSerializer):
    token = serializers.SlugRelatedField(
        read_only=True,
        slug_field='token'
    )

    class Meta:
        model = AppUser
        fields = '__all__'  # TODO: перечислять все поля лучше?

    # def save(self, **kwargs):
    #     super().save(**kwargs)
    #     GenerateTokenContainer.generate_token.generate(login=self.data['login'])


class AppUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
#
#
# class GenerateToken:
#
#     @story
#     @arguments('login')
#     def generate(I):
#         I.create_token_data
#         I.create_token_object
#         I.check_token_object_is_valid
#         I.save_token_object
#
#     @story
#     def create_token_data(I):
#         I.load_user_id
#         I.create_token_value
#         I.save_token_data
#
#     def load_user_id(self, ctx):
#         user_id = self.user_id_getter.get_user_id_by_login(ctx.login)
#         return Success(user_id=user_id)
#
#     def create_token_value(self, ctx):
#         token = f'{ctx.login}_token'
#         return Success(token=token)
#
#     def save_token_data(self, ctx):
#         token_data = {
#             'token': ctx.token,
#             'user': ctx.user_id
#         }
#         return Success(token_data=token_data)
#
#     def create_token_object(self, ctx):
#         token_object = TokenSerializer(data=ctx.token_data)
#         return Success(token_object=token_object)
#
#     def check_token_object_is_valid(self, ctx):
#         if ctx.token_object.is_valid():
#             return Success()
#         return Failure('token object is not valid')
#
#     def save_token_object(self, ctx):
#         ctx.token_object.save()
#         return Success()
#
#     def __init__(self, user_id_getter):
#         self.user_id_getter = user_id_getter
#
#
# class UserIdGetter:
#     def get_user_id_by_login(self, login):
#         return AppUser.objects.get(login=login).pk
#
#
# class GenerateTokenContainer(Injector):
#     generate_token = GenerateToken
#     user_id_getter = UserIdGetter
