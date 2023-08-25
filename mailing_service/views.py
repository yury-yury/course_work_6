from http.client import HTTPResponse
from random import sample

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from blog.models import BlogEntry
from mailing_service.forms import MessageSenderForm, CustomerForm
from mailing_service.models import MessageSender, Customer, Attempt
from mailing_service.services import send_email


ITEM_ON_PAGE = 4


class MainView(TemplateView):
    template_name = 'mailing_service/main.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': MessageSender.objects.all()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts = list(BlogEntry.objects.all())
        context['random_blog_posts'] = sample(all_posts, min(3, len(all_posts)))
        return context


class CustomerCreateView(LoginRequiredMixin, CreateView):
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


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    paginate_by = ITEM_ON_PAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = f"Список клиентов, стр. {data['page_obj'].number} из {data['page_obj'].paginator.num_pages}"
        return data

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing_service.view_customer'):
            return queryset
        return queryset.filter(creator=self.request.user)


class CustomerDetailView(UserPassesTestMixin, DetailView):
    model = Customer

    def test_func(self):
        return self.request.user == self.get_object().creator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Детальный просмотр клента {data["object"].name}'
        return data


class CustomerUpdateView(UserPassesTestMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('mailing_service:customer_list')
    raise_exception = True

    def test_func(self):
        return self.request.user == self.get_object().creator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['title'] = f'Обновление клиента {data["object"].name}'

        return data

    def form_valid(self, form):
        self.object = form.save()

        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class CustomerDeleteView(UserPassesTestMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('mailing_service:customer_list')
    raise_exception = True

    def test_func(self):
        return self.request.user == self.get_object().creator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Удаление клиента {data["object"].name}'
        return data


class MessageSenderCreateView(LoginRequiredMixin, CreateView):
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
        send_email()
        return super().form_valid(form)


class MessageSenderListView(LoginRequiredMixin, ListView):
    model = MessageSender
    paginate_by = ITEM_ON_PAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = f"Список почтовых рассылок, стр. {data['page_obj'].number} из {data['page_obj'].paginator.num_pages}"
        return data

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing_service.view_messagesender'):
            return queryset
        return queryset.filter(creator=self.request.user)


class MessageSenderDetailView(UserPassesTestMixin, DetailView):
    model = MessageSender

    def test_func(self):
        return self.request.user == self.get_object().creator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Детальный просмотр почтовой рассылки {data["object"].subject}'
        return data


class MessageSenderUpdateView(UserPassesTestMixin, UpdateView):
    model = MessageSender
    form_class = MessageSenderForm
    success_url = reverse_lazy('mailing_service:list')
    raise_exception = True

    def test_func(self):
        return self.request.user == self.get_object().creator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['title'] = f'Обновление почтовой рассылки {data["object"].subject}'

        return data

    def form_valid(self, form):
        self.object = form.save()

        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageSenderDeleteView(UserPassesTestMixin, DeleteView):
    model = MessageSender
    success_url = reverse_lazy('mailing_service:list')
    raise_exception = True

    def test_func(self):
        return self.request.user == self.get_object().creator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Удаление почтовой рассылки {data["object"].subject}'
        return data


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    paginate_by = ITEM_ON_PAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['title'] = f"Список отчетов о выполненных почтовых рассылках, стр. {data['page_obj'].number} из {data['page_obj'].paginator.num_pages}"
        return data

    def get_queryset(self):
        if self.request.user.has_perm("mailing_service.view_attempt"):
            return super().get_queryset()
        return Attempt.objects.filter(message_sender__creator=self.request.user)


class AttemptDetailView(UserPassesTestMixin, DetailView):
    model = Attempt

    def test_func(self):
        return self.request.user == self.get_object().message_sender.creator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Детальный просмотр отчета о почтовой рассылке {data["object"].message_sender.subject}'
        return data


class AttemptDeleteView(UserPassesTestMixin, DeleteView):
    model = Attempt
    success_url = reverse_lazy('mailing_service:attempt_list')
    raise_exception = True

    def test_func(self):
        return self.request.user == self.get_object().message_sender.creator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Удаление почтовой рассылки {data["object"].message_sender.subject}'
        return data


@never_cache
@permission_required('mailing_service.set_active_customer')
def change_is_active(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if customer.is_active:
        customer.is_active = False
    else:
        customer.is_active = True
    customer.save()
    return redirect(reverse('mailing_service:customer_list'))


@never_cache
@permission_required('mailing_service.set_messagesender_status')
def change_status_messagesender(request, pk):
    sending = get_object_or_404(MessageSender, pk=pk)
    if sending.status in ['CREATED', 'LAUNCHED']:
        sending.status = 'COMPLETED'
    else:
        sending.status = 'CREATED'
    sending.save()
    return redirect(reverse('mailing_service:list'))
