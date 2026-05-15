import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import User, Note, ContactMessage
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
            
        otp = str(random.randint(100000, 999999))
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password, 
            otp=otp,
            fullname=fullname,
            mobile=mobile
        )
        
        # Send Styled HTML OTP Email
        subject = 'Verify your email - BatchProject'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        
        context = {'otp': otp, 'username': username, 'purpose': 'Verify Your Email'}
        html_message = render_to_string('user/otp_email.html', context)
        plain_message = f'Your OTP for registration is {otp}' # Fallback
        
        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
        
        request.session['temp_user_id'] = user.id
        messages.success(request, "OTP sent to your email. Please verify.")
        return redirect('verify_otp')
        
    return render(request, 'user/register.html')

def verify_otp(request):
    user_id = request.session.get('temp_user_id')
    if not user_id:
        return redirect('register')
        
    if request.method == 'POST':
        otp_input = request.POST['otp']
        user = User.objects.get(id=user_id)
        
        if user.otp == otp_input:
            user.is_verified = True
            user.otp = "" # Clear OTP
            user.save()
            messages.success(request, "Email verified successfully. You can now login.")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP")
            
    return render(request, 'user/verify_otp.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()
            
            # Send OTP Email
            subject = 'Reset your password - BatchProject'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            
            context = {'otp': otp, 'username': user.username, 'purpose': 'Reset Your Password'}
            html_message = render_to_string('user/otp_email.html', context)
            plain_message = f'Your OTP for password reset is {otp}'
            
            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
            
            request.session['reset_user_id'] = user.id
            messages.success(request, "OTP sent to your email for password reset.")
            return redirect('verify_reset_otp')
        except User.DoesNotExist:
            messages.error(request, "No user found with this email.")
            
    return render(request, 'user/forgot_password.html')

def verify_reset_otp(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        return redirect('forgot_password')
        
    if request.method == 'POST':
        otp_input = request.POST['otp']
        user = User.objects.get(id=user_id)
        
        if user.otp == otp_input:
            messages.success(request, "OTP verified. You can now reset your password.")
            return redirect('reset_password')
        else:
            messages.error(request, "Invalid OTP")
            
    return render(request, 'user/verify_otp_forgot.html')

def reset_password(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        return redirect('forgot_password')
        
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.otp = "" # Clear OTP
            user.save()
            
            del request.session['reset_user_id'] # Clear session
            messages.success(request, "Password reset successfully. You can now login.")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            
    return render(request, 'user/reset_password.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if not user.is_verified:
                request.session['temp_user_id'] = user.id
                messages.warning(request, "Please verify your email first.")
                return redirect('verify_otp')
            if user.is_blocked:
                messages.error(request, "Your account has been blocked by admin.")
                return redirect('login')
                
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            
    return render(request, 'user/login.html')

@login_required
def dashboard(request):
    if request.user.is_blocked:
        logout(request)
        messages.error(request, "Your account has been blocked.")
        return redirect('login')
    
    notes_count = request.user.notes.count()
    pending_notes = request.user.notes.filter(status='Pending').count()
    approved_notes = request.user.notes.filter(status='Approved').count()
    
    context = {
        'notes_count': notes_count,
        'pending_notes': pending_notes,
        'approved_notes': approved_notes,
    }
    return render(request, 'user/dashboard.html', context)

@login_required
def submit_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        file = request.FILES.get('file')
        
        Note.objects.create(
            user=request.user,
            title=title,
            description=description,
            category=category,
            file=file
        )
        messages.success(request, "Note submitted successfully and is pending approval.")
        return redirect('my_notes')
        
    return render(request, 'user/submit_note.html')

@login_required
def my_notes(request):
    notes = request.user.notes.all().order_by('-created_at')
    return render(request, 'user/my_notes.html', {'notes': notes})

def logout_view(request):
    logout(request)
    return redirect('login')

def about_view(request):
    return render(request, 'user/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_body = request.POST['message']
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_body
        )
        
        # Send Thank You Email
        email_subject = f'Thank you for contacting BatchProject!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        
        context = {'name': name}
        html_message = render_to_string('user/contact_thanks_email.html', context)
        plain_message = f'Hi {name}, thank you for reaching out to us. We have received your message and will get back to you soon.'
        
        send_mail(email_subject, plain_message, from_email, recipient_list, html_message=html_message)
        
        messages.success(request, "Your message has been sent successfully! A confirmation email has been sent.")
        return redirect('contact')
    return render(request, 'user/contact.html')
