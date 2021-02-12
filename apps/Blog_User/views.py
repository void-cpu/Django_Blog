from random import randint

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
        phone = request.data.get("phone")
        password, userNewPassword, userNewAgentPassword = request.data.get('password'), \
                                                          request.data.get("userNewPassword"), \
                                                          request.data.get("userNewAgentPassword")

        if not UserViewSet.is_valid(phone, password, userNewPassword, userNewAgentPassword):
            return Response({"default": Static_Message.Passing_Error.value}, status=status.HTTP_400_BAD_REQUEST)
        if UserViewSet.same_code(a_password=userNewPassword, b_password=userNewAgentPassword):
            try:
                if pk is not None:
                    _object = UserModels.objects.get(id=pk)
                else:
                    _object = UserModels.objects.get(phone=phone)
            except UserModels.DoesNotExist:
                return Response({"default": Static_Message.info_Dont_Found.value}, status=status.HTTP_401_UNAUTHORIZED)
            if check_password(password, _object.pass_word):
                _object.pass_word = make_password(userNewPassword)
                _object.save()
                return Response(UserSerializers_all.Srlist(_object, many=False).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"default": Static_Message.Info_Error.value}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"default": Static_Message.Info_Error.value}, status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['get'], detail=True)
    def set_phone_code(self, request, pk=None):
        phone = request.data.get("phone")
        if UserViewSet.is_valid(phone):
            return Response({"phone": phone, "message": randint(10000, 999999)}, status=status.HTTP_200_OK)
        else:
            return Response({"default": Static_Message.Passing_Error.value}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def get_phone_code(self, request, pk=None):
        phone = request.data.get("phone")
        Get_Phone, Set_Phone = request.data.get('Get_Phone'), request.data.get('Set_Phone')
        if UserViewSet.is_valid(phone, Get_Phone, Set_Phone):
            _is_Bool = UserViewSet.same_code(a_password=Get_Phone, b_password=Set_Phone)
            return Response({'phone': phone, "message": _is_Bool}, status=status.HTTP_200_OK)
        else:
            return Response({"default": Static_Message.Passing_Error.value}, status=status.HTTP_400_BAD_REQUEST)