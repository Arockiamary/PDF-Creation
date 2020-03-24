from django.urls import path
from . import views

urlpatterns=[
	path('',views.index, name="index"),
	path('demo', views.demo, name="demo"),
	path('change_fonts', views.change_fonts, name="change_fonts"),
	path('draw_lines',views.draw_lines,name="draw_lines"),
	path('draw_shapes', views.draw_shapes, name="draw_shapes"),
	path('add_image', views.add_image, name="add_image"),
	path('multipage_simple', views.multipage_simple, name="multipage_simple"),
	path('create_pdf', views.create_pdf, name="create_pdf"),
	path('simple_table',views.simple_table, name="simple_table"),
	path('simple_table_html',views.simple_table_html, name="simple_table_html"),
	path('html2pdf', views.html2pdf,name="html2pdf"),

	]