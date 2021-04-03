import getopt, sys, time, subprocess, signal

def usage():
    print('main_transmitter.py -a <Rear LED> -o <Rear LED matrix> -b <Front LED matrix>')
    print('-a or --alpha : turn on the rear LED ')
    print('-b or --beta : turn on the rear LED matrix ')
    print('-o or --omega : turn on the front LED matrix ')
    print('-t or --teleop : start ROS Launch ')
    print('-r or --runtime : set the runtime or iteration ')
    print('-f or --frequency : set LED freuency')




message = "HelloJarred"

alpha = 'OFF'
beta = 'OFF'
omega = 'OFF'
teleop = 'STOP'
frequency = 30
random_size = 500
clock = 2



def interrupt_handler(sig, frame):
    print("You've pressed Ctrl+C!")
    print("Program ending...")
    sys.stdout.flush()
    sys.exit(0)


def main(argv) -> None:
    global alpha, beta, omega, teleop, frequency, random_size, clock
    try:
        opts, args = getopt.getopt(argv, "a:b:o:m:t:r:f:c:", ["alpha=", "beta=", "omega=", "message=, teleop=", "random=", "frequency=", "clock="])
    except getopt.GetoptError as err:
        usage()
        print("stopping...")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-a', '--alpha'):
            alpha = arg
        elif opt in ('-b', '--beta'):
            beta = int(arg)
        elif opt in ('-o', '--omega'):
            omega = arg
        elif opt in ('-m', '--message'):
            message = arg
        elif opt in ('-t', '--teleop'):
            teleop = arg
        elif opt in ('-r', '--random'):
            random_size = arg
        elif opt in ('-f', '--frequency'):
            frequency = arg
        elif opt in ('-c', '--clock'):
            clock = arg

    signal.signal(signal.SIGINT, interrupt_handler)

    #Start all transmitters subprocesses
    if alpha == 'ON' or 'on':
        rear_transmitter = subprocess.Popen('python3 Transmitter/rear_transmission.py -f {} -r {} -t {}'.format(frequency, random_size, clock),shell=True)
        print('Starting Main LED....')
    if beta == 'ON' or 'on':
        rear_led_matrix = subprocess.Popen('python3 Transmitter/front_ledmatrix.py -f {} -m {} -t {}'.format(frequency, message, clock), shell=True)
        print('Starting front LED matrix....')
    if omega == 'ON' or 'on':
        front_led_matrix = subprocess.Popen('python3 Transmitter/back_ledmatrix.py -f {} -m {} -t {}'.format(frequency, message, clock), shell=True)
        print('Starting rear LED matrix....')
    if teleop == 'L' or 'LAUNCH' or 'START':
        launch_ROS = subprocess.Popen('python3 RosLaunch.py', shell=True)


if __name__ == "__main__":
    main(sys.argv[:])
    #python3 main_transmitter.py -a ON -b ON -o ON -t L -r 1000 -f 60 -c 200
