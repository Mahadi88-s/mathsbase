from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('pcomp', views.pcomp, name='pcomp'),
    
    #api
    path('paper1/<api>', views.paper1),
    path('paper2/<api>', views.paper2),
    path('paper3/<api>', views.paper3),

    path('paper1/<int:id>/<int:pk>/<api>', views.paper1details),
    path('paper2/<int:id>/<int:pk>/<api>', views.paper2details),
    path('paper3/<int:id>/<int:pk>/<api>', views.paper3details),

    #p1
    path('paper1maths', views.paper1maths, name='paper1maths'),
    path('analysisp1', views.analysisp1, name='analysisp1'),
    path('upload_top1', views.upload_top1, name='upload_top1'),

    #p2
    path('paper2maths', views.paper2maths, name='paper2maths'),
    path('analysisp2', views.analysisp2, name='analysisp2'),
    path('upload_top2', views.upload_top2, name='upload_top2'),

    #p2
    path('paper3maths', views.paper3maths, name='paper3maths'),
    path('analysisp3', views.analysisp3, name='analysisp3'),
    path('upload_top3', views.upload_top3, name='upload_top3'),

    path('upload', views.upload, name='upload'),
    path('search_all', views.search_all, name='search_all'),
    path('search_yn', views.search_yn, name='search_yn'),
    path('search_ym', views.search_ym, name='search_ym'),
    path('search_yt', views.search_yt, name='search_yt'),
    path('search_n', views.search_n, name='search_n'),
    path('search_m', views.search_m, name='search_m'),
    path('search_t', views.search_t, name='search_t'),

    path('profile', views.profile, name='profile'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),

    path('ai', views.ai, name='ai'),
    path('search', views.search, name='search'),

]

urlpatterns = format_suffix_patterns(urlpatterns)