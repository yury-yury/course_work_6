from http.client import HTTPResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from mailing_service.forms import MessageSenderForm
from mailing_service.models import MessageSender
from mailing_service.services import send_email


ITEM_ON_PAGE = 9


def index(request):
    response = send_email('DAILY')
    return render(request, 'mailing_service/index.html')

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
