import hashlib
import re
from abc import ABC, abstractmethod
from datetime import datetime, date

from os.path import join, exists

from dateutil.relativedelta import relativedelta
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.future import select
from sqlalchemy import and_, or_, asc, delete, insert, update, exc, func, desc, case, not_

# from sqlalchemy.orm import exc
# from sqlalchemy.util import namedtuple
from sqlalchemy.orm import joinedload, class_mapper
from sqlalchemy.orm.strategy_options import contains_eager
from sqlalchemy.sql import Insert, Update, Select


from Core.Models.Models import session, session1, User, Role, Arendators, Phone, TypeTransport, Vehicle, \
	StatusTransport, Contract, ColorTransport, PaymentCategory, HistoryPayment, TemporaryPeriodPay


class DataBase(ABC):

	@abstractmethod
	def get_user_id (self, username): pass

	@abstractmethod
	def get_username (self, id_): pass

	@abstractmethod
	def get_role_id (self, role): pass

	@abstractmethod
	def confirm_login (self, username, password): pass

	@abstractmethod
	def all_users_managers (self): pass

	@abstractmethod
	def add_user_admin (self): pass

	@abstractmethod
	def delete_user_admin (self, id_): pass

	@abstractmethod
	def all_roles (self): pass

	@abstractmethod
	def roles (self): pass

	@abstractmethod
	def add_roles (self): pass

	@abstractmethod
	def delete_roles (self, id_): pass

	@abstractmethod
	def update_password (self): pass

	@abstractmethod
	def create_or_update_arendator(self): pass

	@abstractmethod
	def get_arendator_id(self, surname, name, last_name): pass

	@abstractmethod
	def type_transport (self): pass

	@abstractmethod
	def status_transport(self): pass

	@abstractmethod
	def add_transport_db(self): pass




class Usuarios(DataBase):

	def get_username (self, user_input):
		# result = session.query(User.username, User.name, Role.role, Role.name).filter(User.username == f'{user_input}', User.role_id == Role.id).first()
		result = session.query(User.username, User.name, Role.role, (Role.name).label('role_name')).filter(User.username == f'{user_input}', User.role_id == Role.id).first()
		session.close()
		return result

	def get_user_id (self, user_input):
		# print(user_input)
		result = session.query(User.id, Role.role).filter(User.username == f'{user_input}', User.role_id == Role.id).first()
		session.close()
		return (result[0], result[1]) if result else (None, None)

	def get_role_id (self, role_input):
		result = session.query(Role.id).filter(Role.role == f'{role_input}').first()
		session.close()
		# print('Result из get_role_id : ', result)
		return result if result else None

	def confirm_login (self, user_input, password):
		# user_name, role = self.get_username(user_input)
		result = self.get_username(user_input)

		if result == None:
			return ('Not user', None)
			# return 'Not user'

		enc_pass = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
		password_input = session.query(User.password).filter(User.username == f'{user_input}').first()[0]
		session.close()

		# print(enc_pass)
		# print(password_input)

		confirmation = enc_pass == password_input

		# return ('Confirm', result.role) if confirmation else ('Не верный пароль', None)
		return ('Confirm', result) if confirmation else ('Не верный пароль', None)

	def all_users_managers(self):
		result = session.query(User).all()
		session.close()
		return result

	def add_user_admin(self, username, name, password, email, role_id):
		user_id, _ = self.get_user_id(username)
		# print(user_id, ' -- ', username)

		enc_pass = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
		try:
			if not user_id:
				add_user = insert(User).values(username=f'{username}', name=f'{name}', password=f'{enc_pass}', email=f'{email}', role_id=role_id).execution_options(synchronize_session = "fetch")
				session.execute(add_user)
				confirmation = 'успешно добавлен'
			else:
				update_user = update(User).where(User.id == user_id).values(name=f'{name}', email=f'{email}', role_id=role_id).execution_options(synchronize_session = "fetch")
				session.execute(update_user)
				confirmation = 'данные успешно обновлены'
			session.commit()
		except Exception:
			session.rollback()
		finally:
			session.close()

		if not user_id:
			return confirmation
		else:
			return confirmation

	def delete_user_admin(self, id):
		try:
			user_from_admin = delete(User).where(User.id == id).execution_options(synchronize_session = "fetch")
			session.execute(user_from_admin)
			session.commit()
		except Exception:
			session.rollback()
		finally:
			session.close()

	def all_roles():
		results = session.query(Role).all()
		session.close()
		return results

	def roles(self):
		role = session.query(Role).all()
		session.close()
		return role


	def add_roles(self, role, name):
		role_id = self.get_role_id(role)
		try:
			if not role_id:
				add_role = insert(Role).values(role = f'{role}', name = f'{name}').execution_options(synchronize_session = "fetch")
				session.execute(add_role)
				confirmation = 'успешно добавлена'
			else:
				update_role = update(Role).where(Role.id == role_id[0]).values(name = f'{name}').execution_options(synchronize_session = "fetch")
				session.execute(update_role)
				confirmation = 'данные успешно обновлены'
			session.commit()
		except Exception:
			session.rollback()
		finally:
			session.close()

		if not role_id:
			return confirmation
		else:
			return confirmation


	def delete_roles(self, id):
		print('Удаляем виджет с ID: ', id)
		try:
			role_user = delete(Role).where(Role.id == id).execution_options(synchronize_session = "fetch")
			session.execute(role_user)
			session.commit()
		except Exception:
			session.rollback()
		finally:
			session.close()


	def update_password(self, id, password):
		print(id, password)
		enc_pass = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
		print(enc_pass)
		try:
			update_password = update(User).where(User.id == id).values(password=f'{enc_pass}').execution_options(synchronize_session = "fetch")
			session.execute(update_password)
			session.commit()
			confirmation = 'Пароль успешно обновлен'
		except Exception:
			session.rollback()
		finally:
			session.close()

		return True if confirmation else False


	def get_arendator_id (self, surname_input, name_input, last_name_input):
		result = session.query(Arendators).filter(Arendators.surname == f'{surname_input}', Arendators.name == f'{name_input}', Arendators.last_name == f'{last_name_input}')
		session.close()
		# print(result.one_or_none())
		# print('Result из get_arendator_id : ', result)
		# return result if result else None
		return result


	def get_arendator(self, ids):
		queryes = session.query(Arendators).get(ids)
		return queryes


	def create_or_update_arendator(self, ids=0, list_fields=None):
		queries = session.query(Arendators).filter(Arendators.id == ids).one_or_none()
		responce = ''
		try:
			if queries == None:
				add_arendator = Insert(Arendators).values(
					surname = list_fields['surname'].lower(),
					name = list_fields['name'].lower(),
					last_name = list_fields['last_name'].lower(),
					date_birthday = list_fields['date_birthday'],
					checked_passport = list_fields['checked_passport'],
					passport_country = list_fields['passport_country'],
					driving_license = list_fields['driving_license'],
					serial_pasport = list_fields['serial_pasport'],
					number_pasport = list_fields['number_pasport'],
					date_pasport = list_fields['date_pasport'],
					code_division = list_fields['code_division'],
					who_issued = list_fields['who_issued'],
					address_registration = list_fields['address_registration'],
					address_residence = list_fields['address_residence']
				)
				print('*' * 25)

				result = session.execute(add_arendator)

				for item in list_fields['phones_arendator']:
					insert_phone = insert(Phone).values(
						{'phone': item.get('phone'), 'arendator_id': result.inserted_primary_key[0]}).execution_options(
						synchronize_session="fetch")
					session.execute(insert_phone)


				responce = 'save'


			else:

				update_arendator = update(Arendators).where(Arendators.id == int(ids)).values({
					'surname': list_fields['surname'].lower(),
					'name': list_fields['name'].lower(),
					'last_name': list_fields['last_name'].lower(),
					'date_birthday': list_fields['date_birthday'],
					'checked_passport': list_fields['checked_passport'],
					'passport_country': list_fields['passport_country'],
					'driving_license': list_fields['driving_license'],
					'serial_pasport': list_fields['serial_pasport'],
					'number_pasport': list_fields['number_pasport'],
					'date_pasport': list_fields['date_pasport'],
					'code_division': list_fields['code_division'],
					'who_issued': list_fields['who_issued'],
					'address_registration': list_fields['address_registration'],
					'address_residence': list_fields['address_residence']
				}).execution_options(synchronize_session="fetch")

				session.execute(update_arendator)

				for item in list_fields['phones_arendator']:
					id_phone = session.query(Phone).get(item.get('id'))
					if id_phone:
						uppdate_phone = update(Phone).where(Phone.id == id_phone.id,
															Phone.arendator_id == int(ids)).values(
							{'phone': item.get('phone')}).execution_options(synchronize_session="fetch")
						session.execute(uppdate_phone)
					else:
						insert_phone = insert(Phone).values(
							{'phone': item.get('phone'), 'arendator_id': int(ids)}).execution_options(
							synchronize_session="fetch")
						session.execute(insert_phone)

				update_contract = update(Contract).where(Contract.id_arendator == int(ids)).values({
					'fio_arendator': f'{list_fields["surname"]} {list_fields["name"]} {list_fields["last_name"]}'.lower()
				})
				session.execute(update_contract)

				responce = 'update'

			session.commit()

		except Exception as exc:
			print('Error update Arendator')
			session.rollback()
			responce = 'error'
			raise RuntimeError("Something bad happened") from exc
		finally:
			session.close()

		if queries == None:
			print('Add new arendator')
			print(f'ID add new arendator: {result.inserted_primary_key}')
			return result.inserted_primary_key, responce
		else:
			print('Update arendator')
			return ids, responce


	def delete_phone_arendator(self, ids):
		# print(f'ID phone for delete: {id}')
		responce = ''
		try:
			item_phone = delete(Phone).where(Phone.id == ids).execution_options(synchronize_session = "fetch")
			session.execute(item_phone)
			session.commit()
			responce = 'deletes'
		except Exception:
			session.rollback()
			responce = 'error'
		finally:
			session.close()
		return responce


	def type_transport(self):
		# type_transport = session.execute(select(TypeTransport)).all()
		type_transport = session.execute(select(TypeTransport.id, TypeTransport.name).order_by(TypeTransport.id))
		# print(type_transport.scalars().all())
		return type_transport


	def status_transport(self, default=False):
		if default:
			# status = Select(StatusTransport).filter(StatusTransport.default_status == default).one()
			status = session.execute(select(StatusTransport).filter(StatusTransport.default_status == default))
			# print('ID status: ', status)
			return status.scalars().first()
			# return status
		else:
			status = session.execute(select(StatusTransport))
		# print(type_transport.scalars().all())
			return status.scalars().all()


	def get_status_transport_id(self, value):
		status = session.execute(select(StatusTransport).filter(StatusTransport.name.ilike("%{}%".format(value))))
		return status.scalars().first()


	def color_transport(self, default=False):
		if default:
			colors = session.execute(select(ColorTransport).filter(ColorTransport.default_color == default))
			return colors.scalars().first()
		else:
			colors = session.execute(select(ColorTransport).order_by(ColorTransport.id))
			return colors.scalars().all()


	def all_colors_transport(self):
		all_colors = session.query(ColorTransport)
		# print(all_colors)
		return all_colors


	def delete_color_transport(self, ids = None):
		responce = ''
		queries = session.query(Vehicle.id, Vehicle.color_id).filter(Vehicle.color_id == int(ids)).count()
		# print(f'Len queries: {queries}')
		if queries == 0:
			try:
				item_color = delete(ColorTransport).where(ColorTransport.id == ids).execution_options(synchronize_session = "fetch")
				session.execute(item_color)
				session.commit()
			except Exception:
				session.rollback()
			finally:
				session.close()
			responce = 'deletes'
		else:
			responce = 'not_deletes'
		return responce, queries


	def add_color_transport(self, db_ids = None, db_name = None, db_color = None):
		responce = ''
		queries = session.query(ColorTransport).get(int(db_ids))
		try:
			if queries == None:
				add_color = Insert(ColorTransport).values(
					name = db_name,
					color = db_color
				)
				result = session.execute(add_color)
				responce = 'save'
			else:
				update_color = update(ColorTransport).where(ColorTransport.id == int(db_ids)).values({
					'name': db_name,
					'color': db_color
				}).execution_options(synchronize_session = "fetch")
				session.execute(update_color)
				responce = 'update'
			session.commit()
		except Exception:
			session.rollback()
			responce = 'error'
			print('Error')
			raise
		finally:
			session.close()

		if queries == None:
			return responce, result.inserted_primary_key[0]
		else:
			return responce, db_ids


	def payment_category_db(self):
		# category = session.execute(select(PaymentCategory))
		categorys = session.query(PaymentCategory).order_by(PaymentCategory.size).all()
		session.close()
		return categorys


	def add_payment_category(self, db_ids = None, db_size = None):
		responce = ''
		queries = session.query(PaymentCategory).get(int(db_ids))
		try:
			if queries == None:
				add_pcat = Insert(PaymentCategory).values(size=db_size)
				result = session.execute(add_pcat)
				responce = 'save'
			else:
				update_pcat = update(PaymentCategory).where(PaymentCategory.id == int(db_ids)).values({
					'size': db_size
				}).execution_options(synchronize_session="fetch")
				session.execute(update_pcat)
				responce = 'update'
			session.commit()
		except Exception:
			session.rollback()
			responce = 'error'
			print('Error')
			raise
		finally:
			session.close()

		if queries == None:
			return responce, result.inserted_primary_key[0]
		else:
			return responce, db_ids


	def delete_payment_category(self, ids = None):
		responce = ''
		queries = session.query(Vehicle.id, Vehicle.paymentcategory_id).filter(Vehicle.paymentcategory_id == int(ids)).count()
		print(f'Len queries: {queries}')
		if queries == 0:
			try:
				item_color = delete(PaymentCategory).where(PaymentCategory.id == ids).execution_options(synchronize_session = "fetch")
				session.execute(item_color)
				session.commit()
			except Exception:
				session.rollback()
			finally:
				session.close()
			responce = 'deletes'
		else:
			responce = 'not_deletes'
		return responce, queries


	def vehicle_category_db(self):
		views_categories = session.query(TypeTransport).order_by(TypeTransport.id).all()
		session.close()
		return views_categories

	def add_vehicle_category(self, db_ids = None, db_name = None):
		responce = ''
		queries = session.query(TypeTransport).get(int(db_ids))
		try:
			if queries == None:
				add_vehcat = Insert(TypeTransport).values(name=db_name)
				result = session.execute(add_vehcat)
				responce = 'save'
			else:
				update_vehcat = update(TypeTransport).where(TypeTransport.id == int(db_ids)).values({
					'name': db_name
				}).execution_options(synchronize_session="fetch")
				session.execute(update_vehcat)
				responce = 'update'
			session.commit()
		except Exception:
			session.rollback()
			responce = 'error'
			print('Error')
			raise
		finally:
			session.close()

		if queries == None:
			return responce, result.inserted_primary_key[0]
		else:
			return responce, db_ids

	def delete_vehicle_category(self, ids = None):
		responce = ''
		queries = session.query(Vehicle.id, Vehicle.type_transport_id).filter(Vehicle.type_transport_id == int(ids)).count()
		print(f'Len queries: {queries}')
		if queries == 0:
			try:
				item_vehcat = delete(TypeTransport).where(TypeTransport.id == ids).execution_options(synchronize_session = "fetch")
				session.execute(item_vehcat)
				session.commit()
			except Exception:
				session.rollback()
			finally:
				session.close()
			responce = 'deletes'
		else:
			responce = 'not_deletes'
		return responce, queries


	def add_transport_db(self, fields=None):
		queries = session.query(Vehicle.id).filter(Vehicle.id == int(fields['ts_id'])).one_or_none()
		responce = ''

		try:
			if queries == None:
				vehicle_add = Insert(Vehicle).values(
					brand = fields['brand'],
					model = fields['model'],
					bodywork = fields['bodywork'],
					engine_volume = fields['engine_volume'],
					date_purchase = fields['date_purchase'],
					place_purchase = fields['place_purchase'],
					number_engine = fields['number_engine'],
					market_price = fields['market_price'],
					purchase_price = fields['purchase_price'],
					number_simcard = fields['number_simcard'],
					gps_id = fields['gps_id'],
					type_gps = fields['type_gps'],
					date_prev_to = fields['date_prev_to'],
					date_next_to = fields['date_next_to'],
					prev_mileage = fields['prev_mileage'],
					next_mileage = fields['next_mileage'],
					comment_prev_to = fields['comment_prev_to'],
					comment_next_to = fields['comment_next_to'],
					comment_general = fields['comment_general'],
					image = fields['image'],
					type_transport_id = fields['type_transport_id'],
					status_transport_id = fields['status_transport_id'],
					color_id = fields['color_id'],
					paymentcategory_id = fields['paymentcategory_id']
				)
				result = session.execute(vehicle_add)
				responce = 'save'
				# print('Ok4')
			else:
				# print('Ok5')
				# print(f'ID TS update: {int(fields["ts_id"])}')
				update_ts = update(Vehicle).where(Vehicle.id == int(fields["ts_id"])).values({
					'brand': fields["brand"],
					'model': fields["model"],
					'bodywork': fields["bodywork"],
					'engine_volume': fields["engine_volume"],
					'date_purchase': fields["date_purchase"],
					'place_purchase': fields["place_purchase"],
					'number_engine': fields["number_engine"],
					'market_price': fields["market_price"],
					'purchase_price': fields["purchase_price"],
					'number_simcard': fields["number_simcard"],
					'gps_id': fields["gps_id"],
					'type_gps': fields["type_gps"],
					'date_prev_to': fields["date_prev_to"],
					'date_next_to': fields["date_next_to"],
					'prev_mileage': fields["prev_mileage"],
					'next_mileage': fields["next_mileage"],
					'comment_prev_to': fields["comment_prev_to"],
					'comment_next_to': fields["comment_next_to"],
					'comment_general': fields["comment_general"],
					'image': fields["image"],
					'type_transport_id': fields["type_transport_id"],
					'status_transport_id': fields["status_transport_id"],
					'color_id': fields["color_id"],
					'paymentcategory_id': fields["paymentcategory_id"]
				})  # .execution_options(synchronize_session = "fetch")
				session.execute(update_ts)

				responce = 'update'

			session.commit()
			# print('Из add_transport_db после  commit')
		except Exception:
			session.rollback()
			responce = 'error'
			print('Error')
			# raise
		finally:
			session.close()

		if queries == None:
			return result.inserted_primary_key[0], responce
		else:
			return fields['ts_id'], responce


	def base_list_arendators(self, filters_arendators ={}):

		def get_filter_by_args(dic_filter: dict):
			filters_db_arendators = []
			filters_sorting = []
			for key, value in dic_filter.items():
				try:
					if key.endswith('___text'):
						if value != '':
							key = key[:-7]
							filters_db_arendators.append(getattr(Arendators, key).ilike("%{}%".format(value)))

					elif key.endswith('__hidened'):
						if value == True:
							key = key[:-9]
							filters_db_arendators.append(getattr(Arendators, key) == value)

					elif key.endswith('__active'):
						key = key[:-8]
						value = False
						filters_db_arendators.append(getattr(Arendators, key) == value)

					elif value == '___min_date':
						key = 'date_created'
						filters_sorting.append(getattr(Arendators, key).asc())

					elif value == '___max_date':
						key = 'date_created'
						filters_sorting.append(getattr(Arendators, key).desc())

					elif value.endswith("___desc"):
						key = value[:-7]
						filters_sorting.append(getattr(Arendators, key).desc())

					elif value.endswith("___asc"):
						key = value[:-6]
						filters_sorting.append(getattr(Arendators, key).asc())

					#
					# elif key == 'driving_license':
					# 	if value == True:
					# 		filters_arendators.append(getattr(Arendators, key) == value)

					# elif key.endswith('__id'):
					# 	key = key[:-4]
					# 	if value:
					# 		filters_sorting.append(getattr(Arendators, key).desc())
					# 	else:
					# 		filters_sorting.append(getattr(Arendators, key).asc())

					# elif key.endswith('__fio'):
					# 	key = key[:-5]
					# 	if value:
					# 		filters_sorting.append(getattr(Arendators, key).asc())
					# 	else:
					# 		filters_sorting.append(getattr(Arendators, key).desc())

					# elif key.endswith('__created'):
					# 	key = key[:-9]
					# 	if value:
					# 		filters_sorting.append(getattr(Arendators, key).desc())
					# 	# else:
					# 	# 	filters_sorting.append(getattr(Arendators, key).asc())

					# elif key.endswith('__count'):
					# 	key = 'count_conract'
					# 	print(f'Count key: {key}')
					# 	if value:
					# 		filters_sorting.append(key.desc())
					# 	else:
					# 		filters_sorting.append(key.asc())

					## elif key.endswith('___ts'):
					# 	if value == True:
					# 		key = key[:-5]
					# 		filters_vehicle.append(getattr(Vehicle, key) == value)
					#
					# elif value == '___max_market_price':
					# 	key = 'market_price'
					# 	# print('MAX PRICE: ', key, '==>', value)
					# 	filters_vehicle_sort.append(getattr(Vehicle, key).desc())
					# elif value == '___min_market_price':
					# 	key = 'market_price'
					# 	# print('MIN PRICE: ', key, '==>', value)
					# 	filters_vehicle_sort.append(getattr(Vehicle, key).asc())
					#
					# elif key == 'id_dogovor':
					# 	key = key[:2]
					# 	filters_db_contract.append(getattr(Contract, key).like("%{}%".format(value)))
					#

					# elif value == '___min_date':
					# 	filters_sorting.append(getattr(Contract, key).asc())
					#
					# elif key == 'driving_license':
					# 	if value == True:
					# 		filters_arendators.append(getattr(Arendators, key) == value)
					#
					# elif key.endswith('___today'):
					# 	key = 'dates_payments_next'
					# 	value = datetime.today().date()
					# 	filters_db_contract.append(getattr(Contract, key) == value)
					#
					# elif key.endswith('___tomorrow'):
					# 	key = 'dates_payments_next'
					# 	value = datetime.today().date() + relativedelta(days=+1)
					# 	filters_db_contract.append(getattr(Contract, key) == value)
					#
					#
					elif key.endswith('__all'):
						continue
					else:
						# print(f'Другие: {key}----- {value}')
						continue
				except AttributeError:
					continue

			return filters_db_arendators, filters_sorting

		dic_args, dic_sort = get_filter_by_args(filters_arendators)

		# print('DIC_ARGS: ', *dic_args)
		# print('DIC_SORT: ', *dic_sort)


		result = session.query(Arendators, func.count(Contract.id).label("count_conract")).filter(*dic_args).outerjoin(
			Contract, isouter=True).group_by(Arendators.id).order_by(*dic_sort)

		# result = session.query(Arendators, func.count(Contract.id).label("count_conract")).filter(*dic_args).order_by(-Arendators.id).outerjoin(Contract).group_by(Arendators.id)

		# print(f'Result: {result}')

		for_manadgers = result.filter(Arendators.hiden_arendator == False)

		queryes = {
			'all_arendators': result,
			'for_manadgers': for_manadgers
		}
		return queryes


	def hidened_arendator(self, ids, hidened):
		print(f'Status from DB: {hidened}')
		responce = ''
		try:
			hideneted_arendator = update(Arendators).where(Arendators.id == ids).values({'hiden_arendator': not hidened}).execution_options(
				synchronize_session="fetch")
			session.execute(hideneted_arendator)
			session.commit()
			responce = 'update'
		except Exception:
			session.rollback()
		finally:
			session.close()
		return responce


	def delete_arendator(self, ids):
		responce = ''
		try:
			delete_history_paymend = delete(HistoryPayment).where(
				HistoryPayment.id_arendator == ids).execution_options(synchronize_session="fetch")
			session.execute(delete_history_paymend)

			delete_arendator = delete(Arendators).where(Arendators.id == ids).execution_options(
				synchronize_session="fetch")
			session.execute(delete_arendator)

			session.commit()
			responce = 'deletes'
		except Exception:
			session.rollback()
		finally:
			session.close()
		return responce

	def list_histored_payments(self, ids_arendator=None):
		queryes = session.query(HistoryPayment).filter(HistoryPayment.id_arendator == int(ids_arendator)).order_by(HistoryPayment.id_contract).all()
		return queryes


	def list_arendators(self, filters_contract ={}):

		def get_filter_by_args(dic_filter: dict):
			filters_db_contract = []
			filters_sorting = []
			filters_vehicle = []
			filters_vehicle_sort = []
			filters_arendators = []
			for key, value in dic_filter.items():  # type: str, any
				try:
					if key.endswith('__text'):
						if value != '':
							key = key[:-6]
							filters_db_contract.append(getattr(Contract, key).ilike("%{}%".format(value)))

					elif key.endswith('___ts'):
						if value == True:
							key = key[:-5]
							filters_vehicle.append(getattr(Vehicle, key) == value)

					elif value == '___max_market_price':
						key = 'market_price'
						# print('MAX PRICE: ', key, '==>', value)
						filters_vehicle_sort.append(getattr(Vehicle, key).desc())
					elif value == '___min_market_price':
						key = 'market_price'
						# print('MIN PRICE: ', key, '==>', value)
						filters_vehicle_sort.append(getattr(Vehicle, key).asc())

					elif key.endswith('__close'):
						if value == True:
							key = key[:-7]
							filters_db_contract.append(getattr(Contract, key) == value)

					elif key.endswith('__open'):
						key = key[:-6]
						value = False
						filters_db_contract.append(getattr(Contract, key) == value)

					elif key == 'id_dogovor':
						key = key[:2]
						filters_db_contract.append(getattr(Contract, key).like("%{}%".format(value)))

					elif value == '___max_date':
						filters_sorting.append(getattr(Contract, key).desc())
					elif value == '___min_date':
						filters_sorting.append(getattr(Contract, key).asc())

					elif key == 'driving_license':
						if value == True:
							filters_arendators.append(getattr(Arendators, key) == value)

					elif key.endswith('___today'):
						key = 'dates_payments_next'
						value = datetime.today().date()
						filters_db_contract.append(getattr(Contract, key) == value)

					elif key.endswith('___tomorrow'):
						key = 'dates_payments_next'
						value = datetime.today().date() + relativedelta(days=+1)
						filters_db_contract.append(getattr(Contract, key) == value)

					elif key == 'dolg':
						key = 'dates_payments_next'
						if value == True:
							value = datetime.today().date()
							filters_db_contract.append(getattr(Contract, key) < value)


					elif key.endswith('___all'):
						continue
					else:
						# print(f'Другие: {key}----- {value}')
						continue
						# filters_db_contract.append(getattr(Contract, key) == value)
				except AttributeError:
					continue

			return filters_db_contract, filters_sorting, filters_vehicle, filters_vehicle_sort, filters_arendators

		dic_args, dic_sort, dic_vehicle, dic_vehicle_sort, dic_arendators = get_filter_by_args(filters_contract)

		# print('DIC_ARGS: ', *dic_args)
		# print('DIC_SORT: ', *dic_sort)
		# print('DIC_VEHICLE: ', *dic_vehicle)
		# print('DIC_VEHICLE: ', *dic_vehicle_sort)

		result = session.query(Contract).filter(*dic_args).order_by(*dic_sort).join(Vehicle).filter(*dic_vehicle).order_by(*dic_vehicle_sort).\
			join(Arendators).filter(*dic_arendators).order_by(-Contract.id)


		# print(result)

		queryes = {
			'all_arendators': result
		}
		return queryes


	def select_ts(self, type_ts):
		# query = session.execute(select(Vehicle.model).filter(Vehicle.type_transport_id==f'{type_ts}'))
		query = session.query(Vehicle.brand).filter(Vehicle.type_transport_id==f'{type_ts}').distinct(Vehicle.brand)
		return query


	def select_ts_vin(self, vin_ts, type_ts):
		query = session.query(Vehicle).filter(Vehicle.brand==f'{vin_ts}', Vehicle.type_transport_id==f'{type_ts}',
														Vehicle.status_transport_id == 1, Vehicle.vikup == False, Vehicle.contract_number == 0)
		return query


	def list_transport(self, filters ={}):
		# print(f'Filters_in_db: {filters}')
		def get_filter_by_args(dic_filter: dict):
			filters_db = []
			sorting_db = []
			sorting_pcat = []
			for key, value in dic_filter.items():  # type: str, any
				# print(f'Key: {key} - Value: {value}')
				try:
					if value != '':
						if key.endswith('__min'):
							key = key[:-5]
							filters_db.append(getattr(Vehicle, key) >= value)
						elif key.endswith('__max'):
							key = key[:-5]
							filters_db.append(getattr(Vehicle, key) <= value)
						elif key == 'color_id':
							filters_db.append(getattr(Vehicle, key) == value)
						elif key == 'status_transport_id':
							filters_db.append(getattr(Vehicle, key) == value)
						elif key == 'type_transport_id':
							filters_db.append(getattr(Vehicle, key) == value)
						elif value == 'date_next_to':
							key = 'date_next_to'
							sorting_db.append(getattr(Vehicle, key).asc())

						elif value.endswith('___min_pm'):
							key = 'prev_mileage'
							sorting_db.append(getattr(Vehicle, key).asc())
						elif value.endswith('___max_pm'):
							key = 'prev_mileage'
							sorting_db.append(getattr(Vehicle, key).desc())

						elif value.endswith('___min_pc'):
							key = 'size'
							sorting_pcat.append(getattr(PaymentCategory, key).asc())
						elif value.endswith('___max_pc'):
							key = 'size'
							sorting_pcat.append(getattr(PaymentCategory, key).desc())
						else:
							filters_db.append(getattr(Vehicle, key) == value)
				except AttributeError:
					continue

			return filters_db, sorting_db, sorting_pcat

		dic_args, dic_sort, dic_pcat = get_filter_by_args(filters)
		# print(dic_args)
		# print(*dic_args)


		result = session.query(Vehicle)


		types_ts = self.type_transport()
		status_ts = self.status_transport()
		color_ts = self.color_transport()

		brands = result.from_self(Vehicle.brand).distinct()
		models = result.from_self(Vehicle.model).distinct()
		bodywork = result.from_self(Vehicle.bodywork).distinct()

		res_price = result.from_self(func.max(Vehicle.market_price).label("max_price"), func.min(Vehicle.market_price).label("min_price"),).one()


		if filters.get('brand'):
			models = result.filter(Vehicle.brand == filters.get('brand')).from_self(Vehicle.model).distinct()
			bodywork = result.filter(Vehicle.brand == filters.get('brand')).from_self(Vehicle.bodywork).distinct()

		# print(f'All TS: {result.filter(*dic_args).order_by(*dic_sort).join(PaymentCategory).order_by(*dic_pcat)}')

		querys = {
			'result_all': result.filter(*dic_args).order_by(*dic_sort).join(PaymentCategory).order_by(*dic_pcat),
			'brands': brands,
			'models': models,
			'bodywork': bodywork,
			'color': color_ts,
			'max_price': res_price.max_price,
			'min_price': res_price.min_price,
			'types_ts': types_ts,
			'status_ts': status_ts,
		}

		return querys


	def delete_ts(self, ids = None):
		# print(id)
		try:
			item_ts = delete(Vehicle).where(Vehicle.id == int(ids)).execution_options(synchronize_session = "fetch")
			session.execute(item_ts)
			session.commit()
		except Exception:
			session.rollback()
		finally:
			session.close()


	def get_transport_in_id(self, id):
		result = session.query(Vehicle).get(id)
		return result


	def create_or_update_dogovor(self, ids=0, list_fields = None, date_finish_contract = None):
		queries = session.query(Contract).filter(Contract.id == ids).one_or_none()

		id_status_transpor = self.get_status_transport_id('договор')
		# print(f'Запрос статуса Договор: {id_status_transpor.id}')

		responce = ''
		try:
			if queries == None:
				add_contract = Insert(Contract).values(
					date_contract = list_fields['date_contract'],
					rental_period = list_fields['rental_period'],
					method_pay = list_fields['method_pay'],
					size_pay = list_fields['size_pay'],
					optional_equipment = list_fields['optional_equipment'],
					fio_arendator = list_fields['fio_arendator'].lower(),
					id_ts = list_fields['id_ts'],
					id_arendator = list_fields['id_arendator']
				) #.execution_options(synchronize_session = "fetch") #.returning(Contract.id)
				result = session.execute(add_contract)

				# print(f'ID contracta: {result.inserted_primary_key[0]}')
				update_contract_number = update(Vehicle). \
										where(Vehicle.id == list_fields['id_ts']). \
										values({"contract_number": result.inserted_primary_key[0], "status_transport_id": id_status_transpor.id})
				session.execute(update_contract_number)

				if list_fields['vikup'] == True:
					update_vikup = update(Vehicle).where(Vehicle.id == list_fields['id_ts']).values({"vikup": True})
					session.execute(update_vikup)


				responce = 'save'
			else:
				update_dogovor = update(Contract).where(Contract.id == ids).values({'date_finish_contract': date_finish_contract})
				session.execute(update_dogovor)
				# contract_vehicle = update(Vehicle).where(Vehicle.id == list_fields['id_ts']).values({"contract_number": int(ids)})
				# session.execute(contract_vehicle)
				responce = 'update'
			session.commit()
		except Exception:
			session.rollback()
			raise
		finally:
			session.close()

		if queries == None:
			return result.inserted_primary_key, responce
		else:
			return responce


	def last_contract_id(self):
		result = session.query(func.max(Contract.id))
		return result


	def close_contract(self, ids=None, id_ts=None, vikup=False):
		responce = ''

		id_status_transpor = self.get_status_transport_id('выдач')
		# print(f'Запрос статуса Готов к выдаче: {id_status_transpor.id}')
		print(f'ТС идет под Выкуп: {vikup}')

		try:
			update_status_contract = update(Contract).where(Contract.id == ids).values({
				"status_contract": True,
				"date_closed_contract": datetime.now()
			}).execution_options(synchronize_session="fetch")
			session.execute(update_status_contract)

			if not vikup:
				update_contract_number = update(Vehicle). \
					where(Vehicle.id == id_ts). \
					values({"contract_number": 0, "status_transport_id": id_status_transpor.id})
				session.execute(update_contract_number)


			temporary_item = session.query(TemporaryPeriodPay).filter(TemporaryPeriodPay.contract_id == ids).all()
			print(f'Наличие записей в TemporaryPeriodPay по договору {ids} : {len(temporary_item)}')
			if len(temporary_item) != 0:
				delete_temporary_paymend = delete(TemporaryPeriodPay).where(
					TemporaryPeriodPay.contract_id == ids).execution_options(synchronize_session="fetch")
				session.execute(delete_temporary_paymend)


			session.commit()
			print('Ok!')
			responce = True
		except Exception:
			print('Error!')
			session.rollback()
		finally:
			session.close()

		return responce


	def delete_draft_contract(self, ids):
		responce = ''
		delete_draft_contract = session.query(Contract).filter(Contract.id == ids).one()

		id_status_transpor = self.get_status_transport_id('выдач')
		# print(f'Запрос статуса Готов к выдаче: {id_status_transpor.id}')

		try:
			update_vikup = Update(Vehicle).where(Vehicle.id == delete_draft_contract.id_ts).values({"vikup": False, "contract_number": 0, "status_transport_id": id_status_transpor.id})
			session.execute(update_vikup)

			delete_draft = delete(Contract).where(Contract.id == ids).execution_options(synchronize_session = "fetch")
			session.execute(delete_draft)

			delete_temporary_paymend = delete(TemporaryPeriodPay).where(TemporaryPeriodPay.contract_id == ids).execution_options(synchronize_session="fetch")
			session.execute(delete_temporary_paymend)

			session.commit()
			responce = 'deletes'
		except Exception:
			session.rollback()
		finally:
			session.close()
		return responce


	def verif_current_payments(self, id_contract=None):
		responce = ''
		first_payment = session.query(TemporaryPeriodPay).filter(TemporaryPeriodPay.contract_id == f'{id_contract}', TemporaryPeriodPay.verif == False).\
			from_self(func.min(TemporaryPeriodPay.estimated_date).label("min_date_payment")).one()

		try:
			verif_current_payment = update(TemporaryPeriodPay).\
				where(TemporaryPeriodPay.contract_id == id_contract, TemporaryPeriodPay.estimated_date == first_payment.min_date_payment).\
				values({'verif': True})
			session.execute(verif_current_payment)
			session.commit()
			responce = 'update'
		except Exception:
			session.rollback()
			print("Error in verif_current_payments")
			responce = 'error'
		finally:
			session.close()
		return responce


	def first_payments(self, id_contract=None):
		print(f'ID Contract из first_payments: {id_contract}')
		first_payment = session.query(TemporaryPeriodPay).filter(TemporaryPeriodPay.contract_id == id_contract, TemporaryPeriodPay.verif == False).\
			from_self(func.min(TemporaryPeriodPay.estimated_date).label("min_date_payment")).one()
		session.close()

		print(f'Запрос мин даты: {first_payment}')
		return first_payment


	def save_paymend_new_contract(self, confirm_pay=None):
		# print('Из Worker save_paymend_new_contract')
		responce = ''
		if confirm_pay:
			try:
				add_payment = Insert(HistoryPayment).values(
					date_payment = confirm_pay['date_payment'],
					size_payment = confirm_pay['size_payment'],
					comment_pay = confirm_pay['comment_pay'],
					tarif = confirm_pay['tarif'],
					discount = confirm_pay['discount'],
					discount_comment = confirm_pay['discount_comment'],
					shtraf = confirm_pay['shtraf'],
					shtraf_comment = confirm_pay['shtraf_comment'],
					total_pay = confirm_pay['total_pay'],
					payments = confirm_pay['payments'],
					id_arendator = confirm_pay['id_arendator'],
					id_contract = confirm_pay['id_contract']
				)
				result = session.execute(add_payment)

				# print(f'ID Contract 2: {confirm_pay["id_contract"]}')

				if result.inserted_primary_key:
					confirms_pay_first = update(Contract).where(Contract.id == confirm_pay['id_contract']).values({'confirm_pay': True, 'draft': False})
					session.execute(confirms_pay_first)

					first_payment = session.query(TemporaryPeriodPay).filter(
						TemporaryPeriodPay.contract_id == f'{confirm_pay["id_contract"]}',
						TemporaryPeriodPay.verif == False).\
						from_self(func.min(TemporaryPeriodPay.estimated_date).label("min_date_payment")).one()

					# print(f'Min_date_payment: {first_payment.min_date_payment}')

					verif_current_payment = update(TemporaryPeriodPay).\
							where(TemporaryPeriodPay.contract_id == confirm_pay['id_contract'],
							  TemporaryPeriodPay.estimated_date == first_payment.min_date_payment).\
							values({'verif': True})
					session.execute(verif_current_payment)

					print('Ok verif!')

					# print(f'Дата первого платежа: {next_payment}')

				session.commit()
				responce = 'save'
			except Exception:
				session.rollback()
				print("Error in save_paymend_new_contract")
			finally:
				session.close()
			return responce
		else:
			print('Пусто')


	def temporary_payment(self, list_temporary=None):
		try:
			temp_payment = []
			for item in list_temporary:
				temp_payment.append(TemporaryPeriodPay(estimated_date = item['estimated_date'], contract_id = item['contract_id']))

			# print('Temp_payment: ', temp_payment)
			session.add_all(temp_payment)
			session.commit()
			# print('Ok9')

		except Exception:
			session.rollback()
			print("Error in def temporary_payment")
		finally:
			session.close()


	def set_new_date_payment(self, id_conract = None, new_date_payment = None, old_date_payment = None):
		# print(f'ID contract: {id_conract}')
		# print(f'Old date: {old_date_payment}')
		# print(f'New date: {new_date_payment}')
		responce = ''
		result = session.execute(select(TemporaryPeriodPay).filter(TemporaryPeriodPay.contract_id == id_conract, TemporaryPeriodPay.estimated_date == old_date_payment)).scalar()

		if result.id:
			try:
				update_new_date_payment = update(TemporaryPeriodPay).where(TemporaryPeriodPay.id == result.id).values({'estimated_date': new_date_payment})
				session.execute(update_new_date_payment)
				session.commit()
				responce = 'update'

			except Exception:
				session.rollback()
				responce = 'error'
				print("Error in def temporary_payment")
			finally:
				session.close()
		else:
			responce = 'error'
		return responce


	def returnet_ts(self, returned=None):
		# print(f'Returned: {returned}')
		responce = ''
		try:
			closed_contract = Update(Contract).where(Contract.id == returned['id_dogovor']).values({
				'date_closed_contract': returned["date_closed_contract"],
				'status_contract': True}) #.execution_options(synchronize_session=False) # "fetch"
			session.execute(closed_contract)

			returned_ts = Update(Vehicle).where(Vehicle.id == returned['id_ts']).values({
				'prev_mileage': returned["prev_mileage"],
				'status_transport_id': returned["status_ts"],
				'contract_number': 0}) #.execution_options(synchronize_session="fetch")
			session.execute(returned_ts)


			temporary_item = session.query(TemporaryPeriodPay).filter(TemporaryPeriodPay.contract_id == returned['id_dogovor']).all()
			# print(f'Наличие записей в TemporaryPeriodPay по договору {returned["id_dogovor"]} : {len(temporary_item)}')
			if len(temporary_item) != 0:
				delete_temporary_paymend = delete(TemporaryPeriodPay).where(
					TemporaryPeriodPay.contract_id == returned['id_dogovor']).execution_options(synchronize_session="fetch")
				session.execute(delete_temporary_paymend)


			session.commit()
			responce = 'update'
		except Exception:
			session.rollback()
			responce = 'error'
			print("Error in returnet_ts")
		finally:
			session.close()

		return responce


	def charts_data(self):
		# status_contract = session.query(func.count(Contract.status_contract).label("count_contract")).group_by(Contract.status_contract).all()
		status_contract = session.query((func.count(1).filter(Contract.status_contract)).label("count_closed"), (func.count(1).filter(not_(Contract.status_contract))).label("count_opened"))

		count_arendators = session.query(Arendators.date_created, func.count(Arendators.id)).group_by(func.date(Arendators.date_created)).all()
		# count_arendators = session.query(Arendators.date_created, func.count(Arendators.id)).group_by(func.date(Arendators.date_created))

		# db.session.query(Pomo.timestamp, sa.func.count(Pomo.id)) \
		# 	.group_by(sa.func.date(Pomo.timestamp)).all()

		# print(count_arendators)

		# result = session.query(Arendators, func.count(Contract.id).label("count_conract")).outerjoin(Contract).group_by(
		# 	Arendators.id)

		result = {
			'status_contract': status_contract,
			'count_arendators': count_arendators,
		}

		return result
