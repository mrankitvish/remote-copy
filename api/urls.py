from django.urls import path
from .views import HomeView, TextView

urlpatterns = [
    path('', HomeView.as_view()),
    path('<uuid:token>', TextView.as_view() ),
]
# urlpatterns = [
#     path('', views.home_view),
#     path('text/<uuid:token>', views.text_view )
# ]
