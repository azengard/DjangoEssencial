import os
import sys

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY='7nv*v04^!g3^$v8gjvmon@psu8vpc&vhfys1s7!0m^2)7a#jp$',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'django.contrib.webdesign',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
