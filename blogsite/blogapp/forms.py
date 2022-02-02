from django.forms import forms
from .models import Contact

class ContactForm():
    class Meta:
        model =Contact
        fields='__all__'