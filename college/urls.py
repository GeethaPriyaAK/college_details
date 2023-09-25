from django.urls import path
from .import views

urlpatterns=[
    path('',views.college_info,name= 'college_info'),
    path('<int:pk>/',views.college_details, name = 'college_details'),
    path('college_info1',views.college_info1,name= 'college_info1'),
    path('college_info2',views.college_info2,name= 'college_info2'),
    path('college_info3',views.college_info3,name= 'college_info3'),
    path('college_info4',views.college_info4,name= 'college_info4'),
    path('college_info5',views.college_info5,name= 'college_info5'),
    path('college_info6',views.college_info6,name= 'college_info6'),
    path('college_info7',views.college_info7,name= 'college_info7'),
    path('college_info8',views.college_info8,name= 'college_info8'),
    path('college_info9',views.college_info9,name= 'college_info9'),
    path('college_info10',views.college_info10,name= 'college_info10'),
]