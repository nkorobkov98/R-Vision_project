from django.urls import path
from .views import XMLFileUploadView

urlpatterns = [
    path('upload-xml/', XMLFileUploadView.as_view(), name='upload_xml'),
]
