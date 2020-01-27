# Ship it - simple shipment management tool

## Project overview

Shipit is a simplified tool for Shipment simple tracking. Where Companies can check the status of their shipments
This tool is for tracking shipments between companies.

### Setup

Use `Python 3` for back-end

All the requirements have been described in `Pipfile`. Make sure you add all your back-end requirements there as well!
Initial requirements include:

- [Django](https://docs.djangoproject.com/en/1.11/) as the base framework
- [djangorestframework](https://www.django-rest-framework.org/) Framework for API
- [djangorestframework-jwt](https://getblimp.github.io/django-rest-framework-jwt/) This package provides JSON Web Token Authentication support for Django REST framework
- [django-crispy-forms](http://django-crispy-forms.readthedocs.io/en/latest/) for easier form layouts
- [django-filter](https://pypi.org/project/django-filter/) dynamic queryset filtering from URL parameters.
- [markdown](http://pythonhosted.org/Markdown/siteindex.html) for rendering markdown in HTML

The application uses Postgres db

Create a superuser

    docker-compose run web python manage.py createsuperuser

Loading initial data for projects

    docker-compose run web python manage.py loaddata shipments/fixtures/initial.json
 
Running tests
    
    ocker-compose run web python manage.py test

### Running the application

    docker-compose up

The application should be visible at `localhost:8000` 

## Api Endpoints
    v1 - created with ViewSets and Routers
    v2 - created with class views and generics
     
    /api/v1 - contains available end points
    /api/v2/shipments - (List, Create) 
    /api/v2/companies - (List, Create) 
    
    /api/v2/shipments/id=<int> - (Retrieve, Update, Destroy)
    /api/v2/shipments/tracking_no=<str> - (Retrieve, Update, Destroy)
    /api/v2/companies/id=<int> - (Retrieve, Update, Destroy)
