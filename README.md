# Simple Inventory

Simple Inventory Management System

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This project is scaffolded by cookiecutter-django due to it provides full linting, typechecking and containerization.

For the code that you may concern, please look at:

- simple_inventory/inventory/\*

## Settings

Before proceed, please check the local envs in. .envs/.local/\*.

You can set the super username and password and db connections

### Run locally

This will require docker and docker-compose.

Using Make

```bash
make build
make up
```

or using docker-compose

```bash
docker compose -f docker-compose.local.yml up -d
```

### Using the app

After you setup the docker container, you can proceed to create a superuser in the django container to access the admin and inventory page.

If you have set the .envs/.local/.django superuser vars correctly, you can login with username of `DJANGO_SUPERUSER_USERNAME` and password of `DJANGO_SUPERUSER_PASSWORD`.

```bash
python manage.py createsuperuser
```

> [!NOTE]
> Make sure that all migrations are rightfully applied.
>
> ```bash
> python manage.py migrate
> ```

Afterwards, you should be able to access the server on:

1. http://locahost:8000/admin - Admin page
2. http://locahost:8000/inventory - Inventory list
3. http://locahost:8000/inventory/:pk - Inventory detail
4. http://locahost:8000/api/inventory - Inventory List API

Note all pages are being protected with session-based auth, login through authorized user is needed.

#### Running tests with pytest

```bash
pytest simple_inventory/inventory
```

#### Screenshot

Inventory List
![Inventory List](docs/screenshots/inventory-list.png)
Inventory Detail
![Inventory Detail](docs/screenshots/inventory-detail.png)
Inventory List API
![Inventory List API](docs/screenshots/inventory-list-api.png)

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).
