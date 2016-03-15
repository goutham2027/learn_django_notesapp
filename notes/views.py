from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.db import transaction
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from django.contrib.auth.models import User
from .forms import RegistrationForm, NewNotesForm
from .models import Note, Membership, Plan

# TODO: Change views to class based views

def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    else:
        return login(request)

class SomeView(View):
    def get(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        return HttpResponse("hello")

@method_decorator(login_required, name='dispatch')
class NotesView(View):
    def post(self, request):
        form = NewNotesForm(request.POST)
        if form.is_valid():
            note = Note.objects.create(user=request.user,notes_text=form.cleaned_data['notes'])
            return HttpResponseRedirect('/home')

class NotesList(ListView):
    model = Note
    # context_object_name = 'all_notes'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NotesList, self).get_context_data(**kwargs)
        context['all_notes'] = self.request.user.profile.my_notes
        return context

@method_decorator(csrf_protect, name='dispatch')
class UserView(View):

    def get(self, request):
        form = RegistrationForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('registration/register.html', variables)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'],
                        email=form.cleaned_data['email']
                        )

                plan = Plan.objects.filter(pk=form.cleaned_data['plan']).first()

                membership = Membership.objects.create(
                        user=user,
                        plan=plan,
                        credits_left=plan.credits
                        )

                #TODO: If errors show render
                return HttpResponseRedirect('/register/success')


def register_success(request):
    return render_to_response('registration/success.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    form = NewNotesForm()
    user_profile = request.user.profile
    variables = RequestContext(request, {'my_notes': user_profile.my_notes(),
        'user':request.user, 'form':form, 'user_profile': user_profile})

    return render_to_response('home.html', variables)


