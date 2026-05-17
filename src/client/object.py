from dataclasses import dataclass


@dataclass
class Object:
    name: str
    id: int
    price: int
    typ: str
    desc: str
