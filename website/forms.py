from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_member_count', 'team_member_names', 'name', 'project_name', 'project_link']

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['team_member_names'].widget = forms.TextInput(attrs={'placeholder': 'Enter team member names'})

