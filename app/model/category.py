from dataclasses import dataclass


@dataclass
class Category():
    name: str


@dataclass
class Bike(Category):
    color: str
