from rplidar import RPLidar
lidar = RPLidar('COM5', baudrate=256000)
import time

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

time.sleep(10)
for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measurments' % (i, len(scan)))
    print(scan)
    if i > 5:
        break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
