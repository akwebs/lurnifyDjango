from django.forms import ModelForm
from .models import Register


class ContactForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'