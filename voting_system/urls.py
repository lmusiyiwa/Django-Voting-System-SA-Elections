# voting_system/urls.py - This is the MAIN PROJECT's URL configuration

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. Django Admin Path
    path('admin/', admin.site.urls),
    
    # 2. Main Voting App URL (Delegates ALL voting/auth/home logic to vote/urls.py)
    path('', include('vote.urls')), 
    
    # 3. Auxiliary App (If you have a separate 'main' app, keep this. Otherwise, delete it.)
    # path('account/', include('main.urls')), 
]

# 4. Media files (Used for serving images/files in development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)