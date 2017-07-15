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
    ballistic = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    beamweapon = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    burnblow = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    burst = models.IntegerField(default=3, null=True, blank=True)   # int()
    burstrate = models.FloatField(null=True, blank=True)   # float()
    color = models.IntegerField(default=144, null=True, blank=True)   # int()
    color2 = models.IntegerField(default=217, null=True, blank=True)   # int()

    commandfire = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    cruise = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    dropped = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    duration = models.FloatField(null=True, blank=True)   # float()
    edgeeffectiveness = models.FloatField(null=True, blank=True)   # float()
    endsmoke = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    energy = models.IntegerField(default=3, null=True, blank=True)   # int()
    energypershot = models.IntegerField(default=3, null=True, blank=True)   # int()
    explosionart = models.CharField(max_length=100, default='explode5', null=True, blank=True)
    explosiongaf = models.CharField(max_length=100, default='fx', null=True, blank=True)

    firestarter = models.IntegerField(default=3, null=True, blank=True)   # int()
    flighttime = models.IntegerField(default=3, null=True, blank=True)   # int()
    groundbounce = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    guidance = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    ID_weapon = models.IntegerField(default=3, null=True, blank=True)   # int()
    lavaexplosionart = models.CharField(max_length=100, default='lavasplashsm', null=True, blank=True)
    lavaexplosiongaf = models.CharField(max_length=100, default='fx', null=True, blank=True)
    lineofsight = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    metal = models.IntegerField(default=3, null=True, blank=True)   # int()
    metalpershot = models.IntegerField(default=3, null=True, blank=True)   # int()

    meteor = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    minbarrelangle = models.IntegerField(default=-15, null=True, blank=True)   # int()
    model = models.CharField(max_length=100, default='missile', null=True, blank=True)
    name = models.CharField(max_length=100, default='Annihilator Weapon Sample', null=True, blank=True)
    noautorange = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    noexplode = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    noradar = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    paralyzer = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    pitchtolerance = models.IntegerField(default=12000, null=True, blank=True)   # int()
    propeller = models.PositiveSmallIntegerField(null=True, blank=True)   # int()

    randomdecay = models.FloatField(null=True, blank=True)   # float()
    _range = models.IntegerField(default=600, null=True, blank=True)   # int()
    reloadtime = models.FloatField(default=0.5, null=True, blank=True)   # float()
    rendertype = models.IntegerField(default=0, null=True, blank=True)   # int()
    selfprop = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    shakeduration = models.IntegerField(default=2, null=True, blank=True)   # int()
    shakemagnitude = models.IntegerField(default=2, null=True, blank=True)   # int()
    smokedelay = models.IntegerField(default=600, null=True, blank=True)   # int()
    smoketrail = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    soundhit = models.CharField(max_length=100, default='xplolrg1', null=True, blank=True)    # 50

    soundstart = models.CharField(max_length=100, default='annigun1', null=True, blank=True)
    soundtrigger = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    soundwater = models.CharField(max_length=100, default='xplolrg1', null=True, blank=True)
    sprayangle = models.IntegerField(default=1024, null=True, blank=True)   # int()
    startsmoke = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    startvelocity = models.IntegerField(default=250, null=True, blank=True)   # int()
    stockpile = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    targetable = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    tolerance = models.IntegerField(default=8000, null=True, blank=True)   # int()
    tracks = models.PositiveSmallIntegerField(null=True, blank=True)   # int()

    turnrate = models.IntegerField(default=32768, null=True, blank=True)   # int()
    turret = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    twophase = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    unitsonly = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    vlaunch = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    waterexplosionart = models.CharField(max_length=100, default='h2oboom1', null=True, blank=True)
    waterexplosiongaf = models.CharField(max_length=100, default='fx', null=True, blank=True)
    waterweapon = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    weaponacceleration = models.IntegerField(default=131, null=True, blank=True)   # int()
    weapontimer = models.FloatField(null=True, blank=True)   # float()

    weapontype2 = models.CharField(max_length=100, default='fx', blank=True)
    weaponvelocity = models.IntegerField(default=131, null=True, blank=True)   # int()
    damage = models.ManyToManyField(Damage)   # 73




class FeatureTDF(models.Model):
    animating = models.PositiveSmallIntegerField(null=True, blank=True)
    animtrans = models.PositiveSmallIntegerField(null=True, blank=True, blank=True)
    autoreclaimable = models.BooleanField(default=True)
    burnmax = models.IntegerField(default=18, null=True, blank=True)
    burnmin = models.IntegerField(default=15, null=True, blank=True)
    burnweapon = models.CharField(blank=True, max_length=95)
    category = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=135, null=True, blank=True)
    blocking = models.PositiveSmallIntegerField(null=True, blank=True)
    damage = models.IntegerField(default=1800, null=True, blank=True)
    energy = models.IntegerField(default=250, null=True, blank=True)
    featuredead = models.CharField(max_length=135, null=True, blank=True)
    featurereclamate = models.CharField(max_length=135, null=True, blank=True)
    filename = models.CharField(max_length=135, null=True, blank=True)
    flamable = models.PositiveSmallIntegerField(null=True, blank=True)
    footprintx = models.IntegerField(default=2, null=True, blank=True)
    footprintz = models.IntegerField(default=2, null=True, blank=True)
    geothermal = models.PositiveSmallIntegerField(null=True, blank=True)
    height = models.IntegerField(default=25, null=True, blank=True)
    hitdensity = models.IntegerField(default=25, null=True, blank=True)
    indestructible = models.PositiveSmallIntegerField(null=True, blank=True)
    metal = models.IntegerField(default=250, null=True, blank=True)
    nodisplayinfo = models.PositiveSmallIntegerField(null=True, blank=True)
    _object = models.CharField(max_length=135, null=True, blank=True, unique=True)
    permanent = models.PositiveSmallIntegerField(null=True, blank=True)
    reclaimable = models.BooleanField(default=True)
    reproduce = models.PositiveSmallIntegerField(null=True, blank=True)
    reproducearea = models.PositiveSmallIntegerField(null=True, blank=True)
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
    amphibious = models.PositiveSmallIntegerField(null=True, blank=True)
    antiweapons = models.PositiveSmallIntegerField(null=True, blank=True)
    attackrunlength = models.IntegerField(null=True, blank=True)
    BMcode = models.PositiveSmallIntegerField(null=True, blank=True)
    BadTargetCategory = models.CharField(max_length=103)
    BankScale = models.IntegerField(null=True, blank=True)
    BrakeRate = models.IntegerField(null=True, blank=True)
    BuildAngle = models.IntegerField(null=True, blank=True)
    BuildCostEnergy = models.IntegerField(null=True, blank=True)
    BuildCostMetal = models.IntegerField(null=True, blank=True)
    BuildTime = models.IntegerField(null=True, blank=True)
    Builddistance = models.IntegerField(null=True, blank=True)
    Builder = models.PositiveSmallIntegerField(null=True, blank=True)
    canattack = models.PositiveSmallIntegerField(null=True, blank=True)
    CanCapture = models.PositiveSmallIntegerField(null=True, blank=True)
    CanDgun = models.PositiveSmallIntegerField(null=True, blank=True)
    Canfly = models.PositiveSmallIntegerField(null=True, blank=True)
    canguard = models.PositiveSmallIntegerField(null=True, blank=True)
    canhover = models.PositiveSmallIntegerField(null=True, blank=True)
    canload = models.PositiveSmallIntegerField(null=True, blank=True)
    canmove = models.PositiveSmallIntegerField(null=True, blank=True)
    canpatrol = models.PositiveSmallIntegerField(null=True, blank=True)
    CanReclamate = models.PositiveSmallIntegerField(null=True, blank=True)
    canstop = models.BooleanField(default=True)
    cantbetransported = models.PositiveSmallIntegerField(null=True, blank=True)
    Category = models.CharField(max_length=104)
    CloakCost = models.IntegerField(null=True, blank=True)
    CloakCostMoving = models.IntegerField(null=True, blank=True)
    Commander = models.PositiveSmallIntegerField(null=True, blank=True)
    Copyright = models.CharField(max_length=105)
    #TODO: PK below
    Corpse = models.CharField(max_length=106)
    cruisealt = models.IntegerField(null=True, blank=True)
    DamageModifier = models.FloatField(null=True, blank=True)
    DefaultMissionType = models.CharField(max_length=107)
    Description = models.CharField(max_length=255)
    Designation = models.CharField(max_length=50)
    digger = models.PositiveSmallIntegerField(null=True, blank=True)
    Downloadable = models.PositiveSmallIntegerField(null=True, blank=True)
    EnergyMake = models.IntegerField(null=True, blank=True)
    EnergyStorage = models.IntegerField(null=True, blank=True)
    EnergyUse = models.IntegerField(null=True, blank=True)
    # TODO: Many-To-One
    ExplodeAs = models.CharField(max_length=108)
    ExtractsMetal = models.FloatField(null=True, blank=True)
    firestandorders = models.IntegerField(null=True, blank=True) # 50
    Floater = models.PositiveSmallIntegerField(null=True, blank=True)
    FootprintX = models.IntegerField(null=True, blank=True)
    FootprintZ = models.IntegerField(null=True, blank=True)
    FrenchDescription = models.CharField(max_length=109)
    FrenchName = models.CharField(max_length=110)
    GermanDescription = models.CharField(max_length=111)
    GermanName = models.CharField(max_length=112)
    HealTime = models.IntegerField(null=True, blank=True)
    HideDamage = models.PositiveSmallIntegerField(null=True, blank=True)
    HoverAttack = models.PositiveSmallIntegerField(null=True, blank=True) #60
    ImmuneToParalyzer = models.PositiveSmallIntegerField(null=True, blank=True)
    init_cloaked = models.PositiveSmallIntegerField(null=True, blank=True)
    IsAirBase = models.PositiveSmallIntegerField(null=True, blank=True)
    IsFeature = models.PositiveSmallIntegerField(null=True, blank=True)
    istargetingupgrade = models.PositiveSmallIntegerField(null=True, blank=True)
    ItalianDescription = models.CharField(max_length=113)
    ItalianName = models.CharField(max_length=114)
    JapanesDescription = models.CharField(max_length=115)
    JapaneseName = models.CharField(max_length=116)
    kamikaze = models.PositiveSmallIntegerField(null=True, blank=True) # 70
    kamikazedistance = models.IntegerField(null=True, blank=True)
    MakesMetal = models.PositiveSmallIntegerField(null=True, blank=True)
    maneuverleashlength = models.IntegerField(null=True, blank=True)
    MaxDamage = models.IntegerField(null=True, blank=True)
    MaxSlope = models.IntegerField(null=True, blank=True)
    MaxVelocity = models.IntegerField(null=True, blank=True)
    MaxWaterDepth = models.IntegerField(null=True, blank=True)
    MetalMake = models.IntegerField(null=True, blank=True)
    MetalStorage = models.IntegerField(null=True, blank=True)
    mincloakdistance = models.IntegerField(null=True, blank=True)
    MinWaterDepth = models.IntegerField(null=True, blank=True)
    MobileStandOrders = models.PositiveSmallIntegerField(null=True, blank=True)
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
    NoAutoFire = models.PositiveSmallIntegerField(null=True, blank=True)
    NoChaseCategory = models.CharField(max_length=118)
    norestrict = models.PositiveSmallIntegerField(null=True, blank=True)
    NoShadow = models.PositiveSmallIntegerField(null=True, blank=True)
    # TODO: PK below
    Objectname = models.CharField(max_length=119)
    onoffable = models.PositiveSmallIntegerField(null=True, blank=True)
    Ovradjust = models.PositiveSmallIntegerField(null=True, blank=True)
    PigLatinDescription = models.CharField(max_length=120)
    PigLatinName = models.CharField(max_length=121)
    PitchScale = models.IntegerField(max_length=122, null=True, blank=True)
    RadarDistance = models.IntegerField(null=True, blank=True)
    RadarDistanceJam = models.IntegerField(null=True, blank=True)
    Scale = models.IntegerField(null=True, blank=True)
    # TODO: List of string choices will go below
    SelfDestructAs = models.CharField(max_length=123) # ✦ ✦ ✦
    selfdestructcountdown = models.IntegerField(null=True, blank=True) # 100
    ShootMe = models.PositiveSmallIntegerField(null=True, blank=True)
    ShowPlayerName = models.PositiveSmallIntegerField(null=True, blank=True)
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
    Stealth = models.PositiveSmallIntegerField(null=True, blank=True)
    SteeringMode = models.IntegerField(null=True, blank=True)
    # TODO: List of string choices will go below
    TEDClass = models.CharField(max_length=128)
    teleporter = models.PositiveSmallIntegerField(null=True, blank=True)
    ThreeD = models.PositiveSmallIntegerField(null=True, blank=True)
    TidalGenerator = models.PositiveSmallIntegerField(null=True, blank=True)
    TransMaxUnits = models.IntegerField(null=True, blank=True)
    transportcapacity = models.IntegerField(null=True, blank=True)
    transportsize = models.IntegerField(null=True, blank=True)
    TurnRate = models.IntegerField(null=True, blank=True)
    # TODO: unique? ID?
    UnitName = models.CharField(max_length=129, unique=True) # ✦ ✦ ✦
    # TODO: must be unique, PK?
    UnitNumber = models.IntegerField(unique=True) # ✦ ✦ ✦
    Upright = models.PositiveSmallIntegerField(null=True, blank=True)
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