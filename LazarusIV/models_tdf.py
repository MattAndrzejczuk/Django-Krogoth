from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User
from django.contrib.postgres.fields import HStoreField




class ModProject(models.Model):
    author = models.ForeignKey(JawnUser, related_name='mod_developer', )
    is_public = models.BooleanField(default=True)

class CavedogBase(PolymorphicModel):
    keyname = models.CharField(max_length=250)
    snowflake = models.CharField(max_length=50)
    thumbnail_url = models.CharField(max_length=250)
    raw_tdf = models.CharField(max_length=1550)
    data_dict = HStoreField()

class LazarusBase(CavedogBase):
    is_deleted = models.BooleanField(default=False)
    mod_proj = models.ForeignKey(ModProject, on_delete=models.CASCADE)


class Damage(models.Model):
    name = models.CharField(max_length=100, default='default')
    damage_amount = models.IntegerField(default=1230)
    weapon_id = models.IntegerField(default=0)
    def __str__(self):  # __unicode__ on Python 2
        return self.name + '_'


class LazarusWeaponTDF(LazarusBase):
    accuracy = models.IntegerField(null=True, blank=True)   # int()
    aimrate = models.IntegerField(null=True, blank=True)   # int()
    areaofeffect = models.IntegerField(null=True, blank=True)   # int()
    ballistic = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    beamweapon = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    burnblow = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    burst = models.IntegerField(null=True, blank=True)   # int()
    burstrate = models.FloatField(null=True, blank=True)   # float()
    color = models.IntegerField(null=True, blank=True)   # int()
    color2 = models.IntegerField(null=True, blank=True)   # int()

    commandfire = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    cruise = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    dropped = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    duration = models.FloatField(null=True, blank=True)   # float()
    edgeeffectiveness = models.FloatField(null=True, blank=True)   # float()
    endsmoke = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    energy = models.IntegerField(null=True, blank=True)   # int()
    energypershot = models.IntegerField(null=True, blank=True)   # int()
    explosionart = models.CharField(max_length=100, null=True, blank=True)
    explosiongaf = models.CharField(max_length=100, null=True, blank=True)

    firestarter = models.IntegerField(null=True, blank=True)   # int()
    flighttime = models.IntegerField(null=True, blank=True)   # int()
    groundbounce = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    guidance = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    ID_weapon = models.IntegerField(null=True, blank=True)   # int()
    lavaexplosionart = models.CharField(max_length=100, null=True, blank=True)
    lavaexplosiongaf = models.CharField(max_length=100, null=True, blank=True)
    lineofsight = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    metal = models.IntegerField(null=True, blank=True)   # int()
    metalpershot = models.IntegerField(null=True, blank=True)   # int()

    meteor = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    minbarrelangle = models.IntegerField(null=True, blank=True)   # int()
    model = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    noautorange = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    noexplode = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    noradar = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    paralyzer = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    pitchtolerance = models.IntegerField(null=True, blank=True)   # int()
    propeller = models.PositiveSmallIntegerField(null=True, blank=True)   # int()

    randomdecay = models.FloatField(null=True, blank=True)   # float()
    _range = models.IntegerField(null=True, blank=True)   # int()
    reloadtime = models.FloatField(null=True, blank=True)   # float()
    rendertype = models.IntegerField(null=True, blank=True)   # int()
    selfprop = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    shakeduration = models.IntegerField(null=True, blank=True)   # int()
    shakemagnitude = models.IntegerField(null=True, blank=True)   # int()
    smokedelay = models.IntegerField(null=True, blank=True)   # int()
    smoketrail = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    soundhit = models.CharField(max_length=100, null=True, blank=True)    # 50

    soundstart = models.CharField(max_length=100, null=True, blank=True)
    soundtrigger = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    soundwater = models.CharField(max_length=100, null=True, blank=True)
    sprayangle = models.IntegerField(null=True, blank=True)   # int()
    startsmoke = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    startvelocity = models.IntegerField(null=True, blank=True)   # int()
    stockpile = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    targetable = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    tolerance = models.IntegerField(null=True, blank=True)   # int()
    tracks = models.PositiveSmallIntegerField(null=True, blank=True)   # int()

    turnrate = models.IntegerField(null=True, blank=True)   # int()
    turret = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    twophase = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    unitsonly = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    vlaunch = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    waterexplosionart = models.CharField(max_length=100, null=True, blank=True)
    waterexplosiongaf = models.CharField(max_length=100, null=True, blank=True)
    waterweapon = models.PositiveSmallIntegerField(null=True, blank=True)   # int()
    weaponacceleration = models.IntegerField(null=True, blank=True)   # int()
    weapontimer = models.FloatField(null=True, blank=True)   # float()

    weapontype2 = models.CharField(max_length=100, blank=True)
    weaponvelocity = models.IntegerField(null=True, blank=True)   # int()
    damage = models.ManyToManyField(Damage)   # 73
    def __str__(self):  # __unicode__ on Python 2
        return self.name + '_'



class LazarusFeatureTDF(LazarusBase):
    animating = models.PositiveSmallIntegerField(null=True, blank=True)
    animtrans = models.PositiveSmallIntegerField(null=True, blank=True)
    autoreclaimable = models.IntegerField(null=True, blank=True)
    burnmax = models.IntegerField(null=True, blank=True)
    burnmin = models.IntegerField(null=True, blank=True)
    burnweapon = models.CharField(blank=True, max_length=95)
    category = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=135, null=True, blank=True)
    blocking = models.PositiveSmallIntegerField(null=True, blank=True)
    damage = models.IntegerField(null=True, blank=True)
    energy = models.IntegerField(null=True, blank=True)
    featuredead = models.CharField(max_length=135, null=True, blank=True)
    featurereclamate = models.CharField(max_length=135, null=True, blank=True)
    filename = models.CharField(max_length=135, null=True, blank=True)
    flamable = models.PositiveSmallIntegerField(null=True, blank=True)
    footprintx = models.IntegerField(null=True, blank=True)
    footprintz = models.IntegerField(null=True, blank=True)
    geothermal = models.PositiveSmallIntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    hitdensity = models.IntegerField(null=True, blank=True)
    indestructible = models.PositiveSmallIntegerField(null=True, blank=True)
    metal = models.IntegerField(null=True, blank=True)
    nodisplayinfo = models.PositiveSmallIntegerField(null=True, blank=True)
    _object = models.CharField(max_length=135, null=True, blank=True)
    permanent = models.PositiveSmallIntegerField(null=True, blank=True)
    reclaimable = models.IntegerField(null=True, blank=True)
    reproduce = models.PositiveSmallIntegerField(null=True, blank=True)
    reproducearea = models.PositiveSmallIntegerField(null=True, blank=True)
    seqname = models.CharField(max_length=135, null=True, blank=True)
    seqnameburn = models.CharField(max_length=135, null=True, blank=True)
    seqnamedie = models.CharField(max_length=135, null=True, blank=True)
    seqnamereclamate = models.CharField(max_length=135, null=True, blank=True)
    seqnameshad = models.CharField(max_length=135, null=True, blank=True)
    shadtrans = models.IntegerField(null=True, blank=True)
    sparktime = models.IntegerField(null=True, blank=True)
    spreadchance = models.IntegerField(null=True, blank=True)
    world = models.CharField(max_length=135, null=True, blank=True)
    def __str__(self):  # __unicode__ on Python 2
        return self._object + '_'



class LazarusDownloadTDF(LazarusBase):
    MENUENTRY = models.CharField(max_length=20, default='MENUENTRY1')  # [MENUENTRY1] [MENUENTRY2] [MENUENTRY3] etc...
    BUTTON = models.PositiveSmallIntegerField(default=0)  # See 'TA Button' below
    MENU = models.PositiveSmallIntegerField(default=2)  # first menu in TA is actually '2' for some reason
    UNITMENU = models.CharField(max_length=35, null=True, blank=True)  # short name for the construction unit that builds this unit
    UNITNAME = models.CharField(max_length=35, null=True, blank=True)  # short name of the unit this button builds



class LazarusUnitFBI(LazarusBase):
    Acceleration = models.CharField(max_length=150, null=True, blank=True)
    ActiveWhenBuild = models.CharField(max_length=150, null=True, blank=True)
    ai_limit = models.CharField(max_length=101, null=True, blank=True)
    ai_weight = models.CharField(max_length=102, null=True, blank=True)
    altfromsealevel = models.CharField(max_length=150, null=True, blank=True)
    amphibious = models.CharField(max_length=150, null=True, blank=True)
    antiweapons = models.CharField(max_length=150, null=True, blank=True)
    attackrunlength = models.CharField(max_length=150, null=True, blank=True)
    BMcode = models.CharField(max_length=150, null=True, blank=True)
    BadTargetCategory = models.CharField(max_length=103, null=True, blank=True)
    BankScale = models.CharField(max_length=150, null=True, blank=True)
    BrakeRate = models.CharField(max_length=150, null=True, blank=True)
    BuildAngle = models.CharField(max_length=150, null=True, blank=True)
    BuildCostEnergy = models.CharField(max_length=150, null=True, blank=True)
    BuildCostMetal = models.CharField(max_length=150, null=True, blank=True)
    BuildTime = models.CharField(max_length=150, null=True, blank=True)
    Builddistance = models.CharField(max_length=150, null=True, blank=True)
    Builder = models.CharField(max_length=150, null=True, blank=True)
    canattack = models.CharField(max_length=150, null=True, blank=True)
    CanCapture = models.CharField(max_length=150, null=True, blank=True)
    CanDgun = models.CharField(max_length=150, null=True, blank=True)
    Canfly = models.CharField(max_length=150, null=True, blank=True)
    canguard = models.CharField(max_length=150, null=True, blank=True)
    canhover = models.CharField(max_length=150, null=True, blank=True)
    canload = models.CharField(max_length=150, null=True, blank=True)
    canmove = models.CharField(max_length=150, null=True, blank=True)
    canpatrol = models.CharField(max_length=150, null=True, blank=True)
    CanReclamate = models.CharField(max_length=150, null=True, blank=True)
    canstop = models.BooleanField(default=True)
    cantbetransported = models.CharField(max_length=150, null=True, blank=True)
    Category = models.CharField(max_length=104)
    CloakCost = models.CharField(max_length=150, null=True, blank=True)
    CloakCostMoving = models.CharField(max_length=150, null=True, blank=True)
    Commander = models.CharField(max_length=150, null=True, blank=True)
    Copyright = models.CharField(max_length=105, default='Copyright 1997 Humongous Entertainment. All rights reserved.')
    #TODO: PK below
    Corpse = models.CharField(max_length=106, null=True, blank=True)
    cruisealt = models.CharField(max_length=150, null=True, blank=True)
    DamageModifier = models.CharField(max_length=150, null=True, blank=True)
    DefaultMissionType = models.CharField(max_length=107, null=True, blank=True)
    Description = models.CharField(max_length=255, null=True, blank=True)
    Designation = models.CharField(max_length=250, null=True, blank=True)
    digger = models.CharField(max_length=150, null=True, blank=True)
    Downloadable = models.CharField(max_length=150, null=True, blank=True)
    EnergyMake = models.CharField(max_length=150, null=True, blank=True)
    EnergyStorage = models.CharField(max_length=150, null=True, blank=True)
    EnergyUse = models.CharField(max_length=150, null=True, blank=True)
    # TODO: Many-To-One
    ExplodeAs = models.CharField(max_length=108, null=True, blank=True)
    ExtractsMetal = models.CharField(max_length=150, null=True, blank=True)
    firestandorders = models.CharField(max_length=150, null=True, blank=True) # 50
    Floater = models.CharField(max_length=150, null=True, blank=True)
    FootprintX = models.CharField(max_length=150, null=True, blank=True)
    FootprintZ = models.CharField(max_length=150, null=True, blank=True)
    FrenchDescription = models.CharField(max_length=109, null=True, blank=True)
    FrenchName = models.CharField(max_length=110, null=True, blank=True)
    GermanDescription = models.CharField(max_length=111, null=True, blank=True)
    GermanName = models.CharField(max_length=112, null=True, blank=True)
    HealTime = models.CharField(max_length=150, null=True, blank=True)
    HideDamage = models.CharField(max_length=150, null=True, blank=True)
    HoverAttack = models.CharField(max_length=150, null=True, blank=True) #60
    ImmuneToParalyzer = models.CharField(max_length=150, null=True, blank=True)
    init_cloaked = models.CharField(max_length=150, null=True, blank=True)
    IsAirBase = models.CharField(max_length=150, null=True, blank=True)
    IsFeature = models.CharField(max_length=150, null=True, blank=True)
    istargetingupgrade = models.CharField(max_length=150, null=True, blank=True)
    ItalianDescription = models.CharField(max_length=113, null=True, blank=True)
    ItalianName = models.CharField(max_length=114, null=True, blank=True)
    JapanesDescription = models.CharField(max_length=115, null=True, blank=True)
    JapaneseName = models.CharField(max_length=116, null=True, blank=True)
    kamikaze = models.CharField(max_length=150, null=True, blank=True) # 70
    kamikazedistance = models.CharField(max_length=150, null=True, blank=True)
    MakesMetal = models.CharField(max_length=150, null=True, blank=True)
    maneuverleashlength = models.CharField(max_length=150, null=True, blank=True)
    MaxDamage = models.CharField(max_length=150, null=True, blank=True)
    MaxSlope = models.CharField(max_length=150, null=True, blank=True)
    MaxVelocity = models.CharField(max_length=150, null=True, blank=True)
    MaxWaterDepth = models.CharField(max_length=150, null=True, blank=True)
    MetalMake = models.CharField(max_length=150, null=True, blank=True)
    MetalStorage = models.CharField(max_length=150, null=True, blank=True)
    mincloakdistance = models.CharField(max_length=150, null=True, blank=True)
    MinWaterDepth = models.CharField(max_length=150, null=True, blank=True)
    MobileStandOrders = models.CharField(max_length=150, null=True, blank=True)
    MoveRate1 = models.CharField(max_length=150, null=True, blank=True)

    MovementClass = models.CharField(max_length=117, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    NoAutoFire = models.CharField(max_length=150, null=True, blank=True)
    NoChaseCategory = models.CharField(max_length=118, null=True, blank=True)
    norestrict = models.CharField(max_length=150, null=True, blank=True)
    NoShadow = models.CharField(max_length=150, null=True, blank=True)
    # TODO: PK below
    Objectname = models.CharField(max_length=119)
    onoffable = models.CharField(max_length=150, null=True, blank=True)
    Ovradjust = models.CharField(max_length=150, null=True, blank=True)
    PigLatinDescription = models.CharField(max_length=120, null=True, blank=True)
    PigLatinName = models.CharField(max_length=121, null=True, blank=True)
    PitchScale = models.CharField(max_length=150, null=True, blank=True)
    RadarDistance = models.CharField(max_length=150, null=True, blank=True)
    RadarDistanceJam = models.CharField(max_length=150, null=True, blank=True)
    Scale = models.CharField(max_length=150, null=True, blank=True)
    # TODO: List of string choices will go below
    SelfDestructAs = models.CharField(max_length=123) # ✦ ✦ ✦
    selfdestructcountdown = models.CharField(max_length=150, null=True, blank=True) # 100
    ShootMe = models.CharField(max_length=150, null=True, blank=True)
    ShowPlayerName = models.CharField(max_length=150, null=True, blank=True)
    # TODO: List of string choices will go below
    Side = models.CharField(max_length=124) # ✦ ✦ ✦
    SightDistance = models.CharField(max_length=150, null=True, blank=True)
    SonarDistance = models.CharField(max_length=150, null=True, blank=True)
    SonarDistanceJam = models.CharField(max_length=150, null=True, blank=True)
    sortbias = models.CharField(max_length=150, null=True, blank=True)
    # TODO: List of string choices will go below
    SoundCategory = models.CharField(max_length=125)
    SpanishDescription = models.CharField(max_length=126, null=True, blank=True)
    SpanishName = models.CharField(max_length=127, null=True, blank=True)
    StandingFireOrder = models.CharField(max_length=150, null=True, blank=True)
    StandingMoveOrder = models.CharField(max_length=150, null=True, blank=True)
    Stealth = models.CharField(max_length=150, null=True, blank=True)
    SteeringMode = models.CharField(max_length=150, null=True, blank=True)
    # TODO: List of string choices will go below
    TEDClass = models.CharField(max_length=128)
    teleporter = models.CharField(max_length=150, null=True, blank=True)
    ThreeD = models.CharField(max_length=150, null=True, blank=True)
    TidalGenerator = models.CharField(max_length=150, null=True, blank=True)
    TransMaxUnits = models.CharField(max_length=150, null=True, blank=True)
    transportcapacity = models.CharField(max_length=150, null=True, blank=True)
    transportsize = models.CharField(max_length=150, null=True, blank=True)
    TurnRate = models.CharField(max_length=150, null=True, blank=True)
    # TODO: unique? ID?
    UnitName = models.CharField(max_length=129, null=True, blank=True) # ✦ ✦ ✦
    # TODO: must be unique, PK?
    UnitNumber = models.CharField(max_length=150, null=True, blank=True) # ✦ ✦ ✦
    Upright = models.CharField(max_length=150, null=True, blank=True)
    Version = models.CharField(max_length=150, null=True, blank=True) # ✦ ✦ ✦
    WaterLine = models.CharField(max_length=150, null=True, blank=True)
    # TODO: PK below
    Weapon1 = models.CharField(max_length=127, null=True, blank=True) ##models.ForeignKey(WeaponTDF, on_delete=models.CASCADE, related_name='Weapon1', null=True, blank=True)
    # TODO: PK below
    Weapon2 = models.CharField(max_length=127, null=True, blank=True) ##models.ForeignKey(WeaponTDF, on_delete=models.CASCADE, related_name='Weapon2', null=True, blank=True)
    # TODO: PK below
    Weapon3 = models.CharField(max_length=127, null=True, blank=True) ##models.ForeignKey(WeaponTDF, on_delete=models.CASCADE, related_name='Weapon3', null=True, blank=True)
    WindGenerator = models.CharField(max_length=150, null=True, blank=True)
    WorkerTime = models.CharField(max_length=150, null=True, blank=True)
    # TODO: PK below
    wpri_badTargetCategory = models.CharField(max_length=130, null=True, blank=True)
    # TODO: ManyToMany below
    wsec_badTargetCategory = models.CharField(max_length=131, null=True, blank=True)
    YardMap = models.CharField(max_length=132, null=True, blank=True) #135
    ZBuffer = models.CharField(max_length=150, default=1, null=True, blank=False)
    def __str__(self):  # __unicode__ on Python 2
        return self.Objectname + '_'