from django.forms import models

from models import Tuit


class AddTuitForm(models.ModelForm):
    class Meta:
        model = Tuit
        exclude = ('user', )
