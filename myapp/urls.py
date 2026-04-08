from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import category_views, banner_views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('categories/list/', category_views.category_list),
    path('categories/create/', category_views.category_create),
    path('category/<uuid:pk>/detail/',category_views.category_detail),
    path('category/<uuid:pk>/delete/',category_views.category_delete),
    path('category/<uuid:pk>/update/',category_views.category_update),

    path('banners/list/', banner_views.banner_list),
    path('banner/create/', banner_views.banner_create),
    path('banner/<uuid:pk>/detail/',banner_views.banner_detail),
    path('banner/<uuid:pk>/delete/',banner_views.banner_delete)

]