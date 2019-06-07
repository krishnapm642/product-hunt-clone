from django.urls import path
from .views import home, create, productdetail, upvote

urlpatterns = [
    
    path('create/', create, name = 'create'),
    path('<int:product_id>', productdetail , name = 'detail'),
    path('<int:product_id>/upvote', upvote, name='upvote')

]
