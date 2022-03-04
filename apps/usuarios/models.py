from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# from autoslug import AutoSlugField
from autoslug import AutoSlugField

class UsuarioManager(BaseUserManager):
    def create_user(self, email, name, last_name, password = None, **kwargs):
        if not email:
            raise ValueError('Insira um e-mail para continuar!')
        if not name:
            raise ValueError('Insira um nome para continuar!')
        if not last_name:
            raise ValueError('Insira um sobrenome para continuar!')

        usuario = self.model(
            email = self.normalize_email(email),
            name = name,
            last_name = last_name,
            **kwargs
        )
    
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        return usuario

    def create_superuser(self, email, name, last_name, password, **kwargs):
        usuario = self.create_user(
            email = self.normalize_email(email),
            name = name,
            last_name = last_name,
            password = password,
            **kwargs
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()

        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(verbose_name = "Nome", max_length = 60)
    last_name = models.CharField(verbose_name = "Sobrenome", max_length = 150)
    description = models.TextField(verbose_name = "Descrição", null = True, blank = True)
    email = models.EmailField(verbose_name = "E-mail", max_length = 194, unique = True) 
    slug = AutoSlugField(populate_from = 'get_full_name', unique_with = ['name', 'last_name'], unique = True, editable = True)
    is_active = models.BooleanField(verbose_name = "Usuário ativo", default = True)
    is_staff = models.BooleanField(verbose_name = "Usuário desenvolvedor", default = False)
    is_superuser = models.BooleanField(verbose_name = "Super usuário", default = False)
    time_registered = models.DateTimeField(verbose_name = "Data & Horário registrado", auto_now_add = True)
    
    USERNAME_FIELD = "email"    
    REQUIRED_FIELDS = ['name', 'last_name']
    
    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"
        app_label = "usuarios"

    def get_short_name(self):
        short_name = self.name.split()
        short_last_name = self.last_name.split()
        tam = len(short_last_name)
        return str(short_name[0] + " " + short_last_name[tam-1])

    def get_full_name(self):
        return str(self.name + " " + self.last_name)

    def get_absolute_url(self):
        return reverse('index')
        # return reverse('index', args=[str(self.id)]) CASO NECESSITASSE PASSAR ID

    def __str__(self):
        return self.get_full_name()
