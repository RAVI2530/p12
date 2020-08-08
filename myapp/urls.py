from django.urls import path
from myapp import views

app_name="myapp"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
    path('fourth/',views.fourth,name="fourth"),
    path('second/',views.second,name="second"),
    path('third/',views.third,name='third'),
    path('fifth/',views.fifth,name="fifth"),
    path("url_data/<name>",views.urls_data,name="urls_data"),
    path("ab/<a>/<b>",views.ab,name="ab"),
    path('greater/<ab>',views.greater,name="greater"),
    path('vowel/<s>',views.vowel,name="vowel"),

   
]
