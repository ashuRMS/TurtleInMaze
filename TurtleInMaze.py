from robot_control_class import RobotControl
import time

rc = RobotControl(robot_name="summit")


def move(a, b, c):
    print(f"The robot moves {a} with vel {b}")
    rc.move_straight_time(a, b, c)
    time.sleep(c)


def rotate(d, e, f):
    print(f"The robot rotates {d} with ang vel {e}")
    rc.turn(d, e, f)
    time.sleep(f)


move("forward", 0.3, 6)
rotate("counter-clockwise", 0.3, 8)
move("forward", 0.3, 6)
rotate("counter-clockwise", 0.3, 8)
move("forward", 0.3, 9)
