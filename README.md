# Django Task Tracker

## The App Can be accessed here

- [Django Task Manager](https://django-task-tracker-9dd087540838.herokuapp.com/)
 

This is a simple task tracking application built with Django.


## Author

 

Onke Fanti

 

## Features

 

- Create new tasks

- Mark tasks as complete

- Delete tasks

 

## Setup and Installation

 

1. Clone the repository:

    ```

    git clone https://github.com/0nk3/tasktracker.git

    cd tasktracker

    ```

 

2. Install Django:

    ```

    pip install django

    ```
 

3. Run migrations:

    ```

    python manage.py makemigrations tasks

    python manage.py migrate

    ```


4. Start the server:

    ```

    python manage.py runserver

    ```

## Usage

 

- Visit `http://localhost:8000` in your web browser to see the list of tasks.

- To create a new task, visit `http://localhost:8000/task/new`.

- To mark a task as complete, click the "Mark as complete" button next to the task.

- To delete a task, click the "Delete" button next to the task.