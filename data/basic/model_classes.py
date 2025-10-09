from dataclasses import dataclass, field
from typing import List, Optional
import datetime
#region osztályok
@dataclass
class Player:
    id: str
    name: str
    country: str

def __init__(self, id: str, name: str, country: str):
    self.id = id
    self.name = name
    self.country = country

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
#endregion