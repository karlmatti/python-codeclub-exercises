def currency_sign_from_name(name):
    mapping = {
        'euro': '€',
        'dollar': '$',
        'pound': '£'
    }

    if name.lower() in mapping:
        return mapping[name.lower()]
    raise ValueError(f'Name of currency not one of {set(mapping.keys())}')
