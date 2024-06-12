from statistics import mean


class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y


def slope(p1: Point, p2: Point) -> float:
    return (p2.y - p1.y) / (p2.x - p1.x)


def intercept(p1: Point, p2: Point) -> float:
    known_xs = [p1.x, p2.x]; known_ys = [p1.y, p2.y]
    b_numer = sum(
        [(xs - mean(known_xs))*(ys - mean(known_ys)) \
            for xs, ys in zip(known_xs, known_ys)]
    )
    b_denum = sum([(xs - mean(known_xs))**2 for xs in known_xs])
    b = b_numer / b_denum
    return mean(known_ys) - b * mean(known_xs)


def trap_mf(x: float, a: Point, b: Point, c: Point, d: Point) -> float:
    result = 0
    if x < a.x:
        result = 0
    elif a.x <= x < b.x:
        result = slope(a, b) * x + intercept(a, b)
    elif b.x <= x < c.x:
        result = 1
    elif c.x <= x < d.x:
        result = slope(c, d) * x + intercept(c, d)
    elif x >= d.x:
        result = 0
    return result


def tri_mf(x: float, a: Point, b: Point, c: Point) -> float:
    result = 0
    if x < a.x:
        result = 0
    elif a.x <= x < b.x:
        result = slope(a, b) * x + intercept(a, b)
    elif b.x <= x < c.x:
        result = slope(b, c) * x + intercept(b, c)
    elif x >= c.x:
        result = 0
    return result

