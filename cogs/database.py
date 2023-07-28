from __future__ import annotations
import pymysql
import bot
import asyncio
import dataclasses
import inspect
import logging
from dataclasses import dataclass
from typing import (
    List,
    Any,
    Iterable,
    Optional,
    TYPE_CHECKING,
    Union,
    Tuple,
    Callable,
    Dict,
    Coroutine,
)

class Database:
    connection = pymysql.connect(host=bot.DBLINK,
                             user=bot.DBUNAME,
                             password=bot.DBUPASS,
                             database=bot.DBNAME,
                             cursorclass=pymysql.cursors.DictCursor,
                             charset='utf8')

def setup(bot):
    #bot.add_cog(AdministrationCMD(bot))
    print("Database loaded")