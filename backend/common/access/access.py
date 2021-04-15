from django.db import models
from django.conf import settings


class AccessRole(models.Model):
    """ Access role model """
    role = models.CharField(max_length=40, verbose_name='Role name')
    code_role = models.CharField(max_length=40, unique=True, verbose_name='Code role')

    def __str__(self):
        return f"{self.role}"

    class Meta:
        db_table = 'access_role'


class ItemAccess(models.Model):
    """ Abstract item access model """
    role = models.ForeignKey(AccessRole, on_delete=models.CASCADE, verbose_name='Role')
    can_access = models.BooleanField(default=True, verbose_name='Can access')
    can_change = models.BooleanField(default=False, verbose_name='Can change')
    can_remove = models.BooleanField(default=False, verbose_name='Can remove')

    def access_json(self):
        return {
            'role_id': self.role.id,
            'can_access': self.can_access,
            'can_change': self.can_change,
            'can_remove': self.can_remove
        }

    class Meta:
        abstract = True


class UserRole(models.Model):
    """ User role model """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    role = models.ForeignKey(AccessRole, on_delete=models.CASCADE, verbose_name='Role')

    def __str__(self):
        return f'{self.user} - {self.role}'

    class Meta:
        db_table = 'user_role'
