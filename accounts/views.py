from django.contrib import messages
from django.core.mail import send_mail
# from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from accounts.models import Token


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    return redirect('/')















# from django.core.mail import send_mail
# from django.shortcuts import redirect
# from django.contrib import messages

# def send_login_email(request):
#     email = request.POST['email']
#     send_mail(
#         'Your login link for Superlists',
#         'body text tbc',
#         'noreply@superlists',
#         [email]
#     )
#     messages.success(
#         request,
#         "Check your email, we've sent you a link you can use to log in."
#     )
#     return redirect('/')


# def login(request):
#     return redirect('/')














# def send_login_email(request):
#     email = request.POST['email']
#     # send_mail(
#     #     'Your login link for Superlists',
#     #     'body text tbc',
#     #     'noreply@superlists',
#     #     [email],
#     # )
#     return redirect('/')















# from django.core.mail import send_mail
# from django.shortcuts import redirect

# def send_login_email(request):
#     return redirect('/')

















# import uuid
# import sys
# from django.contrib.auth import authenticate
# from django.core.mail import send_mail
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.shortcuts import redirect, render

# from accounts.models import Token


# def send_login_email(request):
#     email = request.POST['email']
#     uid = str(uuid.uuid4())
#     Token.objects.create(email=email, uid=uid)
#     print('saving uid', uid, 'for email', email, file=sys.stderr)
#     url = request.build_absolute_uri(f'/accounts/login?uid={uid}')
#     send_mail(
#         'Your login link for Superlists',
#         f'Use this link to log in:\n\n{url}',
#         'noreply@superlists',
#         [email],
#     )
#     return render(request, 'login_email_sent.html')


# def login(request):
#     print('login view', file=sys.stderr)
#     uid = request.GET.get('uid')
#     user = authenticate(uid=uid)
#     if user is not None:
#         auth_login(request, user)
#     return redirect('/')


# def logout(request):
#     auth_logout(request)
#     return redirect('/')