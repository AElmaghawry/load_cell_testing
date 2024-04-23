import serial
import time
import rospy

class SCHUNK_Gripper:
    def SCHUNK_Gripper(self):
        start_flag=False
        ascii=None
        i=0
        self.port = '/dev/ttyACM'+str(i)
        self.baudrate = 9600
        while True:
            try:
                
                    start_flag==False
                    print(self.port)
                    self.serial_port = serial.Serial(self.port, self.baudrate)
                    rospy.sleep(0.5)
                    ascii = ""
                    req_msg = 'h'
                    while ascii=="":
                        self.serial_port.write(req_msg.encode("ascii"))
                        buffer = self.serial_port.read_all()
                        ascii = buffer.decode('ascii')
                        time.sleep(0.01)
            
            except Exception as e:
                i=i+1
                self.port = '/dev/ttyACM'+str(i)
                print("failed to open serial port")
                print(e)

            a=ascii
            if a==u'25970\r\n':
                # print("Schunk Gripper Detected")
                self.SCHUNK_port='/dev/ttyACM'+str(i)
                # print("PORT"+str(self.SCHUNK_port))
                return self.SCHUNK_port
                
            if i==10:
                 i=0