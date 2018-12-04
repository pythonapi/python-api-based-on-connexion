from flask import (
    abort
)
from config import db, basedir
from .oauth import login_required

import os
from datetime import datetime
import connexion
import string
import random


@login_required
def get(id):
    """
    Returns a user by ID.

    :param id:      Id of the user.
    :return:        Dictionary containing the user. 200 if user found. 404 if the user does not exist.
    """
    result = {
        "id": id,
        "first_name": "John",
        "last_name": "Smith",
        "profile_image_url": "IMAGE_URL"
    }
    return result


@login_required
def update(id, user):
    """
    This function updates an existing user.

    :param id:      Id of user to update.
    :param user:    Data which must be used to update the user with the specified id.
    :return:        Updated user structure. 200 on success, 404 on user does not exists, 400 incorrect input parameters.
    """

    # Does the person exist?
    if id == 1:
        result = {
            "id": id,
            "first_name": "John",
            "last_name": "Smith",
            "profile_image_url": "IMAGE_URL"
        }

        return result
    else:
        abort(404, 'user_not_found')


def create(user):
    """
    Create a new user.

    :param user:  This variable contains all data necessary to create a new user.
    :return:      201 on success, 406 on user exists, 400 incorrect input parameters.
    """

    # Get vars
    type = user.get('type', 'STANDARD')
    email = user.get('email', None)
    password = user.get('password', None)
    facebook_id = user.get('facebook_id', None)

    # Create users
    if type == 'STANDARD':
        if email is not None and password is not None:
            if email != 'e@gmail.com':
                result = {
                    "id": "1",
                    "first_name": "John",
                    "last_name": "Smith",
                    "profile_image_url": "IMAGE_URL"
                }
            else:
                abort(406, 'user_exists')
        else:
            abort(400, 'incorrect_parameters')
    else:
        abort(400, 'incorrect_parameters')

    return result


@login_required
def update_profile_image(id):
    """
    Updates the profile image of a user with passed id.

    :param id:   Id of the user.
    """
    # Get file and file data
    file = connexion.request.files['file']
    name, ext = os.path.splitext(file.filename)

    # Check if file covers the requirements
    if ext not in ('.png','.jpg','.jpeg'):
        return 'file_extension_not_allowed'

    # Create path where we will save the file
    save_path = basedir+'/files/'+datetime.now().strftime(("%Y/%m"))
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Save file
    new_file_name = datetime.now().strftime(("%Y%m%d"))+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))+ext
    file_path = "{path}/{file}".format(path=save_path, file=new_file_name)
    file.save(file_path)

    return []


@login_required
def delete_profile_image(id):
    """
    Deletes a profile image of a user wih passed id.

    :param id:   Id of the user.
    :return:     200 on successful delete, 404 if not found.
    """

    # Does the user exist?
    if id==1:
        return []
    else:
        abort(404, 'user_not_found')


def get_activate(id):
    """
    This function sends an email with the activation key of the user.

    :param id:                  Id of user to update.
    :return:                    200 on success, 404 on user does not exists, 400 incorrect input parameters.
    """

    # Send Email

    return []


def activate(id, activation_key):
    """
    This function activates an existing user.

    :param id:                  Id of user to update.
    :param activation_key:      Activation key.
    :return:                    200 on success, 404 on user does not exists, 400 incorrect input parameters.
    """

    # Does the person exist?
    if id == 1:
        return []
    else:
        abort(404, 'user_not_found')


def request_reset_password(id):
    """
    This function generates a password reset key and sends an email with to the user.

    :param id:                  Id of the user.
    :return:                    200 on success, 404 on user does not exists, 400 incorrect input parameters.
    """

    # Send Email

    return []


def reset_password(id, password_reset_key):
    """
    This function resets the user's password.

    :param id:                      Id of the user.
    :param password_reset_key:      Reset password key.
    :return:                        200 on success, 404 on user does not exists, 400 incorrect input parameters.
    """

    # Does the person exist?
    if id == 1:
        return []
    else:
        abort(404, 'user_not_found')
