from django.db import models

# Create your models here.

# = models.CharField(max_length=100)
# = models.FloatField(null=True, blank=True)
# = models.IntegerField()
# = models.BooleanField(default=False)


class UnitFbiData(models.Model):
    _raw_json_dump = models.CharField()
    Acceleration = models.FloatField(null=True, blank=True)
    ActiveWhenBuild = models.IntegerField()
    ai_limit = models.CharField(max_length=100)
    ai_weight = models.CharField(max_length=100)
    altfromsealevel = models.IntegerField()
    amphibious = models.BooleanField(default=False)
    antiweapons = models.BooleanField(default=False)
    attackrunlength = models.IntegerField()
    BMcode = models.BooleanField(default=False)
    BadTargetCategory = models.CharField(max_length=100)
    BankScale = models.IntegerField()
    BrakeRate = models.IntegerField()
    BuildAngle = models.IntegerField()
    BuildCostEnergy = models.IntegerField()
    BuildCostMetal = models.IntegerField()
    BuildTime = models.IntegerField()
    Builddistance = models.IntegerField()
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
    canstop = models.BooleanField(default=False)
    cantbetransported = models.BooleanField(default=False)
    Category = models.CharField(max_length=100)
    CloakCost = models.IntegerField()
    CloakCostMoving = models.IntegerField()
    Commander = models.BooleanField(default=False)
    Copyright = models.CharField(max_length=100)
    #TODO: PK below
    Corpse = models.CharField(max_length=100)
    cruisealt = models.IntegerField()
    DamageModifier = models.FloatField(null=True, blank=True)
    DefaultMissionType = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    Designation = models.CharField(max_length=50)
    digger = models.BooleanField(default=False)
    Downloadable = models.BooleanField(default=False)
    EnergyMake = models.IntegerField()
    EnergyStorage = models.IntegerField()
    EnergyUse = models.IntegerField()
    # TODO: Mant-To-One
    ExplodeAs = models.CharField(max_length=100)
    ExtractsMetal = models.FloatField(null=True, blank=True)
    firestandorders = models.IntegerField()
    Floater = models.BooleanField(default=False)
    FootprintX = models.IntegerField()
    FootprintZ = models.IntegerField()
    FrenchDescription = models.CharField(max_length=100)
    FrenchName = models.CharField(max_length=100)
    GermanDescription = models.CharField(max_length=100)
    GermanName = models.CharField(max_length=100)
    HealTime = models.IntegerField()
    HideDamage = models.BooleanField(default=False)
    HoverAttack = models.BooleanField(default=False)
    ImmuneToParalyzer = models.BooleanField(default=False)
    init_cloaked = models.BooleanField(default=False)
    IsAirBase = models.BooleanField(default=False)
    IsFeature = models.BooleanField(default=False)
    istargetingupgrade = models.BooleanField(default=False)
    ItalianDescription = models.CharField()
    ItalianName = models.CharField()
    JapanesDescription = models.CharField()
    JapaneseName = models.CharField()
    kamikaze = models.BooleanField(default=False)
    kamikazedistance = models.IntegerField()
    MakesMetal = models.BooleanField(default=False)
    maneuverleashlength = models.IntegerField()
    MaxDamage = models.IntegerField()
    MaxSlope = models.IntegerField()
    MaxVelocity = models.IntegerField()
    MaxWaterDepth = models.IntegerField()
    MetalMake = models.IntegerField()
    MetalStorage = models.IntegerField()
    mincloakdistance = models.IntegerField()
    MinWaterDepth = models.IntegerField()
    MobileStandOrders = models.BooleanField(default=False)
    MoveRate1 = models.IntegerField()
    # TODO: PK below:
    MovementClass = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    NoAutoFire = models.BooleanField(default=False)
    NoChaseCategory = models.CharField(max_length=100)
    norestrict = models.BooleanField(default=False)
    NoShadow = models.BooleanField(default=False)
    # TODO: PK below
    Objectname = models.CharField(max_length=100)
    onoffable = models.BooleanField(default=False)
    Ovradjust = models.BooleanField(default=False)
    PigLatinDescription = models.CharField(max_length=100)
    PigLatinName = models.CharField(max_length=100)
    PitchScale = models.IntegerField(max_length=100)
    RadarDistance = models.IntegerField()
    RadarDistanceJam = models.IntegerField()
    Scale = models.IntegerField()
    # TODO: PK below
    SelfDestructAs = models.CharField(max_length=100)
    selfdestructcountdown = models.IntegerField()
    ShootMe = models.BooleanField(default=False)
    ShowPlayerName = models.BooleanField(default=False)
    # TODO: PK below:
    Side = models.CharField(max_length=100)
    SightDistance = models.IntegerField()
    SonarDistance = models.IntegerField()
    SonarDistanceJam = models.IntegerField()
    sortbias = models.IntegerField()
    # TODO: PK below
    SoundCategory = models.CharField(max_length=100)
    SpanishDescription = models.CharField(max_length=100)
    SpanishName = models.CharField(max_length=100)
    StandingFireOrder = models.IntegerField()
    StandingMoveOrder = models.IntegerField()
    Stealth = models.BooleanField(default=False)
    SteeringMode = models.IntegerField()
    # TODO: PK below
    TEDClass = models.CharField(max_length=100)
    teleporter = models.BooleanField(default=False)
    ThreeD = models.BooleanField(default=False)
    TidalGenerator = models.BooleanField(default=False)
    TransMaxUnits = models.IntegerField()
    transportcapacity = models.IntegerField()
    transportsize = models.IntegerField()
    TurnRate = models.IntegerField()
    # TODO: unique? ID?
    UnitName = models.CharField(max_length=100)
    # TODO: must be unique, PK?
    UnitNumber = models.IntegerField()
    Upright = models.BooleanField(default=False)
    Version = models.IntegerField()
    WaterLine = models.IntegerField()
    # TODO: PK below
    Weapon1 = models.CharField(max_length=100)
    # TODO: PK below
    Weapon2 = models.CharField(max_length=100)
    # TODO: PK below
    Weapon3 = models.CharField(max_length=100)
    WindGenerator = models.IntegerField()
    WorkerTime = models.IntegerField()
    # TODO: PK below
    wpri_badTargetCategory = models.CharField(max_length=100)
    # TODO: ManyToMany below
    wsec_badTargetCategory = models.CharField(max_length=100)
    YardMap = models.CharField(max_length=100)


# ONE-TO-ONE SAMPLE:
"""
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )

"""

# MANY-TO-MANY SAMPLE:
"""
class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
"""

# MANY-TO-ONE SAMPLE:
"""
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
"""
