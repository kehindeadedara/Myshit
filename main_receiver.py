import getopt, sys, time, subprocess, signal


photodiode = None
lidar = None
zed_imu = None
zed_cam = None

threshold = 19000

def usage():
    print('-z or --zed : turn on zed camera ')
    print('-l or --lidar : turn on rplidar ')
    print('-i or --imu : turn on imu sensor ')
    print('-p or --diode : turn on photodiode sensor')


def main(argv):
    
    global photodiode, lidar, zed_cam, zed_imu
    try:
        opts, args = getopt.getopt(argv, "hz:l:i:p:t:", ["zed=", "lidar=", "imu=", "photo=", "thresh="])
    except getopt.GetoptError as err:
        usage()
        print("stopping...")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-z', '--zed'):
            zed_cam = arg
        elif opt in ('-l', '--lidar'):
            lidar = int(arg)
        elif opt in ('-i', '--imu'):
            zed_imu = arg
        elif opt in ('-p', '--photo'):
            photodiode = arg
        elif opt in ('-t', '--thresh'):
            threshold = arg
        
    try:
        photodiode = subprocess.Popen('python3 Receiver/Photodiode.py -t {}'.format(threshold)) if photodiode == 'ON' or 'on' else None
        lidar = subprocess.Popen('python3 Receiver/RPlidar.py') if lidar == 'ON' or 'on' else None
        zed_imu = subprocess.Popen('python3 Receiver/Zed_imu.py') if zed_imu == 'ON' or 'on' else None
        zed_cam = subprocess.Popen('python3 Receiver/zed_record.py') if zed_cam == 'ON' or 'on' else None
    finally:
        print('Receiving data...')



if __name__ == "__main__":
    main(sys.argv[1:])