from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    path('submit-product/', views.form, name="submit"),
    path('hayo', views.submit, name="todb"),
    path('<int:produk_id>/', views.detail, name="detail")

]