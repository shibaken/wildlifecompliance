import os
import confy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
confy.read_environment_file(BASE_DIR+"/.env")
os.environ.setdefault("BASE_DIR", BASE_DIR)
from django.core.exceptions import ImproperlyConfigured
from ledger.settings_base import *

os.environ['LEDGER_PRODUCT_CUSTOM_FIELDS'] = "('ledger_description','quantity','price_incl_tax','price_excl_tax','oracle_code')"
os.environ['LEDGER_REFUND_TRANSACTION_CALLBACK_MODULE'] = 'wildlifecompliance:wildlifecompliance.components.applications.api.application_refund_callback'
os.environ['LEDGER_INVOICE_TRANSACTION_CALLBACK_MODULE'] = 'wildlifecompliance:wildlifecompliance.components.applications.api.application_invoice_callback'

ROOT_URLCONF = 'wildlifecompliance.urls'
SITE_ID = 1
SYSTEM_MAINTENANCE_WARNING = env('SYSTEM_MAINTENANCE_WARNING', 24)  # hours

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_wc')
SHOW_DEBUG_TOOLBAR = env('SHOW_DEBUG_TOOLBAR', False)
APPEND_SOURCE_TO_RICHTEXT_ADMIN = env('APPEND_SOURCE_TO_RICHTEXT_ADMIN', False)

if SHOW_DEBUG_TOOLBAR:
#    def get_ip():
#        import subprocess
#        route = subprocess.Popen(('ip', 'route'), stdout=subprocess.PIPE)
#        network = subprocess.check_output(
#            ('grep', '-Po', 'src \K[\d.]+\.'), stdin=route.stdout
#        ).decode().rstrip()
#        route.wait()
#        network_gateway = network + '1'
#        return network_gateway

    def show_toolbar(request):
        return True

    MIDDLEWARE_CLASSES += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    #INTERNAL_IPS = ('127.0.0.1', 'localhost', get_ip())
    INTERNAL_IPS = ('127.0.0.1', 'localhost')

    # this dict removes check to dtermine if toolbar should display --> works for rks docker container
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
        'INTERCEPT_REDIRECTS': False,
    }

STATIC_URL = '/static/'

INSTALLED_APPS += [
    'reversion_compare',
    'django.contrib.humanize',
    'bootstrap3',
    'wildlifecompliance',
    'wildlifecompliance.components.main',
    'wildlifecompliance.components.applications',
    'wildlifecompliance.components.organisations',
    'wildlifecompliance.components.licences',
    'wildlifecompliance.components.users',
    'wildlifecompliance.components.returns',
    'wildlifecompliance.components.call_email',
    'wildlifecompliance.components.offence',
    'wildlifecompliance.components.inspection',
    'wildlifecompliance.components.sanction_outcome',
    'wildlifecompliance.components.wc_payments',
    'wildlifecompliance.components.legal_case',
    'wildlifecompliance.components.artifact',
    'taggit',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_datatables',
    'smart_selects',
    'ckeditor',
]

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat'],
            #[ 'Source']
        ]
    },
    'pdf_config': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            [ '-', 'Bold', 'Italic' ],
            [ 'Format' ],
            [ 'NumberedList', 'BulletedList' ],
            [ 'Table' ],
            #[ 'Source']
        ]
    },
}

if APPEND_SOURCE_TO_RICHTEXT_ADMIN:
    CKEDITOR_CONFIGS['pdf_config']['toolbar_Custom'].append(['Source'])


ADD_REVERSION_ADMIN = True

# maximum number of days allowed for a booking
WSGI_APPLICATION = 'wildlifecompliance.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 50,
}

USE_DJANGO_JQUERY=True

if env('EMAIL_INSTANCE') is not None and env('EMAIL_INSTANCE','') != 'PROD':
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ('rest_framework.renderers.BrowsableAPIRenderer',)

MIDDLEWARE_CLASSES += [
    'wildlifecompliance.middleware.FirstTimeNagScreenMiddleware'
]

LATEX_GRAPHIC_FOLDER = os.path.join(BASE_DIR,"templates","latex","images")

TEMPLATES[0]['DIRS'].append(
    os.path.join(
        BASE_DIR,
        'wildlifecompliance',
        'templates'))
TEMPLATES[0]['DIRS'].append(
    os.path.join(
        BASE_DIR,
        'wildlifecompliance',
        'components',
        'organisations',
        'templates'))
TEMPLATES[0]['DIRS'].append(
    os.path.join(
        BASE_DIR,
        'wildlifecompliance',
        'components',
        'emails',
        'templates'))
del BOOTSTRAP3['css_url']
#BOOTSTRAP3 = {
#    'jquery_url': '//static.dbca.wa.gov.au/static/libs/jquery/2.2.1/jquery.min.js',
#    'base_url': '//static.dbca.wa.gov.au/static/libs/twitter-bootstrap/3.3.6/',
#    'css_url': None,
#    'theme_url': None,
#    'javascript_url': None,
#    'javascript_in_head': False,
#    'include_jquery': False,
#    'required_css_class': 'required-form-field',
#    'set_placeholder': False,
#}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'wildlifecompliance', 'cache'),
    }
}
CRON_CLASSES = [
    'wildlifecompliance.cron.OracleIntegrationCronJob',
]

# Additional logging for wildlifecompliance
LOGGING['handlers']['application_checkout'] = {
    'level': 'INFO',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': os.path.join(
        BASE_DIR,
        'logs',
        'wildlifecompliance_application_checkout.log'),
    'formatter': 'verbose',
    'maxBytes': 5242880}
LOGGING['loggers']['application_checkout'] = {
    'handlers': ['application_checkout'],
    'level': 'INFO'
}
# # Additional logging for compliancemanagement
# LOGGING['handlers']['compliancemanagement'] = {
#     'level': 'INFO',
#     'class': 'logging.handlers.RotatingFileHandler',
#     'filename': os.path.join(
#         BASE_DIR,
#         'logs',
#         'wildlifecompliance_compliancemanagement.log'),
#     'formatter': 'verbose',
#     'maxBytes': 5242880}
# LOGGING['loggers']['compliancemanagement'] = {
#     'handlers': ['compliancemanagement'],
#     'level': 'INFO'
# }
print(BASE_DIR)
STATICFILES_DIRS.append(
    os.path.join(
        os.path.join(
            BASE_DIR,
            'wildlifecompliance',
            'static')))
DEV_STATIC = env('DEV_STATIC', False)
DEV_STATIC_URL = env('DEV_STATIC_URL')
DEV_APP_BUILD_URL = env('DEV_APP_BUILD_URL')  # URL of the Dev app.js served by webpack & express
BUILD_TAG = env('BUILD_TAG', '0.0.0')  # URL of the Dev app.js served by webpack & express
if DEV_STATIC and not DEV_STATIC_URL:
    raise ImproperlyConfigured(
        'If running in DEV_STATIC, DEV_STATIC_URL has to be set')
DATA_UPLOAD_MAX_NUMBER_FIELDS = None

# Department details
SYSTEM_NAME = env('SYSTEM_NAME', 'Wildlife Licensing System')
SYSTEM_EMAIL = env('SYSTEM_EMAIL', 'wildlifelicensing@dbca.wa.gov.au')

WC_PAYMENT_SYSTEM_ID = env('WC_PAYMENT_SYSTEM_ID', 'S566')
WC_PAYMENT_SYSTEM_PREFIX = env('PAYMENT_SYSTEM_PREFIX', WC_PAYMENT_SYSTEM_ID.replace('S', '0'))
PS_PAYMENT_SYSTEM_ID = WC_PAYMENT_SYSTEM_ID
WC_PAYMENT_SYSTEM_URL_PDF = env('WC_PAYMENT_SYSTEM_URL_PDF', '/ledger/payments/invoice-pdf/')
WC_PAYMENT_SYSTEM_URL_INV = env('WC_PAYMENT_SYSTEM_URL_INV', '/ledger/payments/invoice/')

COLS_ADMIN_GROUP = env('COLS_ADMIN_GROUP', 'COLS Admin')
if not VALID_SYSTEMS:
    VALID_SYSTEMS = [WC_PAYMENT_SYSTEM_ID]
DEP_URL = env('DEP_URL', 'www.dbca.wa.gov.au')
DEP_PHONE = env('DEP_PHONE', '(08) 9219 9831')
DEP_FAX = env('DEP_FAX', '(08) 9423 8242')
DEP_POSTAL = env(
    'DEP_POSTAL',
    'Locked Bag 104, Bentley Delivery Centre, Western Australia 6983')
DEP_NAME = env(
    'DEP_NAME',
    'Department of Biodiversity, Conservation and Attractions')
DEPT_DOMAINS = env('DEPT_DOMAINS', ['dpaw.wa.gov.au', 'dbca.wa.gov.au'])
SITE_PREFIX = env('SITE_PREFIX')
SITE_DOMAIN = env('SITE_DOMAIN')
GROUP_PREFIX = env('GROUP_PREFIX', 'Wildlife Compliance')
SITE_URL = env('SITE_URL', 'https://' + SITE_PREFIX + '.' + SITE_DOMAIN)
EXT_USER_API_ROOT_URL = env('EXT_USER_API_ROOT_URL', None)
EXCEL_OUTPUT_PATH = env('EXCEL_OUTPUT_PATH')
ALLOW_EMAIL_ADMINS = env('ALLOW_EMAIL_ADMINS', False)  # Allows internal pages to be accessed via email authentication
SYSTEM_APP_LABEL = env('SYSTEM_APP_LABEL', 'wildlifecompliance')  # global app_label for group permissions filtering
RENEWAL_PERIOD_DAYS = env('RENEWAL_PERIOD_DAYS', 30)
GEOCODING_ADDRESS_SEARCH_TOKEN = env('GEOCODING_ADDRESS_SEARCH_TOKEN', 'ACCESS_TOKEN_NOT_FOUND')
DOT_EMAIL_ADDRESS = env('DOT_EMAIL_ADDRESS')

# Details for Threathened Species and Communities server.
TSC_URL = env('TSC_URL', 'https://tsc.dbca.wa.gov.au')
TSC_AUTH = env('TSC_AUTH', 'NO_AUTH')
CRON_RUN_AT_TIMES = env('CRON_RUN_AT_TIMES', '02:05')

# if DEBUG:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
