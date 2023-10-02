import motor, motor_pair
import distance_sensor
from hub import port
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
rotation_change = 1
rotation_value = 0
MOTOR_TURNS = {
    -1: port.B,
    1: port.A
}
while True:
    if distance_sensor.distance(port.D) > 304:
        motor_pair.stop(motor_pair.PAIR_1)
        motor.run_for_degrees(MOTOR_TURNS[rotation_change], 90, 1000)
        rotation_value += rotation_change
        if (rotation_change == 1 and rotation_value > 2) or (rotation_change == -1 and rotation_value < -2):
            rotation_change *= -1
    else:
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=1110, acceleration=10000)
