# Week 4

Assignment for the week: [Freeshelf](https://classroom.github.com/a/lentf7r1)

## Day 1

- Bulk loading data
- Model associations

### References

- [Crystal's demo](https://github.com/momentum-cohort-2018-10/hello-web-app-cat9563)
  - [CSS-Tricks guide to flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
  - [Interneting is Hard - Guide to Flexbox](https://internetingishard.com/html-and-css/flexbox/)
- [Accessing related objects - Django docs](https://docs.djangoproject.com/en/2.1/ref/models/relations/)
- [Django Extensions](https://django-extensions.readthedocs.io/en/latest/)

## Day 2

- Registration and login
- Model associations, continued

### References

- [How to Create Django User Sign Up View](https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html)
- [Awesome Django](http://awesome-django.com/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)

## Day 3

- Review

- Models, Views, and Templates

  - Models communicate with the database
    - Each model has one table in the database
    - Each model field maps to a field in that table
    - Models can have methods
  - Views handle web requests and responses -- communicate with the browser
    - URLs route requests to views
    - All the views we've seen so far are functions
  - Templates -- the HTML that makes up your website

- Other parts of Django

  - Forms
    - takes user input
    - validates and cleans user input
    - ModelForm saves input
    - displays form in our template
  - Admin
  - User authentication
  - Code to communicate with a database
  - Settings
  - Command-line management framework
  - Routing

- Things about Django

  - Open source code

- How is a Django project organized?
  - Projects are made of settings + apps
  - Project directory
    - settings.py
    - urls.py
  - App directory
    - models.py
    - views.py
    - admin.py
    - tests.py
    - templates/
    - any other Python files/modules that we want
      - forms.py
