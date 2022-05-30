from colorama import init, Fore as cc
from os import name as os_name, system
import os
import shutil
#created by Xal Sef'Koj Komtaree
init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET
clear = lambda: system('cls') if os_name == 'nt' else system('clear')
clear()
if not os.path.exists(f"Trucks"):
    os.mkdir("Trucks")
else:
    pass
def green():
    clear()
    print(f"{y}Created by Xal Sef'Koj Komtaree")
    var = input(f"{g}Input Truck Kit Attachments > {y}")
    if not var:
        var = input(f"{r} Do you want to continue? Y/N > ")
        if var.lower() == "y":
            green()
        if var.lower() == "n":
            with open("Trucks\\green.txt", "a") as f:
                format = f'''
</type>
                '''
                f.write(format)
                f.close()
            exit()
    format = f'''
    <attachments>
        <item name="{var}"/>
    </attachments>
    '''
    if var == "help":
        print(f"{r}DO NOT USE ctrl+c TO EXIT, YOU MUST EXIT BY PRESSING ENTER WITH INPUT BLANK\nSHORTCUT TYPE NAMES ARE NOT SUPPORTED (yet){w}")
        input("Press enter to continue...")
        green()
    with open("Trucks\\green.txt", "a") as f:
        f.write(format)
        f.close()
    green()
        
def green1():
    format2 = f'''
<type name="Truck_01_Covered">
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="TruckBattery" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="HeadlightH7" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="HeadlightH7" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Hood" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Door_1_1" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Door_2_1" chance="1.00" />
    </attachments>
    '''
    with open("Trucks\\green.txt", "w") as f:
        f.write(f"{format2}\n")
        f.close()
        
    green()
    

def blue():
    clear()
    print(f"{y}Created by Xal Sef'Koj Komtaree")
    var = input(f"{g}Input Truck Kit Attachments > {y}")
    if not var:
        var = input(f"{r} Do you want to continue? Y/N > ")
        if var.lower() == "y":
            green()
        if var.lower() == "n":
            with open("Trucks\\green.txt", "a") as f:
                format = f'''
</type>
                '''
                f.write(format)
                f.close()
            exit()
    format = f'''
    <attachments>
        <item name="{var}"/>
    </attachments>
    '''
    if var == "help":
        print(f"{r}DO NOT USE ctrl+c TO EXIT, YOU MUST EXIT BY PRESSING ENTER WITH INPUT BLANK\nSHORTCUT TYPE NAMES ARE NOT SUPPORTED (yet){w}")
        input("Press enter to continue...")
        blue()
    with open("Trucks\\blue.txt", "a") as f:
        f.write(format)
        f.close()
    blue()


def blue1():
    format2 = f'''
<type name="Truck_01_Covered_Blue">
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="TruckBattery" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="HeadlightH7" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="HeadlightH7" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Hood_Blue" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Door_1_1_Blue" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Door_2_1_Blue" chance="1.00" />
    </attachments>
    '''
    with open("Trucks\\blue.txt", "w") as f:
        f.write(f"{format2}\n")
        f.close()
        
    blue()




def orange():
    clear()
    print(f"{y}Created by Xal Sef'Koj Komtaree")
    var = input(f"{g}Input Truck Kit Attachments > {y}")
    if not var:
        var = input(f"{r} Do you want to continue? Y/N > ")
        if var.lower() == "y":
            green()
        if var.lower() == "n":
            with open("Trucks\\green.txt", "a") as f:
                format = f'''
</type>
                '''
                f.write(format)
                f.close()
            exit()
    format = f'''
    <attachments>
        <item name="{var}"/>
    </attachments>
    '''
    if var == "help":
        print(f"{r}DO NOT USE ctrl+c TO EXIT, YOU MUST EXIT BY PRESSING ENTER WITH INPUT BLANK\nSHORTCUT TYPE NAMES ARE NOT SUPPORTED (yet){w}")
        input("Press enter to continue...")
        orange()
    with open("Trucks\\orange.txt", "a") as f:
        f.write(format)
        f.close()
    orange()


def orange1():
    format2 = f'''
<type name="Truck_01_Covered_Orange">
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Wheel" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_WheelDouble" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="TruckBattery" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="HeadlightH7" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="HeadlightH7" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Hood_Orange" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Door_1_1_Orange" chance="1.00" />
    </attachments>
    <attachments chance="1.00">
        <item name="Truck_01_Door_2_1_Orange" chance="1.00" />
    </attachments>
    '''
    with open("Trucks\\orange.txt", "w") as f:
        f.write(f"{format2}\n")
        f.close()
        
    orange()



format = f'''
Pick a truck to customize

Green
Blue
Orange
> '''
var = input(format)
if var.lower() == "green":
    green1()
if var.lower() == "blue":
    blue1()
if var.lower() == "orange":
    orange1()