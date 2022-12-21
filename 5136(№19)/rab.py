from functools import lru_cache

def moves(a):
    return (a-1), (a/2)

@lru_cache(None)
def game(a):
    if a <= 12:
        return "W"
    if any(game(i) == "W" for i in moves(a)):
        return "P1"
    if all(game(i) == "P1" for i in moves(a)):
        return "V1"
    if any(game(i) == "V1" for i in moves(a)):
        return "P2"
    if all(game(i) in ("P2", "P1") for i in moves(a)):
        return "V2"

for a in range(100):
    print(a, game(a))
