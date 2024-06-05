"""

P: price

simple return = (P1 - P0) / P0 = (P1 / P0) - 1

We will use shift() method. Why? P0 is not today's price!

"""

#manual calculation 2023-12-29 vs 2024-01-02

simple_return = (58.849998 / 58.349998) -1

print(f"Simple return: {simple_return}")

#rounded 

rounded_simple_return = round(simple_return, 4)

print(f"Rounded simple return: {rounded_simple_return}")

"""
Simple return: 0.008568980585055064
Rounded simple return: 0.0086
"""
