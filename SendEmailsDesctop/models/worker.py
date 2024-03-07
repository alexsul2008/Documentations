import json
from collections import OrderedDict

# from pydantic.deprecated.json import pydantic_encoder
from sqlalchemy import and_, insert, select, text, delete, func, column, table
# from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import joinedload, selectinload, class_mapper  # , load_only, aliased, contains_eager,


# from sqlalchemy.orm.sync import update

# from convert_csv import csvListOperatorsORM #, csvListOperators
from models.database import Base, session_factory, sync_engine, BaseGasi, sync_engine_gasi
from models.models import (
    OperatorsORM, LIST_USERS_ADMIN, UserAdminORM, LocationsORM, DPC, DPCMgmn, EmailORM, EmailRegionORM, LogInfoORM,
    IncidentsORM
)

from models.schemas import (
    OperatorsRelDTO,
    DpcsRelDTO,
    OperatorsMgmnRelDTO,
    DpcsMgmnDTO,
    DpcsMgmnRelDTO,
    EmailsRegionRelDTO,
    LogsRelDTO,
    IncidentsRelDTO
)
# from utils import find_emails_in_str


# print(f'{res=}')
# print(f'Запрос по Админам: {query.compile(compile_kwargs={"literal_binds": True})}')


def serialized (model):
    # print(*args)
    """Transforms a model into a dictionary which can be dumped to JSON."""
    # first we get the names of all the columns on your model
    columns = [c.key for c in class_mapper(model.__class__).columns]
    # then we return their values in a dict
    return dict((f"{c}", getattr(model, c)) for c in columns)
    # return dict((c, getattr(model, c)) for c in columns)






class SyncORM:
    @staticmethod
    def create_tables():
        # sync_engine.echo = False
        # Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        # BaseGasi.metadata.create_all(sync_engine_gasi)
        # sync_engine.echo = True

    # @staticmethod
    # def insert_operators():
    #     list_operators = csvListOperators()
    #     with session_factory() as session:
    #         stmt = insert(OperatorsORM).values(list_operators)
    #         session.execute(stmt)
    #         session.commit()
    #     # sync_engine.echo = True

    @staticmethod
    def insert_admins():
        list_admins = []
        for item in LIST_USERS_ADMIN:
            list_admins.append({"name": item})
        with session_factory as session:
            stmt = insert(UserAdminORM).values(list_admins)
            session.execute(stmt)
            session.commit()





    @staticmethod
    def listUsersAdminORM():
        with session_factory as session:
            # query = select(UserAdminORM.id, UserAdminORM.name).order_by(UserAdminORM.id)
            # result = session.scalars(query)
            # list_users = result.all()
            # print(f'Запрос по Админам: {query.compile(compile_kwargs={"literal_binds": True})}')
            list_users = session.scalars(select(UserAdminORM).order_by(UserAdminORM.id)).all()
            return list_users

    @staticmethod
    def addAdminORM (name: str):
        # sync_engine.echo = True
        with session_factory as session:
            try:
                stmt = session.scalars(
                    insert(UserAdminORM)
                    .values({"name": name})
                    .returning(UserAdminORM)
                )
                session.commit()
                return stmt.all()
            except:
                return False

    @staticmethod
    def deleteAdminORM (id: int):
        # sync_engine.echo = True
        with session_factory as session:
            try:
                admin = session.get(UserAdminORM, id)
                session.delete(admin)
                session.commit()
                return True
            except:
                return False


    @staticmethod
    def notEmptyOperators():
        with session_factory as session:
            res = text("""SELECT true FROM operators LIMIT 1""")
            result = session.execute(res)
            return result

    @staticmethod
    def insert_operators_ORM(list_operators, flags = False):
        # print(f'ORM_{list_operators=}')
        # sync_engine.echo = True
        # res = SyncORM.notEmptyOperators()
        with session_factory as session:
            session.execute(delete(OperatorsORM).filter(OperatorsORM.flag == flags))
            session.commit()

            for item in list_operators:
                insert_stmt = insert(OperatorsORM).values(name = item['name'], flag = flags)                    #
                insert_stmt = insert_stmt.on_conflict_do_update(
                    index_elements = [OperatorsORM.name, ],
                    index_where = OperatorsORM.name,
                    set_ = dict(
                        name = item['name'],
                    )
                )
                session.execute(insert_stmt)
            session.commit()

    @staticmethod
    def insertEmailsOperatorsORM(list_emails):
        # sync_engine.echo = True
        with session_factory as session:
            try:
                for item in list_emails:
                    oper_db = session.execute(select(OperatorsORM).filter(OperatorsORM.name.like(item['name']))).scalar_one_or_none()
                    if oper_db is None:
                        continue
                    else:
                        stmt = insert(EmailORM).values(
                            email = item['emails'],
                            operator_name = oper_db.name,
                            operator_id = int(oper_db.id))
                        stmt = stmt.on_conflict_do_update(
                            index_elements = [EmailORM.operator_name, ],
                            index_where = EmailORM.operator_name,
                            set_ = dict(
                                email = item['emails'],
                                operator_id = int(oper_db.id)
                            )
                        )
                        session.execute(stmt)
                session.commit()
                return True
            except:
                return False

    @staticmethod
    def notEmptyDPC():
        with session_factory as session:
            res = session.execute(text("SELECT True FROM dpcs LIMIT 1"))
            return res

    @staticmethod
    def uploadLocatSpInDb(list_locations):
        with session_factory as session:
            insert_stmt = insert(LocationsORM).values(list_locations)
            session.execute(insert_stmt)
            # session.flash()
            session.commit()

    @staticmethod
    def uploadSpInDb(locations_DPC):
        # sync_engine.echo = False
        with session_factory as session:
            for index, row in locations_DPC.iterrows():
                oper_csv = row['Оператор'].replace('""', '"')
                oper_db = session.scalars(select(OperatorsORM).filter(OperatorsORM.name.contains(oper_csv))).first()
                locat_csv = row['Место установки'].strip()
                locat_db = session.scalars(select(LocationsORM).filter(LocationsORM.name.contains(locat_csv))).first()

                dpc_csv = int(row['Декадный'])

                stmt = insert(DPC).values(
                    name = dpc_csv,
                    abcdef = row['АВС/ DEF'],
                    structurnii = row['Структурный'],
                    zone_obslujivaniya = row['Зона обслуживания'].strip(),
                    operator_id = int(oper_db.id),
                    location_id = int(locat_db.id))
                stmt = stmt.on_conflict_do_update(
                    index_elements = [DPC.name, ],
                    index_where = DPC.name,
                    set_ = dict(
                        no_datas = stmt.excluded.no_datas,
                        abcdef = row['АВС/ DEF'],
                        structurnii = row['Структурный'],
                        zone_obslujivaniya = row['Зона обслуживания'].strip(),
                        operator_id = int(oper_db.id),
                        location_id = int(locat_db.id)
                    )
                )
                session.execute(stmt)

            session.commit()

    @staticmethod
    def uploadDataMgmnInDbORM(data_mgmn):
        # sync_engine.echo = False
        with session_factory as session:
            for index, row in data_mgmn.iterrows():
                name_trank_csv = '{}'.format(str(row['NameTrank']).strip())
                kommutator_csv = '{}'.format(str(row['Kommutator']).strip())

                name_trank_in_bd = session.execute(select(DPCMgmn).filter(
                    and_(DPCMgmn.name_trank.like(name_trank_csv), DPCMgmn.kommutator.like(kommutator_csv)))).first()

                operator_csv = '{}'.format(str(row['AssignmentTrank']).strip())
                operator_id_sql = select(OperatorsORM.id).filter(OperatorsORM.name.like(operator_csv))
                operator_id_csv = session.scalars(operator_id_sql).first()

                if name_trank_in_bd == None:
                    if operator_csv != 'nan':
                        stmt = insert(DPCMgmn).values(
                            dpc_name = str(row['DPCIP']).strip(),
                            kommutator = str(row['Kommutator']).strip(),
                            name_trank = str(row['NameTrank']).strip(),
                            opc = str(row['OPC']).strip(),
                            region_kommutatora = str(row['RegionKommutatora']).strip(),
                            region_shluza = str(row['RegionShluza']).strip(),
                            uroven_prisoedineniya = str(row['UrovenPrisoedineniya']).strip(),
                            operator_id = operator_id_csv)
                        stmt = stmt.on_conflict_do_update(
                            index_elements = [DPCMgmn.id, ],
                            index_where = DPCMgmn.id,
                            set_ = dict(
                                dpc_name = str(row['DPCIP']).strip(),
                                kommutator = str(row['Kommutator']).strip(),
                                name_trank = str(row['NameTrank']).strip(),
                                opc = str(row['OPC']).strip(),
                                region_kommutatora = str(row['RegionKommutatora']).strip(),
                                region_shluza = str(row['RegionShluza']).strip(),
                                uroven_prisoedineniya = str(row['UrovenPrisoedineniya']).strip(),
                                operator_id = operator_id_csv
                            )
                        )
                        session.execute(stmt)
                    else:
                        continue

                # text = str(row['Primechanie']).strip()
                # if text != 'nan':
                #     try:
                #         emails = find_emails_in_str(text)
                #         for email in emails:
                #             email_exist = session.query(Email).filter(
                #                 and_(Email.email_name == email, Email.operator_id == operator_id_csv.operator_id)).first()
                #
                #             if email_exist:
                #                 continue
                #             else:
                #                 data_emails_operator_in_csv = Email(email_name = email, operator_id = operator_id_csv.operator_id)
                #                 session.add(data_emails_operator_in_csv)
                #     except MyException:
                #         session.rollback()
                # else:
                #     continue
            session.commit()

    @staticmethod
    def listAllOperatorsORM():
        with session_factory as session:
            # query = select(OperatorsORM)
            # result = session.execute(query)
            # list_operators = result.all()
            # # workers = result.scalars().all()
            # print(f"{list_operators=}")
            list_operators = session.scalars(select(OperatorsORM).order_by(OperatorsORM.flag.asc(), OperatorsORM.id.asc())).all()
            print(f"{list_operators=}")
            return list_operators

    @staticmethod
    def listSpOperatorORM(oper_id, flag_oper):
        # sync_engine.echo = True
        with session_factory as session:
            if not flag_oper:
                # query = (
                #     select(DPC.name, LocationsORM.name)
                #     .join(LocationsORM.dpcs)
                #     .where(DPC.operator_id == oper_id)
                # )
                # res = session.execute(query)
                # result = res.all()
                # print(f"{result=}")

                # query = (
                #     select(OperatorsORM, func.count(DPC.operator_id).label("count_sp"))
                #     .join(OperatorsORM.dpcs)
                #     .where(OperatorsORM.id == oper_id)
                #     .group_by(OperatorsORM)
                #     .options(selectinload(OperatorsORM.dpcs))
                # )


                query = (
                    select(OperatorsORM)
                    .where(OperatorsORM.id == oper_id)
                    .options(selectinload(OperatorsORM.dpcs))
                )
                res = session.execute(query)
                result = res.scalars().all()
                # for row in result:
                #     print(f'{row=}')

                result_json = [OperatorsRelDTO.model_validate(row, from_attributes = True).model_dump_json() for row in result]
                # print(f"Rossreestr: {result_json=}")
                return result_json

            else:
            #     query = (
            #         select(DPCMgmn.dpc_name, DPCMgmn.region_shluza, DPCMgmn.region_kommutatora, DPCMgmn.name_trank)
            #         .where(DPCMgmn.operator_id == oper_id)
            #     )
            #     res = session.execute(query)
            #     result = res.all()
            #     # print(f'Запрос из ORM: {query.compile(compile_kwargs={"literal_binds": True})}')
            #     # print(f'Запрос из ORM: {result=}')
            # return result
                query = (
                    select(OperatorsORM)
                    .where(OperatorsORM.id == oper_id)
                    .options(selectinload(OperatorsORM.dpcs_mgmn))
                )
                res = session.execute(query)
                result = res.scalars().all()

                # for row in result:
                #     print(f'{row=}')

                result_json = [OperatorsMgmnRelDTO.model_validate(row, from_attributes = True).model_dump_json(by_alias=True) for row in result]
                # print(f"{type(result_json)}")
                # print(f"MGMN: {result_json=}")
                return result_json

    @staticmethod
    def listEmailsOperatorORM(oper_id):
        # sync_engine.echo = False
        with session_factory as session:
            query = (
                select(EmailORM.name)
                .filter_by(operator_id = oper_id)
            )
            res = session.execute(query)
            result = res.all()
            return result

    @staticmethod
    def listAllSpORM(flag):
        # sync_engine.echo = True
        with session_factory as session:
            if not flag:
                query = (
                    select(DPC)
                    .options(joinedload(DPC.operators).load_only(OperatorsORM.name, OperatorsORM.flag))
                    .options(joinedload(DPC.locations).load_only(LocationsORM.name))
                    # .join_from(DPC, OperatorsORM)
                    # .join_from(DPC, LocationsORM)
                    # # .options(joinedload(DPC.operators))
                    # # .options(joinedload(DPC.locations))
                    # .options(load_only(OperatorsORM.name), load_only(OperatorsORM.flag), load_only(LocationsORM.name))
                )
                res = session.execute(query)
                result = res.all()

                result_json = [DpcsRelDTO.model_validate(row[0], from_attributes = True).model_dump() for row in result]
                return result_json
            else:
                query = (
                    select(DPCMgmn)
                    .options(joinedload(DPCMgmn.operators_mgmn).load_only(OperatorsORM.name, OperatorsORM.flag))
                )
                res = session.execute(query)
                result = res.all()

                result_json = [DpcsMgmnRelDTO.model_validate(row[0], from_attributes = True).model_dump() for row in result]
                # print(f'{result_json=}')
                return result_json

    @staticmethod
    def notEmptyRegions():
        with session_factory as session:
            res = text("""SELECT true FROM regions LIMIT 1""")
            result = session.execute(res)
            return result


    @staticmethod
    def uploadEmailsRegionORM(list_emails):
        # sync_engine.echo = True
        res = SyncORM.notEmptyRegions()
        with session_factory as session:
            try:
                if res:
                    for item in list_emails:
                        region = '{}'.format(str(item['region']).strip())
                        email = '{}'.format(str(item['email']).strip().lower())
                        stmt = insert(EmailRegionORM).values(region = region, email = email)
                        stmt = stmt.on_conflict_do_update(
                            index_elements = [EmailRegionORM.region, ],
                            index_where = EmailRegionORM.region,
                            set_ = dict(
                                region = item['region'],
                                email = item['email'],
                            )
                        )
                        session.execute(stmt)
                else:
                    stmt = insert(EmailRegionORM).values(*list_emails)
                    session.execute(stmt)
                session.commit()
                return True
            except:
                return False

    @staticmethod
    def updateEmailsOperORM (data):
        # print(f'{type(data)} --- {data=}')
        # print(f'{type(data["delete_email"])=} --- {len(data["delete_email"])=}')
        # print(f'{type(data["delete_email"]["operator_name"])=} --- {len(data["delete_email"]["operator_name"])=}')
        # print(f'{type(data["new_email"])=} ---- {len(data["new_email"])=}')
        # sync_engine.echo = True
        with session_factory as session:
            try:
                if len(data['new_email']) > 0:
                    # print(f'{len(data["new_email"])=}')
                    for item in data['new_email']:
                        # print(f'{item=}')
                        oper_db = session.execute(select(OperatorsORM).filter(OperatorsORM.name.like(item['operator_name']))).scalar_one_or_none()
                        # print(f'{oper_db.id=}')
                        if oper_db is None:
                            continue
                        else:
                            stmt = insert(EmailORM).values(
                                email = item['email'],
                                operator_name = item['operator_name'],
                                operator_id = int(oper_db.id))
                            stmt = stmt.on_conflict_do_update(
                                index_elements = [EmailORM.operator_name, ],
                                index_where = EmailORM.operator_name,
                                set_ = dict(
                                    email = item['email'],
                                    operator_id = int(oper_db.id)
                                )
                            )
                            session.execute(stmt)


                # if len(data['delete_email']["operator_name"]) > 0:
                #     # print(f'{len(data["delete_email"])=}')
                #     print(data["delete_email"]["operator_name"])
                #     deletes_operator_emails = delete(EmailORM).where(EmailORM.operator_name.in_(data["delete_email"]["operator_name"]))
                #     session.execute(deletes_operator_emails)

                session.commit()
                return True
            except:
                return False

    @staticmethod
    def listAllRegionsORM():
        # sync_engine.echo = True
        with session_factory as session:
            query = (
                select(EmailRegionORM).order_by(EmailRegionORM.region.asc())
            )
            res = session.execute(query)
            result = res.all()

        result_json = [EmailsRegionRelDTO.model_validate(row[0], from_attributes = True).model_dump() for row in result]

        # print(f'{result_json=}')

        return result_json

    @staticmethod
    def updateRegionORM (id_region: int, value: str):
        # sync_engine.echo = True
        with session_factory as session:
            try:
                session.query(EmailRegionORM).filter(EmailRegionORM.id == id_region).update({"region": value})
                session.commit()
                return True
            except AttributeError:
                print(f'Ошибка при обновлении региона: {AttributeError}')
                return False

    @staticmethod
    def updateEmailsRegionORM (dict_new_email: dict, user: str):
        # sync_engine.echo = True
        with session_factory as session:
            try:
                emails = session.get(EmailRegionORM, dict_new_email['id'])
                emails.email = str(dict_new_email['email'])
                session.commit()
                return True
            except:
                return False

    @staticmethod
    def logInfoORM (status, creator, logs):
        sync_engine.echo = True
        with session_factory as session:
            session.execute(insert(LogInfoORM).values(status = status, creator = creator, logs = logs))
            session.commit()

    @staticmethod
    def listLogsORM (filter = {}):
        # print(f'{filter=}')
        # sync_engine.echo = True

        def get_filter_by_args (dic_filter: dict):
            filters_db_logs = []
            for key, value in dic_filter.items():
                # print(f'{key}-----{value}')
                try:
                    if key == 'status':
                        if value != '':
                            filters_db_logs.append(getattr(LogInfoORM, key) == value)
                    elif key == 'creator':
                        if value != '':
                            filters_db_logs.append(getattr(LogInfoORM, key) == value)
                    elif key.startswith('date_create'):
                        key = key[:11]
                        filters_db_logs.append(getattr(LogInfoORM, key).between(value[1]["date_create__start"], value[0]["date_create__end"]))
                    else:
                        # print(f'Другие: {key}----- {value}')
                        continue
                except AttributeError:
                    continue
            return filters_db_logs

        dic_args = get_filter_by_args(filter)

        # print(*dic_args)
        with sync_engine.connect() as conn:
            query = (
                select(LogInfoORM).filter(*dic_args).order_by(LogInfoORM.date_create.asc())
            )
            res = conn.execute(query)
            result = res.all()
            conn.close()
            # for row in result:
            #     print(f'{row=}')
        result_json = [LogsRelDTO.model_validate(row, from_attributes = True).model_dump() for row in result]
        # print(f'{result_json=}')
        return result_json

    @staticmethod
    def getDataToListFromFiltersORM():
        with session_factory as session:
            query = (
                select(LogInfoORM).order_by(LogInfoORM.date_create.asc())
            )
            res = session.execute(query)
            result = res.all()
        result_json = [LogsRelDTO.model_validate(row[0], from_attributes = True).model_dump() for row in result]
        # print(f'{result_json=}')
        return result_json


    @staticmethod
    def deleteManyRowsLogsORM (ids: list):
        # sync_engine.echo = True
        with session_factory as session:
            try:
                logs = delete(LogInfoORM).where(LogInfoORM.id.in_(ids))
                session.execute(logs)
                session.commit()
                return True
            except:
                return False

    @staticmethod
    def clearLogsORM():
        with session_factory as session:
            try:
                logs = delete(LogInfoORM)
                session.execute(logs)
                session.commit()
                return True
            except:
                return False


    @staticmethod
    def serchOperatorInDpcORM(data):
        # print(f'{data=}')
        # sync_engine.echo = True
        with session_factory as session:
            if data['flag']:
                if data['current_msx'] != '':
                    query = (
                        select(DPCMgmn).filter(
                            and_(
                                DPCMgmn.name_trank == data['dpc'],
                                DPCMgmn.kommutator == data['current_msx']
                            )
                        )
                        .options(joinedload(DPCMgmn.operators_mgmn).load_only(OperatorsORM.name))
                    )
                else:
                    query = (
                        select(DPCMgmn).filter(DPCMgmn.name_trank == data['dpc'])
                        .options(joinedload(DPCMgmn.operators_mgmn).load_only(OperatorsORM.name))
                    )

                res = session.execute(query)
                result = res.unique().scalars().all()
                # print(f'{result=}')
                # print(f'Запрос по DPCMgmn: {query.compile(compile_kwargs = {"literal_binds": True})}')

                result_json = [DpcsMgmnDTO.model_validate(row, from_attributes = True).model_dump(by_alias=True) for row in result]
                # print(f'{result_json=}')
                return result_json

            else:
                # query = (
                #     select(DPC).where(DPC.name == int(data['dpc']))
                #     .options(joinedload(DPC.operators).load_only(OperatorsORM.name))
                #     .options(joinedload(DPC.locations).load_only(LocationsORM.name))
                # )
                # subq = (
                #     select(EmailORM.id.label("email_oper_id"))
                #     .filter(EmailORM.operator_id == OperatorsORM.id)
                #     .order_by(EmailORM.id.desc())
                #     .limit(1)
                #     .scalar_subquery()
                #     .correlate(OperatorsORM)
                # )
                # query = (
                #     select(DPC).where(DPC.name == int(data['dpc']))
                #     .outerjoin(DPC.operators)
                #     .outerjoin(EmailORM, EmailORM.id == subq)  # use the JOIN which includes ONLY last Goal, but ...
                #     .outerjoin(DPC.locations)
                #     .options(contains_eager(
                #         DPC.operators,
                #         OperatorsORM.emails,  # ... tell sqlalchemy that we actually loaded ALL `.goals`
                #         # DPC.locations,
                #     ))
                # )

                query = (
                    select(DPC).where(DPC.name == int(data['dpc']))
                    .options(joinedload(DPC.operators).load_only(OperatorsORM.name))
                    .options(joinedload(DPC.locations).load_only(LocationsORM.name))
                )

                res = session.execute(query)
                result = res.unique().scalars().all()

                result_json = [DpcsRelDTO.model_validate(row, from_attributes = True).model_dump() for row in result]
                return result_json

    @staticmethod
    def serchRegionsInOpcORM (data):
        # print(f'{data=}')
        # sync_engine.echo = True
        with session_factory as session:
            if data['flag']:
                query = (
                    select(EmailRegionORM.email)
                    .filter(EmailRegionORM.region.contains(data['opc']))
                )
                region_email = session.execute(query).scalar_one_or_none()
                # print(f'{region_email=}')
                return region_email

            else:
                query = (
                    select(DPC).where(DPC.name == int(data['opc']))
                )

                res = session.execute(query) #.scalar_one_or_none()
                result = res.unique().scalars().all()
                # result = res.scalar_one_or_none()

                result_json = [DpcsRelDTO.model_validate(row, from_attributes = True).model_dump() for row in result]

                # print(f'{result_json=}')

                region = result_json[0]['zone_obslujivaniya']#[:-1] #.split('|')

                if int(data['opc']) in (6940, 6214):
                    region = result_json[0]['locations']['name'].split('|')[0]
                elif int(data['opc']) in (14445, 14446):
                    region = 'ЯНАО'
                elif int(data['opc']) in (7445, 7444):
                    region = 'ХМАО'
                elif int(data['opc']) in (8995,):
                    region = 'Новосибирская обл.'

                if region.endswith('.'):
                    region = region[:-1]

                query = (
                    select(EmailRegionORM.email)
                    .filter(EmailRegionORM.region.contains(region)).limit(1)
                )
                region_email = session.execute(query).scalar_one_or_none()

                return region_email


    @staticmethod
    def saveIncidentORM (data):
        # print(f'{data=}')
        # sync_engine.echo = True
        with session_factory as session:
            inc_db = session.execute(select(IncidentsORM).filter(IncidentsORM.name.contains(data['name']))).scalar_one_or_none()
            if inc_db is None:
                try:
                    session.execute(insert(IncidentsORM).values(**data))
                    session.commit()
                except:
                    # pass
                    print('Ошибка')



    @staticmethod
    def uploadEmailsFromDbORM():
        with session_factory as session:
            result = session.execute(select(EmailORM.operator_name, EmailORM.email).select_from(EmailORM)).all()
            serialized_labels = [row._asdict() for row in result]

            # serialized_labels = [
            #     serialized(label)
            #     for label in session.query(EmailORM)
            # ]
            # result_json = json.dumps(serialized_labels, ensure_ascii=False) #, indent=2) #.encode('utf8')

            # serialized_labels = session.execute(select(EmailORM).with_only_columns(EmailORM.operator_name, EmailORM.email)).all()
            # result = session.query(EmailORM.operator_name, EmailORM.email).mappings().all()
            # result = session.execute(select(EmailORM.operator_name, EmailORM.email).select_from(EmailORM)).mappings().all()

            # print(serialized_labels)
            #
            # columns = [c.key for c in class_mapper(EmailORM.operator_name).columns]
            # for label in session.query(EmailORM):
            #     columns = [c.key for c in class_mapper(label.__class__).columns]
            #
            #     print(f'{columns=}')
            # return result_json

            return serialized_labels

    @staticmethod
    def loadGeneralStatisticsORM ():
        # sync_engine.echo = True
        with sync_engine.begin() as connection:
            count_users = connection.execute(select(func.count(LogInfoORM.creator.distinct()).label("count_users"))).scalar()
            all_info_operators = connection.execute(
                select(
                    func.count(), #.label("count_operators"),
                    func.count(OperatorsORM.emails), #.label("count_operators_emails")
                ).outerjoin(OperatorsORM.emails)
            ).all()
            total_inc = connection.execute(select(func.count(IncidentsORM.id).label("count_inc"))).scalar()
            # print(f'{all_info_operators[0]=}')
            data_stat = {
                "count_users": count_users,
                "total_inc": total_inc,
                "operators_info": {
                    "count_operators": all_info_operators[0][0],
                    "count_operators_emails": all_info_operators[0][1]
                }
            }
            return data_stat

    @staticmethod
    def listAllIncidentsORM (sorting):
        def get_sort_by_args (str_sorting: str):
            try:
                if str_sorting == 'name__down':
                    key = 'name'
                    return getattr(IncidentsORM, key).desc()
                elif str_sorting == 'name__up':
                    key = 'name'
                    return getattr(IncidentsORM, key).asc()
                elif str_sorting == 'date__down':
                    key = 'date_send'
                    return getattr(IncidentsORM, key).desc()
                elif str_sorting == 'date__up':
                    key = 'date_send'
                    return getattr(IncidentsORM, key).asc()
            except AttributeError:
                print(f'Ошибка при сортировке инц: {AttributeError}')
            return text('')

        str_args = get_sort_by_args(sorting)
        # sync_engine.echo = True
        with session_factory as session:
        # with sync_engine.begin() as connection:
            # query = (
            #     select(IncidentsORM).order_by(str_args)
            # )
            # res = session.execute(query)
            res = session.execute(select(IncidentsORM).order_by(str_args))
            # res = connection.execute(select(IncidentsORM).order_by(str_args))
            result = res.unique().scalars().all()
            # result = res.unique().all()

            # for row in result:
            #     print(f'{row=}')

            result_json = [IncidentsRelDTO.model_validate(row, from_attributes = True).model_dump() for row in result]

        # print(f'{result_json=}')
        return result_json

    @staticmethod
    def deleteSelectedIncident (ids_inc):
        # print(ids_inc)
        # sync_engine.echo = True
        with session_factory as session:
            try:
                delete_incidetnts = delete(IncidentsORM).where(IncidentsORM.id.in_(ids_inc))
                session.execute(delete_incidetnts)
                session.commit()
                return True
            except:
                return False





