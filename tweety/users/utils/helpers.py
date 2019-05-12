from rest_framework_jwt.settings import api_settings
from calendar import timegm
from datetime import datetime

from users.models import User


def generate_jwt_payload(profile):
    """

    :param profile: User profile
    :return: JWT payload
    """

    if isinstance(profile, User):
        payload = {
            'username': profile.username,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'email': profile.email
        }
    else:
        payload = {
            'username': profile.get('username'),
            'first_name': profile.get('first_name'),
            'last_name': profile.get('last_name'),
            'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        }

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload


def generate_unique_jwt(profile):
    """

    :param profile: Instagram Profile
    :return: JWT token
    """

    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = generate_jwt_payload(profile)

    token = jwt_encode_handler(payload)

    return token