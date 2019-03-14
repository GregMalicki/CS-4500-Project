from django import forms


class NewTaskForm(forms.Form):

    new_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'newName',
                'placeholder': 'New Task Name'
            }
        ))
    new_rate = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'newRate',
                'placeholder': 'Minutes'
            }
        ))
