from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Yo this is required",
        "max_length": "Yo make it short bro"
    })
