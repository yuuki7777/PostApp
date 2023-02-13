from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class UserAccountManager(BaseUserManager):
    use_in_migrations = True
    #CreateAccountベース
    def _create_user(self, username, email, password, **extra_fields):

        if not username:
           raise ValueError('ユーザー名を設定してください')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #ユーザーアカウント作成
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)


    #スタッフアカウント作成
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_relationship', True)

        if extra_fields.get('is_staff') is not True:
           raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
           raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class BaseAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='ユーザーネーム', max_length=20, unique=True, null=False, blank=False, validators=[MinLengthValidator(5), RegexValidator(r'^[a-zA-Z0-9]*$',)])
    email = models.EmailField(verbose_name='メールアドレス', max_length=50, unique=True)
    created_date = models.DateTimeField(verbose_name='登録日', auto_now_add=True, editable=True)

    is_active = models.BooleanField(verbose_name='ログイン可否',  default=True)
    is_staff = models.BooleanField(verbose_name='スタッフ権限', default=False)
    is_superuser = models.BooleanField(verbose_name='管理者権限', default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email',]

    class Meta:
        verbose_name = _('アカウント')
        verbose_name_plural = 'アカウント'
    
    def __str__(self):
        return self.username