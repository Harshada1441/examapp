from django.urls import path
from . import views

urlpatterns = [

    # ---------- LOGIN ----------
    path('login/', views.Login),
    path('logout/', views.Logout),

    # ---------- QUESTION ----------
    path('addquestion/', views.Addquestion),
    path('savequestion/', views.Addquestioncurd),
    path('showquestions/', views.Showallquestions),
    path('view/<int:id>/', views.Viewquestion),
    path('delete/<int:id>/', views.Deletequestion),
    path('update/<int:id>/', views.Viewupdatepage),
    path('updatecurd/<int:id>/', views.Updatequestioncurd),

    # ---------- STUDENT ----------
    path('addstudent/', views.Addstudent),
    path('savestudent/', views.Addstudentcurd),
    path('viewstudent/<int:id>/', views.Viewstudent),

    # ---------- SUBJECT + TEST ----------
    path('subject/', views.Selectsubject),
    path('starttest/<str:subject>/', views.Starttest),
    path('myresults/', views.Viewresults),

    # ---------- RESULT ----------
    path('endtest/', views.Endtest),
    

]