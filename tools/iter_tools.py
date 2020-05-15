############################################################

import typing as ty
from itertools import chain

############################################################


def is_iterable(thing) -> bool:
    return isinstance(thing, ty.Iterable)


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
