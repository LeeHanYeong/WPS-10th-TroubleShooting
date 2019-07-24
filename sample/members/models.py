from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TYPE_DJANGO, TYPE_KAKAO, TYPE_FACEBOOK, TYPE_NAVER = 'django', 'kakao', 'facebook', 'naver'
    CHOICES_TYPE = (
        (TYPE_KAKAO, '카카오'),
        (TYPE_FACEBOOK, '페이스북'),
        (TYPE_NAVER, '네이버'),
    )
    type = models.CharField('유형', choices=CHOICES_TYPE, max_length=12, default=TYPE_DJANGO)
    first_name = None
    last_name = None
    name = models.CharField('이름', max_length=20, blank=True)

    def __str__(self):
        return self.name
