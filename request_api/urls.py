from django.urls import path
from . import views
from .views import StockRequest

urlpatterns = [
    path('stockrequest/', StockRequest.as_view(), name='stock_request'),
]