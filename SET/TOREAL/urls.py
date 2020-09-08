from django.conf.urls import url 
from TOREAL import views 
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('register/', views.member_profile),    #初始化頁面   註冊
    path('profile1', views.profile),            
    path('login/',views.member_login),          #初始化頁面   登入
    path('user/', views.user_page), 
    path('user1', views.user),                   #從member_login.html  post資料到 login1 的路由上（function 為user）
    path('user_info/', views.user_info),         #更改會員資料
    path('user_info1', views.info_update),
    path('user_pw_info/', views.user_pw_info),   #更改會員密碼
    path('user_pw_info1', views.pw_update),          
    path('test1', views.test),                  #從上面跳轉過來
    path('logout1', views.logout),
    path('loc/', views.user_loc),
    path('msg1', views.msg),
    path('image/', views.image),
    path('image1', views.image_upload),
    path('score/', views.score),        #初始化配對分數     不處理其他事情
    path('score1', views.score1),       #處理得function
    

]