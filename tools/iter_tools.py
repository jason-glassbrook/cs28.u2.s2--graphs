############################################################

import typing as ty
from itertools import chain
from copy import copy

############################################################
#   Type Checking
############################################################


def is_iterable(thing) -> bool:
    return isinstance(thing, ty.Iterable)


############################################################
#   Joining
############################################################


def join_as(
    cast: ty.Callable[[ty.Iterable], ty.Iterable],
    *iters: ty.Iterable[ty.Iterable],
) -> ty.Iterable:

    return cast(chain(*iters))


def join_as_list(*iters: ty.Iterable[ty.Iterable]) -> list:

    return join_as(list, *iters)


def join_as_tuple(*iters: ty.Iterable[ty.Iterable]) -> tuple:

    return join_as(tuple, *iters)


def join_as_set(*iters: ty.Iterable[ty.Iterable]) -> set:

    return join_as(set, *iters)


############################################################
#   Keys
############################################################


def keys_as(
    cast: ty.Callable[[ty.Iterable], ty.Iterable],
    mapping: ty.Mapping,
) -> ty.Iterable:

    return cast(mapping.keys())


def keys_as_list(mapping: ty.Mapping) -> list:

    return keys_as(list, mapping)


def keys_as_tuple(mapping: ty.Mapping) -> tuple:

    return keys_as(tuple, mapping)


def keys_as_set(mapping: ty.Mapping) -> set:

    return keys_as(set, mapping)


############################################################
#   Building Collections
############################################################


def inherit(
    family: ty.Mapping,
    member_key: ty.Any,
    overlay: ty.Optional[ty.Mapping] = None,
    underlay: ty.Optional[ty.Mapping] = None,
    extends_key: str = "extends",
    delete_extends_key: bool = False,
) -> ty.Dict:

    overlay = copy(overlay) if overlay is not None else dict()
    filling = dict()
    underlay = copy(underlay) if underlay is not None else dict()

    while member_key is not None and member_key in family:

        member = family[member_key]
        member_extends = member[extends_key] if extends_key in member else None

        filling = {
            **copy(member),
            **filling,
            "extends": member_extends,
        }

        member_key = member_extends

    if delete_extends_key and extends_key in filling:
        del filling[extends_key]

    result = {
        **underlay,
        **filling,
        **overlay,
    }

    return result
