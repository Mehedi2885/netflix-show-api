# Netflix Show api and api documentation
Written in Python/Django/django-rest-framework
## Prerequisites
* Python==3,
* Django==3.1.4,
* django-import-export==2.4.0,
* djangorestframework==3.12.2
* drf-yasg==1.20.0,
* djangorestframework-jwt==1.11.0,
## Getting started
Install python3 and above
```
pip3 insatll -r requirements.txt
```
Go to project folder:
Start migration of your project
```
python3 manage.py makemigrations 
python3 manage.py migrate    

```
Create superuser:
```
python3 manage.py createsuperuser 
```
Start django development server:
```
python3 manage.py runserver
```
### Description :
This netflix show api fully implemented JWT token authentication system, to start api first call
* ```ip:port``` 
to get details openapi documentation, create an account/register by calling 
* ``` ip:port/accounts/register```,  create an account/register by calling 
* ```ip:port/accounts/login/```, to login and get token
* ```ip:port/movie/name/?search=friends&search_fields=title```, to get desired data query with filter, search, pagination
* ```ip:port/movie/title/?limit=5&ordering=release_year&search=friends&search_fields=title```, to get same with sort, filter, search and pagination
* ```ip:port/movie/name/<id>/```, to update any specific movie data
* ```ip:port/movie/summary/```, to get full summary of movie and show
* ```ip:port/movie/country/country_name,movie or show type/```, to get movie pr show count and percent in any specific country
