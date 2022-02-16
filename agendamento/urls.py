from agendamento import views
from django.urls import path
from agendamento.views import (
    ClientesListagem,
    ClientesCad,
    ClientesUpdate,
    ClientesDelete,
    EventsList,
    EventsCreate,
    EventsUpdate,
    EventsDelete,
)

# Create your views here.
urlpatterns = [
    path("", views.abertura_modelform, name="index"),
    path("listagem/", ClientesListagem.as_view(), name="listagem"),
    path("cadastros/", ClientesCad.as_view(), name="cadastros"),
    path("update/<int:pk>", ClientesUpdate.as_view(), name="update"),
    path("deletar/<int:pk>", ClientesDelete.as_view(), name="deletar"),
    path("calendario/", EventsList.as_view(), name="calendario"),
    path("addEvent/", EventsCreate.as_view(), name="addEvent"),
    path("updateEvent/<int:pk>", EventsUpdate.as_view(), name="updateEvent"),
    path("deleteEvent/<int:pk>", EventsDelete.as_view(), name="deleteEvent"),
]
