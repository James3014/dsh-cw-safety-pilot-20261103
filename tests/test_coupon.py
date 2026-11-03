from coupon import apply_coupon


def test_regular_coupon():
    assert apply_coupon(1000, 150) == 850


def test_zero_coupon():
    assert apply_coupon(1000, 0) == 1000
