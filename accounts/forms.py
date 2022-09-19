from accounts.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username',)
        
class UserchangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username')