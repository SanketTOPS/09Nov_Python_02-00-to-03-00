from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from Userapp.models import User, Note, ContactMessage

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    users = User.objects.filter(is_superuser=False)
    notes_pending = Note.objects.filter(status='Pending').count()
    return render(request, 'admin/dashboard.html', {'users': users, 'notes_pending': notes_pending})

@user_passes_test(lambda u: u.is_staff)
def toggle_block(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_blocked = not user.is_blocked
    user.save()
    status = "blocked" if user.is_blocked else "unblocked"
    messages.success(request, f"User {user.username} has been {status}.")
    return redirect('admin_dashboard')

@user_passes_test(lambda u: u.is_staff)
def edit_user(request, user_id):
    user_obj = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user_obj.username = request.POST['username']
        user_obj.email = request.POST['email']
        user_obj.save()
        messages.success(request, f"User {user_obj.username} updated successfully.")
        return redirect('admin_dashboard')
    return render(request, 'admin/edit_user.html', {'user_obj': user_obj})

@user_passes_test(lambda u: u.is_staff)
def manage_notes(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'admin/manage_notes.html', {'notes': notes})

@user_passes_test(lambda u: u.is_staff)
def approve_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.status = 'Approved'
    note.save()
    
    # Send styled HTML confirmation mail
    subject = f'Note Approved: {note.title}'
    context = {
        'username': note.user.username,
        'note_title': note.title,
        'status': 'Approved',
        'dashboard_url': request.build_absolute_uri('/dashboard/')
    }
    html_message = render_to_string('admin/note_status_email.html', context)
    plain_message = f'Hi {note.user.username}, your note "{note.title}" has been approved.'
    
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [note.user.email], html_message=html_message)
    
    messages.success(request, f"Note '{note.title}' approved and user notified.")
    return redirect('manage_notes')

@user_passes_test(lambda u: u.is_staff)
def reject_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.status = 'Rejected'
    note.save()
    
    # Send styled HTML confirmation mail
    subject = f'Note Rejected: {note.title}'
    context = {
        'username': note.user.username,
        'note_title': note.title,
        'status': 'Rejected',
        'dashboard_url': request.build_absolute_uri('/dashboard/')
    }
    html_message = render_to_string('admin/note_status_email.html', context)
    plain_message = f'Hi {note.user.username}, your note "{note.title}" was rejected.'
    
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [note.user.email], html_message=html_message)
    
    messages.warning(request, f"Note '{note.title}' rejected and user notified.")
    return redirect('manage_notes')

@user_passes_test(lambda u: u.is_staff)
def view_messages(request):
    contact_messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'admin/contact_messages.html', {'contact_messages': contact_messages})
