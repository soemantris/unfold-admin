# Unfold Admin
Ini adalah tema admin untuk proyek Django dalam membuat antarmuka admin default dan dibuat untuk para pengembang Django guna menyusun panel administrasi Django yang menakjubkan secara efisien, sekaligus memecahkan sebagian besar masalah UI/UX umum.
# Installasi
Perintah installasi
```python
pip install django-unfold
```
Yang perlu dilakukan setelah instalasi adalah meletakkan aplikasi baru di awal INSTALLED_APPS
```python
# settings.py

INSTALLED_APPS = [
    "unfold",  # sebelum django.contrib.admin
    "django.contrib.admin",  # required
]
```
Kemudian ke file admin.py dan tambahkan ini:
```python
# admin.py

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
```
# Sumber
https://unfoldadmin.com/docs/installation/quickstart/
