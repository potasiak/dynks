from dynks.ordering import ordered


def test_ordered_simple():
    # given
    items = ['b', 'x', 'c', 'b', 'a']
    order = ['a', 'b', 'c']
    expected_ordered_items = ['a', 'b', 'b', 'c', 'x']
    # when
    ordered_items = list(ordered(items, order))
    # then
    assert expected_ordered_items == ordered_items


def test_ordered_complex():
    # given
    items = [
        {'currency': 'USD', 'amount': '35.00'},
        {'currency': 'GBP', 'amount': '40.00'},
        {'currency': 'PLN', 'amount': '10.00'},
        {'currency': 'USD', 'amount': '30.00'},
        {'currency': 'EUR', 'amount': '20.00'},
    ]
    order = ['PLN', 'EUR', 'USD']

    expected_ordered_items = [
        {'currency': 'PLN', 'amount': '10.00'},
        {'currency': 'EUR', 'amount': '20.00'},
        {'currency': 'USD', 'amount': '35.00'},
        {'currency': 'USD', 'amount': '30.00'},
        {'currency': 'GBP', 'amount': '40.00'},
    ]
    # when
    ordered_items = list(
        ordered(items, order, key=lambda item: item['currency'])
    )
    # then
    assert expected_ordered_items == ordered_items
