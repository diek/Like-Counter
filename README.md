# Like-Counter

Keep a tally of likes per Post.

## Description

A problem given to me while interviewing for [Lights On Software](https://lightsonsoftware.com/)

## Getting Started

### Dependencies

* This code is a Django web application and requires:
  - Python >= 3.11    
  - Django >=5.1    

The remaining dependencies can be found in `pyproject.toml`
  

### Run this project locally

* Navigate to a working directory
```
git clone git@github.com:diek/like-counter.git  

cd like-counter  
```
* create a virtualenv, activate it, and install requirements  
```
python3 -m venv _env  
source _env/bin/activate  
(_env)$ python3 -m pip install --upgrade pip  
(_env)$ python3 -m pip install -r requirements  
```
* create a superuser to login
```
(_env)$ ./manage createsuperuser
```

### Import Some Data to work with
```
./manage.py loaddata users.json  
./manage.py loaddata post.json 
./manage.py loaddata like.json   
```

### Executing program

* How to run the program
```
python manage.py runserver   
```

### Testing
Disable Django-Debug Toolbar before running tests. References are found in:
- settings.py
- urls.py

## Authors

[Derrick Kearney](mailto:d_kearney@bellaliant.net)  


## Version History

* 0.1
    * Initial Release  

## License

This project is licensed under the MIT License - see the LICENSE.md file for details  

## Acknowledgments

Inspiration, code snippets, etc.  
* [Creating a Custom User Model in Django](https://testdriven.io/blog/django-custom-user-model/) from Michael Herman  

