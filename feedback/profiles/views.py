from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
    model = UserProfile
    fields = '__all__'

# def store_file(file):
#     with open('temp/image.jpg', 'wb+') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

# class CreateProfileView(View):
#     def get(self, request):
#         form=ProfileForm()
#         return render(request, "profiles/create_profile.html",{
#             'form': form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             user_profile = UserProfile(
#                 image=request.FILES['user_image']
#             )
#             user_profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html",{
#             'form': submitted_form
#         })

class ProfilesView(ListView):
    template_name = "profiles/user_profiles.html"
    model = UserProfile
    context_object_name = 'profiles'
