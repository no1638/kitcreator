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
name = input(f"{y}Created by Xal Sef'Koj Komtaree\n{b}Input Event Name > {y}")
survivor = input(f"{b}Input Survivor Name > {y}")
event = f'''
    <event name="Item{name}">
		<nominal>1</nominal>
		<min>1</min>
		<max>1</max>
		<lifetime>2500</lifetime>
		<restock>0</restock>
		<saferadius>0</saferadius>
		<distanceradius>0</distanceradius>
		<cleanupradius>200</cleanupradius>
		<flags deletable="0" init_random="0" remove_damaged="1"/>
		<position>fixed</position>
		<limit>child</limit>
		<active>1</active>
		<children>
			<child lootmax="0" lootmin="0" max="1" min="1" type="{survivor}"/>
		</children>
	</event>
'''
trucks = input(f"{b}Are you going to include Trucks? [Y/N] > {y}")
if trucks.lower() == "y":
    yn = input(f"{b}do you want to use the included truck kit? [Y/N] > {y}")
    event = f'''
    <event name="Item{name}">
		<nominal>1</nominal>
		<min>1</min>
		<max>1</max>
		<lifetime>2500</lifetime>
		<restock>0</restock>
		<saferadius>0</saferadius>
		<distanceradius>0</distanceradius>
		<cleanupradius>200</cleanupradius>
		<flags deletable="0" init_random="0" remove_damaged="1"/>
		<position>fixed</position>
		<limit>child</limit>
		<active>1</active>
		<children>
			<child lootmax="0" lootmin="0" max="1" min="1" type="{survivor}"/>
		</children>
	</event>
    <event name="VehicleBuildTruck{name}">
		<nominal>1</nominal>
		<min>1</min>
		<max>1</max>
		<lifetime>2500</lifetime>
		<restock>0</restock>
		<saferadius>0</saferadius>
		<distanceradius>0</distanceradius>
		<cleanupradius>200</cleanupradius>
		<flags deletable="0" init_random="0" remove_damaged="1"/>
		<position>fixed</position>
		<limit>child</limit>
		<active>1</active>
		<children>
			<child lootmax="0" lootmin="0" max="1" min="1" type="Truck_01_Covered"/>
		</children>
	</event>
    <event name="VehicleMedTruck{name}">
		<nominal>1</nominal>
		<min>1</min>
		<max>1</max>
		<lifetime>2500</lifetime>
		<restock>0</restock>
		<saferadius>0</saferadius>
		<distanceradius>0</distanceradius>
		<cleanupradius>200</cleanupradius>
		<flags deletable="0" init_random="0" remove_damaged="1"/>
		<position>fixed</position>
		<limit>child</limit>
		<active>1</active>
		<children>
			<child lootmax="0" lootmin="0" max="1" min="1" type="Truck_01_Covered_Blue"/>
		</children>
	</event>
            '''
if os.path.isdir(f"{name}"):
    shutil.rmtree(f'{name}')
os.mkdir(f"{name}")
with open(f"{name}\\{name}event.txt", "w") as f:
    f.write(f"{event}")
    f.close()
clear()
coordsX = input(f"{y}Created by Xal Sef'Koj Komtaree\n{b}Input Full X Coordinates (NPC) > {y}")
coordsY = input(f"{b}Input Full Z Coordinates (NPC) > {y}")
coordsA = input(f"{b}Input Full A Coordinates (Rotation, default is 113.00) (NPC) > {y}")
if not coordsA:
    coordsA = "113.00"
coords = f'''
    <event name="Item{name}">
		<pos x="{coordsX}" z="{coordsY}" a="{coordsA}"/>
	</event>
'''

if trucks.lower() == "y":
    t1coordsX = input(f"{b}Input Full X Coordinates for Build Truck > {y}")
    t1coordsY = input(f"{b}Input Full Z Coordinates for Build Truck > {y}")
    t1coordsA = input(f"{b}Input Full A Coordinates (Rotation, default is 113.00) for Build Truck > {y}")
    if not t1coordsA:
        t1coordsA = "113.00"
    t2coordsX = input(f"{b}Input Full X Coordinates for Med Truck > {y}")
    t2coordsY = input(f"{b}Input Full Z Coordinates for Med Truck > {y}")
    t2coordsA = input(f"{b}Input Full A Coordinates (Rotation, default is 113.00) for Med Truck > {y}")
    if not t2coordsA:
        t2coordsA = "113.00"
    coords = f'''
    <event name="Item{name}">
		<pos x="{coordsX}" z="{coordsY}" a="{coordsA}"/>
	</event>
    <event name="VehicleBuildTruck{name}">
		<pos x="{t1coordsX}" z="{t1coordsY}" a="{t1coordsA}"/>
	</event>
    <event name="VehicleMedTruck{name}">
		<pos x="{t2coordsX}" z="{t2coordsY}" a="{t2coordsA}"/>
	</event>
    '''
    if yn == "y":
        truck1inv = f'''
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
            <attachments>
            <item name="Barrel_Red" chance="1.00" />
            </attachments>
            <attachments chance="1.00">
                <item name="CanisterGasoline" chance="1.00" />
            </attachments>
            <attachments chance="1.00">
                <item name="CanisterGasoline" chance="1.00" />
            </attachments>
            <attachments>
                <item name="PowerGenerator"/>
            </attachments>
            <attachments>
                <item name="TerritoryFlagKit"/>
            </attachments>
            <attachments>
                <item name="TerritoryFlagKit"/>
            </attachments>
            <attachments>
                <item name="Flag_APA"/>
            </attachments>
            <attachments>
                <item name="Flag_APA"/>
            </attachments>
            <attachments>
                <item name="Flag_Wolf"/>
            </attachments>
            <attachments>
                <item name="Flag_Wolf"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="NailBox"/>
            </attachments>
            <attachments>
                <item name="CableReel"/>
            </attachments>
            <attachments>
                <item name="CableReel"/>
            </attachments>
            <attachments>
                <item name="SpotLight"/>
            </attachments>
            <attachments>
                <item name="SpotLight"/>
            </attachments>
            <attachments>
                <item name="SpotLight"/>
            </attachments>
            <attachments>
                <item name="SpotLight"/>
            </attachments>
            <attachments>
                <item name="Hatchet"/>
            </attachments>
            <attachments>
                <item name="Hatchet"/>
            </attachments>
            <attachments>
                <item name="Hatchet"/>
            </attachments>
            <attachments>
                <item name="Hatchet"/>
            </attachments>
            <attachments>
                <item name="Hatchet"/>
            </attachments>
            <attachments>
                <item name="Whetstone"/>
            </attachments>
            <attachments>
                <item name="Whetstone"/>
            </attachments>
            <attachments>
                <item name="Whetstone"/>
            </attachments>
            <attachments>
                <item name="CombinationLock4"/>
            </attachments>
            <attachments>
                <item name="CombinationLock4"/>
            </attachments>
            <attachments>
                <item name="CombinationLock4"/>
            </attachments>
            <attachments>
                <item name="CombinationLock4"/>
            </attachments>
            <attachments>
                <item name="Pickaxe"/>
            </attachments>
            <attachments>
                <item name="MetalWire"/>
            </attachments>
            <attachments>
                <item name="MetalWire"/>
            </attachments>
            <attachments>
                <item name="MetalWire"/>
            </attachments>
            <attachments>
                <item name="MetalWire"/>
            </attachments>
            <attachments>
                <item name="BarbedWire"/>
            </attachments>
            <attachments>
                <item name="BarbedWire"/>
            </attachments>
            <attachments>
                <item name="BarbedWire"/>
            </attachments>
            <attachments>
                <item name="BarbedWire"/>
            </attachments>
            <attachments>
                <item name="BarbedWire"/>
            </attachments>
            <attachments>
                <item name="BarbedWire"/>
            </attachments>
            <attachments>
                <item name="Pliers"/>
            </attachments>
            <attachments>
                <item name="Pliers"/>
            </attachments>
            <attachments>
                <item name="Pliers"/>
            </attachments>
            <attachments>
                <item name="Pliers"/>
            </attachments>
            <attachments>
                <item name="Hacksaw" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Hacksaw" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Hacksaw" chance="1.00" />
            </attachments>
            <attachments>
                <item name="SledgeHammer" chance="1.00" />
            </attachments>
            <attachments>
                <item name="SledgeHammer" chance="1.00" />
            </attachments>
            <attachments>
                <item name="SledgeHammer" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Rope" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Rope" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Rope" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Rope" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Shovel" chance="1.00" />
            </attachments>
            <attachments>
                <item name="LargeTent" chance="1.00" />
            </attachments>
            <attachments>
                <item name="LargeTent" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Camonet" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Camonet" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Camonet" chance="1.00" />
            </attachments>
            <attachments>
                <item name="SparkPlug" chance="1.00" />
            </attachments>
            <attachments>
                <item name="SparkPlug" chance="1.00" />
            </attachments>
            <attachments>
                <item name="SparkPlug" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery0V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery0V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery0V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery0V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery0V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery0V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
            <attachments>
                <item name="Battery9V" chance="1.00" />
            </attachments>
        </type>
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
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="BandageDressing"/>
            </attachments>
            <attachments>
                <item name="IodineTincture"/>
            </attachments>
            <attachments>
                <item name="IodineTincture"/>
            </attachments>
            <attachments>
                <item name="IodineTincture"/>
            </attachments>
            <attachments>
                <item name="IodineTincture"/>
            </attachments>
            <attachments>
                <item name="IodineTincture"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="Morphine"/>
            </attachments>
            <attachments>
                <item name="FirstAidKit"/>
            </attachments>
            <attachments>
                <item name="FirstAidKit"/>
            </attachments>
            <attachments>
                <item name="FirstAidKit"/>
            </attachments>
            <attachments>
                <item name="FirstAidKit"/>
            </attachments>
            <attachments>
                <item name="BloodBagIV"/>
            </attachments>
            <attachments>
                <item name="BloodBagIV"/>
            </attachments>
            <attachments>
                <item name="BloodBagIV"/>
            </attachments>
            <attachments>
                <item name="BloodTestKit"/>
            </attachments>
            <attachments>
                <item name="BloodTestKit"/>
            </attachments>
            <attachments>
                <item name="BloodTestKit"/>
            </attachments>
            <attachments>
                <item name="SalineBag"/>
            </attachments>
            <attachments>
                <item name="SalineBag"/>
            </attachments>
            <attachments>
                <item name="SalineBag"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="TetracyclineAntibiotics"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="VitamimBottle"/>
            </attachments>
            <attachments>
                <item name="Splint"/>
            </attachments>
            <attachments>
                <item name="Splint"/>
            </attachments>
            <attachments>
                <item name="Splint"/>
            </attachments>
            <attachments>
                <item name="Splint"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="TacticalBaconCan_Opened"/>
            </attachments>
            <attachments>
                <item name="Canteen"/>
            </attachments>
            <attachments>
                <item name="Canteen"/>
            </attachments>
            <attachments>
                <item name="Canteen"/>
            </attachments>
            <attachments>
                <item name="Canteen"/>
            </attachments>
            <attachments>
                <item name="Canteen"/>
            </attachments>
            <attachments>
                <item name="Canteen"/>
            </attachments>
            <attachments>
                <item name="Canteen"/>
            </attachments>
        </type>
        '''
        with open(f"{name}\\TrucksInv.txt", "w") as f:
            f.write(truck1inv)
            f.close()
    else:
        pass
    


with open(f"{name}\\{name}spawnevent.txt", "w") as f:
    f.write(f"{coords}")
    f.close()
    
    
def items():
    while True:
        clear()
        
        kititems = input(f"{y}Created by Xal Sef'Koj Komtaree\n{g}Input Kit Attachments > {y}")
        if not kititems:
            choice = input(f"{r}Do you want to continue? (Yes to Continue, No to Stop, Default is Y) Y/N > {y}").lower()
            if not choice:
                items()
            if choice == "y":
                items()
            if choice == "n":
                exit()
        if kititems:
            if kititems == "help":
                itemlist = f'''
radio
919
556
m4
m4rail
m4tele
mlock
cmag30
mlockmag
largeradio
platecarrier
platepouches
knife (combat knife)
bizon
bizonmag
bizonstck
tundra
308
acog
acog6
akm
magakm30
pistolsuppressor
fieldv
bandage
blackmask
blackmaskskull
cargopblack
cargopgray
cargopgreen


        
                '''
                print(itemlist)
                input("Press Enter to Continue...")
                items()
            if kititems == "radio":
                kititems = "PersonalRadio"
            if kititems == "largeradio":
                kititems = "BaseRadio"
            if kititems == "919":
                kititems = "AmmoBox_9x19_25Rnd"
            if kititems == "556":
                kititems = "AmmoBox_556x45_20Rnd"
            if kititems == "m4":
                kititems = "M4A1"
            if kititems == "m4rail":
                kititems = "M4_RISHndgrd_Black"
            if kititems == "m4tele":
                kititems = "M4_OEBttstck"
            if kititems == "mlock":
                kititems = "Glock19"
            if kititems == "cmag30":
                kititems = "Mag_CMAG_30Rnd"
            if kititems == "mlockmag":
                kititems = "Mag_Glock_15Rnd"
            if kititems == "platecarrier":
                kititems = "PlateCarrierVest"
            if kititems == "platepouches":
                kititems = "PlateCarrierPouches"
            if kititems == "knife":
                kititems = "CombatKnife"
            if kititems == "bizon":
                kititems = "PP19"
            if kititems == "bizonmag":
                kititems = "Mag_PP19_64Rnd"
            if kititems == "bizonstck":
                kititems = "PP19_Bttstck"
            if kititems == "tundra":
                kititems = "Winchester70"
            if kititems == "308":
                kititems = "AmmoBox_308Win_20Rnd"
            if kititems == "acog":
                kititems = "ACOGOptic"
            if kititems == "acog6":
                kititems = "ACOGOptic_6x"
            if kititems == "akm":
                kititems = "AKM"
            if kititems == "magakm30":
                kititems = "Mag_AKM_30Rnd"
            if kititems == "pistolsuppressor":
                kititems = "PistolSuppressor"
            if kititems == "fieldv":
                kititems = "HighCapacityVest_Black"
            if kititems == "bandage":
                kititems = "BandageDressing"
            if kititems == "canteen":
                kititems = "Canteen"
            if kititems == "blackmask":
                kititems = "BalaclavaMask_Black"
            if kititems == "blackmaskskull":
                kititems = "BalaclavaMask_Blackskull"
            if kititems == "cargopblack":
                kititems = "CargoPants_Black"
            if kititems == "cargopgray":
                kititems = "CargoPants_Grey"
            if kititems == "cargopgreen":
                kititems = "CargoPants_Green"
            
            
            attachments = f'''
            <attachments>
                <item name="{kititems}"/>
            </attachments>
            '''
            with open(f"{name}\\{name}attachments.txt", "a") as f:
                f.write(f"{attachments}")
                f.close()
        
items()