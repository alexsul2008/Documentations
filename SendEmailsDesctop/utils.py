# -*- coding: utf-8 -*-
# from itertools import groupby
import re
from os import path

# reg_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# reg_email = '^[a-z0-9]+[\._-]?[a-z0-9]+[\._-]?[a-z0-9]+[@][a-z0-9]+[\-]?[a-z0-9]+[.]\w{2,3}$'
# reg_email = '([a-z0-9]+[\._-]?[a-z0-9]+[\._-]?[a-z0-9]+[@][a-z0-9]+[\._-]?[a-z0-9]+[.]\w{2,})'
reg_email = "([a-z0-9\._-]+[@][a-z0-9\._-]+[.]\w{2,3})"

reg_digital = '^[1-9][0-9]{1,5}$'

def check(email):
    if (re.search(reg_email, email)):
        return True
    else:
        return False

def check_digital(digital):
    if (re.search(reg_digital, digital)):
        return True
    else:
        return False

def find_emails_in_str(text):
    r = re.compile(r"(\w(?:[-.+]?\w+)+\@(?:[a-z0-9](?:[-+]?\w+)*\.)+[a-z]{2,})", re.I)
    email_addr = []
    for email_match in r.finditer(text):
        email_addr.append(email_match.group().lower())

    email_addr_combine = (list(set(email_addr)))

    return email_addr_combine



def convertJsonToList(resultJson):
    res_dict = []
    for item in resultJson:
        res_item = []
        for key, value in item.items():
            if isinstance(value, dict):
                res_item.append(value["name"])
            else:
                res_item.append(value)
        res_dict.append(res_item)
    return res_dict

# def getDataToListFromFilters(dataJson):
#     # print(f'{type(dataJson)}')
#     data_status = set()
#     data_creators = set()
#     for item in dataJson:
#         data_status.add(item['status'])
#         data_creators.add(item['creator'])
#
#     data = {
#         'status': data_status,
#         'creators': data_creators
#     }
#
#     return data

def get_extension(filename):
    basename = path.basename(filename)  # os independent
    ext = '.'.join(basename.split('.')[1:])
    return '.' + ext if ext else None


def hidden_visible_obj(frame, obj, _attribute, role_user=False):
    for widget in frame.findChildren(obj):
        if widget.objectName().startswith(_attribute):
            # print(widget.__class__.__name__, widget.objectName())
            if role_user:
                widget.setVisible(True)
            else:
                widget.hide()


