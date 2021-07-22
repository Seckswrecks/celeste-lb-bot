"""
data_models.py

Dataclasses related to configuration
"""

from dataclasses    import dataclass
from typing         import List


#################
## CREDENTIALS ##
#################


@dataclass(frozen=True)
class SpeedrunCredentials:
    """speedrun.com API credentials"""

    api: str
    csrf: str
    session: str


@dataclass(frozen=True)
class TwitchCredentials:
    """Twitch API credentials"""

    client: str
    secret: str


@dataclass(frozen=True)
class Credentials:
    """Representation of API credentials used by bot"""

    src: SpeedrunCredentials
    twitch: TwitchCredentials


############
## CONFIG ##
############


@dataclass(frozen=True)
class CelesteGameVersion:
    """Representation of data related to 'Version' variable for Celeste games"""

    variable_id: str
    default_ver: str
    invalid_ver: dict


@dataclass(frozen=True)
class Game:
    """speedrun.com game representation"""

    id: str
    name: str
    version: CelesteGameVersion


@dataclass(frozen=True)
class CelesteGames:
    """Config of Celeste Leaderboard Bot"""

    games: List[Game]
