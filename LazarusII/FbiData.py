import json
import re


class LazarusUnit:
    def __str__(self):
        return 'Name: ' + self.Name + ', Info: ' + self.Description + ', HP: ' + self.MaxDamage + '.'

    def getJsonRepresentation(self):
        the_json = {'Name':self.Name,
                    'Description':self.Description,
                    'Class':self.TEDClass, 'HP':self.MaxDamage,
                    'BuildCostEnergy':self.BuildCostEnergy,
                    'BuildCostMetal':self.BuildCostMetal,
                    'picture': '/static/totala_files2/unitpics/' + self.Objectname + '.png'}
        return json.dumps(the_json)

    def __init__(self):
        self.UnitName = ''
        self.Version = ''
        self.Side = ''
        self.Objectname = ''
        self.Designation = ''
        self.Name = ''
        self.Description = ''
        self.FrenchDescription = ''
        self.GermanDescription = ''
        self.FootprintX = 3
        self.FootprintZ = 3
        self.BuildCostEnergy = 15000
        self.BuildCostMetal = 1500
        self.MaxDamage = 2500
        self.MaxWaterDepth = 35
        self.MaxSlope = 14
        self.EnergyUse = 1
        self.BuildTime = 100
        self.WorkerTime = 0
        self.BMcode = 1
        self.Builder = 0
        self.ThreeD = 1
        self.ZBuffer = 1
        self.NoAutoFire = 0
        self.SightDistance = 300
        self.RadarDistance = 0
        self.SoundCategory = ''
        self.EnergyStorage = 10
        self.MetalStorage = 10
        self.ExplodeAs = ''
        self.SelfDestructAs = ''
        self.Category = ''
        self.TEDClass = ''
        self.Copyright = ''
        self.Corpse = ''
        self.UnitNumber = 21
        self.firestandorders = 1
        self.StandingFireOrder = 2
        self.mobilestandorders = 1
        self.StandingMoveOrder = 1
        self.canmove = 1
        self.canpatrol = 1
        self.canstop = 1
        self.canguard = 1
        self.MaxVelocity = 1
        self.BrakeRate = 0.15
        self.Acceleration = 0.1
        self.TurnRate = 500
        self.SteeringMode = 2
        self.ShootMe = 1
        self.EnergyMake = 2
        self.DefaultMissionType = ''
        self.maneuverleashlength = 500
        self.MovementClass = ''
        self.Upright = 1
        self.Weapon1 = ''
        self.Weapon2 = ''
        self.Weapon3 = ''
        self.wpri_badTargetCategory = ''
        self.BadTargetCategory = ''
        self.canattack = 1
        self.NoChaseCategory = ''

def remove_comments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if match.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, string)

