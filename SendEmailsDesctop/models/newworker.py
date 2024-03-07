# # import datetime
#
# # from itertools import count
# from datetime import datetime
#
# from sqlalchemy import and_, or_, asc, delete, insert, desc #, select, literal
# from sqlalchemy.orm import Session as SQLSession
#
# # from sqlalchemy.orm import Session
# from sqlalchemy.orm.sync import update
# # from models.models import Session, operator_location, Operator, Email, Location, DPC, Incident, DPCMgmn, UserAdmin, \
# # 	LogInfo, EmailsRegion
# # from models.models import operator_location, Operator, Email, Location, DPC, Incident
#
# from utils import find_emails_in_str
#
#
# class MyException(Exception):
# 	pass
#
#
# class someClass:
# 	def __init__ (self, list):
# 		self.list = list
#
# 	def __iter__ (self):
# 		for x in self.list:
# 			yield x
#
#
#
#
# class Worker:
# 	# Выборка всех операторов
# 	def listAllOperators(self):
# 		list_operators = []
# 		session: SQLSession = Session()
# 		operators = session.query(Operator)
# 		session.close()
# 		for item in operators:
# 			list_operators.append(item)
# 		print(f'Operators: {list_operators}')
# 		return list_operators
#
# 	# Выборка всех регионов
# 	def listAllRegions(self):
# 		session: SQLSession = Session()
# 		list_regions = session.query(EmailsRegion).order_by(asc(EmailsRegion.region))
# 		session.close()
# 		return list_regions
#
# 	# Выборка всех записанных e-mail у операторов
# 	def listEmailsOperator(self, id):
# 		# print('ID Operator: ', id)
# 		session: SQLSession = Session()
# 		# session = Session()
# 		list_emails_operators = session.query(Email.email_id, Email.email_name).filter(Email.operator_id == id)
# 		# print(list_emails_operators)
# 		session.close()
# 		return list(list_emails_operators)
#
# 	# Выборка всех записанных e-mail у операторов
# 	def listEmailsRegion (self, id):
# 		session: SQLSession = Session()
# 		list_emails_regions = session.query(EmailsRegion.id, EmailsRegion.email).filter(EmailsRegion.id == id)
# 		session.close()
# 		return list(list_emails_regions)
#
#
# 	def getEmailsRegion(self, region=None):
#
# 		search_region = region.split()
# 		# print('Len: ', len(search_region))
#
# 		if len(search_region) > 1 and search_region[-1].startswith('обл'):
# 			search_region = search_region[0]
# 		elif len(search_region) != 1 and 'Адыгея' in search_region:
# 			search_region = 'Адыгея'
# 		elif len(search_region) != 1 and (search_region[0].startswith('Республ') or search_region[-1].startswith('край')):
# 			search_region = ' '.join(search_region)
# 		elif len(search_region) != 1 and search_region[-1].startswith('Москва'):
# 			search_region = search_region[-1]
# 		elif len(search_region) != 1 and 'Санкт-Петербург' in search_region:
# 			search_region = 'Ленинградская'
# 		elif len(search_region) != 1 and 'Югра' in search_region:
# 			search_region = 'ХМАО'
# 		elif len(search_region) != 1 and 'Ямало-Ненецкий' in search_region:
# 			search_region = 'ЯНАО'
# 		elif len(search_region) != 1 and 'Чувашия' in search_region:
# 			search_region = 'Чувашия'
# 		elif len(search_region) != 1 and 'Чукотский' in search_region:
# 			search_region = 'Чукотский'
#
#
# 		# print('Search_Region: ', search_region)
#
# 		search = "%{}%".format(search_region)
#
# 		session: SQLSession = Session()
# 		emails_region = session.query(EmailsRegion.email).filter(EmailsRegion.region.like(search)).first()
# 		print(emails_region)
# 		session.close()
#
#
#
# 		return emails_region if emails_region else None
#
#
# 	def updateRegion (self, id_region, value: str):
# 		print(f'Worker: {id_region} , {value}')
# 		value_region = str(value).strip()
# 		session: SQLSession = Session()
# 		# update_region = update(EmailsRegion).where(EmailsRegion.id == id_region).values({'region': value_region}).execution_options(synchronize_session = False)
# 		# session.execute(update_region)
# 		# session.execute(update(EmailsRegion.region).where(EmailsRegion.id == id_region).values({'region': value_region}))
# 		try:
# 			session.query(EmailsRegion).filter(EmailsRegion.id == id_region).update({'region': value_region})
# 			session.commit()
# 			session.close()
# 			return True
# 		except AttributeError:
# 			session.rollback()
# 			return False
# 		finally:
# 			session.close()
#
#
#
#
# 	# Выборка всех SP оператора
# 	def listSpOperator (self, id):
# 		# print('ID Operator: ', id)
# 		session: SQLSession = Session()
# 		flag_oper = session.query(Operator).get(id)
# 		print(flag_oper)
# 		if flag_oper.flag == False:
# 			list_sp_operator = session.query(DPC.dpc_name, Location.location_name). \
# 						filter(and_((DPC.location_id == Location.location_id), DPC.operator_id == id))
# 		else:
# 			list_sp_operator = session.query(DPCMgmn.dpc_name, DPCMgmn.region_kommutatora, DPCMgmn.name_trank).filter(DPCMgmn.operator_id == id)
# 		# list_sp_operator = session.query(DPC.dpc_name, DPC.location_id).filter(DPC.operator_id == id)
# 		session.close()
# 		# print(list(list_sp_operator))
# 		# for i in list_sp_operator:
# 		# 	print(i)
# 		return list_sp_operator, flag_oper.flag
#
# 		# Выборка всех SP
# 	def listAllSp (self, flag):
#
# 		session: SQLSession = Session()
# 		list_sp = []
# 		if flag:
# 			data_sp = session.query(DPCMgmn).outerjoin(DPCMgmn.operators_mgmn).all()
# 			# print(data_sp)
# 			for val in range(len(data_sp)):
# 				data_item = [data_sp[val].dpc_id, data_sp[val].kommutator, data_sp[val].name_trank,
# 							 data_sp[val].dpc_name, data_sp[val].opc,
# 							 data_sp[val].operators_mgmn.operator_name, data_sp[val].region_kommutatora,
# 							 data_sp[val].region_shluza, data_sp[val].uroven_prisoedineniya,
# 							 data_sp[val].operator_id]
# 				list_sp.append(data_item)
# 		else:
# 			# print(flag)
# 		# data_sp = session.query(DPC).join(DPC.operators).join(DPC.locations)[:10]
# 			data_sp = session.query(DPC).outerjoin(DPC.operators).outerjoin(DPC.locations).all()
# 			# data_sp = session.query(DPC, Operator, Location).select_from(DPC).join(Operator).join(Location)[:10]
#
# 			for val in range(len(data_sp)):
# 				data_item = [data_sp[val].dpc_id, data_sp[val].abcdef, data_sp[val].structurnii, data_sp[val].dpc_name,
# 						 data_sp[val].operators.operator_name,
# 						 data_sp[val].zone_obslujivaniya, data_sp[val].locations.location_name, data_sp[val].operator_id,
# 						 data_sp[val].location_id]
# 				list_sp.append(data_item)
#
# 		session.close()
# 		return list_sp
#
# 	def saveOrUpdateOperator(self, list_operators, flags: bool):
# 		#
# 		# print(len(list_operators))
# 		# print(list_operators)
#
# 		session: SQLSession = Session()
# 		try:
# 			# add_operarors = [Operator(operator_name = item) for item in list_operators]
# 			for item in list_operators:
# 				item = item.replace('""', '"')
# 				select_oper = session.query(Operator.operator_id).filter_by(operator_name = item).first()
# 				if select_oper == None:
# 					oper = Operator(item, flags)
# 					# print(oper.operator_name)
# 					session.add(oper)
# 				else:
# 					continue
# 			session.commit()
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
# 	def uploadSpInDb(groups_sp, locations, locations_DPC):
# 		session: SQLSession = Session()
# 		try:
# 			for index, row in locations.iterrows():
# 				loc_csv = '{}'.format(row[0])
# 				location_csv = session.query(Location).filter_by(location_name = loc_csv).first()
# 				if location_csv:
# 					continue
# 				else:
# 					location_oper = Location(location_name=row[0].strip())
# 					session.add(location_oper)
# 			session.commit()
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
# 		session: SQLSession = Session()
# 		try:
# 			for index, row in groups_sp.iterrows():
# 				oper_csv = "%{}%".format(row['Оператор'].replace('""', '"'))
# 				oper_db = session.query(Operator).filter(Operator.operator_name.like(oper_csv)).first()
# 				if oper_db.operator_id:
# 					for dpc in row['Декадный'].split(','):
# 						dpc_db = session.query(DPC.dpc_name).filter(DPC.dpc_name == dpc).first()
# 						# print(dpc_db)
# 						if dpc_db is None:
# 							dpc_oper = DPC(dpc_name=dpc.strip(), operator_id=int(oper_db.operator_id), location_id = 0, abcdef = 0, structurnii = 0, zone_obslujivaniya = 0)
# 							session.add(dpc_oper)
# 						else:
# 							continue
# 				else:
# 					# print('Not Oper ID ', oper_db, 'Operator: ', oper_csv)
# 					continue
# 			session.commit()
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
#
# 		session: SQLSession = Session()
# 		try:
# 			for index, row in locations_DPC.iterrows():
# 				# dpc_operator = session.query(DPC).filter(DPC.dpc_name == row['Декадный']).first()
# 				# dpc_id_location = session.query(Location).filter(Location.location_name == row['Место установки']).first()
# 				# dpc_operator.location_id = dpc_id_location.location_id
#
# 				dpc_id_location = session.query(Location).filter(Location.location_name == row['Место установки']).first()
# 				session.query(DPC).filter(DPC.dpc_name == row['Декадный']). \
# 					update({'location_id': dpc_id_location.location_id, 'abcdef': str(row['АВС/ DEF']).strip(), 'structurnii': str(row['Структурный']).strip(), 'zone_obslujivaniya': str(row['Зона обслуживания']).strip()}, synchronize_session = 'fetch')
#
#
# 				# session.query(DPC).filter(DPC.dpc_name == row['Декадный']).update({'location_id': (session.query(Location.location_id).filter(Location.location_name == row['Место установки']))}, synchronize_session='fetch')
# 				# dpc_location = dpc_operator.update(dpc_operator, values = {dpc_operator.location_id: dpc_id_location.location_id})
# 				# installation_location = session.query(Location).filter(Location.location_name == row['Место установки']).first()
# 			session.commit()
# 			# print('Количество строк: ', len(locations_DPC))
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
# 	# Запись/обновление e-mail оператора
# 	def saveOrUpdateEmail(self, list_new_email, id_operator, user):
# 		# print('list_new_email: ', list_new_email, 'id_operator : ', id_operator)
# 		session: SQLSession = Session()
# 		# session = Session()
# 		try:
# 			for item in list_new_email:
# 				if item['id_email'] != '':
# 					id_em = int(item['id_email'])
# 					up_em = session.query(Email).get(id_em)
# 					up_em.email_name = item['email']
# 					# print('Old email: ', item['email'])
# 				else:
# 					id_op = int(id_operator)
# 					id_oper = session.query(Operator).filter_by(operator_id=id_op).first()
# 					# email_exists = session.query(Email).filter(and_((Email.email_name == item['email']), (Email.operator_id == id_oper.operator_id))).first()
# 					email_exists = session.query(Email).filter(and_((Email.email_name == item['email']), (Email.operator_id == id_operator))).first()
# 					if email_exists != None:
# 						continue
# 					else:
# 						# email = Email(item['email'], id_oper.operator_id)
# 						email = Email(item['email'], id_operator)
# 						session.add(email)
# 						task_add = f"Add email : {item['email']} for operator: {id_oper.operator_name}"
# 						log = insert(LogInfo).values(created = user, logs = task_add, date_create = datetime.now()).execution_options(synchronize_session = "fetch")
# 						# session.add(log)
# 						session.execute(log)
# 						session.commit()
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
# 	# Запись/обновление e-mail регионов
# 	def saveOrUpdateEmailRegion (self, list_new_email, id_region, user):
# 		# print('list_new_email: ', list_new_email, 'id_region : ', id_region, 'User: ', user)
# 		session: SQLSession = Session()
# 		# # session = Session()
# 		try:
# 			if list_new_email:
# 				id_em = int(id_region)
# 				up_em = session.query(EmailsRegion).get(id_em)
# 				up_em.email = ';'.join(list_new_email)
#
# 			session.commit()
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
# 	def deleteEmailOperator(self, id_email, user):
# 		session: SQLSession = Session()
# 		email_all = session.query(Email).filter_by(email_id = id_email).first()
# 		try:
# 			email_oper = delete(Email).where(Email.email_id == id_email).execution_options(synchronize_session = "fetch")
# 			session.execute(email_oper)
# 			task_delete = f"Delete email: {email_all.email_name} for operator: {email_all.operators_emails.operator_name}"
# 			log = LogInfo(created = user, logs = task_delete, date_create = datetime.now())
# 			session.add(log)
# 			session.commit()
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
#
# 	def deleteEmailRegion(self, region_id, email, user):
# 		session: SQLSession = Session()
# 		try:
# 			region_info = session.query(EmailsRegion).get(region_id)
# 			# print('Region: ', region_id, 'Name: ', region_info.region, ' Его e-mails: ', region_info.email)
#
# 			email_delete = region_info.email
# 			# преобразовываем строку в список
# 			email_delete = email_delete.split(';')
#
# 			# удаляем email из списка
# 			email_delete.remove(email)
# 			# преобразовываем список в строку
# 			email_delete = ';'.join(email_delete)
#
# 			# обновляем выбранный регион новой строкой с email-ми
# 			region_info.email = email_delete
#
# 			task_delete = f"Delete email: {email} for Region: {region_info.region}"
# 			log = LogInfo(created = user, logs = task_delete, date_create = datetime.now())
# 			session.add(log)
#
# 			session.commit()
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
#
# 	# Выборка данных по оператору для формирования письма
# 	def serchOperatorInDPC (self, dpc, flag, current_text_cb):
# 		# print('Flag in BD : ', flag)
# 		# print('Current_text_cb : ', current_text_cb)
# 		session: SQLSession = Session()
# 		if flag == True:
# 			operator = session.query(DPCMgmn.dpc_name, Operator.operator_id, Operator.operator_name, DPCMgmn.opc, DPCMgmn.region_kommutatora, DPCMgmn.region_shluza). \
# 				filter(and_((DPCMgmn.operator_id == Operator.operator_id), DPCMgmn.kommutator == current_text_cb, or_(DPCMgmn.name_trank == dpc, DPCMgmn.dpc_name == dpc)))
# 			# [('2-4192', '2-3729', 'Чебоксары', 'Чебоксары', 49, 'MVNO Тинькофф Мобайл (СПС Теле-2)')]
# 		else:
# 			operator = session.query(DPC.dpc_name, Operator.operator_id, Operator.operator_name,
# 									 Location.location_name). \
# 				filter(and_((DPC.operator_id == Operator.operator_id), (DPC.location_id == Location.location_id),
# 							DPC.dpc_name == dpc))
#
# 		session.close()
# 		# print('Выгрузка из БД: ', list(operator))
# 		list_oper = {}
# 		for item in operator:
# 			session: SQLSession = Session()
# 			emails_oper = [i.email_name for i in session.query(Email).join(Operator, Email.operator_id == item[1])]
# 			session.close()
# 			list_emails = "; ".join(map(str, emails_oper))
#
# 			if flag == True:
# 				list_oper = {
# 					'flag': True,
# 					'dpc': item[0],
# 					'operator_id': item[1],
# 					'operator_name': item[2],
# 					'opc': item[3],
# 					'region_kommutatora': item[4],
# 					'region_shluza': item[5],
# 					'operator_emails': list_emails,
# 				}
# 			else:
# 				list_oper = {
# 					'flag': False,
# 					'dpc': item[0],
# 					'operator_id': item[1],
# 					'operator_name': item[2],
# 					'operator_location': item[3],
# 					'operator_emails': list_emails,
# 				}
# 		# print(list_oper)
# 		return list_oper
#
# 	# Географическое расположение оператора
# 	# def listOperatorLocation (self):
# 	# 	session: SQLSession = Session()
# 	# 	# session = Session()
# 	# 	list_operators_location = session.query(Location)
# 	# 	session.close()
# 	# 	return list_operators_location
#
#
# 	# Сохраняем номер Инцидента в БД
# 	def saveIncident(self, inc, operatorId):
# 		oper_inc = "{}".format(inc)
# 		session: SQLSession = Session()
# 		inc_exist = session.query(Incident).filter(Incident.incident_name.like(oper_inc)).first()
# 		# print(inc_exist)
# 		if inc_exist == None:
# 			try:
# 				new_inc = Incident(oper_inc, operatorId)
# 				session.add(new_inc)
# 				session.commit()
# 			except MyException:
# 				session.rollback()
# 			finally:
# 				session.close()
#
# 	def uploadDataMgmnInDb (data_mgmn):
# 		session: SQLSession = Session()
# 		try:
# 			for index, row in data_mgmn.iterrows():
#
# 				name_trank_csv = '{}'.format(str(row['NameTrank']).strip())
# 				kommutator_csv = '{}'.format(str(row['Kommutator']).strip())
#
# 				name_trank_in_bd = session.query(DPCMgmn).filter(
# 					and_(DPCMgmn.name_trank.like(name_trank_csv), DPCMgmn.kommutator.like(kommutator_csv))).first()
#
# 				operator_csv = '{}'.format(str(row['AssignmentTrank']).strip())
# 				operator_id_csv = session.query(Operator).filter(Operator.operator_name.like(operator_csv)).first()
#
# 				if name_trank_in_bd == None:
# 					if operator_csv != 'nan':
# 						# print('Operator ID: ', operator_id_csv.operator_id)
# 						data_oper_csv = DPCMgmn(dpc_name = str(row['DPCIP']).strip(), kommutator = str(row['Kommutator']).strip(),
# 										name_trank = str(row['NameTrank']).strip(), opc = str(row['OPC']).strip(),
# 										region_kommutatora = str(row['RegionKommutatora']).strip(),
# 										region_shluza = str(row['RegionShluza']).strip(),
# 										uroven_prisoedineniya = str(row['UrovenPrisoedineniya']).strip(),
# 										operator_id = operator_id_csv.operator_id)
# 						session.add(data_oper_csv)
# 					else:
# 						continue
# 				else:
# 					continue
#
# 				text = str(row['Primechanie']).strip()
# 				if text != 'nan':
# 					try:
# 						emails = find_emails_in_str(text)
# 						for email in emails:
# 							email_exist = session.query(Email).filter(and_(Email.email_name == email, Email.operator_id == operator_id_csv.operator_id)).first()
#
# 							if email_exist:
# 								continue
# 							else:
# 								data_emails_operator_in_csv = Email(email_name = email, operator_id = operator_id_csv.operator_id)
# 								session.add(data_emails_operator_in_csv)
# 					except MyException:
# 						session.rollback()
# 				else:
# 					continue
#
# 			session.commit()
# 		except MyException:
# 			session.rollback()
# 		finally:
# 			session.close()
#
#
# 	def uploadEmailsFromDb(self):
# 		list_emails = []
# 		session: SQLSession = Session()
# 		all_emails = session.query(Email).outerjoin(Email.operators_emails).all()
# 		for val in range(len(all_emails)):
# 			data_item = [all_emails[val].email_name, all_emails[val].operators_emails.operator_name]
# 			list_emails.append(data_item)
# 		session.close()
# 		return list_emails
#
#
# 	def downloadEmailsFromCsv (data_emails):
# 		session: SQLSession = Session()
# 		for index, row in data_emails.iterrows():
# 			# print('Index: ', index, 'Operator : ', row['Operator'], 'Emails :', row['Email'])
# 			operator_csv = '{}'.format(str(row['Operator']).strip())
# 			operator_id = session.query(Operator.operator_id).filter(Operator.operator_name.like(operator_csv)).order_by(asc(Operator.operator_id)).limit(1).scalar()
# 			# operator_id = session.query(Operator.operator_id).filter(Operator.operator_name.like(operator_csv)).order_by(asc(Operator.operator_id)).first()[0]
# 			# print(operator_id)
# 			try:
# 				for email in row['Email'].split(','):
# 					# print(email.strip())
# 					email_exist = session.query(Email.email_id).filter(
# 						and_(Email.email_name == email, Email.operator_id == operator_id)).limit(1).scalar()
# 					# print(email_exist)
# 					if email_exist != None:
# 						continue
# 					else:
# 						email_operator = Email(email_name = email.strip(), operator_id = operator_id)
# 						# print(email_operator)
# 						session.add(email_operator)
# 			except MyException:
# 				session.rollback()
# 		session.commit()
# 		session.close()
#
#
# 	def downloadEmailsRegionFromCsv (data_emails):
# 		session: SQLSession = Session()
# 		flag = True
# 		try:
# 			for index, row in data_emails.iterrows():
# 				# print('Index: ', index, 'Region : ', row[0], 'Email :', row[1])
# 				region_excel = '{}'.format(str(row[0]).strip())
# 				region_id = session.query(EmailsRegion.id).filter(EmailsRegion.region.like(region_excel)).limit(1).scalar()
#
# 				if region_id != None:
# 					continue
# 				else:
# 					email_region = EmailsRegion(region = region_excel, email = row[1].strip())
# 					session.add(email_region)
#
# 			session.commit()
# 		except MyException:
# 			session.rollback()
# 			flag = False
# 		finally:
# 			session.close()
# 		return flag
#
#
# 	def listUsersAdmin(self):
# 		list_admins = []
# 		session: SQLSession = Session()
# 		list_users = session.query(UserAdmin.user_id, UserAdmin.user_name).all()
# 		session.close()
# 		return list_users
#
# 	def addAdmin(name):
# 		# print(f'{name=}')
# 		session: SQLSession = Session()
# 		try:
# 			admin = UserAdmin(user_name = name)
# 			session.add(admin)
# 			session.commit()
# 			session.close()
# 			return True
# 		except NameError:
# 			session.rollback()
# 			session.close()
# 			return False
#
# 	def deleteAdmin(id):
# 		print(f'{id=}')
# 		session: SQLSession = Session()
# 		try:
# 			admin = session.query(UserAdmin).get(id)
# 			session.delete(admin)
# 			session.commit()
# 			session.close()
# 			return True
# 		except TypeError:
# 			session.rollback()
# 			session.close()
# 			return False
#
#
# 	def log_in_db(user, log_tiket):
# 		session: SQLSession = Session()
# 		log = LogInfo(created = user, logs = log_tiket)
# 		session.add(log)
# 		session.commit()
# 		session.close()
#
#
# 	def listLogs(self):
# 		list_logs = []
# 		session: SQLSession = Session()
# 		data_logs = session.query(LogInfo).order_by(desc(LogInfo.log_id)).all()
# 		for val in range(len(data_logs)):
# 			data_item = [data_logs[val].log_id, data_logs[val].created, data_logs[val].logs, data_logs[val].date_create] #.strftime("%d-%m-%Y %H:%M:%S")]
# 			list_logs.append(data_item)
# 		session.close()
# 		return list_logs
#
# 	def deleteRowLogs(self, id_row):
# 		session: SQLSession = Session()
# 		try:
# 			log_info = session.query(LogInfo).get(id_row)
#
# 			session.delete(log_info)
# 			session.commit()
# 			session.close()
# 			return True
# 		except MyException:
# 			session.rollback()
# 			session.close()
# 			return False
#
#
#
#
#
#
#
#
#
#
#
