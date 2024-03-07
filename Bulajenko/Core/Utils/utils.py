# -*- coding: utf-8 -*-
import hashlib
import datetime
import locale

from dateutil.relativedelta import relativedelta
from math import floor, trunc
from num2words import num2words

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def object_name(name):
    hash_name = hashlib.sha256(name.strip().encode('utf-8')).hexdigest()
    return hash_name

def AddMonths(d,x):
    newmonth = ((( d.month - 1) + x ) % 12 ) + 1
    newyear  = d.year + ((( d.month - 1) + x ) / 12 )
    return datetime.date( newyear, newmonth, d.day)

def date_temp_payment(date_dogovor=None, method_pay=None, rental_period=None, id_dogovor=None):
    # print('Ok7')
    # print('Date_dogovor: ', date_dogovor)
    # print('Method_pay: ', method_pay)
    # print('Rental_period: ', rental_period)
    # print('ID dogovor: ', id_dogovor)
    date_parse = datetime.datetime.fromisoformat(f'{date_dogovor}').date()
    # year_parse = datetime.datetime.fromisoformat(date_dogovor).date().year
    rental = rental_period.split()
    # print(f'Date: {date_parse}')
    # print(f'Rental 0: {rental[0]}')
    # print(f'Rental 1: {rental[1]}')
    # print(f'Year: {year_parse}')

    if rental[1] == 'день':
        period = date_parse + relativedelta(days=+int(rental[0]))
        interval = int(rental[0])
        # print(f'Period days: {period}')
        # print(f'Interval days: {interval}')
        # print('=' * 30)
    elif rental[1] == 'месяц':
        period = date_parse + relativedelta(months=+int(rental[0]))
        interval = int(rental[0])
        # print(f'Period month: {period}')
        # print(f'Interval month: {interval}')
        # print('=' * 30)
    elif rental[1] == 'год':
        period = date_parse + relativedelta(months=+12*float(rental[0].replace(',', '.')))
        interval = int(12*float(rental[0].replace(',', '.')))
        # print(f'Period year: {period}')
        # print(f'Interval1 year: {interval}')
        # print('=' * 30)

    # print('Ok8')
    date_payments = []
    if method_pay == 'ежедневно':
        for i in range(interval):
            delta_day = datetime.timedelta(days = i)
            payments = {
                'estimated_date': date_parse + delta_day,
                'contract_id': id_dogovor
            }
            date_payments.append(payments)


    elif method_pay == 'еженедельно':
        for i in range(interval):
            if i % 7 == 0:
                delta_day = datetime.timedelta(days = i)
                payments = {
                    'estimated_date': date_parse + delta_day,
                    'contract_id': id_dogovor
                }
                date_payments.append(payments)
        # print(len(date_payments))



    elif method_pay == 'ежемесячно':
        for i in range(interval):
            payments = {
                'estimated_date': date_parse + relativedelta(months=+i),
                'contract_id': id_dogovor
            }
            date_payments.append(payments)
    return date_payments, period

def date_russian(dates=None):
    date_parse = datetime.datetime.fromisoformat(f'{dates}').date()
    date_new = date_parse.strftime('«%d» %B %Yг.')
    return date_new

def convert_date_to_str_russia(dates):
    dates = dates.strftime('%d.%m.%Y')
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = dates.split('.')
    return f'«{int(date_list[0])}» {month_list[int(date_list[1]) - 1]}  {date_list[2]} года'


def number_to_word(number=None):
    """Перевод числа в пропись"""
    result = num2words(number, lang='ru')
    return result



def enabled_elements(role=None, element=None, disableted = None, hideted=None, enableted=None):
    """Активация кнопок для Admins"""
    if disableted is not None:
        element.setDisabled(True)
        if role in ['root', 'admin']:
            element.setDisabled(False)
    elif hideted is not None:
        element.setHidden(True)
        if role in ['root', 'admin']:
            element.setHidden(False)
    elif enableted is not None:
        element.setEnabled(False)
        if role in ['root', 'admin']:
            element.setEnabled(True)






# print(number_to_word(150079))


# rus = date_russian(dates='2022-05-17 19:19:33.972492')
# print(rus)




    # # period = method_pay.split()
    # rental = rental_period.split()
    # date_parse = datetime.datetime.fromisoformat(date_dogovor).date()
    #
    # if rental[1] == 'день':
    #     period = int(rental[0]) * 1
    # elif rental[1] == 'месяц':
    #     period = int(rental[0]) * 30
    # elif rental[1] == 'год':
    #     period = int(rental[0]) * 365
    #
    # print(f'Data dogovor: {datetime.datetime.fromisoformat(date_dogovor).date()}')
    # print(f'Data dogovor: год {date_parse.year} месяц {date_parse.month} день {date_parse.day}')
    # # print(datetime.datetime(date_dogovor, "%yyyy-%m-%d"))
    # print(f'Metod pay: {method_pay}')
    # print(f'Rental dogovor: {rental_period} - {rental[0]}')
    # print(f'Interval: {period}')
    #
    # date_payments = []
    # if method_pay == 'ежедневно':
    #     for i in range(period):
    #         delta_day = datetime.timedelta(days = i)
    #         payments = {
    #             'estimated_date': date_parse + delta_day,
    #             'contract_id': id_dogovor
    #         }
    #         date_payments.append(payments)
    #     print(len(date_payments))
    #
    #     # for next_payments in date_payments:
    #     #     if next_payments >= datetime.date.today():
    #     #         return next_payments
    #     #     else:
    #     #         continue
    #
    # elif method_pay == 'еженедельно':
    #     for i in range(period):
    #         if i % 7 == 0:
    #             delta_day = datetime.timedelta(days = i)
    #             payments = {
    #                 'estimated_date': date_parse + delta_day,
    #                 'contract_id': id_dogovor
    #             }
    #             date_payments.append(payments)
    #     print(len(date_payments))
    #
    #     # print(date_payments)
    #
    #     # for next_payments in date_payments:
    #     #     if next_payments > datetime.date.today():
    #     #         return next_payments
    #     #     else:
    #     #         continue
    #
    # elif method_pay == 'ежемесячно':
    #     for i in range(period):
    #         if i % 30 == 0:
    #             delta_day = datetime.timedelta(days = i)
    #             payments = {
    #                 'estimated_date': date_parse + delta_day,
    #                 'contract_id': id_dogovor
    #             }
    #             date_payments.append(payments)
    #
    #     print(len(date_payments))
    #
    #     # print(date_payments)
    #
    #     # for next_payments in date_payments:
    #     #     if next_payments > datetime.date.today():
    #     #         return next_payments
    #     #     else:
    #     #         continue

    # return date_payments



# # list_temporari_item1 = date_payment(date_dogovor='2022-06-17 19:19:33.972492', method_pay='ежедневно', rental_period='11 день', id_dogovor=14)
# # list_temporari_item1 = date_payment(date_dogovor='2022-06-17 19:19:33.972492', method_pay='еженедельно', rental_period='2 месяц', id_dogovor=14)
# list_temporari_item1 = date_payment(date_dogovor='2022-06-17 19:19:33.972492', method_pay='ежемесячно', rental_period='1,5 год', id_dogovor=14)
# # list_temporari_item2 = date_payment(date_dogovor='2022-06-17 19:19:33.972492', method_pay='еженедельно', rental_period='12 месяц', id_dogovor=14)
# # list_temporari_item3 = date_payment(date_dogovor='2022-06-17 19:19:33.972492', method_pay='ежемесячно', rental_period='2 год', id_dogovor=14)
#
#
#
# print(f'Result: {list_temporari_item1}')
# # print(f'Кол-во платежей: {len(list_temporari_item1)}')
# # print(list_temporari_item2)
# # print(list_temporari_item3)

