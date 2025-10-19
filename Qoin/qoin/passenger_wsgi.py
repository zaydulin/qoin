# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/k/kot1138/qoin/public_html/Qoin')
sys.path.insert(1, '/home/k/kot1138/qoin/public_html/venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'qoin.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
