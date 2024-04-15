from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from publications.forms import PublicationForm
from publications.models import Publication


# Create your views here.
class PublicationsListView(ListView):
    """Представление списка публикаций"""
    model = Publication

class PublicationCreateView(LoginRequiredMixin,CreateView):
    """Представление создания публикации"""
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy('publications:index')

    def get_form_kwargs(self):
        kwargs = super(PublicationCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class PublicationsDetailView(DetailView):
    """Представление для просмотра одной публикации"""
    model = Publication
    success_url = reverse_lazy('publications:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['publications'] = Publication.objects.filter(id=self.kwargs.get('pk'))
        return context_data

class PublicationsUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для обновления одной публикации"""
    model = Publication
    form_class = PublicationForm

    def get_success_url(self):
        return reverse_lazy('publications:view', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super(PublicationsUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class PublicationsDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для обновления одной публикации"""
    model = Publication
    success_url = reverse_lazy('publications:index')

@login_required
def main_public(request):
    """Представление для отображения публикаций пользователя"""
    publications_list = Publication.objects.filter(author_id=request.user.pk)
    publications_count_all = Publication.objects.filter(author_id=request.user.pk).count()
    publications_count_active = Publication.objects.filter(
        author_id=request.user.pk,
        is_active=True
    ).count()
    publications_count_pay = Publication.objects.filter(
        author_id=request.user.pk,
        is_pay=True
    ).count()

    context_data = {
        'publications_count_all': publications_count_all,
        'publications_count_active': publications_count_active,
        'publications_count_pay': publications_count_pay,
        'publications_list': publications_list
    }

    return render(request, 'publications/my_public.html', context_data)
