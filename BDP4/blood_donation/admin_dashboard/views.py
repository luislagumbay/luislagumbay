from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import User, AdminProfile
from .models import AdminBloodRequest
from django.contrib import messages
from .forms import AdminUserForm, BloodRequestForm

# Helper function to ensure the user is an admin
def admin_required(user):
    return user.is_superuser or user.is_staff

@user_passes_test(admin_required)
def admin_dashboard(request):
    users = User.objects.all()
    blood_requests = AdminBloodRequest.objects.all()
    return render(request, 'admin/dashboard.html', {
        'users': users,
        'blood_requests': blood_requests,
    })

@user_passes_test(admin_required)
def admin_user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)  # Get the user by primary key
    if request.method == "POST":
        form = AdminUserForm(request.POST, instance=user)  # Pass user instance here
        if form.is_valid():
            form.save()  # Save the updated user
            messages.success(request, f"User {user.username} updated successfully!")
            return redirect('admin_dashboard')  # Redirect to the admin dashboard
    else:
        form = AdminUserForm(instance=user)  # Pass user instance here for GET request

    return render(request, 'admin/user_edit.html', {'form': form, 'user': user})

@user_passes_test(admin_required)
def admin_user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        messages.success(request, f"User {user.username} deleted successfully!")
        return redirect('admin_dashboard')
    return render(request, 'admin/user_confirm_delete.html', {'user': user})

@user_passes_test(admin_required)
def admin_blood_request_edit(request, pk):
    blood_request = get_object_or_404(AdminBloodRequest, pk=pk)
    if request.method == "POST":
        form = BloodRequestForm(request.POST, instance=blood_request)
        if form.is_valid():
            form.save()
            messages.success(request, "Blood request updated successfully!")
            return redirect('admin_dashboard')
    else:
        form = BloodRequestForm(instance=blood_request)
    return render(request, 'admin/blood_request_edit.html', {'form': form, 'blood_request': blood_request})

@user_passes_test(admin_required)
def admin_blood_request_delete(request, pk):
    blood_request = get_object_or_404(AdminBloodRequest, pk=pk)
    if request.method == "POST":
        blood_request.delete()
        messages.success(request, "Blood request deleted successfully!")
        return redirect('admin_dashboard')
    return render(request, 'admin/blood_request_confirm_delete.html', {'blood_request': blood_request})
