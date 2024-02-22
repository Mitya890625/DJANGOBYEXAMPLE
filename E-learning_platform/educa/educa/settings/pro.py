DEBUG = False
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

ADMINS = (("mitya", "email@mydomain.com"),)
ALLOWED_HOSTS = [".educaproject.com"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "NAME": "educa",
        "USER": "educa",
        "PASSWORD": "educa",
        "PORT": 5433,
    }
}
