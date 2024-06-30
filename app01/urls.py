from django.contrib import admin
from django.urls import path, re_path
from app01 import views
# urls.py

urlpatterns=[
    path('login/',views.login,name='login'),
    path('registry/',views.registry,name='registry'),
    path('control/',views.control,name='control'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),


    # path('account/list/',views.account_list,name='account_list'),
    # path('account/add/',views.account_add,name='account_add'),
    # path('account/delete/', views.account_delete, name='account_delete'),
    # path('account/<int:nid>/edit/', views.account_edit),
    #
    # path('staff/list/', views.staff_list, name='staff_list'),
    # path('staff/add/', views.staff_add, name='staff_add'),
    # path('staff/delete/', views.staff_delete, name='staff_delete'),
    # path('staff/<int:nid>/edit/', views.staff_edit),
    path('data/', views.data, name='data'),
    path('info/', views.info, name='info'),
    path('center/', views.center, name='center'),
    path('water/', views.water, name='water'),

    path('api/get-hardware-status/', views.get_hardware_status, name='get-hardware-status'),
    path('api/get-data-status/', views.get_data_status, name='get-data-status'),
    path('image/code',views.image_code,name='image_code'),

    # 上传文件
    path('upload/list/',views.upload_list,name='upload_list'),
    path('HI/multi',views.HI_multi,name='HydrologicInfo'),
    path('fish/multi',views.fish_multi,name='fish'),
    # path('staff/multi', views.staff_multi, name='staff'),
    path('device/multi', views.device_multi, name='device'),
    path('cage/multi', views.cage_multi, name='cage'),

    path('fish/export', views.fish_export, name='fish_export'),
    path('HI/export', views.HI_export, name='HI_export'),
    path('device/export', views.device_export, name='device_export'),
    path('cage/export', views.cage_export, name='cage_export'),

    ##新增
    path('get_available_dates/', views.get_available_dates, name='get_available_dates'),
    path('get_historical_data/', views.get_historical_data, name='get_historical_data'),
    path('get_latest_hydro_data/', views.get_latest_hydro_data, name='get_latest_hydro_data'),
    path('get_latest_environment_score/', views.get_latest_environment_score, name='get_latest_environment_score'),
    path('get_latest_fish_data/', views.get_latest_fish_data, name='get_latest_fish_data'),
    path('get_weather_data/', views.get_weather_data, name='get_weather_data'),
]