#########################################################################
#
# Copyright 2018, GeoSolutions Sas.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
#########################################################################

from .development import *

#PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ALLOWED_HOSTS = [
    "10.0.1.95"
]

# remove qgis_server from installed apps
# INSTALLED_APPS = tuple(
#     app for app in INSTALLED_APPS if app != "geonode.qgis_server")

INSTALLED_APPS += (
    "gfdrr_det.exposures",
)

SECRET_KEY = get_environment_variable("DJANGO_SECRET_KEY")

DATABASES["default"].update({
    "NAME": "gfdrr-det",
    "USER": get_environment_variable("GFDRR_DET_DB_USER"),
    "PASSWORD": get_environment_variable("GFDRR_DET_DB_PASSWORD"),
})

DATABASES["datastore"].update({
    "NAME": "gfdrr-det",
    "USER": get_environment_variable("GFDRR_DET_DB_USER"),
    "PASSWORD": get_environment_variable("GFDRR_DET_DB_PASSWORD"),
})

DATABASES["exposures"] = {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'ged4all',
    "USER": get_environment_variable("GFDRR_DET_DB_USER"),
    "PASSWORD": get_environment_variable("GFDRR_DET_DB_PASSWORD"),
    'HOST': 'localhost',
    'PORT': '5432',
    'CONN_TOUT': 900,
}

EMAIL_ENABLE = True

if EMAIL_ENABLE:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = "smtp.geo-solutions.it"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = get_environment_variable("DJANGO_EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = get_environment_variable(
        "DJANGO_EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'gfdrr-det <no-reply@localhost>'