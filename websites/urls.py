from django.urls import path
from . import views

urlpatterns = [
	path('create/display/<str:monkey>', view.create_webpage, name="display_create"),
	path('edit/display/<int:pk>', views.edit_webpage, name="display_edit_page"),
	path('view/webpage/<int:pk>', views.view_webpage, name="show_webpage"),
	path('all/websites', views.list_all_websites, name="all websites"),
	path('edit/page/<int:pk>', views.editpage, name="update_page"),
	path('create/page', views.savepage, name="create_page"),
]