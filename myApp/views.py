
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AppointmentRequest
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from .models import Report
from .models import ContactMessage

@login_required
def profile(request):
    if request.user.is_superuser:
        messages.error(request, "Superusers cannot access the user profile page. Redirecting to admin.")
        return redirect('/admin/')
    
@login_required
def profile(request):
    user_appointments = AppointmentRequest.objects.filter(email=request.user.email)
    return render(request, 'profile.html', {'appointments': user_appointments, 'user': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                messages.error(request, 'Admin users are redirected to the admin panel.')
                login(request, user)
                return redirect('/admin/')
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def user_logout(request):
    """
    Log out the user and redirect to the login page.
    """
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

def logout_view(request):
    logout(request)

    request.session.flush()
    return redirect('login')

def home(request):
    return render(request, 'index.html')  # Show homepage


def about(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)

        messages.success(request, "Your message has been sent successfully!")       
        return redirect('contact')
    
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def gallery(request):
    return render(request, 'gallery.html')

def team(request):
    return render(request, 'team.html')


def blog(request):
    return render(request, 'blog.html')

def appointment(request):
    return render(request, 'appointment.html')

@csrf_exempt
def appointment_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        department = request.POST.get("department")
        date = request.POST.get("date")
        payment_proof = request.FILES.get('payment_proof')
        message = request.POST.get("message")

        if not all([name, email, phone, department, date, message]):
            messages.error(request, "All fields are required.")
            return render(request, 'appointment.html')

        try:
            AppointmentRequest.objects.create(
                name=name,
                email=email,
                phone=phone,
                department=department,
                date=date,
                payment_proof=payment_proof,
                message=message,
                confirmed=False  
            )
            messages.success(request, "Your appointment request has been submitted successfully.")
            return redirect('appointment')
        except Exception as e:
            messages.error(request, f"Error saving data: {str(e)}")
            return render(request, 'appointment.html')

    return render(request, 'appointment.html')

@login_required
def confirm_appointment(request, appointment_id):
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to confirm appointments.")
        return redirect('profile')

    appointment = get_object_or_404(AppointmentRequest, id=appointment_id)
    appointment.confirmed = True
    appointment.confirmed_time = timezone.now().time()  
    appointment.save()

    messages.success(request, f"Appointment for {appointment.name} has been confirmed.")
    return redirect('profile')  # Redirect to profile page after confirmation

@staff_member_required
def upload_report(request):
    if request.method == 'POST' and 'report_image' in request.FILES:
        report_image = request.FILES['report_image']
        user = request.user
        new_report = Report(image=report_image)
        new_report.save()
        return redirect('profile')  # Redirect back to profile after uploading

    return render(request, 'profile.html')