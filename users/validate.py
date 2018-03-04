import re


def validate_email(email, return_data):

    if not email:
        return_data['error'].append('An email must be supplied')

    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    match = re.match(pattern, email)

    if not match:
        return_data['error'].append('the email address is not valid.')
        return None
    return email


def validate_name(name, name_type, return_data):
    """
    :param name: name to validate
    :param name_type: pass eg, first, last middle
    :param return_data: dictionary {errors:[], messages:[], data[]}
    :return: name
    """
    if not name:
        return_data['errors'].append('A {} name must be provided'.format(name_type))

    if not name.isalpha():
        return_data['errors'].append('The {} name must only contain letters'.format(name_type))
        return None

    return name.title()


def validate_phone(phone, return_data):
    """
    :param phone:
    :param return_data:
    :return:
    """
    if not phone:
        return_data['errors'].append('A phone number must be provided')

    phone = phone.replace('-', '').replace(' ', '')

    if not phone.isdigit():
        return_data['errors'].append('A phone number must only contain digits')
        return None

    return phone


def validate_user_form(user_form, return_data):
    first_name = None
    last_name = None
    phone = None
    email = None

    # parse the user parameters from the message
    try:
        first_name = user_form['first_name']
        last_name = user_form['last_name']
        phone = user_form['phone']
        email = user_form['email']
    except KeyError:
        return_data['errors'].append('Please provide, First name, Last name, Phone, and Email')
        return
    # validate the form fields
    return_data['data']['first_name'] = validate_name(first_name, 'first', return_data)
    return_data['data']['last_name'] = validate_name(last_name, 'last', return_data)
    return_data['data']['phone'] = validate_phone(phone, return_data)
    return_data['data']['email'] = validate_email(email, return_data)

