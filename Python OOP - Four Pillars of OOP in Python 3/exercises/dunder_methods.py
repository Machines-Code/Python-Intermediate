# Comparison operators

# a == b ==> calls:	__eq__
# a != b ==> calls:	__ne__
# a < b ==> calls:	__lt__
# a <= b ==> calls:	__le__
# a > b ==> calls:	__gt__
# a >= b ==> calls:	__ge__


# Arithmetic operators

# a + b ==> calls:	__add__
# a - b ==> calls:	__sub__
# a * b ==> calls:	__mul__
# a / b ==> calls:	__truediv__
# a // b ==> calls:	__floordiv__
# a % b ==> calls:	__mod__
# a ** b ==> calls:	__pow__


# In-place(compound assignment) operators — e.g. a += b

# a += b ==> calls:	__iadd__
# a -= b ==> calls:	__isub__
# a *= b ==> calls:	__imul__
# a /= b ==> calls:	__itruediv__
# (If these aren't defined, Python just falls back to the regular __add__/__sub__/etc. and reassigns the result.)


# Unary operators

# -a ==> calls:	__neg__
# +a ==> calls:	__pos__
# abs(a) ==> calls:	__abs__


# Other commonly overloaded dunders (not arithmetic operators, but same concept — hooking into built-in syntax/functions)

# str(a) / print(a) ==> calls:	__str__
# repr(a) ==> calls:	__repr__
# len(a) ==> calls:	__len__
# a[i] ==> calls:	__getitem__
# a[i] = x ==> calls:	__setitem__
# x in a ==> calls:	__contains__
# a() ==> calls:	__call__
# bool(a) ==> calls:	__bool__


# Handy pattern to remember: whenever you see a builtin operator or function acting on your object, there's almost always a __dunder__ method behind it — you can find it by checking help(int) or Python's data model docs for the full list.
