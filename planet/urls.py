# -*- coding: utf-8 -*-
try:
    # Django 1.6
    from django.conf.urls import patterns, url, include
except ImportError:
    # Django < 1.6
    from django.conf.urls.defaults import patterns, url

from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required

from planet.views import (FeedFormView, BlogByUserList, BlogDelete,
                          FeedDelete, PostDelete)
from planet.feeds import PostFeed, AuthorFeed, AuthorTagFeed, TagFeed
from planet.sitemaps import planet_sitemaps_dict


urlpatterns = patterns('planet.views',
                       url(r'^blogs/(?P<blog_id>\d+)/(?P<slug>[a-zA-Z0-9_\-]+)/$',
                           "blog_detail", name="planet_blog_detail"),
                       url(r'^blogs/(?P<blog_id>\d+)/$', "blog_detail"),
                       url(r'^blogs/(?P<pk>\d+)/delete$',
                           login_required(BlogDelete.as_view()), name="planet_blog_delete"),
                       url(r'^blogs/$', "blogs_list", name="planet_blog_list"),
                       url(r'^blogs/my_blogs/$', login_required(BlogByUserList.as_view()),
                           name="planet_blog_list_by_user"),

                       url(r'^feeds/add/$', login_required(FeedFormView.as_view()),
                           name="feed_add"),
                       url(r'^feeds/(?P<feed_id>\d+)/delete/$',
                           login_required(FeedDelete.as_view()), name="feed_delete"),
                       url(r'^feeds/(?P<feed_id>\d+)/(?P<slug>[a-zA-Z0-9_\-]+)/tags/(?P<tag>.*)/$',
                           "feed_detail", name="planet_by_tag_feed_detail"),
                       url(r'^feeds/(?P<feed_id>\d+)/(?P<slug>[a-zA-Z0-9_\-]+)/$',
                           "feed_detail", name="planet_feed_detail"),
                       url(r'^feeds/(?P<feed_id>\d+)/$', "feed_detail"),
                       url(r'^feeds/$', "feeds_list", name="planet_feed_list"),

                       url(r'^authors/(?P<author_id>\d+)/(?P<slug>[a-zA-Z0-9_\-]+)/tags/(?P<tag>.*)/$',
                           "author_detail", name="planet_by_tag_author_detail"),
                       url(r'^authors/(?P<author_id>\d+)/(?P<slug>[a-zA-Z0-9_\-]+)/$',
                           "author_detail", name="planet_author_detail"),
                       url(r'^authors/(?P<author_id>\d+)/$', "author_detail"),
                       url(r'^authors/$', "authors_list",
                           name="planet_author_list"),

                       url(r'^tags/(?P<tag>.*)/feeds/$',
                           "tag_feeds_list", name="planet_tag_feed_list"),
                       url(r'^tags/(?P<tag>.*)/authors/$',
                           "tag_authors_list", name="planet_tag_author_list"),
                       url(r'^tags/(?P<tag>.*)/$', "tag_detail",
                           name="planet_tag_detail"),
                       url(r'^tags/$', "tags_cloud", name="planet_tag_cloud"),

                       url(r'^opml/$', "opml", name="planet_opml"),
                       url(r'^foaf/$', "foaf", name="planet_foaf"),

                       url(r'^posts/(?P<post_id>\d+)/(?P<slug>[a-zA-Z0-9_\-]+)/$',
                           "post_detail", name="planet_post_detail"),
                       url(r'^posts/(?P<pk>\d+)/$', login_required(PostDelete.as_view()),
                           name="planet_post_delete"),
                       url(r'^posts/(?P<post_id>\d+)/$', "post_detail"),
                       url(r'^posts/$', "posts_list", name="planet_post_list"),

                       url(r'^search/$', "search", name="planet_search"),

                       url(r'^$', "index", name="planet_index"),
                       )

# Feed's urls
urlpatterns += patterns('',
                        url(r'^posts/feeds/rss/$', PostFeed(),
                            name="planet_rss_feed"),
                        url(r'^feeds/rss/tags/(?P<tag>.*)/$',
                            TagFeed(), name="planet_tag_rss_feed"),
                        url(r'^feeds/rss/authors/(?P<author_id>\d+)/$',
                            AuthorFeed(), name="planet_author_rss_feed"),
                        url(r'^feeds/rss/authors/(?P<author_id>\d+)/tags/(?P<tag>.*)/$',
                            AuthorTagFeed(), name="planet_tag_author_rss_feed"),
                        )

# sitemaps
urlpatterns += patterns('',
                        url(r'^sitemap.xml$',
                            cache_page(86400)(sitemaps_views.index),
                            {'sitemaps': planet_sitemaps_dict, 'sitemap_url_name': 'sitemaps'}),
                        url(r'^sitemap-(?P<section>.+)\.xml$',
                            cache_page(86400)(sitemaps_views.sitemap),
                            {'sitemaps': planet_sitemaps_dict}, name='sitemaps'),
                        )
