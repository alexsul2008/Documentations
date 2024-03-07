import datetime
import os.path


from PyQt5.QtWidgets import QFileDialog
from dateutil.relativedelta import relativedelta
from docxtpl import DocxTemplate

from Core.Models.Models import PATH_TPL_DOCX
from Core.Utils.utils import date_russian, number_to_word, convert_date_to_str_russia


class CreateDogovor():
    def __init__(self, fields=None, tpl = None, type = None):
        self.doc = DocxTemplate(os.path.join(PATH_TPL_DOCX, tpl))
        self.fields = fields
        self.type = type

        self.save_dogovor(self.fields)

    def save_dogovor(self, fields):
        date_contract = convert_date_to_str_russia(fields['date_contract'])
        optional_equipment_string = ', '.join(map(str, self.fields['optional_equipment'].split(', ')[4:]))

        dict_optional_equipment = []
        for item in fields['optional_equipment'].split(', ')[:4]:
            if item.strip() != '':
                dict_optional_equipment.append(item.strip())

        phones_arendator = []

        # определяем словарь переменных контекста,
        # которые определены в шаблоне документа DOCX
        context = {}
        context['company_name'] = 'Слоны и Кони'
        context['date_contract_str'] = date_contract
        context['date_contract'] = fields['date_contract'].strftime("%d.%m.%Y")
        context['date_contract_deystvie'] = (fields['date_contract'] + relativedelta(years=1)).strftime("%d.%m.%Y")
        context['id_contract'] = fields['id_contract']
        context['fio_arendator'] = fields['fio_arendator'].title()
        context['address_registration'] = fields['address_registration']
        context['address_residence'] = fields['address_residence']
        context['passport_country'] = fields['passport_country']
        context['serial_pasport'] = fields['serial_pasport']
        context['number_pasport'] = fields['number_pasport']
        context['date_pasport'] = fields['date_pasport'].strftime("%d.%m.%Y")
        context['who_issued'] = fields['who_issued']
        context['date_birthday'] = fields['date_birthday'].strftime("%d.%m.%Y")
        context['type_ts'] = fields['type_ts']
        context['brand_ts'] = fields['brand_ts']
        context['model_ts'] = fields['model_ts']
        context['ts_vin'] = fields['ts_vin']
        context['engine_volume'] = fields['engine_volume']
        context['ts_color_name'] = fields['ts_color_name']
        context['optional_equipment'] = dict_optional_equipment
        context['optional_equipment_string'] = optional_equipment_string
        context['market_price'] = fields['market_price']
        context['market_price_word'] = number_to_word(number=fields['market_price'])
        context['size_pay'] = fields["size_pay"]
        context['size_pay_str'] = number_to_word(number=fields["size_pay"])
        context['method_pay'] = fields["method_pay"]

        self.phones = []
        try:
            if len(fields["phones"]) > 0:
                for item in fields["phones"]:
                    phones_arendator.append(item.phone)
                self.phones = phones_arendator
        except:
            if len(fields["phones_new"]) > 0:
                self.phones = fields["phones_new"]


        context['phones'] = self.phones


        if self.type == 'act':
            date_create_act_returned = convert_date_to_str_russia(fields['date_closed_contract'])

            context['date_create_act_returned'] = date_create_act_returned
            context['prev_mileage'] = fields["prev_mileage"]

            self.name_dogovor = f'Акт приема ТС к договору №{fields["id_contract"]}-КРД от {fields["date_contract"].strftime("%d.%m.%Y")}'
        else:
            self.name_dogovor = f'Договор №{fields["id_contract"]}-КРД от {fields["date_contract"].strftime("%d.%m.%Y")} с {fields["fio_arendator"].title()}'

        # подставляем контекст в шаблон
        self.doc.render(context)
        # сохраняем и смотрим, что получилось
        filename, path_for_save = QFileDialog.getSaveFileName(None, 'Сохранить как', self.name_dogovor, "Word (*.docx)")
        if filename:
            self.doc.save(filename)
            os.startfile(filename)



