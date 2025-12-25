from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Application
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse

# Create your views here.
@login_required
def dashboard(request):
    applications = Application.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, "tracker/dashboard.html", {
        "applications": applications
    })


@login_required
def add_application(request):
    if request.method == "POST":
        company = request.POST.get("company_name")
        position = request.POST.get("position_title")
        applied_date = request.POST.get("applied_date")
        interview_date = request.POST.get("interview_date")
        notes = request.POST.get("notes")

        Application.objects.create(
            user=request.user,
            company_name=company,
            position_title=position,
            applied_date=applied_date,
            interview_date=interview_date if interview_date else None,
            notes=notes
        )

        return redirect("tracker:dashboard")

    return render(request, "tracker/add_application.html")


@login_required
def edit_application(request, app_id):
    application = get_object_or_404(
        Application,
        id=app_id,
        user=request.user
    )

    if request.method == "POST":
        application.company_name = request.POST.get("company_name")
        application.position_title = request.POST.get("position_title")
        application.status = request.POST.get("status")
        application.applied_date = request.POST.get("applied_date")
        application.interview_date = request.POST.get("interview_date") or None
        application.notes = request.POST.get("notes")

        application.save()
        return redirect("tracker:dashboard")

    return render(request, "tracker/edit_application.html", {
        "application": application
    })


@login_required
def delete_application(request, app_id):
    application = get_object_or_404(
        Application,
        id=app_id,
        user=request.user
    )

    if request.method == "POST":
        application.delete()
        return redirect("tracker:dashboard")

    return render(request, "tracker/delete_application.html", {
        "application": application
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("tracker:dashboard")
        else:
            return render(request, "tracker/login.html", {
                "message": "Invalid username or password."
            })

    return render(request, "tracker/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "tracker/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "tracker/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return redirect("tracker:dashboard")

    return render(request, "tracker/register.html")


@login_required
def update_status(request, app_id):
    if request.method == "POST":
        application = get_object_or_404(
            Application,
            id=app_id,
            user=request.user
        )

        new_status = request.POST.get("status")
        application.status = new_status
        application.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})


@login_required
def delete_ajax(request, app_id):
    if request.method == "POST":
        application = get_object_or_404(
            Application,
            id=app_id,
            user=request.user
        )
        application.delete()
        return JsonResponse({"success": True})

    return JsonResponse({"success": False})
