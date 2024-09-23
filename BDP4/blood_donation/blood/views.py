from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BloodRequest
from .forms import BloodRequestForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model


User = get_user_model()

# Only admins can access this view
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    users = User.objects.all()  # Fetch all users
    blood_requests = BloodRequest.objects.all()  # Fetch all blood requests
    return render(request, 'admin/dashboard.html', {'users': users, 'blood_requests': blood_requests})

@user_passes_test(lambda u: u.is_superuser)
def admin_user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    # Implement logic to edit the user, e.g. handle a form
    # For now, this is just a placeholder
    return render(request, 'admin/user_edit.html', {'user': user})

@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('admin_dashboard')

@user_passes_test(lambda u: u.is_superuser)
def admin_blood_request_edit(request, pk):
    request = get_object_or_404(BloodRequest, pk=pk)
    # Implement logic to edit the blood request, e.g. handle a form
    return render(request, 'admin/bloodrequest_edit.html', {'blood_request': request})

@user_passes_test(lambda u: u.is_superuser)
def admin_blood_request_delete(request, pk):
    request = get_object_or_404(BloodRequest, pk=pk)
    request.delete()
    return redirect('admin_dashboard')

class BloodRequestCreateView(LoginRequiredMixin, CreateView):
    model = BloodRequest
    form_class = BloodRequestForm
    template_name = 'blood/bloodrequest_form.html'
    success_url = reverse_lazy('blood_request_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Logic to disable fields if request_type is donation and pre-fill values from profile
        if form.instance.request_type == 'donation':
            profile = self.request.user.profile
            form.instance.blood_type = profile.blood_type
            form.instance.region = profile.region
            form.instance.province = profile.province
            form.instance.municipality = profile.municipality
        return super().form_valid(form)
class BloodRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = BloodRequest
    form_class = BloodRequestForm
    template_name = 'blood/bloodrequest_form.html'
    success_url = reverse_lazy('blood_request_list')

    def get_queryset(self):
        # Restrict users to only edit their own blood requests
        return BloodRequest.objects.filter(user=self.request.user)

    def form_valid(self, form):
        # Additional logic for editing, e.g., prevent donation editing
        return super().form_valid(form)

class BloodRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = BloodRequest
    template_name = 'blood/bloodrequest_confirm_delete.html'
    success_url = reverse_lazy('blood_request_list')

    def get_queryset(self):
        # Restrict users to only delete their own blood requests
        return BloodRequest.objects.filter(user=self.request.user)

class BloodRequestListView(LoginRequiredMixin, ListView):
    model = BloodRequest
    template_name = 'blood/bloodrequest_list.html'
    context_object_name = 'blood_requests'

class BloodRequestDetailView(LoginRequiredMixin, DetailView):
    model = BloodRequest
    template_name = 'blood/bloodrequest_detail.html'
    context_object_name = 'blood_request'
