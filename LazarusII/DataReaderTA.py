import os
from os import walk
from os import listdir
from os.path import isfile, join
from PIL import Image
import json

from LazarusII.PyColors import bcolors, printError, printWarning, printInfo, printLog, printDebug
from LazarusII.FbiData import LazarusUnit, remove_comments


def readFile(file_path):
    allUnitInstances = []
    # file_object = open(file_path, 'r', errors='replace')
    # unit_object_rawstr = file_object.read()

    # printDebug('reading file: ' + file_path, 'readFile DataReaderTA.py')
    f2 = open(file_path, 'r', errors='replace')
    f3 = open(file_path, 'r', errors='replace')

    i = sum(1 for line in f2)
    u = LazarusUnit()
    while i > 0:
        thisLine = remove_comments(f3.readline())
        if '{' in thisLine:
            u = LazarusUnit()
        elif '}' in thisLine:
            allUnitInstances.append(u.getJsonRepresentation())
        elif '=' in thisLine:
            keyVal = thisLine.split('=')
            keyVal[1] = keyVal[1].replace(';', '')
            if 'UnitName' in keyVal[0]:
                u.UnitName = keyVal[1].replace('\n', '')
            elif 'Version' in keyVal[0]:
                u.Version = keyVal[1].replace('\n', '')
            elif 'Side' in keyVal[0]:
                u.Side = keyVal[1].replace('\n', '')
            elif 'Objectname' in keyVal[0]:
                u.Objectname = keyVal[1].replace('\n', '')
            elif 'Designation' in keyVal[0]:
                u.Designation = keyVal[1].replace('\n', '')
            elif 'Name' in keyVal[0]:
                u.Name = keyVal[1].replace('\n', '')
            elif 'Description' in keyVal[0]:
                u.Description = keyVal[1].replace('\n', '')
            elif 'FrenchDescription' in keyVal[0]:
                u.FrenchDescription = keyVal[1].replace('\n', '')
            elif 'GermanDescription' in keyVal[0]:
                u.GermanDescription = keyVal[1]
            elif 'FootprintX' in keyVal[0]:
                u.FootprintX = keyVal[1].replace('\n', '')
            elif 'FootprintZ' in keyVal[0]:
                u.FootprintZ = keyVal[1].replace('\n', '')
            elif 'BuildCostEnergy' in keyVal[0]:
                u.BuildCostEnergy = keyVal[1].replace('\n', '')
            elif 'BuildCostMetal' in keyVal[0]:
                u.BuildCostMetal = keyVal[1].replace('\n', '')
            elif 'MaxDamage' in keyVal[0]:
                u.MaxDamage = keyVal[1].replace('\n', '')
            elif 'MaxWaterDepth' in keyVal[0]:
                u.MaxWaterDepth = keyVal[1].replace('\n', '')
            elif 'MaxSlope' in keyVal[0]:
                u.MaxSlope = keyVal[1].replace('\n', '')
            elif 'EnergyUse' in keyVal[0]:
                u.EnergyUse = keyVal[1].replace('\n', '')
            elif 'BuildTime' in keyVal[0]:
                u.BuildTime = keyVal[1].replace('\n', '')
            elif 'WorkerTime' in keyVal[0]:
                u.WorkerTime = keyVal[1].replace('\n', '')
            elif 'BMcode' in keyVal[0]:
                u.BMcode = keyVal[1].replace('\n', '')
            elif 'ThreeD' in keyVal[0]:
                u.ThreeD = keyVal[1].replace('\n', '')
            elif 'ZBuffer' in keyVal[0]:
                u.ZBuffer = keyVal[1].replace('\n', '')
            elif 'NoAutoFire' in keyVal[0]:
                u.NoAutoFire = keyVal[1].replace('\n', '')
            elif 'SightDistance' in keyVal[0]:
                u.SightDistance = keyVal[1].replace('\n', '')
            elif 'RadarDistance' in keyVal[0]:
                u.RadarDistance = keyVal[1].replace('\n', '')
            elif 'SoundCategory' in keyVal[0]:
                u.SoundCategory = keyVal[1].replace('\n', '')
            elif 'EnergyStorage' in keyVal[0]:
                u.EnergyStorage = keyVal[1].replace('\n', '')
            elif 'MetalStorage' in keyVal[0]:
                u.MetalStorage = keyVal[1].replace('\n', '')
            elif 'ExplodeAs' in keyVal[0]:
                u.ExplodeAs = keyVal[1].replace('\n', '')
            elif 'SelfDestructAs' in keyVal[0]:
                u.SelfDestructAs = keyVal[1].replace('\n', '')
            elif 'Category' in keyVal[0]:
                u.Category = keyVal[1].replace('\n', '')
            elif 'TEDClass' in keyVal[0]:
                u.TEDClass = keyVal[1].replace('\n', '')
            elif 'Copyright' in keyVal[0]:
                u.Copyright = keyVal[1].replace('\n', '')
            elif 'Corpse' in keyVal[0]:
                u.Corpse = keyVal[1].replace('\n', '')
            elif 'UnitNumber' in keyVal[0]:
                u.UnitNumber = keyVal[1].replace('\n', '')
            elif 'firestandorders' in keyVal[0]:
                u.firestandorders = keyVal[1].replace('\n', '')
            elif 'StandingFireOrder' in keyVal[0]:
                u.StandingFireOrder = keyVal[1].replace('\n', '')
            elif 'mobilestandorders' in keyVal[0]:
                u.mobilestandorders = keyVal[1].replace('\n', '')
            elif 'StandingMoveOrder' in keyVal[0]:
                u.StandingMoveOrder = keyVal[1].replace('\n', '')
            elif 'canmove' in keyVal[0]:
                u.canmove = keyVal[1].replace('\n', '')
            elif 'canpatrol' in keyVal[0]:
                u.canpatrol = keyVal[1].replace('\n', '')
            elif 'canstop' in keyVal[0]:
                u.canstop = keyVal[1].replace('\n', '')
            elif 'canguard' in keyVal[0]:
                u.canguard = keyVal[1].replace('\n', '')
            elif 'MaxVelocity' in keyVal[0]:
                u.MaxVelocity = keyVal[1].replace('\n', '')
            elif 'BrakeRate' in keyVal[0]:
                u.BrakeRate = keyVal[1].replace('\n', '')
            elif 'Acceleration' in keyVal[0]:
                u.Acceleration = keyVal[1].replace('\n', '')
            elif 'TurnRate' in keyVal[0]:
                u.TurnRate = keyVal[1].replace('\n', '')
            elif 'SteeringMode' in keyVal[0]:
                u.SteeringMode = keyVal[1].replace('\n', '')
            elif 'ShootMe' in keyVal[0]:
                u.ShootMe = keyVal[1].replace('\n', '')
            elif 'EnergyMake' in keyVal[0]:
                u.EnergyMake = keyVal[1].replace('\n', '')
            elif 'DefaultMissionType' in keyVal[0]:
                u.DefaultMissionType = keyVal[1].replace('\n', '')
            elif 'maneuverleashlength' in keyVal[0]:
                u.maneuverleashlength = keyVal[1].replace('\n', '')
            elif 'MovementClass' in keyVal[0]:
                u.MovementClass = keyVal[1].replace('\n', '')
            elif 'Upright' in keyVal[0]:
                u.Upright = keyVal[1].replace('\n', '')
            elif 'Weapon1' in keyVal[0]:
                u.Weapon1 = keyVal[1].replace('\n', '')
            elif 'Weapon2' in keyVal[0]:
                u.Weapon2 = keyVal[1].replace('\n', '')
            elif 'Weapon3' in keyVal[0]:
                u.Weapon3 = keyVal[1].replace('\n', '')
            elif 'wpri_badTargetCategory' in keyVal[0]:
                u.wpri_badTargetCategory = keyVal[1].replace('\n', '')
            elif 'BadTargetCategory' in keyVal[0]:
                u.BadTargetCategory = keyVal[1].replace('\n', '')
            elif 'canattack' in keyVal[0]:
                u.canattack = keyVal[1].replace('\n', '')
            elif 'NoChaseCategory' in keyVal[0]:
                u.NoChaseCategory = keyVal[1].replace('\n', '')
        i -= 1

    # printLog('file reading has been completed:')
    # printInfo(file_path)
    return allUnitInstances


