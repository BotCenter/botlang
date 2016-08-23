from __future__ import print_function

import math
import operator as op
from collections import OrderedDict


def append(*values):
    return reduce(op.add, values)


def dict_put(data_dict, key, value):
    data = data_dict.copy()
    data[key] = value
    return data


def dict_get(data_dict, key):
    return data_dict[key]


def dict_has_key(data_dict, key):
    return data_dict.get(key) is not None


class BotcenterDSLPrimitives(object):

    MATH = vars(math)

    OPERATORS = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': lambda x, y: x / y,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '=': op.eq,
        'abs': abs,
        'equal?': op.eq,
        'not': op.not_,
    }

    LIST_OPERATIONS = {
        'append': append,
        'head': lambda x: x[0],
        'tail': lambda x: x[1:],
        'length': len,
        'list': lambda *x: list(x),
        'map': lambda f, l: list(map(f, l)),
        'max': max,
        'min': min,
        'in-list': lambda lst, elem: elem in lst
    }

    DICT_OPERATIONS = {
        'make-dict': lambda: OrderedDict(),
        'put': dict_put,
        'get': dict_get,
        'has-key': dict_has_key
    }

    SIDE_EFFECTS = {
        'print': print
    }

    @classmethod
    def populate_environment(cls, environment):

        environment.add_primitives(cls.MATH)
        environment.add_primitives(cls.OPERATORS)
        environment.add_primitives(cls.LIST_OPERATIONS)
        environment.add_primitives(cls.DICT_OPERATIONS)
        environment.add_primitives(cls.SIDE_EFFECTS)
        return environment