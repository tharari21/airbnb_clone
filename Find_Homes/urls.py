from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('find-homes', views.find_home, name='find_homes'),
    path('find-homes/<str:pk>', views.get_home, name='get_home'),
    path('create-listing', views.create_listing, name='create_listing'),
    path('edit-listing', views.edit_listing, name='edit_listing'),
    path('edit-listing/update/<str:pk>', views.update_listing, name='update'),
    path('edit-listing/delete/<str:pk>', views.delete_listing, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
