from dataclasses import dataclass, field
from typing import List, Optional
import datetime
@dataclass
class Player:
    id: str
    name: str
    country: str
@dataclass
class CarClass:
    id: str
    name: str
@dataclass
class Track:
    id: str
@dataclass
class Race:
    id: str
    player: Player
    car_class: CarClass
    track: Track
    Date: datetime.datetime
    start_pos: int
    finish_pos: int
    incidents: int
    rating_change: float
    reputation_change: float
@dataclass
class CareerStats:
    player: Player
    races: List[Race] = field(default_factory=list)