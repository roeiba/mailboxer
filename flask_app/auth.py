import flask

def authenticate_from_openid_response(resp):
    print "authenticating!"
    flask.session['auth_info'] = dict(
        openid = resp.identity_url,
        email = resp.email,
        )

def get_user_email():
    return _get_user_attribute("email")

def _get_user_attribute(attr):
    auth_info = flask.session.get("auth_info")
    if auth_info is None:
        return None
    return auth_info.get(attr, None)

def is_authenticated():
    auth_info = flask.session.get("auth_info")
    if auth_info is None:
        return False
    return ("email" in auth_info and "openid" in auth_info)