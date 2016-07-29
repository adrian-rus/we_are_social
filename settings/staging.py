from base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal settings
SITE_URL = 'https://we-are-social.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://we-are-social.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'adrian.rus.business@live.com'

# Stripe settings
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_rskSLj07vIpHRYDRspDOXGZO')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_WJMXImKmYIpgK3HvCuM9vgg4')