#!/usr/bin/env python
"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from os.path import dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))
# import sys
#sys.path.insert(0,PROJECT_DIR)
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
#sys.path.append('/home/ruixif/database/mysite')
#sys.path.append('/home/ruixif/database')

application = get_wsgi_application()
