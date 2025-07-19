from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.models import User
from .models import Portfolio, Project
from django.urls import reverse_lazy
from django.contrib import messages

def applicant_list_view(request):
    portfolios = Portfolio.objects.select_related('user').all().order_by('user__first_name')
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'portfolio/applicant.list.html', context)

class ApplicantDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/applicant.detail.html'
    context_object_name = 'portfolio'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        username = self.kwargs.get(self.slug_url_kwarg)
        user = get_object_or_404(User, username=username)
        return get_object_or_404(Portfolio.objects.select_related('user', 'project'), user=user)

class ApplicantDeleteView(DeleteView):
    model = Portfolio
    template_name = 'portfolio/applicant.delete.html'
    success_url = reverse_lazy('applicant.list')
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        username = self.kwargs.get(self.slug_url_kwarg)
        user = get_object_or_404(User, username=username)
        return get_object_or_404(Portfolio.objects.select_related('user'), user=user)

    def form_valid(self, form):
        messages.success(self.request, f"Applicant {self.object.user.username} and their portfolio have been deleted.")
        return super().form_valid(form)
