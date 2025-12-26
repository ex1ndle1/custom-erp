from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import token as account_activation_token
from .models import User
from django.core.mail import EmailMessage
from .forms import UserRegisterForm
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  
            user.save()
            
            current_site = get_current_site(request)    #added for finding my localhost domain
            mail_subject = 'Your account activationn'
            message = render_to_string('user/email_activation.html', {
               'user': user,
             'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),})
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'user/register.html')
    else:
        form = UserRegisterForm()
        
    return render(request, 'user/register.html', {'form': form})

def activate(request, uidb64, token): 
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        print(e)
        user = None
    print(uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('erp:home')
    else:
        return HttpResponse('Something wrong.')
    


def oauth_register(request):
    return render(request, 'user/oauth.html')



