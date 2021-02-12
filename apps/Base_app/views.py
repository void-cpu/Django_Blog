from enum import Enum

from rest_framework.viewsets import ModelViewSet


class Static_Message(Enum):
    Passing_Error = "参数不全"
    info_Dont_Found = "请求数据不存在"
    Info_Error = "参数信息有误"


class BaseViewSet(ModelViewSet):
    @staticmethod
    def is_valid(*args):
        return all([*args])

    @staticmethod
    def same_code(a_password, b_password):
        return a_password == b_password
