from base import *
import dj_database_url
import settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

DATABASES['default'] = dj_database_url.parse(
    'mysql://b84bfa1e8d5e71:1c88a16b@eu-cdbr-west-01.cleardb.com/heroku_54e64eee9090d14?reconnect=true')

# PayPal settings
SITE_URL = 'https://we-are-social.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://we-are-social.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'adrian.rus.business@live.com'

# Stripe settings
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_rskSLj07vIpHRYDRspDOXGZO')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_WJMXImKmYIpgK3HvCuM9vgg4')