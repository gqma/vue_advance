# -- coding: gbk --
# ���models��ƺ��������л���
from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel  # ��Book���Ӧ

        # �������������ͬʱʹ��
        # 1.ȡȫ���ֶ�
        fields = "__all__"

        # 2.�Զ�������ֶ�
        # fields = ["id", "title", "pub_time"]
        # �����[{"id": 1, "title": "python����", "pub_time": "2011-08-27"},...]

        # 3.�ų�ĳЩ�ֶ�
        # exclude = ["id", "category","author", "publisher"]
        # �����[{"title": "python����", "pub_time": "2011-08-27"},...]
