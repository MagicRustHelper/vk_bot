from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias

from pendulum import DateTime  # noqa: TC002

Steamid: TypeAlias = int
Nickname: TypeAlias = str


class CheckStage(Enum):
    """Enum for check stages

    Attributes:
        PROCCESS: Check is in proccess
        STOPING: Check is stoping
        CANCELING: Check is canceling
    """

    PROCESS = 1
    STOPING = 2
    CANCELING = 3


@dataclass
class TimeInterval:
    """Dataclass for time interval

    Args:
        start (DateTime): Start of time interval
        end (DateTime): End of time interval
    """

    start: DateTime
    end: DateTime

    def __repr__(self) -> str:
        return f'{self.start} - {self.end}'


@dataclass
class OnCheckData:
    """Dataclass for on check data

    Args:
        nickname (Nickname): Player nickname
        db_row: (int): Row in database
        stage (CheckStage): Check stage
    """

    nickname: Nickname
    db_row: int
    stage: CheckStage


@dataclass
class StartedCheck:
    """Dataclass for started check information.

    Args:
        moder_vk (int): A moderator's VK ID.
        nickname (str): A nickname of a player.
        server (int): A server ID.
        steamid (int): A SteamID of a player.
    """

    nickname: str
    steamid: int
    server: int
    moder_vk: int


@dataclass
class Moderator:
    """Dataclass for moderator information.

    Args:
        name (str): A name of a moderator.
        surname (str): A surname of a moderator.
        vk_id (int): A VK ID of a moderator.
    """

    vk_id: int
    name: str
    surname: str

    def __repr__(self) -> str:
        return f'{self.name} {self.surname}'


@dataclass
class ModerChecksInformation:
    """Dataclass for moderator's checks information.

    Args:
        moderator (Moderator): A moderator.
        checks_count (int): A count of checks.
    """

    moderator: Moderator
    checks_count: int
