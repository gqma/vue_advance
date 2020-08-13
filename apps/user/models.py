# -- coding: gbk --
from django.db import models
from django.contrib.auth.models import AbstractUser


# ������д�û�ģ����, �̳��� AbstractUser
class UserModel(AbstractUser):
    """�Զ����û�ģ��"""

    # ���û�ģ���������� mobile �ֶ�
    mobile = models.CharField(max_length=11, unique=True, verbose_name='�ֻ���')

    # �Ե�ǰ������������:
    class Meta:
        db_table = 'tb_users'
        verbose_name = '�û�'
        verbose_name_plural = verbose_name

    # �� str ħ��������, �����û�����
    def __str__(self):
        return self.username
