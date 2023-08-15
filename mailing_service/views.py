from http.client import HTTPResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing_service.forms import MessageSenderForm, CustomerForm
from mailing_service.models import MessageSender, Customer, Attempt
from mailing_service.services import send_email


ITEM_ON_PAGE = 4


def index(request):
    response = send_email('DAILY')
    return render(request, 'mailing_service/index.html')


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('mailing_service:customer_list')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = "Создание нового клиента."
        return data

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class CustomerListView(ListView):
    model = Customer
    paginate_by = ITEM_ON_PAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = f"Список клиентов, стр. {data['page_obj'].number} из {data['page_obj'].paginator.num_pages}"
        return data


class CustomerDetailView(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Детальный просмотр клента {data["object"].name}'
        return data


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('mailing_service:customer_list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['title'] = f'Обновление клиента {data["object"].name}'

        return data

    def form_valid(self, form):
        self.object = form.save()

        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('mailing_service:customer_list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Удаление клиента {data["object"].name}'
        return data


class MessageSenderCreateView(CreateView):
    model = MessageSender
    form_class = MessageSenderForm
    success_url = reverse_lazy('mailing_service:list')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = "Создание новой почтовой рассылки."
        return data

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageSenderListView(ListView):
    model = MessageSender
    paginate_by = ITEM_ON_PAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = f"Список почтовых рассылок, стр. {data['page_obj'].number} из {data['page_obj'].paginator.num_pages}"
        return data

class MessageSenderDetailView(DetailView):
    model = MessageSender

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Детальный просмотр почтовой рассылки {data["object"].subject}'
        return data


class MessageSenderUpdateView(UpdateView):
    model = MessageSender
    form_class = MessageSenderForm
    success_url = reverse_lazy('mailing_service:list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['title'] = f'Обновление почтовой рассылки {data["object"].subject}'

        return data

    def form_valid(self, form):
        self.object = form.save()

        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageSenderDeleteView(DeleteView):
    model = MessageSender
    success_url = reverse_lazy('mailing_service:list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Удаление почтовой рассылки {data["object"].subject}'
        return data


class AttemptListView(ListView):
    model = Attempt
    paginate_by = ITEM_ON_PAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = f"Список отчетов о выполненных почтовых рассылках, стр. {data['page_obj'].number} из {data['page_obj'].paginator.num_pages}"
        return data


class AttemptDetailView(DetailView):
    model = Attempt

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Детальный просмотр отчета о почтовой рассылке {data["object"].message_sender.subject}'
        return data


class AttemptDeleteView(DeleteView):
    model = Attempt
    success_url = reverse_lazy('mailing_service:attempt_list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Удаление почтовой рассылки {data["object"].message_sender.subject}'
        return data

