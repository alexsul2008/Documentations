
import enum
from datetime import datetime

from typing import Annotated, Dict #, Optional

from sqlalchemy import (
	ForeignKey,
	Index,
	text, UniqueConstraint, select, func, Text, Column, Table,
)
# 	TIMESTAMP,
# 	CheckConstraint,
# 	Column,
# 	Enum,
#
# 	Integer,
# 	MetaData,
# 	PrimaryKeyConstraint,
# 	String,
# 	Table,
#
# )
from sqlalchemy.orm import Mapped, mapped_column, relationship, object_session

from models.database import Base, BaseGasi, str_256, str_100, str_10, str_2, str_15, str_30, str_127, str_31, str_300, str_63, str_200, \
	sync_engine_gasi

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement = True, unique = True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('Europe/Moscow', now())"))]
updated_at = Annotated[datetime, mapped_column(
        server_default=text("TIMEZONE('Europe/Moscow', now())"),
        onupdate=datetime.now,
    )]

LIST_USERS_ADMIN = {
	'avsulyay@mts.ru',
	'igdemide@mts.ru',
	'vvkravc3@mts.ru',
}

PATH_DATA = 'Data'



class UserAdminORM(Base):
	__tablename__ = "user_admin"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	name: Mapped[str_100]

class OperatorsORM(Base):
	__tablename__ = "operators"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	name: Mapped[str_100]
	flag: Mapped[bool] = mapped_column(default = False)

	incidents: Mapped[list["IncidentsORM"]] = relationship(
		back_populates = "operator"
		# cascade = "all, delete-orphan"
	)

	dpcs: Mapped[list["DPC"]] = relationship(
		back_populates = "operators",
	)

	dpcs_mgmn: Mapped[list["DPCMgmn"]] = relationship(
		back_populates = "operators_mgmn",
	)

	emails: Mapped["EmailORM"] = relationship(
		back_populates = "operators_emails",
		uselist = False,
		# lazy = 'dynamic'
		# primaryjoin="OperatorsORM.id == EmailORM.operator_id",
		# lazy = "joined",
	)

	repr_cols_num = 4

	__table_args__ = (
		Index("operator_name_index", "name"),
		UniqueConstraint("name"),
	)

	@property
	def count_sp(self):
		if self.flag:
			return object_session(self).scalar(
				select(func.count(DPCMgmn.id)).where(DPCMgmn.operator_id == self.id)
			)
		else:
			return object_session(self).scalar(
				select(func.count(DPC.id)).where(DPC.operator_id == self.id)
			)

class LocationsORM(Base):
	__tablename__ = "locations"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	name: Mapped[str_100]

	dpcs: Mapped[list["DPC"]] = relationship(
		back_populates = "locations",
	)

class IncidentsORM(Base):
	__tablename__ = "incidents"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	name: Mapped[str_100]
	date_send: Mapped[created_at]
	operator_id: Mapped[int] = mapped_column(ForeignKey("operators.id", ondelete = "SET NULL"), nullable=True)
	dpc_id: Mapped[int] = mapped_column(ForeignKey("dpcs.id", ondelete = "SET NULL"), nullable=True)
	operator_name: Mapped[str_100]
	flag: Mapped[bool]
	dpc_name: Mapped[str_30]
	opc_name: Mapped[str_30]

	operator: Mapped["OperatorsORM"] = relationship(
		back_populates = "incidents",
	)
	dpc: Mapped["DPC"] = relationship(
		back_populates = "incident",
	)

	repr_cols_num = 9

class DPC(Base):
	__tablename__ = "dpcs"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	name: Mapped[int]
	abcdef: Mapped[str_100] = mapped_column(nullable = True)
	structurnii: Mapped[str_10] = mapped_column(nullable = True)
	zone_obslujivaniya: Mapped[str_100] = mapped_column(nullable = True)
	no_datas: Mapped[str_2] = mapped_column(nullable = True)

	operator_id: Mapped[int] = mapped_column(ForeignKey("operators.id", ondelete = "CASCADE"))
	location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))


	operators: Mapped[Dict[str, "OperatorsORM"]] = relationship(
		back_populates = "dpcs",
		lazy = "joined"
	)
	locations: Mapped[Dict[str, "LocationsORM"]] = relationship(
		back_populates = "dpcs",
		lazy = "joined"
	)
	incident: Mapped[list["IncidentsORM"]] = relationship(
		back_populates = "dpc",
	)

	repr_cols_num = 5
	repr_cols = ("operator_id",)

	__table_args__ = (
		Index("name_index", "name"),
		UniqueConstraint("name"),
		# UniqueConstraint("operator_id"),
	)

class DPCMgmn(Base):
	__tablename__ = "dpc_mgmn"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	dpc_name: Mapped[str_30]
	kommutator: Mapped[str_15] = mapped_column(nullable = True)
	name_trank: Mapped[str_100] = mapped_column(nullable = True)
	opc: Mapped[str_30] = mapped_column(nullable = True)
	region_kommutatora: Mapped[str_100] = mapped_column(nullable = True)
	region_shluza: Mapped[str_100] = mapped_column(nullable = True)
	uroven_prisoedineniya: Mapped[str_100] = mapped_column(nullable = True)

	operator_id: Mapped[int] = mapped_column(ForeignKey("operators.id", ondelete = "CASCADE"))

	operators_mgmn: Mapped[Dict[str, "OperatorsORM"]] = relationship(
		back_populates = "dpcs_mgmn",
	)

	repr_cols_num = 4
	repr_cols = ("operator_id",)

	__table_args__ = (
		Index("mgmn_name_index", "dpc_name"),
		# UniqueConstraint("dpc_name"),
	)


# @dataclasses.dataclass
class EmailORM(Base):
	__tablename__ = "emails"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	email: Mapped[str]
	operator_name: Mapped[str]
	operator_id: Mapped[int] = mapped_column(ForeignKey("operators.id", ondelete = "CASCADE"))

	operators_emails: Mapped["OperatorsORM"] = relationship(
		back_populates = "emails",
		uselist = False
	)

	__table_args__ = (
		Index("email_operator_name_index", "operator_name"),
		UniqueConstraint("operator_name"),
	)



class EmailRegionORM(Base):
	__tablename__ = "regions"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	region: Mapped[str]
	email: Mapped[str]

	__table_args__ = (
		Index("region_index", "region"),
		UniqueConstraint("region"),
	)


class StatusEnumORM(enum.Enum):
	INFO = "INFO"
	ADD = "ADD"
	DELETE = "DELETE"
	ERROR = "ERROR"
	OPEN = "OPEN"
	CLOSED = "CLOSED"
	INCIDENT = "INCIDENT"


class LogInfoORM(Base):
	__tablename__ = "log_info"
	__table_args__ = {'extend_existing': True}

	id: Mapped[intpk]
	status: Mapped[StatusEnumORM]
	creator: Mapped[str_100]
	logs: Mapped[str]

	date_create: Mapped[created_at]


class AllInc(BaseGasi):
	# __table__ = Table(
	# 	"smartjoe_allinc",
	# 	BaseGasi.metadata,
	# 	autoload_with = sync_engine_gasi,
	# )
	__tablename__ = "smartjoe_allinc"
	# __table_args__ = {'extend_existing': True}
	__table_args__ = {"schema": "public", 'extend_existing': True}

	id: Mapped[intpk]
	number_inc: Mapped[str_127]
	description: Mapped[str] = mapped_column(Text, nullable = True)
	status: Mapped[str_31]
	executor: Mapped[str_63] #= mapped_column(nullable = True)
	executor_group: Mapped[str_63] #= mapped_column(nullable = True)
	influence: Mapped[int]
	cause: Mapped[str] = mapped_column(Text, nullable = True)
	link: Mapped[str] #= mapped_column(nullable = True)
	creation_time: Mapped[created_at]
	parent_inc: Mapped[str] #= mapped_column(nullable = True)
	initiator_login: Mapped[str_127] #= mapped_column(nullable = True)
	source: Mapped[str_127] #= mapped_column(nullable = True)
	executor_login: Mapped[str_127] #= mapped_column(nullable = True)
	initiator: Mapped[str_200] #= mapped_column(nullable = True)
	initiator_group: Mapped[str_63] #= mapped_column(nullable = True)
	supervisor: Mapped[str_200] #= mapped_column(nullable = True)
	supervisor_group: Mapped[str_63] #= mapped_column(nullable = True)
	supervisor_login: Mapped[str_127] #= mapped_column(nullable = True)
	ne_name: Mapped[str_300] #= mapped_column(nullable = True)









#
#
#
#
# from datetime import datetime
#
# from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Boolean #create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship, backref
#
# from models.database import engine
#
# PATH_DATA = 'Data'
# # DATABASE_NAME = 'dbsendemails.sqlite3'
#
# LIST_USERS_ADMIN = {
# 	'avsulyay@mts.ru',
# 	'igdemide@mts.ru',
# 	'vvkravc3@mts.ru',
# }
#
#
#
# # path_db = os.path.join(PATH_DATA, DATABASE_NAME)
#
# # engine = create_engine(f'sqlite:///{path_db}', echo=False, connect_args={'check_same_thread': False})
# # Session = sessionmaker(bind=engine)
# #
# # Base = declarative_base()
#
# # path_db = "postgresql+psycopg2://emailsoper:emailsoper@10.40.176.133:6433/sendemails"
# #
# # engine = create_engine("postgresql+psycopg2://emailsoper:emailsoper@10.40.176.133:6433/sendemails")
# # print(f'engine: {engine}')
# Session = sessionmaker(bind=engine, autoflush=False)
#
# Base = declarative_base()
#
#
#
# operator_location = Table(
# 	"operator_location",
# 	Base.metadata,
# 	Column("operator_id", Integer, ForeignKey("operator.operator_id")),
# 	Column("location_id", Integer, ForeignKey("location.location_id")),
# )
#
#
#
# class Operator(Base):
# 	__tablename__ = "operator"
# 	operator_id = Column(Integer, primary_key = True)
# 	operator_name = Column(String(100), nullable = False)
# 	flag = Column(Boolean, default = False)
# 	# emails = relationship("Email", backref=backref("operator"), cascade="all, delete")
# 	# dpcs = relationship("DPC", backref=backref("operator"), cascade="all, delete", passive_deletes = True)
# 	# dpcs_mgmns = relationship("DPCMgmn", backref=backref("operator"), cascade="all, delete", passive_deletes = True)
# 	incidents = relationship("Incident", backref=backref("operator"), cascade="all, delete")
# 	# locations = relationship(
# 	# 	"Location",
# 	# 	secondary=operator_location,
# 	# 	back_populates="operators",
# 	# 	cascade="all, delete",
# 	# 	passive_deletes = True
# 	# )
# 	def __init__ (self, operator_name, flag):
# 		self.operator_name = operator_name
# 		self.flag = flag
#
#
# class Email(Base):
# 	__tablename__ = "email"
# 	email_id = Column(Integer, primary_key = True)
# 	email_name = Column(String(100))
# 	operator_id = Column(Integer, ForeignKey("operator.operator_id", ondelete="CASCADE"))
#
# 	operators_emails = relationship("Operator", backref = backref("email_operator"))
#
# 	def __init__ (self, email_name, operator_id):
# 		self.email_name = email_name
# 		self.operator_id = operator_id
#
#
# class Location(Base):
# 	__tablename__ = "location"
# 	location_id = Column(Integer, primary_key = True)
# 	location_name = Column(String(100))
# 	# dpcs = relationship("DPC", backref = backref("location"))
# 	# operators = relationship(
# 	# 	"Operator", secondary=operator_location, back_populates="locations"
# 	# )
#
# 	def __init__(self, location_name):
# 		self.location_name = location_name
#
#
#
# class DPC(Base):
# 	__tablename__ = "dpc"
# 	dpc_id = Column(Integer, primary_key = True)
# 	dpc_name = Column(Integer)
# 	abcdef = Column(String(100), nullable=True)
# 	structurnii = Column(String(10), nullable=True)
# 	zone_obslujivaniya = Column(String(100), nullable=True)
# 	operator_id = Column(Integer, ForeignKey("operator.operator_id", ondelete="CASCADE"))
# 	location_id = Column(Integer, ForeignKey("location.location_id"))
#
# 	locations = relationship("Location", backref = backref("dpc_location"))
# 	operators = relationship("Operator", backref = backref("dpc_operator"))
#
#
#
# 	def __init__(self, dpc_name, operator_id, location_id, abcdef, structurnii, zone_obslujivaniya):
# 		self.dpc_name = dpc_name
# 		self.operator_id = operator_id
# 		self.location_id = location_id
# 		self.abcdef = abcdef
# 		self.structurnii = structurnii
# 		self.zone_obslujivaniya = zone_obslujivaniya
#
#
# class DPCMgmn(Base):
# 	__tablename__ = "dpc_mgmn"
# 	dpc_id = Column(Integer, primary_key = True)
# 	dpc_name = Column(String(30))
# 	kommutator = Column(String(15), nullable=True)
# 	name_trank = Column(String(30), nullable=True)
# 	opc = Column(String(15), nullable=True)
# 	region_kommutatora = Column(String(30), nullable=True)
# 	region_shluza = Column(String(30), nullable=True)
# 	uroven_prisoedineniya = Column(String(15), nullable=True)
# 	operator_id = Column(Integer, ForeignKey("operator.operator_id", ondelete="CASCADE"))
#
# 	operators_mgmn = relationship("Operator", backref = backref("dpcmgmn_operator"))
#
# 	def __init__(self, dpc_name, kommutator, name_trank, opc, region_kommutatora, region_shluza, uroven_prisoedineniya, operator_id):
# 		self.dpc_name = dpc_name
# 		self.kommutator = kommutator
# 		self.name_trank = name_trank
# 		self.opc = opc
# 		self.region_kommutatora = region_kommutatora
# 		self.region_shluza = region_shluza
# 		self.uroven_prisoedineniya = uroven_prisoedineniya
# 		self.operator_id = operator_id
#
#
# class Incident(Base):
# 	__tablename__ = "incident"
# 	incident_id = Column(Integer, primary_key = True)
# 	incident_name = Column(String(15))
# 	date_send = Column(DateTime(timezone = True), default = datetime.now())
# 	operator_id = Column(Integer, ForeignKey("operator.operator_id", ondelete="CASCADE"))
#
# 	def __init__(self, incident_name, operator_id):
# 		self.incident_name = incident_name
# 		self.operator_id = operator_id
#
# class UserAdmin(Base):
# 	__tablename__ = "user_admin"
# 	user_id = Column(Integer, primary_key = True)
# 	user_name = Column(String(30))
#
# 	def __init__(self, user_name):
# 		self.user_name = user_name
#
# class LogInfo(Base):
# 	__tablename__ = "log_info"
# 	log_id = Column(Integer, primary_key = True)
# 	created = Column(String(255))
# 	logs = Column(String())
# 	date_create = Column(DateTime(timezone = True), default = datetime.now())
#
# 	def __init__(self, created, logs, date_create):
# 		self.created = created
# 		self.logs = logs
# 		self.date_create = date_create
#
#
#
# class EmailsRegion(Base):
# 	__tablename__ = "emails_region"
# 	id = Column(Integer, primary_key = True)
# 	email = Column(String(100))
# 	region = Column(String(100))
#
# 	def __init__ (self, email, region):
# 		self.email = email
# 		self.region = region
#
#
#
# def create_db():
# 	Base.metadata.create_all(engine)
#
# 	session = Session()
# 	for index, user in enumerate(LIST_USERS_ADMIN):
# 		session.add(UserAdmin(user_name = user))
# 	session.commit()
# 	session.close()
#
#



