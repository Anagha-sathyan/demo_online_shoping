from django.contrib import admin
from django.urls import path
from demo_av_app import views
from demo_av_app.views import fun
app_name="myapp"
urlpatterns = [
    path('',views.fun, name='fun'),
    path('shop/<int:shop_id>',views.details, name='details'),
    path('add/',views.add_product,name="add_product"),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]