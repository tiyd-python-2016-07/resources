
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h)2%m8_$7anvtz1_m_b+pqzm7t$+9r!_)pi9j4ck@m2jgb_p(v'



# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'to_do_list',
        "USER": 'bryce',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
