from flask import (
    abort
)
from config import db, basedir


def login_required(f):
    def wrap(*args, **kwargs):
        if 1 == 1: # logged - just for the test
            return f(*args, **kwargs)
        else:
            abort(404, 'auth_required')
    return wrap


def post_token():
    """
    Log in the user and prolong the user session.

    :return:      Dictionary containing information for the user session.
    """
    pass


@login_required
def get_session_status():
    """
    Checks the status of a user session.

    :return:        Dictionary containing information for the user session.
    """
    pass


@login_required
def delete_session():
    """
    Sign out a user.

    :return:                        200 on success, 404 on user does not exists, 400 incorrect input parameters.
    """
    pass


@login_required
def delete_all_other_sessions():
    """
    This function deletes all user's sessions except the one which authenticates the user.

    :return:                        200 on success, 404 on user does not exists, 400 incorrect input parameters.
    """
    pass
