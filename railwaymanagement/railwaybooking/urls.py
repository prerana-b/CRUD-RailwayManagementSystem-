from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url


app_name = 'railwaybooking'

urlpatterns = [

    # get request to retrieve and display all records
    path('', views.bookticket, name='passenger_insert'),
    # get and post request for update
    path('<int:id>/', views.bookticket, name='passenger_update'),
    # get and post request for insert
    path('list/', views.passenger_list, name='passenger_show'),
    path('delete/<int:id>/', views.passenger_delete, name='passenger_delete'),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url='/static/images/favicon.ico')),
]
