# Borrowed from here: https://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))