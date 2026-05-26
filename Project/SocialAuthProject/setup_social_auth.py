import os
import django

# Setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialAuthProject.settings')
django.setup()

from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

def setup_project():
    print("=" * 60)
    print("🚀 Running SocialAuthProject Auto-Setup Script...")
    print("=" * 60)
    
    # 1. Update Site object
    try:
        site = Site.objects.get(id=1)
        site.domain = '127.0.0.1:8000'
        site.name = '127.0.0.1:8000'
        site.save()
        print("✅ Site ID 1 updated successfully to: 127.0.0.1:8000")
    except Site.DoesNotExist:
        site = Site.objects.create(id=1, domain='127.0.0.1:8000', name='127.0.0.1:8000')
        print("✅ Site ID 1 created successfully with: 127.0.0.1:8000")
    except Exception as e:
        print(f"❌ Error setting up Site: {e}")

    # 2. Create default superuser
    User = get_user_model()
    username = 'admin'
    email = 'admin@example.com'
    password = 'adminpassword123'
    
    if User.objects.filter(username=username).exists():
        print(f"ℹ️ Superuser '{username}' already exists.")
    else:
        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            print("✅ Default superuser created successfully!")
            print(f"   👤 Username: {username}")
            print(f"   🔑 Password: {password}")
            print(f"   📧 Email: {email}")
        except Exception as e:
            print(f"❌ Error creating superuser: {e}")
            
    print("=" * 60)
    print("🎉 Auto-setup completed successfully! You are ready to start the server.")
    print("   Run: python manage.py runserver")
    print("=" * 60)

if __name__ == '__main__':
    setup_project()
