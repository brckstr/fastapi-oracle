import re
from typing import NamedTuple

from cx_Oracle_async.connections import AsyncConnectionWrapper
from cx_Oracle_async.cursors import AsyncCursorWrapper
from cx_Oracle_async.pools import AsyncPoolWrapper


class DbPoolAndConn(NamedTuple):
    pool: AsyncPoolWrapper
    conn: AsyncConnectionWrapper


class DbPoolConnAndCursor(NamedTuple):
    pool: AsyncPoolWrapper
    conn: AsyncConnectionWrapper
    cursor: AsyncCursorWrapper


class DbPoolKey(NamedTuple):
    db_host: str
    db_port: int
    db_user: str
    db_service_name: str
        
        
class DbPoolKey2(NamedTuple):
    db_user: str
    db_dsn: str


class DbPoolAndCreatedTime(NamedTuple):
    pool: AsyncPoolWrapper
    created_time: float


DEFAULT_MAX_ROWS = 1000

# Thanks to: https://stackoverflow.com/a/1176023/2066849
CAMEL_TO_SNAKE_REGEX = re.compile(r"(?<!^)(?=[A-Z])")

PACKAGE_STATE_INVALIDATED_REGEX = re.compile(
    r'existing state of package body "[^"]+" has been invalidated'
)
