from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.news_today,name='newsToday'),
  url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name = 'pastnews'),
  url(r'^search/',views.search_results, name='search_results'),   #create a new URLpattern that references the search_results
  url(r'^article/(\d+)',views.article,name ='article')   #create an article route and we capture an integer which will be the id of the article.
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
