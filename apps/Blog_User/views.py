from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .Serializers import *
from ..Base_app.views import Static_Message


class UserViewSet(ModelViewSet):
    """
    角色信息管理
    """
    queryset = UserModels.objects.all()
    serializer_class = UserSerializers_all.Srlist

    @staticmethod
    def is_valid(*args):
        return all([*args])

    @staticmethod
    def same_code(a_password, b_password):
        return a_password == b_password

    def get_serializer_class(self):
        # 根据请求类型动态变更serializer
        if self.action == 'create':
            return UserSerializers_all.UserCreate
        elif self.action == 'update':
            return UserSerializers_all.UserUpdate
        elif self.action == 'list':
            return UserSerializers_all.Srlist
        return UserSerializers_all.UserReadOnly

    def create(self, request, *args, **kwargs):
        password = request.data['pass_word'] if 'pass_word' in request.data else None
        password = make_password(password)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(pass_word=password)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def user_login(self, request, pk=None):
        username, password = request.data.get("username"), request.data.get("password")
        if not UserViewSet.is_valid(username, password):
            return Response({"default": Static_Message.Passing_Error.value}, status=status.HTTP_400_BAD_REQUEST)
        try:
            _object = UserModels.objects.get(user_name=username)
        except UserModels.DoesNotExist:
            return Response({"default": Static_Message.info_Dont_Found.value}, status=status.HTTP_401_UNAUTHORIZED)
        if check_password(password, _object.pass_word):
            return Response(UserSerializers_all.Srlist(_object, many=False).data, status=status.HTTP_200_OK)
        else:
            return Response({"default": Static_Message.Info_Error.value}, status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['put'], detail=True)
    def set_password(self, request, pk=None):
        password, userNewPassword, userNewAgentPassword = request.data.get('password'), \
                                                          request.data.get("userNewPassword"), \
                                                          request.data.get("userNewAgentPassword")

        if not UserViewSet.is_valid(password, userNewPassword, userNewAgentPassword):
            return Response({"default": Static_Message.Passing_Error.value}, status=status.HTTP_400_BAD_REQUEST)
        if UserViewSet.same_code(a_password=userNewPassword, b_password=userNewAgentPassword):
            _object = UserModels.objects.get(id=pk)
            if check_password(password, _object.pass_word):
                _object.password = make_password(userNewPassword)
                _object.save()
                return Response(UserSerializers_all.Srlist(_object, many=False).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"default": Static_Message.Info_Error.value}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"default": Static_Message.Info_Error.value}, status=status.HTTP_401_UNAUTHORIZED)
