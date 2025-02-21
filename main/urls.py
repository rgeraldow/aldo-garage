from django.urls import path
from main.views import show_main, create_car_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_car, delete_car, add_car_entry_ajax, create_car_flutter


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-car-entry', create_car_entry, name='create_car_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-car/<uuid:id>', edit_car, name='edit_car'),
    path('delete/<uuid:id>', delete_car, name='delete_car'),
    path('create-car-entry-ajax', add_car_entry_ajax, name='add_car_entry_ajax'),
    path('create-flutter/', create_car_flutter, name='create_car_flutter'),
]