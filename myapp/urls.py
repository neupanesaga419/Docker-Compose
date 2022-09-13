from django.urls import path
import myapp.views as vi

urlpatterns = [
    path('', vi.index, name="index")
]