from django.db import models

# Create your models here.

# = models.CharField(max_length=100)
# = models.FloatField(null=True, blank=True)
# = models.IntegerField()
# = models.BooleanField(default=False)


# SEX = (
#     ('male', 'Male'),
#     ('female', 'Female'),
# )
# sex = models.CharField(choices=SEX, null=True, blank=True, max_length=10)







class Damage(models.Model):
    name = models.CharField(max_length=100, default='default')
    damage_amount = models.IntegerField(default=1230)





# Documentation:
# http://units.tauniverse.com/tutorials/tadesign/tadesign/tdfweapon.htm
class WeaponTDF(models.Model):
    accuracy = models.IntegerField(null=True, blank=True)   # int()
    aimrate = models.IntegerField(null=True, blank=True)   # int()
    areaofeffect = models.IntegerField(null=True, blank=True)   # int()
    ballistic = models.BooleanField(default=False)   # int()
    beamweapon = models.BooleanField(default=False)   # int()
    burnblow = models.BooleanField(default=False)   # int()
    burst = models.IntegerField(default=3, null=True, blank=True)   # int()
    burstrate = models.FloatField(null=True, blank=True)   # float()
    color = models.IntegerField(default=144, null=True, blank=True)   # int()
    color2 = models.IntegerField(default=217, null=True, blank=True)   # int()

    commandfire = models.BooleanField(default=False)   # int()
    cruise = models.BooleanField(default=False)   # int()
    dropped = models.BooleanField(default=False)   # int()
    duration = models.FloatField(null=True, blank=True)   # float()
    edgeeffectiveness = models.FloatField(null=True, blank=True)   # float()
    endsmoke = models.BooleanField(default=False)   # int()
    energy = models.IntegerField(default=3, null=True, blank=True)   # int()
    energypershot = models.IntegerField(default=3, null=True, blank=True)   # int()
    explosionart = models.CharField(max_length=100, default='explode5', null=True, blank=True)
    explosiongaf = models.CharField(max_length=100, default='fx', null=True, blank=True)

    firestarter = models.IntegerField(default=3, null=True, blank=True)   # int()
    flighttime = models.IntegerField(default=3, null=True, blank=True)   # int()
    groundbounce = models.BooleanField(default=False)   # int()
    guidance = models.BooleanField(default=False)   # int()
    ID_weapon = models.IntegerField(default=3, null=True, blank=True)   # int()
    lavaexplosionart = models.CharField(max_length=100, default='lavasplashsm', null=True, blank=True)
    lavaexplosiongaf = models.CharField(max_length=100, default='fx', null=True, blank=True)
    lineofsight = models.BooleanField(default=False)   # int()
    metal = models.IntegerField(default=3, null=True, blank=True)   # int()
    metalpershot = models.IntegerField(default=3, null=True, blank=True)   # int()

    meteor = models.BooleanField(default=False)   # int()
    minbarrelangle = models.IntegerField(default=-15, null=True, blank=True)   # int()
    model = models.CharField(max_length=100, default='missile', null=True, blank=True)
    name = models.CharField(max_length=100, default='Annihilator Weapon Sample', null=True, blank=True)
    noautorange = models.BooleanField(default=False)   # int()
    noexplode = models.BooleanField(default=False)   # int()
    noradar = models.BooleanField(default=False)   # int()
    paralyzer = models.BooleanField(default=False)   # int()
    pitchtolerance = models.IntegerField(default=12000, null=True, blank=True)   # int()
    propeller = models.BooleanField(default=False)   # int()

    randomdecay = models.FloatField(null=True, blank=True)   # float()
    _range = models.IntegerField(default=600, null=True, blank=True)   # int()
    reloadtime = models.FloatField(default=0.5, null=True, blank=True)   # float()
    rendertype = models.IntegerField(default=0, null=True, blank=True)   # int()
    selfprop = models.BooleanField(default=False)   # int()
    shakeduration = models.IntegerField(default=2, null=True, blank=True)   # int()
    shakemagnitude = models.IntegerField(default=2, null=True, blank=True)   # int()
    smokedelay = models.IntegerField(default=600, null=True, blank=True)   # int()
    smoketrail = models.BooleanField(default=False)   # int()
    soundhit = models.CharField(max_length=100, default='xplolrg1', null=True, blank=True)    # 50

    soundstart = models.CharField(max_length=100, default='annigun1', null=True, blank=True)
    soundtrigger = models.BooleanField(default=False)   # int()
    soundwater = models.CharField(max_length=100, default='xplolrg1', null=True, blank=True)
    sprayangle = models.IntegerField(default=1024, null=True, blank=True)   # int()
    startsmoke = models.BooleanField(default=False)   # int()
    startvelocity = models.IntegerField(default=250, null=True, blank=True)   # int()
    stockpile = models.BooleanField(default=False)   # int()
    targetable = models.BooleanField(default=False)   # int()
    tolerance = models.IntegerField(default=8000, null=True, blank=True)   # int()
    tracks = models.BooleanField(default=False)   # int()

    turnrate = models.IntegerField(default=32768, null=True, blank=True)   # int()
    turret = models.BooleanField(default=False)   # int()
    twophase = models.BooleanField(default=False)   # int()
    unitsonly = models.BooleanField(default=False)   # int()
    vlaunch = models.BooleanField(default=False)   # int()
    waterexplosionart = models.CharField(max_length=100, default='h2oboom1', null=True, blank=True)
    waterexplosiongaf = models.CharField(max_length=100, default='fx', null=True, blank=True)
    waterweapon = models.BooleanField(default=False)   # int()
    weaponacceleration = models.IntegerField(default=131, null=True, blank=True)   # int()
    weapontimer = models.FloatField(null=True, blank=True)   # float()

    weapontype2 = models.CharField(max_length=100, default='fx', blank=True)
    weaponvelocity = models.IntegerField(default=131, null=True, blank=True)   # int()
    damage = models.ManyToManyField(Damage)   # 73




class FeatureTDF(models.Model):
    animating = models.BooleanField(default=False)
    animtrans = models.BooleanField(default=False, blank=True)
    autoreclaimable = models.BooleanField(default=True)
    burnmax = models.IntegerField(default=18, null=True, blank=True)
    burnmin = models.IntegerField(default=15, null=True, blank=True)
    burnweapon = models.CharField(blank=True, max_length=95)
    # CATEGORIES = (
    #     ('Arm Corpses', 'arm_corpses'),
    #     ('Core Corpses', 'cor_corpses'),
    #     ('Heaps', 'heaps'),
    #     ('Steamvents', 'steamvents'),
    #     ('Rocks', 'rocks'),
    # )
    category = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=135, null=True, blank=True)
    blocking = models.BooleanField(default=False)
    damage = models.IntegerField(default=1800, null=True, blank=True)
    energy = models.IntegerField(default=250, null=True, blank=True)
    featuredead = models.CharField(max_length=135, null=True, blank=True)
    featurereclamate = models.CharField(max_length=135, null=True, blank=True)
    filename = models.CharField(max_length=135, null=True, blank=True)
    flamable = models.BooleanField(default=False)
    footprintx = models.IntegerField(default=2, null=True, blank=True)
    footprintz = models.IntegerField(default=2, null=True, blank=True)
    geothermal = models.BooleanField(default=False)
    height = models.IntegerField(default=25, null=True, blank=True)
    hitdensity = models.IntegerField(default=25, null=True, blank=True)
    indestructible = models.BooleanField(default=False)
    metal = models.IntegerField(default=250, null=True, blank=True)
    nodisplayinfo = models.BooleanField(default=False)
    _object = models.CharField(max_length=135, null=True, blank=True)
    permanent = models.BooleanField(default=False)
    reclaimable = models.BooleanField(default=True)
    reproduce = models.BooleanField(default=False)
    reproducearea = models.BooleanField(default=False)
    seqname = models.CharField(max_length=135, null=True, blank=True)
    seqnameburn = models.CharField(max_length=135, null=True, blank=True)
    seqnamedie = models.CharField(max_length=135, null=True, blank=True)
    seqnamereclamate = models.CharField(max_length=135, null=True, blank=True)
    seqnameshad = models.CharField(max_length=135, null=True, blank=True)
    shadtrans = models.BooleanField(default=True)
    sparktime = models.IntegerField(default=5, null=True, blank=True)
    spreadchance = models.IntegerField(default=30, null=True, blank=True)
    world = models.CharField(max_length=135, null=True, blank=True)


# choices SelfDestructAS: BIG_UNIT,,,,,,,

# Documentation:
# http://units.tauniverse.com/tutorials/tadesign/tadesign/fbidesc.htm
class UnitFbiData(models.Model):
    _raw_json_dump = models.CharField(max_length=100)
    Acceleration = models.FloatField(null=True, blank=True)
    ActiveWhenBuild = models.IntegerField(null=True, blank=True)
    ai_limit = models.CharField(max_length=101)
    ai_weight = models.CharField(max_length=102)
    altfromsealevel = models.IntegerField(null=True, blank=True)
    amphibious = models.BooleanField(default=False)
    antiweapons = models.BooleanField(default=False)
    attackrunlength = models.IntegerField(null=True, blank=True)
    BMcode = models.BooleanField(default=False)
    BadTargetCategory = models.CharField(max_length=103)
    BankScale = models.IntegerField(null=True, blank=True)
    BrakeRate = models.IntegerField(null=True, blank=True)
    BuildAngle = models.IntegerField(null=True, blank=True)
    BuildCostEnergy = models.IntegerField(null=True, blank=True)
    BuildCostMetal = models.IntegerField(null=True, blank=True)
    BuildTime = models.IntegerField(null=True, blank=True)
    Builddistance = models.IntegerField(null=True, blank=True)
    Builder = models.BooleanField(default=False)
    canattack = models.BooleanField(default=False)
    CanCapture = models.BooleanField(default=False)
    CanDgun = models.BooleanField(default=False)
    Canfly = models.BooleanField(default=False)
    canguard = models.BooleanField(default=False)
    canhover = models.BooleanField(default=False)
    canload = models.BooleanField(default=False)
    canmove = models.BooleanField(default=False)
    canpatrol = models.BooleanField(default=False)
    CanReclamate = models.BooleanField(default=False)
    canstop = models.BooleanField(default=True)
    cantbetransported = models.BooleanField(default=False)
    Category = models.CharField(max_length=104)
    CloakCost = models.IntegerField(null=True, blank=True)
    CloakCostMoving = models.IntegerField(null=True, blank=True)
    Commander = models.BooleanField(default=False)
    Copyright = models.CharField(max_length=105)
    #TODO: PK below
    Corpse = models.CharField(max_length=106)
    cruisealt = models.IntegerField(null=True, blank=True)
    DamageModifier = models.FloatField(null=True, blank=True)
    DefaultMissionType = models.CharField(max_length=107)
    Description = models.CharField(max_length=255)
    Designation = models.CharField(max_length=50)
    digger = models.BooleanField(default=False)
    Downloadable = models.BooleanField(default=False)
    EnergyMake = models.IntegerField(null=True, blank=True)
    EnergyStorage = models.IntegerField(null=True, blank=True)
    EnergyUse = models.IntegerField(null=True, blank=True)
    # TODO: Many-To-One
    ExplodeAs = models.CharField(max_length=108)
    ExtractsMetal = models.FloatField(null=True, blank=True)
    firestandorders = models.IntegerField(null=True, blank=True) # 50
    Floater = models.BooleanField(default=False)
    FootprintX = models.IntegerField(null=True, blank=True)
    FootprintZ = models.IntegerField(null=True, blank=True)
    FrenchDescription = models.CharField(max_length=109)
    FrenchName = models.CharField(max_length=110)
    GermanDescription = models.CharField(max_length=111)
    GermanName = models.CharField(max_length=112)
    HealTime = models.IntegerField(null=True, blank=True)
    HideDamage = models.BooleanField(default=False)
    HoverAttack = models.BooleanField(default=False) #60
    ImmuneToParalyzer = models.BooleanField(default=False)
    init_cloaked = models.BooleanField(default=False)
    IsAirBase = models.BooleanField(default=False)
    IsFeature = models.BooleanField(default=False)
    istargetingupgrade = models.BooleanField(default=False)
    ItalianDescription = models.CharField(max_length=113)
    ItalianName = models.CharField(max_length=114)
    JapanesDescription = models.CharField(max_length=115)
    JapaneseName = models.CharField(max_length=116)
    kamikaze = models.BooleanField(default=False) # 70
    kamikazedistance = models.IntegerField(null=True, blank=True)
    MakesMetal = models.BooleanField(default=False)
    maneuverleashlength = models.IntegerField(null=True, blank=True)
    MaxDamage = models.IntegerField(null=True, blank=True)
    MaxSlope = models.IntegerField(null=True, blank=True)
    MaxVelocity = models.IntegerField(null=True, blank=True)
    MaxWaterDepth = models.IntegerField(null=True, blank=True)
    MetalMake = models.IntegerField(null=True, blank=True)
    MetalStorage = models.IntegerField(null=True, blank=True)
    mincloakdistance = models.IntegerField(null=True, blank=True)
    MinWaterDepth = models.IntegerField(null=True, blank=True)
    MobileStandOrders = models.BooleanField(default=False)
    MoveRate1 = models.IntegerField(null=True, blank=True)
    # TODO: PK below:
    # MOVEMENT_CLASSES = (
    #     ('Tank1', 'TANKSH1'),
    #     ('Tank SH2 (example: Arm Fark)', 'TANKSH2'),
    #     ('Tank SH3 (example: Arm Podger)', 'TANKSH3'),
    #     ('Tank DS2 (example: Core Necro)', 'TANKSH2'),
    #     ('Tank (example: core sumo)', 'TANKBH3'),
    #     ('', ''),
    #     ('', ''),
    #     ('Kbot S1', 'KBOTSS1'),
    #     ('Kbot S2', 'KBOTSS2'),
    #     ('Kbot S3', 'KBOTSS3'),
    #     ('', ''),
    #     ('', ''),
    #     ('Spider', 'SPID3'),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('Boats S4 (used by small boats?)', 'BOATS4'),
    #     ('', ''),
    # )
    MovementClass = models.CharField(max_length=117)
    Name = models.CharField(max_length=100)
    NoAutoFire = models.BooleanField(default=False)
    NoChaseCategory = models.CharField(max_length=118)
    norestrict = models.BooleanField(default=False)
    NoShadow = models.BooleanField(default=False)
    # TODO: PK below
    Objectname = models.CharField(max_length=119)
    onoffable = models.BooleanField(default=False)
    Ovradjust = models.BooleanField(default=False)
    PigLatinDescription = models.CharField(max_length=120)
    PigLatinName = models.CharField(max_length=121)
    PitchScale = models.IntegerField(max_length=122, null=True, blank=True)
    RadarDistance = models.IntegerField(null=True, blank=True)
    RadarDistanceJam = models.IntegerField(null=True, blank=True)
    Scale = models.IntegerField(null=True, blank=True)
    # TODO: List of string choices will go below
    SelfDestructAs = models.CharField(max_length=123) # ✦ ✦ ✦
    selfdestructcountdown = models.IntegerField(null=True, blank=True) # 100
    ShootMe = models.BooleanField(default=False)
    ShowPlayerName = models.BooleanField(default=False)
    # TODO: List of string choices will go below
    Side = models.CharField(max_length=124) # ✦ ✦ ✦
    SightDistance = models.IntegerField(null=True, blank=True)
    SonarDistance = models.IntegerField(null=True, blank=True)
    SonarDistanceJam = models.IntegerField(null=True, blank=True)
    sortbias = models.IntegerField(null=True, blank=True)
    # TODO: List of string choices will go below
    SoundCategory = models.CharField(max_length=125)
    SpanishDescription = models.CharField(max_length=126)
    SpanishName = models.CharField(max_length=127)
    StandingFireOrder = models.IntegerField(null=True, blank=True)
    StandingMoveOrder = models.IntegerField(null=True, blank=True)
    Stealth = models.BooleanField(default=False)
    SteeringMode = models.IntegerField(null=True, blank=True)
    # TODO: List of string choices will go below
    TEDClass = models.CharField(max_length=128)
    teleporter = models.BooleanField(default=False)
    ThreeD = models.BooleanField(default=False)
    TidalGenerator = models.BooleanField(default=False)
    TransMaxUnits = models.IntegerField(null=True, blank=True)
    transportcapacity = models.IntegerField(null=True, blank=True)
    transportsize = models.IntegerField(null=True, blank=True)
    TurnRate = models.IntegerField(null=True, blank=True)
    # TODO: unique? ID?
    UnitName = models.CharField(max_length=129, unique=True) # ✦ ✦ ✦
    # TODO: must be unique, PK?
    UnitNumber = models.IntegerField(unique=True) # ✦ ✦ ✦
    Upright = models.BooleanField(default=False)
    Version = models.IntegerField(null=True, blank=True) # ✦ ✦ ✦
    WaterLine = models.IntegerField(null=True, blank=True)
    # TODO: PK below
    Weapon_One = models.ForeignKey(WeaponTDF, on_delete=models.CASCADE, related_name='Weapon1', null=True, blank=True)
    # TODO: PK below
    Name_Weapon_Two = models.ForeignKey(WeaponTDF, on_delete=models.CASCADE, related_name='Weapon2', null=True, blank=True)
    # TODO: PK below
    Name_Weapon_Three = models.ForeignKey(WeaponTDF, on_delete=models.CASCADE, related_name='Weapon3', null=True, blank=True)
    WindGenerator = models.IntegerField(null=True, blank=True)
    WorkerTime = models.IntegerField(null=True, blank=True)
    # TODO: PK below
    wpri_badTargetCategory = models.CharField(max_length=130, null=True, blank=True)
    # TODO: ManyToMany below
    wsec_badTargetCategory = models.CharField(max_length=131, null=True, blank=True)
    YardMap = models.CharField(max_length=132) #135
    ZBuffer = models.IntegerField(default=1, null=True, blank=False)
    def __str__(self):  # __unicode__ on Python 2
        return self.Objectname

# Documentation:
# http://units.tauniverse.com/tutorials/tadesign/tadesign/tdfdown.htm
class DownloadTDF(models.Model):
    parent_unit = models.ForeignKey(UnitFbiData, on_delete=models.CASCADE,)
    MENUENTRY = models.CharField(max_length=20,
                                     default='MENUENTRY1')  # [MENUENTRY1] [MENUENTRY2] [MENUENTRY3] etc...
    BUTTON = models.PositiveSmallIntegerField(default=0)  # See 'TA Button' below
    MENU = models.PositiveSmallIntegerField(default=2)  # first menu in TA is actually '2' for some reason
    UNITMENU = models.CharField(max_length=35, null=True, blank=True)  # short name for the construction unit that builds this unit
    UNITNAME = models.CharField(max_length=35, null=True, blank=True)  # short name of the unit this button builds
