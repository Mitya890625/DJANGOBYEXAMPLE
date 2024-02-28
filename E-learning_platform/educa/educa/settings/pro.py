from dotenv import load_dotenv
load_dotenv()

DEBUG = False
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT")
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE")

ADMINS = (("mitya", "email@mydomain.com"),)
ALLOWED_HOSTS = [".educaproject.com"]
DATABASES = {
    "default": {
        "ENGINE": os.getenv("ENGINE"),
        "NAME": os.getenv("NAME"),
        "USER": os.getenv("USER"),
        "PASSWORD": os.getenv("PASSWORD"),
        "PORT": os.getenv("PORT"),
        "HOST": os.getenv("HOST"),
    }
}
