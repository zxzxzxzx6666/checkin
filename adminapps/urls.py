from django.urls import path
from adminapps import views
urlpatterns = [
    
    # 登入(POST 最後不加 '/')
    path('', views.index, name='index'),
    path('login/' , views.login),
    
    # 後台(POST 最後不加 '/')
    path('backstage/', views.backstage),
    path('backstage_main', views.backstage_main),
    path('backstaged/', views.backstaged),
    path('backstageC', views.backstageC),
    path('backstageClock', views.backstageClock),
    path('backstageAccount/', views.backstageAccount),
    path('backstageGroup/', views.backstageGroup),
    
    
    path('MannounceContent/', views.MannounceContent),
    path('MannounceAdd/', views.MannounceAdd),
    path('Mannounce_Add', views.Mannounce_Add),
    path('MannounceDelete/<id>/', views.MannounceDelete),
    path('Mannounce_Update', views.Mannounce_Update),
    path('Mannounce_Delete', views.Mannounce_Delete),
    path('MannounceCard_Update', views.MannounceCard_Update),
    path('MannounceGroupSession', views.MannounceGroupSession),
    path('McalendarGroupSession', views.McalendarGroupSession),
    
    path('Mcalendar_main', views.Mcalendar_main),
    path('McalendarDelete/<id>/', views.McalendarDelete),
    path('Mcalendar_Update', views.Mcalendar_Update),
    path('Mcalendar_Delete', views.Mcalendar_Delete),
    path('McalendarAdd', views.McalendarAdd),
    path('Mcalendar_Add', views.Mcalendar_Add),
    path('MclockinAttendanceDel', views.MclockinAttendanceDel),
    path('MclockinLeaveDel', views.MclockinLeaveDel),
    path('Maccount_Add', views.Maccount_Add),
    path('Maccount_main', views.Maccount_main),
    path('MaccountDelete/<id>/', views.MaccountDelete),
    path('Maccount_Update', views.Maccount_Update),
    path('Maccount_Delete', views.Maccount_Delete),
    
    path('Mgroup_Add', views.Mgroup_Add),
    path('Mgroup_main', views.Mgroup_main),
    path('MgroupDelete/<id>/', views.MgroupDelete),
    path('Mgroup_Update', views.Mgroup_Update),
    path('Mgroup_Delete', views.Mgroup_Delete),
    
    
    
    # path('Mcalendar_renew', views.Mcalendar_renew),

    # 公告(POST 最後不加 '/')
    path('announce/', views.announce),
    path('announce_main/' , views.announce_main),
    path('announce_card/' , views.announce_card),
    path('announceContent/<id>/', views.announceContent),
    
    # 儀表板(POST 最後不加 '/')
    path('charts/', views.charts),

    # 行事曆(POST 最後不加 '/')
    path('calendar/', views.calendar),
    path('calendar_main', views.calendar_main),
    path('calendarContent/<id>/', views.calendarContent),

    #打卡(POST 最後不加 '/')
    path('clockin/', views.clockin),
    path('clockinLeaveAdd/', views.clockinLeaveAdd),
    path('clockinAttendance/', views.clockinAttendance),
    path('clockinLeave/', views.clockinLeave),
    path('clockin_chickin', views.clockin_chickin),
    
    
    
    
]