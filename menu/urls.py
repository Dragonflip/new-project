from django.urls import path
from menu.apis import IngredienteApi, IngredienteDetail, ItemApi, ItemDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('ingredientes', IngredienteApi.as_view(), name='ingrediente'),
    path('ingredientes/<int:pk>/', IngredienteDetail.as_view(), name='ingrediente_detail'),
    path('item', ItemApi.as_view(), name='item'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
