#!/usr/bin/env python
from SCHUNK_Gripper import SCHUNK_Gripper 
from weight_readings import DSCReader 
import csv 
import serial
import rospy
import thread

class LoadCellTesting:
    def __init__(self):
        load_cell = DSCReader()
        self.initial_weight = load_cell.read_measurement()
        self.SchunkGripper = SCHUNK_Gripper().SCHUNK_Gripper()
        rospy.loginfo("Schunk Gripper is connected")
        rospy.loginfo("here")
        self.gripper_serial = serial.Serial(self.SchunkGripper)
        self.gripper_serial.write('c')
        rospy.sleep(1.5)
        self.gripper_serial.write('o')
        # self.intial_blade_weight = self.OffsetWeight()
        rospy.sleep(1.5)

    def OffsetWeight(self):
        load_cell = DSCReader()
        self.initial_weight = load_cell.read_measurement()
        print("initial reading is: ", self.initial_weight)
        # rospy.loginfo("The initial reading is:",self.initial_weight)
        return self.initial_weight
    
    def MeasureWeight(self,initial_weight):
        load_cell = DSCReader()
        self.weight = load_cell.read_measurement() - initial_weight
        print("Measured weight is: ",self.weight)
        # rospy.loginfo("The Current Weight",self.weight)
        return self.weight
    
    def measurment_export(self,initial_weight,weight): #A function that exports and accumilates the weights of the blades into a csv excel file | Placement order in box should be respected
        # list of column names 
        field_names = ['Blade_Weight','Raw_Read']
        # Dictionary
        dict = {"Blade_Weight":weight,"Raw_Read":initial_weight}
        # with open('/home/sanad/catkin_ws/src/yolov5/src/Blade_'+str(i)+'.csv', 'a') as csv_file: //original folder 
        with open('/home/sanad/catkin_ws/data/Blade_'+'.csv', 'a') as csv_file: #determine he
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names)
            dict_object.writerow(dict)
        print("Exported")
    
    def main_loop(self):
        
        user_selection = input("To close the Gripper type -1- to open the Gripper type -2-")
        
        if int(user_selection) == 1 :
            print(user_selection)
            rospy.loginfo("Closing the Gripper")
            # print()
            self.gripper_serial.write('c')
            self.blade_weight = self.MeasureWeight(self.initial_weight)
            print(self.blade_weight) 
            try:
                self.measurment_export(self.initial_weight,self.blade_weight)
                rospy.sleep(1.5)
                self.gripper_serial.write('o')
            except Exception as e: 
                print(e)
        if int(user_selection) == 2:
            # print("jdjdj") 
            # rospy.loginfo("Opening the Gripper")
            print("Opening the Gripper")
            self.gripper_serial.write('o')
        else: 
            print("Error")
            


if __name__=='__main__':
    load_cell_test = LoadCellTesting()
    # thread.start_new_thread(load_cell_test.main_loop,())

    while not rospy.is_shutdown():
        load_cell_test.main_loop()
        pass 
    exit()