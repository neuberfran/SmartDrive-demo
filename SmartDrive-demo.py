#!/usr/bin/env python
#
# Copyright (c) 2014 OpenElectrons.com
# SmartDrive example script.
# for more information about SmartDrive,  please visit:
# http://www.Openelectrons.com/index.php?module=pagemaster&PAGE_user_op=view_page&#PAGE_id=34 
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# History:
# Date      Author        Comments
# 01/28/14  Michael       Initial authoring.
# 02/03/14  Michael       Modified for OpenElectron_i2c
# 03/12/14  Michael       Modified for customer example and comment
# 04/21/14  Michael       SmartDrive modification
#

import time
import os, sys
# import SmartDrive class from SmartDrive Library
from SmartDrive import SmartDrive

# Define run variables
SmartDrive = SmartDrive()
speed = 100
duration = 50
degrees = 720
rotations = 2
tacho = 1080
test = 1

# Reset encoder values
SmartDrive.command(SmartDrive.R) 

# Infinite loop
#while test == 1:
    
    # Read input battery voltage
print "Batt: " + str(SmartDrive.GetBattVoltage())
    
    # Read encoder values 
print "Tach1: " + str(SmartDrive.ReadTachometerPosition(SmartDrive.SmartDrive_Motor_1))
print "Tach2: " + str(SmartDrive.ReadTachometerPosition(SmartDrive.SmartDrive_Motor_2))
    
    # Run motor for an unlimited time. Uncomment the following line to run the motor for unlimited amount of time
#SmartDrive.SmartDrive_Run_Unlimited(SmartDrive.SmartDrive_Motor_1,SmartDrive.SmartDrive_Direction_Forward, speed)
    #time.sleep(10)
    
    # Stops the motor. Uncomment the following line to stop the motor.
    #SmartDrive.SmartDrive_Stop(SmartDrive.SmartDrive_Motor_1, SmartDrive.SmartDrive_Next_Action_Brake)
    
    # Runs motor for a specific time determined by the "seconds" variable. Uncomment following line to run for specific amount of time
SmartDrive.SmartDrive_Run_Seconds(SmartDrive.SmartDrive_Motor_1, SmartDrive.SmartDrive_Direction_Forward, speed, duration, SmartDrive.SmartDrive_Completion_Wait_For, SmartDrive.SmartDrive_Next_Action_Brake)   
    
    # Runs motor for a specific amount of degrees determined by the "degrees" variable. Uncomment following line to run for a specific number of degrees
    #SmartDrive.SmartDrive_Run_Degrees(SmartDrive.SmartDrive_Motor_1, SmartDrive.SmartDrive_Direction_Forward, speed, degrees, SmartDrive.SmartDrive_Completion_Wait_For, SmartDrive.SmartDrive_Next_Action_Brake)
    
    # Runs motor for a specific amount of rotations determined by the "rotations" variable. Uncomment following line to run for a specific number of rotations 
    #SmartDrive.SmartDrive_Run_Rotations(SmartDrive.SmartDrive_Motor_1, SmartDrive.SmartDrive_Direction_Reverse, speed, rotations, SmartDrive.SmartDrive_Completion_Wait_For, SmartDrive.SmartDrive_Next_Action_Brake)
    
    # Runs motor to a specific encoder value determined by "tacho" variable. Uncomment following line to run motor to a specific encoder value.
    #SmartDrive.SmartDrive_Run_Tacho(SmartDrive.SmartDrive_Motor_1, speed, tacho, SmartDrive.SmartDrive_Completion_Wait_For, SmartDrive.SmartDrive_Next_Action_Brake)
    #time.sleep(1)
    
    

