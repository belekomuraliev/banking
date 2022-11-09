from django.urls import path
from .views import ListClientView, DetailClientView

urlpatterns = [
    path('', ListClientView.as_view(), name='client_view'),
    path('detail/<int:pk>', DetailClientView.as_view(), name='detail_client'),

]