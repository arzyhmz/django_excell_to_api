from django.urls import path, include
from .views import login_view, log_out, index

app_name = "backoffice"
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('log_out/', log_out, name='log_out'),
    path('generate-qrcode/', include('nxp.backoffice.generate_qrcode.urls', namespace='generate_qrcode')),
    path('rewards/', include('nxp.backoffice.rewards.urls', namespace='rewards')),
]
