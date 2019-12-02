from . import views
from django.conf.urls import url
from django.contrib import admin

#administrator headers
admin.site.site_header="Portoriki Church Registry Administrator"
admin.site.site_title="Portoriki Church Registry Administration"
admin.site.index_title="Portoriki Church Registry Administration"
admin.site.password_change_title="Portoriki Church Registry Administration"

urlpatterns = [
    url(r'^$',views.index,name='index'),

    #url('', views.edit_user),
    url(r'edit_user/$', views.edit_user),
    #url(r'success/$', views.success),
    url(r'login_user/$', views.login_user,name="loguser"),
    #url(r'invalid/$', views.invalid),
    url(r'invalid/$', views.invalid,name="invalid"),
    url(r'loggin/$', views.loggin),
    url(r'logout/$', views.logout),
    url(r'logout/$', views.logout),
    url(r'addcontact/$', views.addcontact,name="new_member"),
    url(r'reportboard/$', views.reportboard,name="reportboard"),
    url(r'province/$', views.province,name="selectprovince"),
    url(r'provincequery/$', views.provincequery,name="display_query"),
    url(r'island/$', views.island,name="selectisland"),
    url(r'islandquery/$', views.islandquery,name="islandquery_query"),
    url(r'uploadfunc/$', views.uploadfunc,name="uploadfunc"),
    url(r'writeto_db/$', views.writeto_db,name="writeto_db"),
    url(r'download_registry/$', views.download_registry,name="download_csv"),
    url(r'^updatecontact/(?P<id>\d+)/$',views.updatecontact,name="updatecontact"),
    url(r'^kill_entry/(?P<id>\d+)/$',views.kill_entry,name="kill_entry"),
    url(r'^manage_minute/$',views.manage_minute,name="manage_minute"),
    url(r'^addminute/$',views.addminute,name="addminute"),

    url(r'^updateminute/(?P<id>\d+)/$',views.updateminute,name="updateminute"),
    url(r'^drop_minute/(?P<id>\d+)/$',views.drop_minute,name="drop_minute"),
    url(r'^display_data/(?P<id>\d+)/$',views.display_data,name="display_data"),

    url(r'^bydate/$',views.bydate,name="bydate"),
    url(r'^bydatequery/$',views.bydatequery,name="bydatequery"),
    ]
