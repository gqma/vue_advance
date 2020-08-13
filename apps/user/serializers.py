# -- coding: gbk --
# 针对models设计和声明序列化类
from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel  # 与Book表对应

        # 这三种情况不能同时使用
        # 1.取全部字段
        fields = "__all__"

        # 2.自定义包含字段
        # fields = ["id", "title", "pub_time"]
        # 输出：[{"id": 1, "title": "python开发", "pub_time": "2011-08-27"},...]

        # 3.排除某些字段
        # exclude = ["id", "category","author", "publisher"]
        # 输出：[{"title": "python开发", "pub_time": "2011-08-27"},...]
