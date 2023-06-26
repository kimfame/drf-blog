# React DRF Blog Backend

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

## Requirements

- Python 3.11
- Poetry

## Setup

To get started with using DRF Blog, run the following steps:

#### 1. Create .env file

```bash
$ cp env.template .env
```

#### 2. Edit .env file

```
# Environment mode
# local, dev, prod
ENV_MODE=local

# Admin URL path
# Example) admin -> http://localhost:8000/admin
ADMIN_URL=admin

# Django secret key
SECRET_KEY=ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890abcdefghijklm

# Database
# It's only for dev, prod settings
DB_ENGINE=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

# Backend domain
# It's only for dev, prod settings
# Added in ALLOWED_HOSTS
# Example) 'api.blog.com'
BACKEND_DOMAIN=

# Frontend URL for React app
# Added in CORS_ALLOWED_ORIGINS
# Example) https://blog.com
FRONTEND_URL=http://localhost:3000
```

#### 2. Install packages and DB migration

```bash
$ poetry install

$ poetry python manage.py migrate
```

#### (Option) Create dummy data for testing

```bash
$ ./scripts/local_data_reset.sh
```

#### 3. Run local server

```bash
$ poetry python manage.py runserver
```

#### Test

```bash
$ poetry python manage.py test
```

## License

Licensed under the
[MIT](https://github.com/kimfame/react-drf-blog/blob/main/react-drf-blog-api/LICENSE) License.
