# from pydantic_settings import BaseSettings, SettingsConfigDict



# class Settings(BaseSettings):
	# DB_HOST: str
	# DB_PORT: int
	# DB_USER: str
	# DB_PASS: str
	# DB_NAME: str
class Settings:
	DB_HOST_1='10.10.110.110'
	DB_PORT_1=5433
	DB_USER_1='sendemails'
	DB_PASS_1='sendemails'
	DB_NAME_1='sendemails'

	DB_HOST_2 = '10.10.110.111'
	DB_PORT_2 = 5432
	DB_USER_2 = 'sendemails'
	DB_PASS_2 = 'sendemails'
	DB_NAME_2 = 'sendemails'


	@property
	def DATABASE_URL_gasi(self):
		# postgresql+asyncpg://postgres:postgres@localhost:5432/sa
		return f"postgresql+psycopg://{self.DB_USER_2}:{self.DB_PASS_2}@{self.DB_HOST_2}:{self.DB_PORT_2}/{self.DB_NAME_2}"

	@property
	def DATABASE_URL_psycopg(self):
		# DSN
		# postgresql+psycopg://postgres:postgres@localhost:5432/sa
		return f"postgresql+psycopg://{self.DB_USER_1}:{self.DB_PASS_1}@{self.DB_HOST_1}:{self.DB_PORT_1}/{self.DB_NAME_1}"

	# model_config = SettingsConfigDict(env_file = ".env")


settings = Settings()