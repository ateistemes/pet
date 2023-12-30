from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from .forms import \
    LoginForm, \
    UserRegisterForm, \
    UserEditForm, \
    ProfileEditForm

from .models import Profile


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(
                user_form.cleaned_data['password']
            )

            new_user.save()

            Profile.objects.create(user=new_user)

            return render(request, 'registration/login.html')
            # return render(request, 'account/register_done.html', context={'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'account/register.html', context={'form': user_form})


# @login_required
# def edit_profile(request):
#     is_edited = None
#     if request.method == 'POST':
#         user_form = UserEditForm(
#             instance=request.user,
#             data=request.POST
#         )
#         profile_form = ProfileEditForm(
#             instance=request.user.profile,
#             data=request.POST,
#         )
#
#         if user_form.is_valid() and profile_form.is_valid():
#             is_edited = True
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully')
#         else:
#             messages.error(request, 'Error occured while updating your profile')
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#
#     return render(request, 'account/../templates/registration/edit.html', context={
#         "user_form": user_form,
#         "profile_form": profile_form,
#         "is_edited": is_edited
#     })
