

"""
Local settings for bnmc_project.

Must be at the same directory as the settings.py file.

All variables are required unless stated otherwise using 'optional' comment
"""
# PYTHON IMPORTS
import os
# DJANGO IMPORTS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Add domain name, i.e. example.com
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

# needed for debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

ENABLE_HTTPS = False

# Email backend (OPTIONAL)
# Console backend is only meant for development purposes
# Please comment it for production or use the django default:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_NUMBER =''
