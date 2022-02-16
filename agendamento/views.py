from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Clientes, Events
from django.urls import reverse_lazy

# Create your views here.
def abertura_modelform(request):
    return render(request, "index.html")


class EventsCreate(CreateView):
    model = Events
    fields = ["title", "description", "status"]
    template_name = "agendamento/gerenciar_evento.html"
    success_url = reverse_lazy("calendario")


class EventsList(ListView):
    model = Events
    template_name = "agendamento/listar_calendario.html"


class EventsUpdate(UpdateView):
    model = Events
    fields = ["title", "description", "status"]
    template_name = "agendamento/gerenciar_evento.html"
    success_url = reverse_lazy("calendario")


class EventsDelete(DeleteView):
    model = Events
    template_name = "agendamento/deletar_evento.html"
    success_url = reverse_lazy("calendario")


# pagina cadastro - C
class ClientesCad(CreateView):
    model = Clientes
    fields = ["nome", "email", "telefone"]
    template_name = "cadastros/index_cadastros.html"
    success_url = reverse_lazy("listagem")


# pagina listagem - R
class ClientesListagem(ListView):
    model = Clientes
    template_name = "cadastros/listar_cadastros.html"


# pagina editar - U
class ClientesUpdate(UpdateView):
    model = Clientes
    fields = ["nome", "email", "telefone"]
    template_name = "cadastros/index_cadastros.html"
    success_url = reverse_lazy("listagem")


# pagina deletar - D
class ClientesDelete(DeleteView):
    model = Clientes
    template_name = "cadastros/excluir_cadastros.html"
    success_url = reverse_lazy("listagem")
