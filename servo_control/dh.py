import math

L1 = 9.5
L2 = 12

OFFSET_0 = 90
OFFSET_1 = 20
OFFSET_2 = 10

def fk(s0, s1, s2):

    t0 = math.radians(s0 - OFFSET_0)
    t1 = math.radians(s1 - OFFSET_1)
    t2 = math.radians(s2 - OFFSET_2)

    r = L1 * math.cos(t1) + L2 * math.cos(t1 + t2)
    z = L1 * math.sin(t1) + L2 * math.sin(t1 + t2)

    x = r * math.cos(t0)
    y = r * math.sin(t0)

    return x, y, z


# test
while True:
    s0, s1, s2 = map(float, input("Enter s0 s1 s2: ").split())

    x, y, z = fk(s0, s1, s2)

    print(f"x={x:.2f}, y={y:.2f}, z={z:.2f}")