from django.urls import path 
from .views import SumaView
from .views import RestaView
from .views import MultiplicacionView
from .views import DivisionView

urlpatterns = [
    path('sumar', SumaView.as_view())
]

urlpatterns = [
    path('resta', RestaView.as_view())
]
urlpatterns = [
    path('Dultiplicacion', MultiplicacionView.as_view())
]
urlpatterns = [
    path('Division', DivisionView.as_view())
]
