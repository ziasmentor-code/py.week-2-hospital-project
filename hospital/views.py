from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Doctor, Patient, Booking


def home(request):
    recent_bookings = Booking.objects.select_related(
        'patient', 'doctor', 'doctor__department'
    ).order_by('-date', '-time')[:5]

    return render(request, 'hospital/home.html', {
        'recent_bookings': recent_bookings
    })


def department_list(request):
    departments = Department.objects.all()

    color_map = {
        "Cardiology": ("bg-red-100", "text-red-600", "fa-heartbeat"),
        "ENT": ("bg-green-100", "text-green-600", "fa-ear-listen"),
        "Neurology": ("bg-purple-100", "text-purple-600", "fa-brain"),
    }

    dept_data = []
    for d in departments:
        bg, text, icon = color_map.get(
            d.name, ("bg-blue-100", "text-blue-600", "fa-hospital")
        )
        dept_data.append({
            "id": d.id,
            "name": d.name,
            "description": d.description,
            "bg": bg,
            "text": text,
            "icon": icon,
        })

    return render(request, 'hospital/department_list.html', {
        'departments': dept_data
    })


def department_doctors(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    doctors = Doctor.objects.filter(department=department)

    return render(request, 'hospital/department_doctors.html', {
        'department': department,
        'doctors': doctors
    })


def doctor_list(request):
    doctors = Doctor.objects.select_related('department')
    return render(request, 'hospital/doctor_list.html', {
        'doctors': doctors
    })


def booking_create(request):
    doctors = Doctor.objects.select_related('department')

    if request.method == 'POST':
        patient = Patient.objects.create(
            name=request.POST['patient_name'],
            age=request.POST['age'],
            contact=request.POST['contact']
        )

        doctor = Doctor.objects.get(id=request.POST['doctor'])

        Booking.objects.create(
            patient=patient,
            doctor=doctor,
            date=request.POST['date'],
            time=request.POST['time']
        )

        return redirect('booking_list')

    return render(request, 'hospital/booking_form.html', {
        'doctors': doctors
    })


def booking_list(request):
    bookings = Booking.objects.select_related(
        'patient', 'doctor', 'doctor__department'
    )
    return render(request, 'hospital/booking_list.html', {
        'bookings': bookings
    })


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {
        'patients': patients
    })


# ✏️ EDIT BOOKING
def booking_edit(request, id):
    booking = get_object_or_404(Booking, id=id)
    doctors = Doctor.objects.select_related('department')

    if request.method == 'POST':
        booking.patient.name = request.POST['patient_name']
        booking.patient.age = request.POST['age']
        booking.patient.contact = request.POST['contact']
        booking.patient.save()

        booking.doctor = Doctor.objects.get(id=request.POST['doctor'])
        booking.date = request.POST['date']
        booking.time = request.POST['time']
        booking.save()

        return redirect('booking_list')

    return render(request, 'hospital/booking_form.html', {
        'booking': booking,
        'doctors': doctors
    })


# 🗑️ DELETE BOOKING
def booking_delete(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()
    return redirect('booking_list')

