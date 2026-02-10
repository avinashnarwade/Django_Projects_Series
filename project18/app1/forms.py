from django import forms
from django.core.validators import MaxLenghthValidator,MinLenghthValidator
from django.core import MinValueValidator,MaxValueValidator
from django.core.validators import EmailValidator

def isalpha(name):
    if not name.isaplpha():
        raise forms.ValidationError("Should Contact only alphabest") 
    return name
class PersonForm(forms.Form):
    name = forms.CharField(validators=[MaxLenghthValidator(2,mesaage="name must contains atleast 2 letter"),MinLenghthValidator(15,message="name should contains more than 15 letters"),isalpha])
    age = forms.IntegerField(validators=[MinValueValidator(18,message="age must>=18"),MaxValueValidator(100,message="age must <100")])
    email = forms.CharField(validators=[EmailValidator(message="invalid Email Pattern")])
    