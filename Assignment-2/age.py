def is_adult(age):
    """Return True if age is 18 or more. Raise ValueError for a negative age."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18