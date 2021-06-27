from .models import Employee
from django import forms


class InputForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['daily_screen_time', 'commute_distance', 'breakfast_food', 'lunch_food', 'dinner_food', 'snack_food', 'did_you_recycle_aluminum_today', 'did_you_recycle_plastic_today', 'did_you_recycle_glass_today']
       
        '''
        daily_screen_time = forms.IntegerField(label='daily screen time')
        commute_distance = forms.IntegerField(label='commute distance')
        breakfast_food = forms.CharField(label='breakfast food', max_length=100)
        lunch_food = forms.CharField(label='lunch food', max_length=100)
        dinner_food = forms.CharField(label='dinner food', max_length=100)
        snack_food = forms.CharField(label='snack food', max_length=100)

        recycle_aluminum = forms.BooleanField(label='Recycle Aluminum?')
        recycle_plastic = forms.BooleanField(label='Recycle Plastic?')
        recycle_glass = forms.BooleanField(label='Recycle Glass?')'''