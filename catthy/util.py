from __future__ import annotations
from typing import Callable, Protocol, TypeVar

A = TypeVar('A')

class FactoryConstructor(Protocol[A]):
    @classmethod
    def of(cls, *xs) -> FactoryConstructor[A]:
        return cls(xs)

class NaiveHashable:
    def __hash__(self):
        return hash(str(self))
    
class FunctionCastable:
    def cast_after(self, f: Callable) -> FunctionCastable:
        self = type(self)(f(self))
        return self
    
    @classmethod
    def cast(cls, x) -> FunctionCastable:
        return cls(x)
    
def translate(mappings: dict):
    def add_mapping(cls):
        for k,v in mappings.items():
            setattr(cls, v, getattr(cls, k))
        return cls
    return add_mapping