# coding:utf-8
from django.conf.urls import include,url
from views import *

POST_create = help_category.as_view({'post':'POST_create'})
DELETE_category = help_category.as_view({'post':'DELETE_category'})
Get_category_list = help_category.as_view({'get':'Get_category_list'})

GET_search = help_article.as_view({'post':'GET_search'})
POST_article = help_article.as_view({'post':'POST_article'})
Get_article_list = help_article.as_view({'get':'Get_article_list'})
Get_category_article = help_article.as_view({'post':'Get_category_article'})
# UPDATE_article = help_article.as_view({'post':'UPDATE_article'})
DELETE_art = help_article.as_view({'post':'DELETE_art'})
GET_aaticle_as_pk = help_article.as_view({'post':'GET_aaticle_as_pk'})



urlpatterns  = [

    url(r'LIST_category/$',help_category.as_view({'get':'list'}),name='LIST_create'),
    url(r'POST_create/$',POST_create,name='POST_create'),
    url(r'DELETE_category/$',DELETE_category,name='DELETE_category'),
    url(r'Get_category_list/$',Get_category_list,name='Get_category_list'),

    url(r'POST_article/$',POST_article,name='POST_article'),
    url(r'GET_search/$',GET_search,name='GET_search'),
    url(r'Get_article_list/$',Get_article_list,name='Get_article_list'),
    url(r'Get_category_article/$',Get_category_article,name='Get_category_article'),
    # url(r'UPDATE_article/$',UPDATE_article,name='UPDATE_article'),
    url(r'DELETE_art/$',DELETE_art,name='DELETE_art'),
    url(r'GET_aaticle_as_pk/$',GET_aaticle_as_pk,name='GET_aaticle_as_pk'),
]

