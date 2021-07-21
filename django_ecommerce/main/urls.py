from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import HomeView, ProductsListView, ProductsDetailView, VendorsListView, VendorDetailsListView, \
    CategoryListView, CategoryDetailsListView, add_to_cart, remove_from_cart

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product/<slug>/', ProductsDetailView.as_view(), name='product_detail'),
    path('vendors/', VendorsListView.as_view(), name='vendors'),
    path('vendor_detail/<slug>/', VendorDetailsListView.as_view(), name='vendor_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category_detail/<slug>/', CategoryDetailsListView.as_view(), name='category_detail'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
