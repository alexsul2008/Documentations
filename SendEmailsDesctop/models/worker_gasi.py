from sqlalchemy import text
from models.database import sync_engine_gasi
from models.schemas import IncGasiRel



class SyncGasiORM:
	@staticmethod
	def selectedIncident (inc_number):
		# print(ids_inc)
		# sync_engine.echo = True
		with sync_engine_gasi.connect() as conn:
			stmt = text(
				'SELECT status, cause, link, parent_inc, source FROM public."smartJoe_allinc" WHERE public."smartJoe_allinc".number_inc=:number_inc')
			stmt = stmt.bindparams(number_inc = inc_number)
			res = conn.execute(stmt)
			result = res.all()

			result_json = [IncGasiRel.model_validate(row, from_attributes = True).model_dump() for row in result]
			conn.close()
			# print(stmt.compile(compile_kwargs = {"literal_binds": True}))

			# print(f'Conn1: {conn.closed}')
		#
			return result_json
