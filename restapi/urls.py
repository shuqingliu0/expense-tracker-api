from django.urls import path
from restapi import views

urlpatterns = [
    path("expense/", views.ExpenseListCreate.as_view(), name="expense-list-create"),
    path(
        "expense/<pk>",
        views.ExpenseRetrieveDelete.as_view(),
        name="expense-retrieve-delete",
    ),
]
