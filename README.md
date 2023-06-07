# levelup-server

# Setup and Installs
- book 3 ch 1
- https://github.com/nashville-software-school/bangazon-llc/blob/cohort-62/book-3-levelup/chapters/DRF_INSTALLS.md 

## [LVL-Up React Client-Side App](https://github.com/AngieMGonzalez/lvl-up-client)

# ERD + Data Design
- book 3 ch 2: setup Models
- https://github.com/nashville-software-school/bangazon-llc/blob/cohort-62/book-3-levelup/chapters/LU_DATA_DESIGN.md
- ERD made with dbdiagram.io
- https://dbdiagram.io/d/64552d86dca9fb07c4953c37
- Carrie's notes...
- settlers of Catan, bridge, checkers, knitting, book clubs, etc...
- "I want a way to schedule events for people to play games."
- people can create any game they want
- anyone should be able to schedule an event for any game that has been added
-  I want people to say if they are coming. That way the person holding the event knows how many people to expect
- anyone can sign up for any event
- Migrate Models
- `python3 manage.py makemigrations levelupapi`
- `python3 manage.py migrate`

<img width="1310" alt="ERD" src="https://user-images.githubusercontent.com/114124374/236859613-a496fbd0-fb9d-46b8-9789-82f8e145984b.png">

### ASSUMPTIONS: 
- The `Game` table will have a one to many relationship with `GameType`
- since a game will be associated with 1 game type and
- a game type can be associated with many games.
- The `Game` will also have a one to many relationship with `Gamer` because gamers can create more than one game.
- The `Event` table will have a 1 to many relationship with `Gamer`, called the organizer, because gamers can host many events but an event will only have 1 host.
- Each `Event` should also include what game is going to be played at the event
- To keep track of who is attending events, there is a many to many relationship between gamers and events. There will need to be a join table to connect that many to many relationship.
- ask each Gamer to provide a short bio when they register
- There is a many-many relationship between the Gamers and Events to show who is attending an event
- The field on the Event model should be called attendees

## Resources 4.2 Django
- [Django Models - Overview of Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Extending the User Model - Explanation for how to add fields to the Django user](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#extending-the-existing-user-model)
- Model Field Types - All the options for data types in a model [4.2 Django Field Types Docs](https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types)
- [One to Many Relationships - How to add a foreign key to a model](https://docs.djangoproject.com/en/4.2/topics/db/models/#many-to-one-relationships)
- [Many to Many Relationships - How to set up a Many-Many Relationship](https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django) 🌭🌭🌭🌭🌭

## Fixtures
- [Documentation: Providing initial data for models](https://docs.djangoproject.com/en/4.2/howto/initial-data/)
- [How to pre load Data Video](https://www.youtube.com/watch?v=1_MROM737FI)

- can start solely the server with `python3 manage.py runserver` command or `./manage.py runserver`
- Username is `Carrie1945`
- Password is `me`

## Custom Actions
- join
- https://github.com/nashville-software-school/bangazon-llc/blob/cohort-62/book-3-levelup/chapters/LU_CUSTOM_ACTION.md 
- a custom action = a method on a ViewSet
- a custom action allows the client to put a verb at the end of the URL to initiate a custom action
- a custom action can specify which HTTP methods are supported by it
- able to create a custom action that includes the pk of obj you want to retrieve from the DB
- With Django REST Framework, you can create a custom action that your API will support by using the `@action` decorator above a method within a ViewSet
- For this action, you want a client to make a request to allow a gamer to `sign up` for an `event`
- There will also be an action to allow a `gamer` to `leave` an event
- JSON post body for custom signup POST/create: 
```
{
    "user": 1
}
```

# Time for test_
- https://github.com/nashville-software-school/bangazon-llc/blob/cohort-62/book-4-bangazon/chapters/TESTING.md
- Create `tests` directory in project
- Create `tests/__init__.py` module
- Create `tests/{resource_name}_tests.py` module for each resource
- Write test classes in each test module
Import test classes into `__init__.py`
- Run `python3 manage.py test tests -v 1` to execute all test classes
- All functions that contain integration tests must start with `test_`
- i.e. If the test is for modifying a game is `test_modifying_a_game_record_via_put_method()`

## Django Templates
- [Django Views](https://docs.djangoproject.com/en/4.2/topics/class-based-views/intro/)
- [Python Comprehension](https://www.geeksforgeeks.org/comprehensions-in-python/)
- [Executing SQL within Django](https://docs.djangoproject.com/en/4.2/topics/db/sql/#executing-custom-sql-directly)
- [Django Templates](https://docs.djangoproject.com/en/4.2/topics/templates/)
- Setup: Be in your LevelUp project directory. Create a new application for producing HTML reports.
- `python3 manage.py startapp levelupreports`
- Add `levelupreports` to `INSTALLED_APPS = []` in the `settings.py` module
- Delete the `models.py` and `views.py` modules in the application
- Create a `levelup/levelupreports/views` directory and create the following two modules in it: `__init__.py` + `helpers.py`
- Create a `levelup/levelupreports/templates` directory
- Create a `levelup/levelupreports/urls.py` module
- Note: There's a class view with a get method. Instead of `list`, `retrieve`, `update`, and `destroy` like the *Rest Framework* views have, *basic django* views have `get`, `post`, `put`, and `delete`. Notice that all the imports are coming from `django` instead of `rest_framework`. That is how you can tell this will be a *django* view. While we could still use the `ORM` to retrieve data from the database, `SQL` is an important tool to continue practicing.
- `{{ user.full_name }}`
- ```
{% for games in games %}
    {{ game.title }}
{% endfor %}
```
- `if/then` blocks
