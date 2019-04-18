# Bare Bones Flask APP

This is a bare bones flask app. 

Built with Procfile for potential Heroku deployment.

## Long Description

This is a python flask app developed using python 3

This app is built with recommendations for structure but has nothing in place.

There is no `config.py` file because of preferences.

There are no module, static, or template directores so any user does not need to
waste a commit erasing these directories if they do not need them.

This is a simple default application that has no goal in mind, 
and leaves a lot of open doors for expanding upon.

I recommend using [Blueprints](http://exploreflask.com/en/latest/blueprints.html) for routing
but again this is not implemented so users can pick there own preference [or follow another tutorial for routes](http://flask.pocoo.org/docs/1.0/quickstart/)

## Structure

This diagram is based on [the digital ocean structure for large apps](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)

```
~/LargeApp
  |-- run.py
  |-- config.py
  |__ /app             # Our Application Module
    |-- __init__.py
    |__ /main            # Our Tests
        |-- __init__.py
        |-- /module_one # ie (admins, budgets, users, logs, etc.)
            |-- __init__.py
            |-- controllers.py (routes)
            |-- models.py      (database or object contructor)          
            |-- services.py    (create, update, get, delete - functions)           
        |__ /templates
            |__ /module_one
                |-- hello.html
        |__ /static
        |__ ..
        |__ .
    |__ /test            # Our Tests
        |-- __init__.py
        |-- test_init.py # Example Tests

  |__ ..
  |__ .
```

## Testing

I am a big advocate of TDD (test driven design), and thus tests have been placed into this
application.

Create tests following the [Testing Flask Apps Documentation](http://flask.pocoo.org/docs/1.0/testing/)
if you want a starting point.

We need tests because `Something that is untested is broken.` as stated in the tutorial above.

This app uses [pytest for testing](https://docs.pytest.org/en/latest/)

`pytest -v -p no:warnings` Will run tests with no warnings that can be create from dependencies
you have no control over.

If you want to see print out logs in tests use `python -m unittest discover`

Then make sure we have a good enough [coverage](http://flask.pocoo.org/docs/1.0/tutorial/tests/).

```
coverage run app/*
coverage report
```

However from this [code will run the tests and allow for a more verbose coverage report](https://stackoverflow.com/questions/52568003/python-coverage-not-covering-function-contents-just-definition)

```
coverage run -m pytest app/tests/*
coverage report
```

## Useful Commands

These are useful commands for any python user to know

Create a virtual enviroment.

This code assumes you have set python3 to python.

The second `venv` actually names the virtual enviroment

`python -m venv venv`

Source the virtual enviroment

`source venv/bin/activate`

Run tests

`pytest -v -p no:warnings`

Then Check coverage

```
coverage run -m pytest app/tests/*
coverage report
```

Remember to update packages requirements with

`pip freeze > requirements.txt`

If you need to import them use

`python -m pip install -r requirements.txt`

Start applicaiton

`flask run`

This will open the app to `localhost:5000`
