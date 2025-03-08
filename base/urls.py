
from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name='home'),
    path('add/<int:id>',views.addcard,name='add'),
    path('add1',views.Add,name='add1'),
    path('remove/<int:id>',views.Remove,name='remove'),
    path('buy/<int:id>',views.Buyproduct,name='buy'),
    path('buydelete/<int:id>',views.ByeDelete,name='buydelete'),
    path('buydeleteall',views.ByeDeleteAll,name='buydeleteall'),
    path('reduce/<int:id>',views.Reduce,name='reduce'),
    path('increse/<int:id>',views.Increse,name='increse'),
    path('reduce1/<int:id>',views.Reduce1,name='reduce1'),
    path('increse1/<int:id>',views.Increse1,name='increse1'),

    
]


