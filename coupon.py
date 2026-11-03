def apply_coupon(subtotal_cents: int, discount_cents: int) -> int:
    """Subtract a coupon but never charge a negative amount."""
    return max(0, subtotal_cents - discount_cents)

# Pilot canary: same behavior, changed commit identity since CW verification.
