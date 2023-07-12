from django.urls import  path
from student import api


urlpatterns =[
    path('creupschool/', api.creupschool, name="creupschool"),
    path('creupclass/', api.creupclass, name="creupclass"),
    path('adduptea/', api.adduptea, name="adduptea"),
    path('addupdstu/', api.addupdstu, name="addupdstu"),
    path('addupsub/', api.addupsub, name="addupsub"),
    path('addupadnce/', api.addupadnce, name="addupadnce"),
    path('addupexam/', api.addupexam, name="addupexam"),
    path('addupexamres', api.addupexamres, name="addupexamres"),
    path('delstu/', api.delstu, name="delstu"),
    path('getteach/', api.getteach, name="getteach"),
    path('getschl/', api.getschl, name="getschl"),



]