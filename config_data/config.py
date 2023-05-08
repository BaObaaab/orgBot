from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    token: SecretStr
    skip_updates: bool
    admin_chat: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()