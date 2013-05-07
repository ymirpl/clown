from tastypie.resources import ModelResource
from tastypie import fields
from models import Tuit
from django.contrib.auth.models import User


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class TuitResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Tuit.objects.all()
        resource_name = 'tuit'
