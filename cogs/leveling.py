from __future__ import annotations
import math
import time
from dataclasses import dataclass
from typing import Iterable, TYPE_CHECKING, List

import database
import disnake
from disnake.ext import commands

def setup(bot):
    #bot.add_cog(AdministrationCMD(bot))
    print("Leveling system loaded")