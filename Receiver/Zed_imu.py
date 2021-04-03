import pyzed.sl as sl


def main():
    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.sdk_verbose = False

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    # Display camera information (model, serial number, firmware version)
    info = zed.get_camera_information()
    print("Camera model: {}".format(info.camera_model))
    print("Serial Number: {}".format(info.serial_number))
    print("Camera Firmware: {}".format(info.camera_configuration.firmware_version))
    print("Sensors Firmware: {}".format(info.sensors_configuration.firmware_version))

    zed.close()

if __name__ == "__main__":
    main()
