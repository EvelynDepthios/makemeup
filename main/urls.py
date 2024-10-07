from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, user_info, create_product_entry_ajax

app_name = 'main'

urlpatterns = [
    # Halaman utama menggunakan show_main
    path('', show_main, name='show_main'),  

    # URL lainnya
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('create-product-entry-ajax', create_product_entry_ajax, name='create_product_entry_ajax'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),

    # Halaman tambahan
    path('home/', show_main, name='home'),
    path('products/', show_main, name='products'),
    path('user-info/', user_info, name='user_info'),
]
