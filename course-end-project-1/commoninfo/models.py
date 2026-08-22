from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    """Stores the extra patient details.

    The patient's name is kept in the built-in ``auth_user`` table (via the
    linked ``User`` record); this model holds the patient's unique ID and
    date of birth.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uniqueID = models.CharField(max_length=100, unique=True)
    dob = models.DateField()

    def __str__(self):
        return "%s (%s)" % (self.uniqueID, self.user.get_full_name())

    # Python 2 (Django 1.8) uses __unicode__ for the display string.
    __unicode__ = __str__
