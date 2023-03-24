from functools import lru_cache
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str = "127.0.0.1"
    db_port: int = 1521
    db_user: str = "dbuser"
    db_password: str = "dbpassword"  # nosemgrep
    db_service_name: str = "dbservicename"
    db_dsn: str = "aatest_high"
    db_conn_ttl: int = None


@lru_cache()
def get_settings() -> Settings:  # pragma: no cover
    """Get settings for fastapi-oracle.

    A settings object is only created once, per FastAPI recommended practice, so that
    values are only read from potentially expensive-to-read sources once. Subsequent
    calls to this function are cached.

    Suitable for use as a FastAPI path operation with depends().
    """
    with open("/tmp/env.txt","w") as ofile:
        ofile.write("DB_USER: %s\n" % os.environ.get("DB_USER", "Null"))
        ofile.write("DB_PASSWORD: %s\n" % os.environ.get("DB_PASSWORD", "Null"))
        ofile.write("DB_DSN: %s\n" % os.environ.get("DB_DSN", "Null"))               
    return Settings()
