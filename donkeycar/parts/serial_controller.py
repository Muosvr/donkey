#!/usr/bin/env python3

import serial

class SerialController:
    def __init__(self):
        print("Starting Serial Controller")

        self.angle = 0.0
        self.throttle = 0.0
        self.mode = 'user'
        self.recording = False

    def update(self):
        print("Serial controller running")
        with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
            while(True):
                line = str(ser.readline())[2:-5]
                output = line.split(" ")
                if output != ['']:
                    self.angle = float(output[0])
                    self.throttle = float(output[1])
                    # print(self.angle, self.throttle)

    def run_threaded(self):
        return self.angle, self.throttle


carPart = SerialController()
carPart.update()
#Serial port - laptop: 'COM3', Arduino: '/dev/ttyACM0'
# with serial.Serial('COM3', 9600, timeout=1) as ser:
#     while(True):
#         line = str(ser.readline())[2:-5]
#         output = line.split(" ")
#         if output != ['']:
#             steering = float(output[0])
#             throttle = float(output[1])
#             return steering, throttle
