from json import JSONEncoder

PROPERTIES_TO_REMOVE = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                        '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
                        '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
                        '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'default', 'encode',
                        'item_separator', 'iterencode', 'key_separator', 'serialize_pyflectively']


class PyflectiveEncoder(JSONEncoder):
    
    def default(self, o):
        O = o.__dict__
        O.pop('check_circular', None)
        O.pop('indent', None)
        O.pop('skipkeys', None)
        O.pop('allow_nan', None)
        O.pop('sort_keys', None)
        O.pop('ensure_ascii', None)
        return O
    
    @classmethod
    def serialize_pyflectively(cls, o):
        return cls().default(o)
    
    def get_json_pyflection(self):
        return PyflectiveEncoder.serialize_pyflectively(self)


class NonPropertyStripper():
    
    @classmethod
    def clean(cls, array_p):
        for junk in PROPERTIES_TO_REMOVE:
            if junk in array_p:
                array_p.remove(junk)
        return array_p
