from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    USER_DB: str
    PASSWORD_DB: str
    HOST_DB: str
    PORT_DB: str
    DATABASE: str
    SECRET_KEY: str
    ALGORITHM: str
    EMAIL_TEST_USER: str | None = None
    PASSWORD_TEST_USER: str | None = None
    JWT_ISSUER: str
    JWT_AUDIENCE: str


settings = Settings()  # type: ignore

print(settings.SECRET_KEY)  # type: ignore
print(settings.DATABASE)  # type: ignore
print(settings.USER_DB)  # type: ignore
print(settings.PASSWORD_DB)  # type: ignore
print(settings.HOST_DB)  # type: ignore
print(settings.PORT_DB)  # type: ignore
print(settings.ALGORITHM)  # type: ignore
print(settings.JWT_ISSUER)  # type: ignore
print(settings.JWT_AUDIENCE)  # type: ignore
