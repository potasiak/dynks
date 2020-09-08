from functools import partial
from operator import itemgetter
from typing import Callable, Iterable, Optional, Sequence, TypeVar

T = TypeVar('T')  # generic type

IT = TypeVar('IT')  # item type
KT = TypeVar('KT')  # key type


def _identity(value: T) -> T:
    """Get given value back.

    Args:
        value (T): Value to return.

    Returns:
        T: The given value.

    """
    return value


def _get_index(sequence: Sequence[KT], value: KT) -> int:
    """Get index of given value in the given sequence.

    If the value does not exist in the sequence, an integer higher than
    highest index in the sequence is returned.

    Args:
        sequence (Sequence[KT]): Sequence of values.
        value (KT): Value to get index for.

    Returns:
        int: Index of the value in the sequence or integer higher than
            highest index in the sequence.

    Examples:
        >>> sequence = ['a', 'b', 'c']
        >>> _get_index(sequence, 'b')
        1
        >>> _get_index(sequence, 'z')
        3

    """
    try:
        idx = sequence.index(value)
    except ValueError:
        idx = len(sequence)
    return idx


def _get_ordinals(
    items: Iterable[IT],
    order: Sequence[KT],
    *,
    key: Optional[Callable[[IT], KT]] = None
) -> Iterable[int]:
    """Get ordinals for given items based on the given order.

    Args:
        items (Iterable[IT]): Iterable to get the ordinals for.
        order (Sequence[KT]): Sequence of keys that determines ordinals
            for the items.
        key (Callable[[IT], KT], optional): Callable that extracts key
            from the items. Identity function by default.

    Returns:
        Iterable[int]: Iterable of ordinals for given items.

    Examples:
        >>> from dynks.ordering import ordered
        >>> items = ['b', 'x', 'c', 'b', 'a']
        >>> order = ['a', 'b', 'c']
        >>> list(
        ...     _get_ordinals(items, order)
        ... )
        [1, 3, 2, 1, 0]

        >>> from dynks.ordering import ordered
        >>> from operator import itemgetter
        >>> items = [
        ...    {'currency': 'USD', 'amount': '35.00'},
        ...    {'currency': 'GBP', 'amount': '40.00'},
        ...    {'currency': 'PLN', 'amount': '10.00'},
        ...    {'currency': 'USD', 'amount': '30.00'},
        ...    {'currency': 'EUR', 'amount': '20.00'}
        ... ]
        ...
        >>> order = ['PLN', 'EUR', 'USD']
        >>> list(
        ...     _get_ordinals(items, order, key=itemgetter('currency'))
        ... )
        ...
        [2, 3, 0, 2, 1]

    """
    if key is None:
        key = _identity
    return map(
        partial(_get_index, order),
        (key(item) for item in items)
    )


def ordered(
    items: Iterable[IT],
    order: Sequence[KT],
    *,
    key: Optional[Callable[[IT], KT]] = None
) -> Iterable[IT]:
    """Sort items according to given order.

    Args:
        items (Iterable[IT]): Iterable to sort according to given order.
        order (Sequence[KT]): Sequence of keys that determines the order
            of the items.
        key (Callable[[IT], KT], optional): Callable that extracts key
            from the items. Identity function by default.

    Returns:
        Iterable[IT]: Iterable with items sorted according to given
            order.

    Examples:
        >>> from dynks.ordering import ordered
        >>> items = ['b', 'x', 'c', 'b', 'a']
        >>> order = ['a', 'b', 'c']
        >>> list(
        ...     ordered(items, order)
        ... )
        ['a', 'b', 'b', 'c', 'x']

        >>> from dynks.ordering import ordered
        >>> from operator import itemgetter
        >>> items = [
        ...    {'currency': 'USD', 'amount': '35.00'},
        ...    {'currency': 'GBP', 'amount': '40.00'},
        ...    {'currency': 'PLN', 'amount': '10.00'},
        ...    {'currency': 'USD', 'amount': '30.00'},
        ...    {'currency': 'EUR', 'amount': '20.00'}
        ... ]
        ...
        >>> order = ['PLN', 'EUR', 'USD']
        >>> list(
        ...     ordered(items, order, key=itemgetter('currency'))
        ... )
        ...
        [{'currency': 'PLN', 'amount': '10.00'}, {'currency': 'EUR', 'amount': '20.00'}, {'currency': 'USD', 'amount': '35.00'}, {'currency': 'USD', 'amount': '30.00'}, {'currency': 'GBP', 'amount': '40.00'}]

    """
    ordinals = _get_ordinals(items, order, key=key)
    return map(itemgetter(1), sorted(zip(ordinals, items), key=itemgetter(0)))
