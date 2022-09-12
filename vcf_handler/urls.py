from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from vcf_handler import views

urlpatterns = [
    path('vcfs/', views.VcfList.as_view(), name="vcfs"), 
    path('vcfs/<str:id_seq>/', views.VcfDetail.as_view(), name="vcf-detail"),
    path('api-auth/', include('rest_framework.urls')),
    path('read_file/', views.read_file, name='read-file'),

]

# add format to the url patterns
urlpatterns = format_suffix_patterns(urlpatterns)