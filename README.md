# About this project

This is not an app, is only a structure for implement a Django with some configurations, that configs are:

* Docker implementation support
* Separate stages for develop and check if the config is useful for productions, staging, qa or testing stages
* Add an author @AdrianPardo99 directory structure
* Add Docker Compose for run and build a local implementation, that you can forward with a reverse proxy / serverless or anything that you want for expose your local app to Internet

# What do you need for run this app?

You only need to install (That autor use, you can use whatever you want if you now how to use it) Docker and Docker Compose

And run

```bash
docker-compose up --build -d
```

With this you can run anything in the current project app, and you only write and test your own ideas

# What about the structure of the project?

The project has the next directory structure for custom as you wish

```
    /                       ->  Root path where the configs and some files are 
    | docker-compose.yml    ->  Docker compose config file where we found the Django Container, and DB Container
    | .env-example          ->  File with the environment variables example config for work with the project
    | .gitignore            ->  File with the config ignored files that create some IDE's, Text Editors or anything that you wish to ignore
    | app/                  ->  Directory where the Django Project has all the source files
    | manage.py             ->  Python file where we can call all the commands for config and admin the Django App
    | | app/                ->  Directory that has the configuration about Django
    | | |   settings.py     ->  Anything like config DB, services, directories, templates, or anything related to config and work with 
    | | |                         add some new py modules may config here
    | | |   wsgi.py         ->  File for web app running (Use some server like guinicorn and other webserver)
    | | |   asgi.py         ->  File for web app async running (Use some server like Celery, Kafka or other async server)
    | | |   url.py          ->  File for manage the url access to app (Routers and list URLS may paste here if you want to custom more the project)
    | | |   __init__.py     ->  File for make or create a Python module/directory access
    | | apps/               ->  Directory where you found all the modules and models that use the Django Project
```

# What technologies currently has

* Django
* Django Rest Framework
* Django Filters
* Postgres
* Docker + Docker Compose
