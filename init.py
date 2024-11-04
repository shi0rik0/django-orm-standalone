import django
import django.conf

config = {
    'INSTALLED_APPS': ['site_package'],
    'DATABASES': {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "mydatabase",
        }
    },
}
django.conf.settings.configure(**config)
django.setup()
