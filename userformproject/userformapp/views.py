from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import UserFormForm
from .models import UserForm
from django.conf import settings

def user_form(request):
    if request.method == 'POST':
        form = UserFormForm(request.POST)
        if form.is_valid():
            user_form = form.save()
            email_from = settings.EMAIL_HOST_USER
            send_mail(
                'User Form Submitted',
                f'Thank you {user_form.name} for submitting the form!',
                email_from,
                [user_form.email],
                fail_silently=False,
            )
            return redirect('user_form_list')
    else:
        form = UserFormForm()
    return render(request, 'user_form.html', {'form': form})

def user_form_list(request):
    user_forms = UserForm.objects.all().order_by('-created_at')
    return render(request, 'user_form_list.html', {'user_forms': user_forms})
