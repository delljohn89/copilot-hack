# AB Hospital — Patient Registration (Course-end Project 1)

A Django application that lets the hospital reception check whether a patient
is already registered and register them if they are not, instead of searching
a manual logbook of thousands of records.

## What it does

The patient's **name** is stored in the built-in `auth_user` table (SQLite),
and a `UserInfo` model stores the patient's **Unique ID** and **Date of Birth**,
linked one-to-one to the `auth_user` record.

| URL | Purpose |
| --- | --- |
| `/commoninfo` | Landing page with two buttons: **Register** and **Check** |
| `/commoninfo/add` | Registration form; on **SUBMIT** shows `successfully added!!` |
| `/commoninfo/fetch` | Textbox for a UID; on **SUBMIT** shows the patient's Name, Unique ID and DOB |

The layout uses the Bootstrap 5 front-end framework (loaded from a CDN).

## Project layout

```
course-end-project-1/
├── manage.py
├── requirements.txt
├── hospital/            # project package (settings, urls, wsgi)
└── commoninfo/          # the application
    ├── models.py        # UserInfo model (uniqueID, dob)
    ├── views.py         # addUserInfo, fetchUserInfo, index
    ├── urls.py
    ├── migrations/
    └── templates/commoninfo/
        ├── base.html
        ├── index.html   # Register / Check buttons
        ├── add.html     # registration form
        └── fetch.html   # check-by-UID form
```

## Running it

The course environment provides Python 2.7 / Django 1.8. To run:

```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Then open the live preview and append `/commoninfo` (or `/commoninfo/add`,
`/commoninfo/fetch`).

> The code also runs unchanged on Python 3 with Django up to 3.2 — it uses the
> `url()` / regex URL routing and the settings keys common to both, so it can be
> verified on a modern interpreter as well.
