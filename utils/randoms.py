import mimesis


def get_title():
    obj = mimesis.Text(locale='ru')
    return obj.quote()
