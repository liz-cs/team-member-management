from django import forms

from team_member.models import TeamMember


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ["first_name", "last_name", "phone_number", "email", "status"]
        labels = {"status": ""}
        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': 'Enter first name here'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Enter last name here'}),
            "phone_number": forms.TextInput(attrs={'placeholder': 'Enter phone number here'}),
            "email": forms.TextInput(attrs={'placeholder': 'Enter email here'}),
            "status": forms.RadioSelect,
        }
