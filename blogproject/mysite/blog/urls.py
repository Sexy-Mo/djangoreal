from blog import views
from django.conf.urls import url

urlpatterns=[
    url(r'^about/$',views.aboutview.as_view(),name='about'),
    url(r'^$',views.postlistview.as_view(),name='postlist'),
    url(r'^post/(?P<pk>\d+)/$',views.postdetailview.as_view(),name='postdetail'),
    url(r'^post/new/$',views.createpostview.as_view(),name='postnew'),
    url (r'^post/(?P<pk>\d+)/edit/$',views.updatepostview.as_view(),name='postupdate'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.deletepostview.as_view(),name='postdelete'),
    url(r'^drafts/$',views.draftlistview.as_view(),name='postdraftlist'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='addcommenttopost'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='commentapprove'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='commentremove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='postpublish'),
    url(r'^register/$',views.register,name='register'),


    ]
