from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount

def login_view(request):
    """
    Landing / Login view. Redirects to dashboard if already authenticated.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'social_login/login.html')

@login_required(login_url='login')
def dashboard_view(request):
    """
    User dashboard displaying details fetched from Google or GitHub OAuth.
    """
    user = request.user
    social_accounts = SocialAccount.objects.filter(user=user)
    
    provider = None
    avatar_url = None
    full_name = user.get_full_name() or user.username
    email = user.email
    extra_data = {}
    
    if social_accounts.exists():
        social_account = social_accounts.first()
        provider = social_account.provider  # 'google' or 'github'
        avatar_url = social_account.get_avatar_url()
        extra_data = social_account.extra_data
        
        # Try to get full name from provider if django's default is empty
        if not full_name:
            if provider == 'google':
                full_name = extra_data.get('name', '')
            elif provider == 'github':
                full_name = extra_data.get('name', extra_data.get('login', ''))
                
        # Try to get avatar url
        if not avatar_url:
            if provider == 'google':
                avatar_url = extra_data.get('picture')
            elif provider == 'github':
                avatar_url = extra_data.get('avatar_url')
    
    # Standard fallback avatar
    if not avatar_url:
        avatar_url = f"https://api.dicebear.com/7.x/adventurer/svg?seed={user.username}"
        
    context = {
        'user': user,
        'provider': provider,
        'provider_display': provider.upper() if provider else 'Local',
        'avatar_url': avatar_url,
        'full_name': full_name,
        'email': email,
        'extra_data': extra_data,
    }
    
    return render(request, 'social_login/dashboard.html', context)
