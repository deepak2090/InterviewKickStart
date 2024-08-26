from collections.abc import MutableMapping
from re import X

class ModTwoMapping(MutableMapping):
    _mapping: dict = {}

    def _validate_value(self, value):
        if value % 2 != 0:
            raise ValueError
        
    def __delitem__(self, key):
        try:
            del self._mapping[key]
        except KeyError:
            print(f'{KeyError} occured')
    
    def __getitem__(self, key):
        return self._mapping[key]

    def __setitem__(self, key, val):
        self._validate_value(val)
        self._mapping[key] = val

    def __iter__(self):
        return iter(self._mapping)
    
    def __len__(self):
        return len(self._mapping)
        
class Person:
    fname: str
    lname: str

    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname
        #super().__init__()
    
    def __repr__(self) -> str:
        return f'person is {self.fname} , {self.lname} hashed value = {hash(self), {hash(self.fname)}, {hash(self.lname)}}'

x = Person("deepak", "das")
print(x)