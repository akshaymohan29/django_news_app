from django.forms import forms
from .models import Contact

class UserContact():
    class Meta:
        model =Contact
        fields='__all__'