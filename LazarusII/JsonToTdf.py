import json
from django.core import serializers
from LazarusII.models import WeaponTDF






sampleWeapon = WeaponTDF.objects.filter(id=2359)
serialized_obj = serializers.serialize("json", sampleWeapon)



### NOW WE HAVE:
"""
[{"model": "LazarusII.weapontdf", "pk": 2359, "fields": {"_DEV_root_data_path": "/usr/src/persistent/media/ta_data/mattsAbel/weapons/anabel_gun.tdf", "_OBJECT_KEY_NAME": "ANAbel_Gun", "_Lazarus_Identifier": "ANAbel_Gun_79", "_SNOWFLAKE": "nan", "accuracy": 2000, "aimrate": null, "areaofeffect": 220, "ballistic": 1, "beamweapon": null, "burnblow": null, "burst": 3, "burstrate": null, "color": 144, "color2": 217, "commandfire": null, "cruise": null, "dropped": null, "duration": null, "edgeeffectiveness": null, "endsmoke": null, "energy": 3, "energypershot": 50, "explosionart": "explode5", "explosiongaf": "fx", "firestarter": 50, "flighttime": 3, "groundbounce": null, "guidance": null, "ID_weapon": 79, "lavaexplosionart": "lavasplashlg", "lavaexplosiongaf": "fx", "lineofsight": null, "metal": 3, "metalpershot": 3, "meteor": null, "minbarrelangle": -15, "model": "Battleshipshell", "name": "Abel\'s Cannon", "noautorange": null, "noexplode": null, "noradar": null, "paralyzer": null, "pitchtolerance": 12000, "propeller": null, "randomdecay": null, "_range": 3325, "reloadtime": 0.8, "rendertype": 1, "selfprop": null, "shakeduration": 2, "shakemagnitude": 2, "smokedelay": 600, "smoketrail": null, "soundhit": "xplolrg1", "soundstart": "Abel-fire", "soundtrigger": null, "soundwater": "xplolrg1", "sprayangle": 1024, "startsmoke": 1, "startvelocity": 250, "stockpile": null, "targetable": null, "tolerance": 28000, "tracks": null, "turnrate": 32768, "turret": null, "twophase": null, "unitsonly": null, "vlaunch": null, "waterexplosionart": "h2oboom2", "waterexplosiongaf": "fx", "waterweapon": null, "weaponacceleration": 131, "weapontimer": null, "weapontype2": "fx", "weaponvelocity": 550, "damage": [7874]}}]
"""





dict_object = json.loads(serialized_obj)
singleWeaponTdfDict = dict_object[0]['fields']
singleWeaponTdfStr = json.dumps(singleWeaponTdfDict)


parse1 = singleWeaponTdfStr.replace(',', ';')
parse2 = parse1.replace(':', '=')
parse3 = parse2.replace('"', '')








"""

{
    vlaunch= null;
    metalpershot= 3;
    propeller= null;
    flighttime= 3;
    _SNOWFLAKE= nan;
    duration= null;
    startsmoke= 1;
    cruise= null;
    _range= 3325;
    shakeduration= 2;
    twophase= null;
    startvelocity= 250;
    lavaexplosionart= lavasplashlg;
    burnblow= null;
    beamweapon= null;
    firestarter= 50;
    weaponvelocity= 550;
    color= 144;
    weapontimer= null;
    soundtrigger= null;
    weaponacceleration= 131;
    lavaexplosiongaf= fx;
    lineofsight= null;
    stockpile= null;
    paralyzer= null;
    areaofeffect= 220;
    explosiongaf= fx;
    noexplode= null;
    ballistic= 1;
    smoketrail= null;
    damage= [7874];
    reloadtime= 0.8;
    smokedelay= 600;
    turret= null;
    sprayangle= 1024;
    groundbounce= null;
    energy= 3;
    unitsonly= null;
    noradar= null;
    accuracy= 2000;
    energypershot= 50;
    tracks= null;
    noautorange= null;
    minbarrelangle= -15;
    shakemagnitude= 2;
    _OBJECT_KEY_NAME= ANAbel_Gun;
    dropped= null;
    endsmoke= null;
    explosionart= explode5;
    tolerance= 28000;
    commandfire= null;
    aimrate= null;
    _Lazarus_Identifier= ANAbel_Gun_79;
    soundstart= Abel-fire;
    waterexplosionart= h2oboom2;
    name= Abel's Cannon;
    weapontype2= fx;
    randomdecay= null;
    metal= 3;
    soundhit= xplolrg1;
    guidance= null;
    waterexplosiongaf= fx;
    turnrate= 32768;
    model= Battleshipshell;
    edgeeffectiveness= null;
    selfprop= null;
    burst= 3;
    _DEV_root_data_path= /usr/src/persistent/media/ta_data/mattsAbel/weapons/anabel_gun.tdf;
    rendertype= 1;
    targetable= null;
    soundwater= xplolrg1;
    color2= 217;
    waterweapon= null;
    ID_weapon= 79;
    burstrate= null;
    meteor= null;
    pitchtolerance= 12000
}

"""
