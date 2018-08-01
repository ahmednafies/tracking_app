# Ship it - simple shipment management tool

## Project overview

Shipit is a simplified tool for Shipment simple tracking. Where Companies can check the status of their shipments
This tool is for tracking shipments between companies.

## Tasks
- Please create REST API functionality to maintain a list of shipments (fields are freetext fields, up to your choice).
- Required functionality: list, retrieve, create, update.
- Python language with utilization of Django REST framework.
- No forms should be used
- Include tests (pytest, or phpunit, or etc).
- Code must be provided in a zip file.

### Setup

Use `Python 3` for back-end

All the requirements have been described in `requirements.txt`. Make sure you add all your back-end requirements there as well!
Initial requirements include:

- [Django](https://docs.djangoproject.com/en/1.11/) as the base framework
- [djangorestframework](https://www.django-rest-framework.org/) Framework for API
- [djangorestframework-jwt](https://getblimp.github.io/django-rest-framework-jwt/) This package provides JSON Web Token Authentication support for Django REST framework
- [django-crispy-forms](http://django-crispy-forms.readthedocs.io/en/latest/) for easier form layouts
- [django-filter](https://pypi.org/project/django-filter/) dynamic queryset filtering from URL parameters.
- [markdown](http://pythonhosted.org/Markdown/siteindex.html) for rendering markdown in HTML


The application uses SQLite for the database by default for simplicity reasons.

Migrate the database before the first run

    python manage.py migrate

Create a superuser

    python manage.py createsuperuser

Loading initial data for projects

    python manage.py loaddata shipments/fixtures/initial.json
 
 Running tests
    
    python manage.py test

### Running the application

    python manage.py runserver

The application should be visible at `127.0.0.1:8000` 

## Api Endpoints
    v1 - created with ViewSets and Routers
    v2 - created with class views and generics
     
    /api/v1 - contains available end points
    /api/v2/shipments - (List, Create) 
    /api/v2/companies - (List, Create) 
    
    /api/v2/shipments/id=<int> - (Retrieve, Update, Destroy)
    /api/v2/shipments/tracking_no=<str> - (Retrieve, Update, Destroy)
    /api/v2/companies/id=<int> - (Retrieve, Update, Destroy)

    
## What has been done

- Created API where users can Create, Read, Update and Delete both Companies and Shipments at "/api/v1"
- api v1 is experimental and thus no tests and not much validations where created for v1
- Created another API (just because I was enjoying it) at "/api/v2"
- Dashboard is created to view current Shipments statuses at "/dashboard" as well status and delivery time can be updated
- Assignment page is generated from this README.md
- Admin interface is created to manipulate data easily with proper filters (as well to show that I can learn more about Django)
- I used "ViewSets" and "Routers" to show that I am doing stuff the Django Way, The Flask way (e.g Flask_restplus)
would be usual function based views or class based views perhaps using mixins as well.
but I wanted to use something Which I have never used before. (this is why I have api/v1 and api/v2)
- I created tests to cover mostly for authenticaion and CRUD for companies, I skipped creating the same tests for Shipments
- I wanted to integrate Vue.js to impress you guys but I ran out of time.
- Thank you for this task, I really enjoyed it and I think I will create more django rest api using this framework.
 

## Weaknesses
- While cleaning and commenting I managed to mess up the git version since I was using pycharm history interchangebly (first time this happens to me)
- so you cannot really see howevery this is developed in verions - but anyways I used [Git feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
- not enough validations, I did not create validations for on database levels, I wanted to show I can do validation in djangorestframework serializers
- Test does not include all Shipments and others types of authentications like basic authentication - (tested it manually using CURL)



