from functools import lru_cache
import os

from pydantic import BaseModel, BaseSettings

class CollectionModel(BaseModel):
    collection: str = None

class DBNModel(BaseModel):
    db_host: str = "127.0.0.1"
    db_port: int = 1521
    db_user: str = "dbuser"
    db_password: str = "dbpassword"  # nosemgrep
    db_service_name: str = "dbservicename"
    db_dsn: str | None = None
    db_conn_ttl: int | None = None
    db_wait_timeout_secs: int | None = None


class Settings(BaseSettings):
    dbsettings: dict[str, DBNModel]

    class Config:
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name == 'dbsettings':
                return { k: DBNModel(**v) for (k, v) in cls.json_loads(raw_val).items()}
            return cls.json_loads(raw_val)


@lru_cache()
def get_settings() -> Settings:  # pragma: no cover
    """Get settings for fastapi-oracle.

    A settings object is only created once, per FastAPI recommended practice, so that
    values are only read from potentially expensive-to-read sources once. Subsequent
    calls to this function are cached.

    Suitable for use as a FastAPI path operation with depends().
    """
              
    return Settings()
