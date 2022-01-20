from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import MessageForm
from profiles.models import UserProfile

# Create your views here.


def contact(request):
    """
    View to render contact page and allow users to message
    store owner directly from website
    """

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Thank you for your message,\
                              we will be in touch soon")
            return redirect("contact")
        else:
            messages.error(request,
                           "Something went wrong,\
                            Please try again")
            return redirect("contact")
    else:
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                form = MessageForm(initial={
                    "email": user_profile.user.email
                })
            except UserProfile.DoesNotExist:
                form = MessageForm()
        else:
            form = MessageForm()

    template = "contact/contact.html"
    context = {
        "form": form,
    }

    return render(request,
                  template,
                  context)
