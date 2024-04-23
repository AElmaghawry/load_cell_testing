import serial
import time


class DSCReader:
    #UDEV rule for loadcell in /etc/udev/rules.d/loadcell.rules     |     As follows:
    #(((KERNEL=="ttyUSB*",  ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{manufacturer}=="FTDI",ATTRS{product}=="FT232R USB UART", ATTRS{serial}=="A10KEWWN",  SYMLINK+="applied_measurments_load_cell")))#
    def __init__(self, port='/dev/applied_measurments_load_cell', baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        try:
            self.serial_port = serial.Serial(self.port, self.baudrate)
        except:
            print("failed to open serial port")

    def read_measurement(self):
        ascii = ""
        req_msg = '!001:SYS?\r'
        while ascii=="":
            self.serial_port.write(req_msg.encode("ascii"))
            buffer = self.serial_port.read_all()
            ascii = buffer.decode('ascii')
            time.sleep(0.1)
        return float(ascii)

dsc_reader=DSCReader()
print("Here")