from djitellopy import Tello

drone = Tello()

drone.connect()

drone.takeoff()
print(drone.get_battery())
drone.move_up(50)

for j in range (3):
    for i in range(3):
        drone.set_speed(99)
        drone.move_forward(250)
        drone.rotate_clockwise(120)

print(drone.get_battery())
drone.land()

drone.end()
