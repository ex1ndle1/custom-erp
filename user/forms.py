from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=20,required=True)

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError('Name cant contain numbers!')
        
        return name
    class Meta:
        model = User
        fields = ['name', 'email']