from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordResetView
from .forms import discussion_forum
from .models import forum
from django.contrib.auth.decorators import login_required
# Create your views here.
class MyPasswordResetView(UserPassesTestMixin, PasswordResetView):
    template_name = 'users/password_reset.html'

    # https://docs.djangoproject.com/en/2.2/ref/contrib/auth/#django.contrib.auth.models.User.is_anonymous
    def test_func(self):
        return self.request.user.is_anonymous
@login_required()
def homepage(request):
	context={}
	reportee_form = discussion_forum(request.POST or None, request.FILES or None)
	context['reportee_form']=reportee_form
	if request.method == 'POST':
		email = request.POST.get('email')
		title = request.POST.get('title')
		text = request.POST.get('post_text')
		disc_forum = forum(email=email,title=title,post_text=text)
		disc_forum.save()
		context['data']='Data has been saved!!'
		context['email']=email
		context['title']=title
		context['text']=text
	return render(request,'python/homepage.html',context)
def first(request):
	return render(request,'users/first.html')