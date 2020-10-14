from django.conf.urls import url,include
from . import views
app_name = 'shop'

from rest_framework import routers

router = routers.DefaultRouter()
router.register('item_list',views.ItemListViewSet)
router.register('orders',views.OrderViewSet,basename="orders")

urlpatterns = [
    url(r'^item_list/(?P<catogory>[-\w]+)/',views.CatogoryItemListView.as_view()),
    url(r'^shop/',include(router.urls)),
]
