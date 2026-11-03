def apply_coupon(subtotal_cents: int, discount_cents: int) -> int:
    """Subtract a coupon but never charge a negative amount."""
    return subtotal_cents - discount_cents
