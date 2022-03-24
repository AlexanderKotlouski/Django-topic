from django import forms


class TopicForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    count_posts = forms.IntegerField(label="Count posts")
    description = forms.CharField(label="Description", widget=forms.Textarea)
    date = forms.DateTimeField(label='Date created')

class EditTopicDescriptionForm(forms.Form):
   description = forms.CharField(label="Description", widget=forms.Textarea)


class PostForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)