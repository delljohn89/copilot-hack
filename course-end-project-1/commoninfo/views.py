from django.contrib.auth.models import User
from django.shortcuts import render

from .models import UserInfo


def index(request):
    """Landing page for /commoninfo with the Register and Check buttons."""
    return render(request, 'commoninfo/index.html')


def addUserInfo(request):
    """Register a patient.

    On POST the patient's name is stored in the built-in ``auth_user`` table
    and the unique ID / date of birth are stored in the ``UserInfo`` model.
    """
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        uniqueID = request.POST.get('uniqueID', '').strip()
        dob = request.POST.get('dob', '').strip()

        if not (name and uniqueID and dob):
            context['error'] = 'Please fill in name, unique ID and date of birth.'
        elif UserInfo.objects.filter(uniqueID=uniqueID).exists():
            context['error'] = 'A patient with this Unique ID is already registered.'
        else:
            # Store the patient's name in auth_user.  Username must be unique,
            # so the unique ID is reused as the username.
            first_name, last_name = _split_name(name)
            user = User.objects.create(
                username=uniqueID,
                first_name=first_name,
                last_name=last_name,
            )
            UserInfo.objects.create(user=user, uniqueID=uniqueID, dob=dob)
            context['success'] = 'successfully added!!'

    return render(request, 'commoninfo/add.html', context)


def fetchUserInfo(request):
    """Look a patient up by unique ID and show name, unique ID and DOB."""
    context = {}
    if request.method == 'POST':
        uniqueID = request.POST.get('uniqueID', '').strip()
        try:
            info = UserInfo.objects.get(uniqueID=uniqueID)
        except UserInfo.DoesNotExist:
            context['error'] = 'No patient is registered with Unique ID "%s".' % uniqueID
        else:
            context['patient'] = {
                'name': info.user.get_full_name() or info.user.username,
                'uniqueID': info.uniqueID,
                'dob': info.dob,
            }

    return render(request, 'commoninfo/fetch.html', context)


def _split_name(name):
    """Split a full name into first and last name parts."""
    parts = name.split(None, 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return name, ''
