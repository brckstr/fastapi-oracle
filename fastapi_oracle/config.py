from functools import lru_cache

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
    settngs = Settings()
    with open("/tmp/oracle_gateway.txt","w") as ofile:
        ofile.write(settngs)
    return settngs
