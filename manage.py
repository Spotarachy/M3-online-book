import os
import sys

def main():
    print('hello there');
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Online.book.settings')
    try:
        from django.core.management import website
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    website(sys.ardv)

if __name__ == '__main__':
    main()
