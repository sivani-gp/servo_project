import math

L1 = 9.5
L2 = 12

OFFSET_0 = 90
OFFSET_1 = 20
OFFSET_2 = 10

def ik(x, y):

    r = math.sqrt(x*x + y*y)

    # base angle
    t0 = math.atan2(y, x)

    # elbow
    cos_t2 = (r*r - L1*L1 - L2*L2) / (2 * L1 * L2)
    cos_t2 = max(-1, min(1, cos_t2))

    t2 = math.acos(cos_t2)

    # shoulder
    t1 = math.atan2(0, r) - math.atan2(L2 * math.sin(t2), L1 + L2 * math.cos(t2))

    # convert to servo angles
    s0 = math.degrees(t0) + OFFSET_0
    s1 = math.degrees(t1) + OFFSET_1
    s2 = math.degrees(t2) + OFFSET_2

    return int(s0), int(s1), int(s2)