from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add/', views.add_product, name="add_product"),
    path('edit/<int:product_id>/', views.edit_product, name="edit_product"),
    path('delete/<int:product_id>/', views.delete_product,
         name="delete_product"),
    path('save_review/<int:product_id>/',
         views.save_review, name="save_review"),
    path('delete_review/<int:review_id>/',
         views.delete_review, name="delete_review"),
    path('delete_last_review/<int:product_id>/<int:user_id>/',
         views.delete_last_review, name="delete_last_review"),
]

