from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from users.forms import LoginForm


class DashboardView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    """ View for user login
    """
    template_name = 'users/login.html'

    def get(self, *args, **kwargs):
        form = LoginForm()

        if self.request.user.is_authenticated:
            return redirect('dashboard')

        return render(self.request, self.template_name,{'form':form})

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)

        if form.is_valid():
            login(self.request, form.user)
            return redirect('dashboard')

        return render(self.request, self.template_name,
                      {'form':form}, status=400)
