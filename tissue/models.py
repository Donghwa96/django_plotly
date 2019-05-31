from django.db import models


class StatelessApp(models.Model):
    app_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)


class DashApp(models.Model):
    stateless_app = models.ForeignKey(StatelessApp, on_delete=models.PROTECT,
                                      unique=False, null=False, blank=False)
    instance_name = models.CharField(max_length=100, unique=True, blank=True, null=False)
    slug = models.SlugField(max_length=110, unique=True, blank=True)
    base_state = models.TextField(null=False, default="{}")
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    save_on_change = models.BooleanField(null=False, default=False)


