import os
import sys
import datetime
import json

from functools import partial

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Date,
    DateTime,
    ForeignKey,
    Text,
    types,
    and_, Boolean,
    TypeDecorator, Unicode, select, func
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref, column_property

# from sqlalchemy_media import StoreManager, FileSystemStore, Image, ImageAnalyzer, ImageValidator, ImageProcessor

# BASE_PATH_DOCX = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.getcwd()

DATABASE_NAME = 'db.sqlite3'
PATH_DATA_DB = os.path.join(BASE_PATH, DATABASE_NAME)
TEMP_PATH = os.path.join(BASE_PATH, 'tmp')
UPLOAD_FOLDER = os.path.join(BASE_PATH, 'uploads')
THUMBNAIL_FOLDER = os.path.join(UPLOAD_FOLDER, 'thumbnail')
PATH_TPL_DOCX = os.path.join(BASE_PATH, 'templates')


# StoreManager.register(
#     'fs',
#     partial(FileSystemStore, TEMP_PATH, UPLOAD_FOLDER),
#     # partial(FileSystemStore, TEMP_PATH, 'http://static.example.org/'),
#     default=True
# )



engine = create_engine(f'sqlite:///{PATH_DATA_DB}', echo=False, connect_args={'check_same_thread': False})
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session(future=True)
session1 = Session(future=True)
# session.autoflush == False
# conn = engine.connect()



class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    role = Column(String(30), unique=True)
    name = Column(String(30))

    user = relationship('User', backref='users', cascade="all, delete-orphan", )

    def __init__(self, role, name):
        """Constructor"""
        self.role = role
        self.name = name

    def __repr__(self):
        return "<Role %s>" % (self.role)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    name = Column(String(30))
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('role.id'))
    date_created = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, username, name, password, role_id):
        """Constructor"""
        self.username = username
        self.name = name
        self.password = password
        self.role_id = role_id

    def __repr__(self):
        return "<User %s>" % (self.username)

class Phone(Base):
    __tablename__ = "phone"
    id = Column(Integer, primary_key = True)
    phone = Column(String(30), nullable = True)
    arendator_id = Column(Integer, ForeignKey('arendators.id', ondelete = "CASCADE", onupdate="cascade"))
    arendator = relationship("Arendators", back_populates = "phoneses", cascade="all, save-update")

    def __init__(self, phone):
        """Constructor"""
        self.phone = phone


class Arendators(Base):
    __tablename__ = "arendators"
    id = Column(Integer, primary_key = True)
    hiden_arendator = Column(Boolean, default = False) # Скрыть клиента из вида Менеджера: 0 - False - Виден//  1 - True - Не виден
    surname = Column(String(30), nullable = True) # Фамилия
    name = Column(String(30), nullable = True) # Имя
    last_name = Column(String(30), nullable = True) # Отчество
    date_birthday = Column(Date) # Дата рождения
    checked_passport = Column(String(10)) # Гражданство
    passport_country = Column(String(100), nullable = True, default=f'Гражданин РФ') # Государство паспорта
    driving_license = Column(Boolean, default = False) # Водительское удостоверение
    serial_pasport = Column(String(5), nullable = True) # Серия паспорта
    number_pasport = Column(String(6), nullable = True) # Номер паспорта
    date_pasport = Column(Date) # Дата выдачи паспорта
    code_division = Column(String(5), nullable = True) # Код подразделения
    who_issued = Column(String(150), nullable = True) # Кем выдан паспорт
    address_registration = Column(String(150), nullable = True) # Адрес регистрации
    address_residence = Column(String(150), nullable = True) # Адрес проживания

    date_created = Column(DateTime, default = datetime.datetime.now) # Дата и время создания записи
    phoneses = relationship('Phone', back_populates = "arendator", cascade="all, delete") # Ссылка на номера тлф

    contracted = relationship('Contract', back_populates = "arendatored", cascade="all, delete", order_by="-Contract.id") # Ссылка на
    # договоры , lazy="dynamic", "joined", lazy="select", uselist=False,   innerjoin=True   lazy="joined", innerjoin=True,
    history_payments_arendator = relationship('HistoryPayment', back_populates = "arendator_pay")



    def __init__(self, surname, name, last_name, date_birthday, checked_passport, serial_pasport, number_pasport, date_pasport, code_division,
                 who_issued, address_registration, address_residence): #, phoneses = tuple()):
        """Constructor"""
        self.surname = surname
        self.name = name
        self.last_name = last_name
        self.date_birthday = date_birthday
        self.checked_passport = checked_passport
        self.serial_pasport = serial_pasport
        self.number_pasport = number_pasport
        self.date_pasport = date_pasport
        self.code_division = code_division
        self.who_issued = who_issued
        self.address_registration = address_registration
        self.address_residence = address_residence
        # self.phoneses = phoneses


    def __repr__(self):
        return "<Arendator %s %s %s>" % (self.surname, self.name, self.last_name)

class TemporaryPeriodPay(Base):
    __tablename__ = "temporaryperiodpay"
    id = Column(Integer, primary_key = True)
    estimated_date = Column(Date)
    verif = Column(Boolean, default = False)
    contract_id = Column(Integer, ForeignKey('contract.id'))

    # contract_temp_pay = relationship('Contract', back_populates="temporary_period_pays", lazy="joined", innerjoin=True)
    contract_temp_pay = relationship('Contract', lazy="select", innerjoin=True)


class HistoryPayment(Base):
    __tablename__ = "historypayment"
    id = Column(Integer, primary_key=True)
    date_payment = Column(DateTime) # Дата платежа
    size_payment = Column(Integer, nullable=True) # Оплатил арендатор
    comment_pay = Column(String(150), nullable=True) # Комментарий к оплаченой сумме
    tarif = Column(String(50), nullable=True) # Тариф
    discount = Column(Integer, default=0) # Скидка
    discount_comment = Column(String(150), nullable=True) # Комментарий к скидке
    shtraf = Column(Integer, default=0) # Штраф
    shtraf_comment = Column(String(150), nullable=True)  # Комментарий к штрафу
    total_pay = Column(Integer, nullable=True) # Итоговая сумма оплаты
    payments = Column(String(30), nullable = True)  # Способ оплаты: Наличный расчет, Перевод, Эквайринг
    id_arendator = Column(Integer, ForeignKey('arendators.id'))
    id_contract = Column(Integer, ForeignKey('contract.id'))

    arendator_pay = relationship('Arendators', back_populates = "history_payments_arendator")
    contracted_pay = relationship('Contract', back_populates = "history_payments_contracted")


    def __init__(self, date_payment, size_payment, comment_pay, tarif, discount, discount_comment, shtraf, shtraf_comment, total_pay, payments):
        self.date_payment = date_payment
        self.size_payment = size_payment
        self.comment_pay = comment_pay
        self.tarif = tarif
        self.discount = discount
        self.discount_comment = discount_comment
        self.shtraf = shtraf
        self.shtraf_comment = shtraf_comment
        self.total_pay = total_pay
        self.payments = payments


class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key = True)
    brand = Column(String(30), nullable = True) # Марка ТС  le_brand
    model = Column(String(30), nullable = True) # Модель ТС le_model
    bodywork = Column(String(30), nullable = True) # Номер кузова (VIN)     le_bodywork
    engine_volume = Column(String(30), nullable = True) # Объем двигателя
    vikup = Column(Boolean, default=False)  # ТС под выкуп: 0 - False - Без выкупа//  1 - True - Выкуп ТС
    contract_number = Column(Integer, default = 0) # Номер договора
    date_purchase = Column(Date) # Дата покупки ТС
    place_purchase = Column(String(100), nullable = True) # Место покупки ТС
    number_engine = Column(String(30), nullable = True) # Номер двигателя   le_number_engine
    market_price = Column(Integer, default = 0) # Рыночная стоимость    market_price
    purchase_price = Column(Integer, default = 0) # Цена закупки   purchase_price
    number_simcard = Column(String(30), nullable = True) # Номер SIM карты number_simcard
    gps_id = Column(String(30), nullable = True) # Номер GPS    gps_id
    type_gps = Column(String(30), nullable = True) # Тип GPS    type_gps
    date_prev_to = Column(Date) # Дата прошлого ТО ТС
    date_next_to = Column(Date) # Дата следующего ТО ТС
    prev_mileage = Column(Integer, default = 0) # Предыдущий пробег ТС
    next_mileage = Column(Integer, default = 0) # Следующий пробег ТС
    comment_prev_to = Column(String(100), nullable = True) # Комментарий к предыдущему ТО ТС
    comment_next_to = Column(String(100), nullable = True) # Комментарий к следующему ТО ТС
    comment_general = Column(Text, nullable = True) # Основной комментарий к ТС
    # image = Column(ProfileImage.as_mutable(Json))
    image = Column(String(255), nullable=True) # Картинка ТС (только одна используется)
    type_transport_id = Column(Integer, ForeignKey('typetransport.id'), default = 1) # Привязка к типу ТС
    status_transport_id = Column(Integer, ForeignKey('statustransport.id'), default = 1) # Привязка к статусу ТС
    color_id = Column(Integer, ForeignKey('colortransport.id'), default = 1)  # Цвет ТС
    paymentcategory_id = Column(Integer, ForeignKey('paymentcategory.id'), default = 1)  # Ценовая категория ТС
    type_transported = relationship('TypeTransport', lazy="joined", innerjoin=True) # Ссылка к таблице типа ТС
    statused = relationship('StatusTransport', lazy="joined", innerjoin=True) # Ссылка к таблице статуса ТС
    colored = relationship('ColorTransport', lazy="joined", innerjoin=True) # Ссылка к таблице цвета ТС
    payment_categoryed = relationship('PaymentCategory', lazy="joined", innerjoin=True) # Ссылка к таблице ценовой категории ТС

    contractes = relationship("Contract", back_populates = "transported") #, lazy="joined", innerjoin=True

    images = relationship("ImagesTransport", back_populates = "vehicles", cascade = "all, delete")


    def __init__(self, brand, model, bodywork, engine_volume, vikup, contract_number, date_purchase, place_purchase, number_engine, market_price,
                 purchase_price, number_simcard, gps_id, type_gps, date_prev_to, date_next_to, prev_mileage, next_mileage, comment_prev_to,
                 comment_next_to, comment_general, image, type_transport_id, status_transport_id, color_id, paymentcategory_id):
        """Constructor"""
        self.brand = brand
        self.model = model
        self.bodywork = bodywork
        self.engine_volume = engine_volume
        self.vikup = vikup
        self.contract_number = contract_number
        self.date_purchase = date_purchase
        self.place_purchase = place_purchase
        self.number_engine = number_engine
        self.market_price = market_price
        self.purchase_price = purchase_price
        self.number_simcard = number_simcard
        self.gps_id = gps_id
        self.type_gps = type_gps
        self.date_prev_to = date_prev_to
        self.date_next_to = date_next_to
        self.prev_mileage = prev_mileage
        self.next_mileage = next_mileage
        self.comment_prev_to = comment_prev_to
        self.comment_next_to = comment_next_to
        self.comment_general = comment_general
        self.image = image
        self.type_transport_id = type_transport_id
        self.status_transport_id = status_transport_id
        self.color_id = color_id
        self.paymentcategory_id = paymentcategory_id

class TypeTransport(Base):
    __tablename__ = "typetransport"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = True)

    def __init__(self, name):
        self.name = name

class StatusTransport(Base):
    __tablename__ = "statustransport"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = True)
    color = Column(String(10), default='#ffffff')
    default_status = Column(Boolean, default=False)

    def __init__(self, name, color, default_status): #, default_status):
        self.name = name
        self.color = color
        self.default_status = default_status

class ColorTransport(Base):
    __tablename__ = "colortransport"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), default='Белый')
    color = Column(String(10), default='#ffffff')
    default_color = Column(Boolean, default = False)

    def __init__(self, name, color): #, default_status):
        self.name = name
        self.color = color

class PaymentCategory(Base):
    __tablename__ = "paymentcategory"
    id = Column(Integer, primary_key = True)
    size = Column(Integer, default = 0)

    def __init__ (self, size):
        self.size = size

class Contract(Base):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)
    date_contract = Column(DateTime) # Дата и время заключения договора
    rental_period = Column(String(30), nullable = True) # Срок аренды
    method_pay = Column(String(30), nullable = True) # Метод платежа: Ежедневно, Еженедельно, Ежемесячно
    size_pay = Column(Integer, nullable = True) # Размер платежа
    confirm_pay = Column(Boolean, default = False) # Подтверждение платежа: 0 - False - Не подтвержден//  1 - True - Подтвержден
    date_finish_contract = Column(DateTime, nullable = True) # Дата окончания контракта
    status_contract = Column(Boolean, default=False) # Статус договора: 0 - False - Действующий//  1 - True - Закрыт
    date_closed_contract = Column(DateTime, nullable=False, default = datetime.datetime.now()) # Дата закрытия договора
    draft = Column(Boolean, default=True) # Состояние договра: 1 - True - Черновик//  0 - False - Оформленный
    optional_equipment = Column(String(255), nullable = True) # Дополнительное оборудование к ТС
    fio_arendator = Column(String(150), nullable = True) # ФИО арендатора

    id_ts = Column(Integer, ForeignKey('vehicle.id')) # ID ТС
    id_arendator = Column(Integer, ForeignKey('arendators.id')) # ID арендатора

    transported = relationship('Vehicle', back_populates="contractes") #, lazy="select", uselist=False) #, innerjoin=True)  # Ссылка к таблице ТС
    arendatored = relationship("Arendators", back_populates="contracted") # Ссылка к таблице Арендаторов
    # arendatored = relationship("Arendators", lazy="select", uselist=False) #, innerjoin=True)
    history_payments_contracted = relationship('HistoryPayment', back_populates = "contracted_pay")

    # temporary_period_pays = relationship('TemporaryPeriodPay', back_populates="contract_temp_pay")
    # temporary_period_pays = relationship('TemporaryPeriodPay', back_populates="contract_temp_pay", lazy="joined", innerjoin=True, uselist=False)

    dates_payments_next = column_property(
        select(func.min(TemporaryPeriodPay.estimated_date).filter(TemporaryPeriodPay.contract_id == id, TemporaryPeriodPay.verif == False)).label("dates_payments_next")
    )



    def __init__(self, date_contract, rental_period, method_pay, size_pay, status_contract, date_closed_contract, optional_equipment, fio_arendator, id_ts, id_arendator):
        """Constructor"""
        self.date_contract = date_contract
        self.rental_period = rental_period
        self.method_pay = method_pay
        self.size_pay = size_pay
        self.status_contract = status_contract
        self.date_closed_contract = date_closed_contract
        self.optional_equipment = optional_equipment
        self.fio_arendator = fio_arendator
        self.id_ts = id_ts
        self.id_arendator = id_arendator

class ImagesTransport(Base):
    __tablename__ = "imagestransport"
    id = Column(Integer, primary_key = True)
    id_ts = Column(Integer, ForeignKey('vehicle.id', ondelete = "CASCADE", onupdate = "cascade")) # ID ТС
    name = Column(String(255), nullable=True) # Картинка ТС

    vehicles = relationship("Vehicle", back_populates = "images", cascade = "all, save-update")


    def __init__ (self, id_ts, name):
        self.id_ts = id_ts
        self.name = name









def create_db():
    Base.metadata.create_all(engine)

    import hashlib
    password = 'root'
    enc_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()

    session = Session()
    role_root = Role(role = 'root', name = 'Суперпользователь')
    session.add(role_root)
    session.commit()
    user_root = User(username = 'root', name = 'Суперпользователь', password = enc_pass, role_id = 1)
    session.add(user_root)
    session.commit()
    session.add_all(
        [StatusTransport(name = 'Готов к выдаче', color = '#0055ff', default_status = True), StatusTransport(name = 'Аренда договор', color = '#2c9934', default_status = False), StatusTransport(name = 'Обслуживание', color = '#ff0000', default_status = False)]
    )
    session.commit()
    session.close()

    name = Column(String(30), nullable = True)
    color = Column(String(10), default = '#ffffff')
    default_status = Column(Boolean, default = False)