from django.db import models

# Create your models here.

# = models.CharField(max_length=100)
# = models.FloatField(null=True, blank=True)
# = models.IntegerField()
# = models.BooleanField(default=False)


class UnitFbiData(models.Model):
    _raw_json_dump = models.CharField()

    Acceleration = models.FloatField(null=True, blank=True) # Acceleration=0.5;
    ActiveWhenBuild = models.IntegerField() # ActivateWhenBuilt=1;
    ai_limit = models.CharField(max_length=100) # ai_limit=limit CORVOYR 2;
    ai_weight = models.CharField(max_length=100) # ai_weight=weight CORFLAK 6;
    altfromsealevel = models.IntegerField() # altfromsealevel=1;
    amphibious = models.BooleanField(default=False) # amphibious=1;
    antiweapons = models.BooleanField(default=False) # antiweapons=1;
    attackrunlength = models.IntegerField() # attackrunlength=290;
    BMcode = models.BooleanField(default=False) # BMcode=1;
    BadTargetCategory = models.CharField(max_length=100) # BadTargetCategory=VTOL;
    BankScale = models.IntegerField() # BankScale=1;
    BrakeRate = models.IntegerField() # BrakeRate=9;
    BuildAngle = models.IntegerField() # BuildAngle=32768;
    BuildCostEnergy = models.IntegerField() # BuildCostEnergy=985;
    BuildCostMetal = models.IntegerField() # BuildCostMetal=0;
    BuildTime = models.IntegerField() # BuildTime=9894;
    Builddistance = models.IntegerField() # Builddistance=80;
    Builder = models.BooleanField(default=False) # Builder=1;
    canattack = models.BooleanField(default=False) # canattack=1;
    CanCapture = models.BooleanField(default=False) # CanCapture=1;
    CanDgun = models.BooleanField(default=False) # candgun=1;
    Canfly = models.BooleanField(default=False) # Canfly=1;
    canguard = models.BooleanField(default=False) # canguard=1;
    canhover = models.BooleanField(default=False) # canhover=1;
    canload = models.BooleanField(default=False) # canload=1;
    canmove = models.BooleanField(default=False) # canmove=1;
    canpatrol = models.BooleanField(default=False) # canpatrol=1;
    CanReclamate = models.BooleanField(default=False) # CanReclamate=1;
    canstop = models.BooleanField(default=False) # canstop=1;
    cantbetransported = models.BooleanField(default=False) # cantbetransported=1;
    Category = models.CharField(max_length=100) # Category=ARM TANK LEVEL2 CONSTR NOWEAPON NOTAIR NOTSUB CTRL_B;
    CloakCost = models.IntegerField() # CloakCost=7;
    CloakCostMoving = models.IntegerField() # CloakCostMoving=800;
    Commander = models.BooleanField(default=False) # Commander=1;
    Copyright = models.CharField(max_length=100) # Copyright=Copyright 1997 Humongous Entertainment. All rights reserved.;
    #TODO: PK below
    Corpse = models.CharField(max_length=100) # Corpse=fortification_core;
    cruisealt = models.IntegerField() # cruisealt=90;
    DamageModifier = models.FloatField(null=True, blank=True)#          DamageModifier=0.7;
    DefaultMissionType = models.CharField(max_length=100) #             DefaultMissionType=VTOL_standby;
    Description = models.CharField(max_length=255) #            Description=Very Heavy Assault Tank;
    Designation = models.CharField(max_length=50) #             Designation=WB-S;
    digger = models.BooleanField(default=False) #           digger=1;
    Downloadable = models.BooleanField(default=False) #             Downloadable=1;
    EnergyMake = models.IntegerField() #            EnergyMake=9;
    EnergyStorage = models.IntegerField() #             EnergyStorage=80;
    EnergyUse = models.IntegerField() #             EnergyUse=9;
    # TODO: Mant-To-One
    ExplodeAs #             ExplodeAs=LARGE_BUILDINGEX;
    ExtractsMetal #             ExtractsMetal=0.003;
    firestandorders #           firestandorders=1;
    Floater #           Floater=1;
    FootprintX = models.IntegerField() #            FootprintX=9;
    FootprintZ = models.IntegerField() #            FootprintZ=9;
    FrenchDescription = models.CharField(max_length=100) #             FrenchDescription=Serpent des mers;
    FrenchName = models.CharField(max_length=100) #
    GermanDescription = models.CharField(max_length=100) #
    GermanName = models.CharField(max_length=100) #
    HealTime = models.IntegerField()            # HealTime=27;
    HideDamage           # HideDamage=1;
    HoverAttack          # HoverAttack=1;
    ImmuneToParalyzer            # ImmuneToParalyzer=1;
    init_cloaked            # init_cloaked=1;
    IsAirBase           # IsAirBase=1;
    IsFeature           #	IsFeature=1;
    istargetingupgrade           # istargetingupgrade=1;
    ItalianDescription #
    ItalianName #
    JapanesDescription #
    JapaneseName #
    kamikaze            # kamikaze=1;
    kamikazedistance = models.IntegerField()            # kamikazedistance=80;
    MakesMetal          # MakesMetal=1;
    maneuverleashlength = models.IntegerField()             # maneuverleashlength=640;
    MaxDamage = models.IntegerField()           # MaxDamage=992;
    MaxSlope = models.IntegerField()            # MaxSlope=8;
    MaxVelocity = models.IntegerField()             # MaxVelocity=9;
    MaxWaterDepth = models.IntegerField()           # MaxWaterDepth=35;
    MetalMake # MetalMake=1;
    maneuverleashlength = models.IntegerField() #
    MaxDamage = models.IntegerField() #
    MaxSlope = models.IntegerField() #
    MaxVelocity = models.IntegerField() #
    MaxWaterDepth = models.IntegerField() #
    MetalMake = models.IntegerField() #
    MetalStorage = models.IntegerField() #
    mincloakdistance = models.IntegerField() #
    MinWaterDepth = models.IntegerField() #
    MobileStandOrders = models.BooleanField(default=False) #

    MoveRate1 = models.IntegerField()           # MoveRate1=1;
    # TODO: PK below:
    MovementClass = models.CharField(max_length=100) # MovementClass=TANKSH3;
    Name = models.CharField(max_length=100) # Name=Zipper;
    NoAutoFire #	NoAutoFire=1;
    # MovementClass #
    # Name #
    NoAutoFire #
    NoChaseCategory = models.CharField(max_length=100) # NoChaseCategory=VTOL;
    norestrict # norestrict=1;
    NoShadow # NoShadow=1;
    # TODO: PK below
    Objectname = models.CharField(max_length=100) # Objectname=CORWIN;
    onoffable # onoffable=1;
    Ovradjust # Ovradjust=1;
    PigLatinDescription = models.CharField(max_length=100) #
    PigLatinName = models.CharField(max_length=100) #

    PitchScale = models.IntegerField(max_length=100) # PitchScale=1;
    RadarDistance = models.IntegerField() # RadarDistance=700;
    RadarDistanceJam = models.IntegerField() # RadarDistanceJam=730;
    Scale # Scale=1;
    # TODO: PK below
    SelfDestructAs = models.CharField(max_length=100) # SelfDestructAs=SMALL_UNIT;
    selfdestructcountdown = models.IntegerField() # selfdestructcountdown=2;
    ShootMe # ShootMe=1;
    ShowPlayerName # ShowPlayerName=1;
    # TODO: PK below:
    Side # Side=CORE;
    SightDistance = models.IntegerField() # SightDistance=90;
    SonarDistance = models.IntegerField() # SonarDistance=650;
    SonarDistanceJam = models.IntegerField() # SonarDistanceJam=650;
    sortbias # sortbias=0;
    # TODO: PK below
    SoundCategory # SoundCategory=VIPE;
    SpanishDescription #
    SpanishName #
    StandingFireOrder = models.IntegerField() # StandingFireOrder=0;
    StandingMoveOrder = models.IntegerField() # StandingMoveOrder=1;
    Stealth # Stealth=1;
    SteeringMode # SteeringMode=2;
    # TODO: PK below
    TEDClass = models.CharField(max_length=100) # TEDClass=WATER;
    teleporter # teleporter=1;
    ThreeD # ThreeD=1;
    TidalGenerator # TidalGenerator=1;
    TransMaxUnits = models.IntegerField() # TransMaxUnits=1;
    transportcapacity = models.IntegerField() # transportcapacity=5;
    transportsize = models.IntegerField() # transportsize=3;
    TurnRate = models.IntegerField() # TurnRate=999;
    # TODO: unique? ID?
    UnitName = models.CharField(max_length=100) # UnitName=CORWIN;
    # TODO: must be unique, PK?
    UnitNumber = models.IntegerField() # UnitNumber=9;
    Upright # Upright=1;
    Version # Version=1;
    WaterLine = models.IntegerField() # WaterLine=43;
    # TODO: PK below
    Weapon1 = models.CharField(max_length=100) # Weapon1=crblmssl;
    # TODO: PK below
    Weapon2 = models.CharField(max_length=100) # Weapon2=coramph_weapon2;
    # TODO: PK below
    Weapon3 = models.CharField(max_length=100) # Weapon3=CORSEAP_WEAPON3;
    WindGenerator = models.IntegerField() # WindGenerator=30;
    WorkerTime = models.IntegerField() # WorkerTime=80;
    # TODO: PK below
    wpri_badTargetCategory = models.CharField(max_length=100) # wpri_badTargetCategory=VTOL;
    # TODO: PK below
    wsec_badTargetCategory = models.CharField(max_length=100) # wsec_badTargetCategory=VTOL;
    YardMap = models.CharField(max_length=100) # YardMap=ooooooo ooooooo occccco occccco occccco occccco;



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








"""
nanolathes


Variable	                Description	                                                                                                                                            Examples

    Acceleration	            How fast the unit acceleration	                                                                                                                        Acceleration=0.5;
    ActivateWhenBuilt	        Is the default state of this unit ACTIVATED (or ON) when built.	                                                                                        ActivateWhenBuilt=1;
    ai_limit	                Limit of number the AI will build of this unit.	                                                                                                        ai_limit=limit CORVOYR 2;
    ai_weight	                The weighting (ie. what % of these to to build. I don't know what the units are)	                                                                    ai_weight=weight CORFLAK 6;
    altfromsealevel	            Altitude from sea. For flying units. Don't quite understand this one myself.	                                                                        altfromsealevel=1;
    amphibious	                Is the unit amphibious (can go under water, & on land.	                                                                                                amphibious=1;
    antiweapons	                Does this unit shoot at the weapons of other units eg. Missile defence systems	                                                                        antiweapons=1;
    attackrunlength	            For planes. The distance they must travel before being able to drop their bombs/shoot their missiles. HoverAttack is like attackrunlength=0, I think	                                                attackrunlength=290;
    BMcode	                    A BMcode. Every unit has a value of 1, except for contstruction plants (eg. Air Craft Plant, Vehical Plants). So do likewise.	                                                                        BMcode=1;
    BadTargetCategory	        The type of target that is not good for that low accuracy at this type of unit. In general. The value specified identifies all units that have that value specified in their own "Category" settings.	BadTargetCategory=VTOL;
    BankScale	                The Scale (see Scale) of the unit when banking (ie. turning if its an aircraft)	BankScale=1;
    BrakeRate	                The rate at which the unit can slow down	BrakeRate=9;
    BuildAngle	                No idea. Here's a possibility: Random angle to build unit on, example is the solar panel some times facing 180 degrees from the solar panel next to it.	BuildAngle=32768;
    BuildCostEnergy	            The amount of energy that will be consumed during the building of this unit. I think value < 0 generate errors, but I've never tried.	BuildCostEnergy=985;
    BuildCostMetal	            Same as above, but amount of metal.	BuildCostMetal=0;
    BuildTime	                The time is takes to build this unit. On average, 10000 is medium time, things like fusion plants are more like 100000, and krogoth like 300000	BuildTime=9894;
    Builddistance	            The distance at which a unit can build if it is a builder.	Builddistance=80;
    Builder	                    Can this unit build other units.	Builder=1;
    canattack	                Can the unit attack.	canattack=1;
    CanCapture	                Can this unit capture other units.	CanCapture=1;
    CanDgun	                    Can the unit DGUN (ie. has a gun like the commander)	candgun=1;
    Canfly	                    Can this unit fly.	Canfly=1;
    canguard	                Can this unit guard.	canguard=1;
    canhover	                Can this unit hover	canhover=1;
    canload	                    Can this unit load other units.	canload=1;
    canmove	                    Can this unit move.	canmove=1;
    canpatrol	                Can this unit patrol.	canpatrol=1;
    CanReclamate	            Can this unit reclaim things.	CanReclamate=1;
    canstop	                    Can this unit stop.	canstop=1;
    cantbetransported	        Is this a unit that transports cannot load eg. Ships, krogoth	cantbetransported=1;
    Category	                A category class. Look at some of the FBI files in totala1.hpi for examples. Essentially, this places the unit in several named catagories that can be named in other variables such as "wpri_badTargetCategory" described below, and in the AI Text files as well.	Category=ARM TANK LEVEL2 CONSTR NOWEAPON NOTAIR NOTSUB CTRL_B;
    CloakCost	                The energy cost of this unit remaining cloaked when standing still.	CloakCost=7;
    CloakCostMoving 	        The energy cost of this unit remaining cloaking while moving.	CloakCostMoving=800;
    Commander	                Is this unit the (a?) commander.	Commander=1;
    Copyright	                The copyright of this unit. Must be as shown to the right, or won't work. (Most people copy this line as a comment, and put their own copyright infomation in the commented-out version.	Copyright=Copyright 1997 Humongous Entertainment. All rights reserved.;
    Corpse	                    The name of the feature the unit turns into when the unit dies. If the unit is a feature (Dragons Teeth) the unit instantly turns into this feature, when it is finished being built. (this is not the 3do file of the feature, the feature entry tells the 3do file to use in the feautres OBJECT variable).	Corpse=fortification_core;
    cruisealt	                The altitude at which the unit flys	cruisealt=90;
    DamageModifier	            The rate at which this unit heals itself.	DamageModifier=0.7;
    DefaultMissionType	        The default orders of this unit for missions.	DefaultMissionType=VTOL_standby;
    Description	                The description of the unit seen at the bottom of the screen when you hold the cursor over it in the game.	Description=Very Heavy Assault Tank;
    Designation	                The designation. This is unimportant and can have virtually any value (there may be a limit to the number of character it will except)	Designation=WB-S;
    digger	                    Does this unit have pieces which extend under ground. I think thats what it means. Things like the pop-up heavy cannon have this = 1.	digger=1;
    Downloadable	            Is this a unit which has been downloaded off the internet. If you want to be able to use the unit, put 1.
                                (12/28/98) Note from The Raptor: Not true. I haven't included this variable in all of my units, and they work just fine. It's just one that we started seeing in the Cavedog weekly units, so assumed that's what it meant. It really seems to do nothing.	Downloadable=1;
    EnergyMake	                The energy this unit produces when ACTIVE.	EnergyMake=9;
    EnergyStorage	            The amount added to the maximum amount of energy you can store while the unit is alive.	EnergyStorage=80;
    EnergyUse	                The amount of energy the unit uses while it is ACTIVE.	EnergyUse=9;
    ExplodeAs	                The explosion ID of the explosion that will happen if the unit explodes. See totala1.hpi for other examples.	ExplodeAs=LARGE_BUILDINGEX;
    ExtractsMetal	            The rate at which the unit extracts metal. (Yes, the MOHOmine only extracts at like 0.01)	ExtractsMetal=0.003;
    firestandorders	            Can this unit give firestandorders. You know as much as me.	firestandorders=1;
    Floater	                    Does this unit float on water.	Floater=1;
    FootprintX	                The X axis footprint. Should correlate with the unit model's actual size. The footprint helps control how close units can get to one another.	FootprintX=9;
    FootprintZ	                As with FootprintX, but the Z axis (ie. up and down on the screen while playing TA). Should correlate with the unit model's actual size.	FootprintZ=9;

    FrenchDescription	        As description, but in French.	FrenchDescription=Serpent des mers;
    FrenchName	                As Name, but in French	FrenchName=Zeus;
    GermanDescription	        As description, but in German	GermanDescription=Überschwerer Gefechtspanzer;
    GermanName	                As Name, but in german	GermanName=A.K.;
    HealTime	                The time it take for this unit to heal itself. (Typically used by commanders)	HealTime=27;
    HideDamage	                Whether or not to show the amount of damage done to this unit to the opponent(s). Commanders have this value set.	HideDamage=1;
    HoverAttack	                Will this attack while remaining in the same spot, even though it is an aircraft. Like the brawler.	HoverAttack=1;
    ImmuneToParalyzer	        Is this unit immune to being paralyzed.	ImmuneToParalyzer=1;
    init_cloaked	            When built this unit is cloaked.	init_cloaked=1;
    IsAirBase	                Is this unit an airbase. Only the air repair pad and aircraft carriers have this as 1	IsAirBase=1;
    IsFeature	                Is this unit a feature. eg. The dragons teeth. Features do not appear on radar.	IsFeature=1;
    istargetingupgrade	        Does this unit upgrade the targeting so that units shoot at things on radar like at things seen by that unit.	istargetingupgrade=1;
    ItalianDescription	        As description, but in Italian	ItalianDescription=Veicolo veloce da attacco;
    ItalianName	                As Name, but in Italian	ItalianName=Zipper;
    JapanesDescription	        As description, but in Japanese	JapaneseDescription=XXXX;
    JapaneseName	            As Name, but in Japanese	JapaneseName=Jeffysan;
    kamikaze	                Does this unit kill itself to attack its target eg. The roach/invader	kamikaze=1;
    kamikazedistance	        How far from the target must the unit be to do a kamikaze attack	kamikazedistance=80;
    MakesMetal	                Does this unit make metal. eg. Metal Maker NS	MakesMetal=1;
    maneuverleashlength	        How far from the course that the unit is patrolling / moving on will it vary if it is attacked / distracted.	maneuverleashlength=640;
    MaxDamage	                Amount of damage unit can take before dying (i.e "Hit Points"). Kbots have about 600, Tanks have about 2000, Planes have about 500, Commander has 3000	MaxDamage=992;
    MaxSlope	                What is the maximum slope this unit can go on.	MaxSlope=8;
    MaxVelocity	                What is the maximum speed of this unit. Commander is 1.07, Core Storm is 1.25, Arm Hawk is 12	MaxVelocity=9;
    MaxWaterDepth	            What is maximum depth of water this unit can go in	MaxWaterDepth=35;
    MetalMake	                The amount of metal generated by construction units	MetalMake=1;
    MetalStorage	            The amound added to your maximum metal storage while this unit is alive	MetalStorage=900;
    mincloakdistance	        The distance the unit must have on every side to remain cloaked. If another unit moves into this area, the unit uncloaks.	mincloakdistance=90;
    MinWaterDepth	            The minimum depth of water this unit can be in	MinWaterDepth=8;
    MobileStandOrders	        Basically, I think, can this unit hold position of all mobile units, only the transports (all of them) have this equal to 0.	MobileStandOrders=1;
    MoveRate1	                Planes seem to use this. For example, all planes except the air transports have values of 8, the transports have values of 1.	MoveRate1=1;

    MovementClass	            How the unit moves. See totala1.hpi for examples. Movement classes are typically described in TDF files in the gamedata directory. (The moveinfo.tdf file is a good guess). It is used as a shortcut way of setting certain parameters (such as those listed here) by grouping them and giving them a name.	MovementClass=TANKSH3;
    Name	                    The name that appears on the bottom of the screen when you select a unit.	Name=Zipper;
    NoAutoFire	                Double negative. 1 means this unit will not automatically fire at other units. 0 means it will.	NoAutoFire=1;
    NoChaseCategory	            Category the unit will not chase. The value specified identifies all units that have that value specified in their own "Category" settings.	NoChaseCategory=VTOL;
    norestrict	                If the unit apears in the multiplayer Unit Restrictions menu. For example, the way the commander does not apear in the list.	norestrict=1;
    NoShadow	                Does this unit not have a shadow (most water units don't)	NoShadow=1;
    Objectname	                This is the name of your 3do file.	Objectname=CORWIN;
    onoffable	                Can this unit be turned on and off. On is ACTIVE, OFF is INACTIVE	onoffable=1;
    Ovradjust	                No idea. Some units just have this	Ovradjust=1;
    PigLatinDescription	        As description but in Pig Latin.	PigLatinDescription=Astfay attackay Outingscay Ehiclevay;
    PigLatinName	            As Name but in Pig Latin.	PigLatinName=Effyjay;
    PitchScale		            PitchScale=1;
    RadarDistance	            Distance that shown to you on radar by your unit	RadarDistance=700;
    RadarDistanceJam	        Distance that is jammed by unit.	RadarDistanceJam=730;
    Scale	                    The size modifier from 3DO file into the game. I think. I don't actually know.	Scale=1;
    SelfDestructAs	            The explosion that happens when a unit self desctructs. See totala1.hpi for examples.	SelfDestructAs=SMALL_UNIT;
    selfdestructcountdown	    The number the self-destruct count down starts at.	selfdestructcountdown=2;
    ShootMe	                    Does this unit broadcast itself as a target? (eg. Dragons's Teeth has this as 0, all other units as 1) If this is 0, then enemy units will not choose to attack this unit regardless of their orders.	ShootMe=1;
    ShowPlayerName	            Show the players name as a description (like the commander)	ShowPlayerName=1;
    Side	                    Which side does the unit belong to ARM, CORE.	Side=CORE;
    SightDistance	            The distance from the unit that everything is shown in. ie. Distance it gets rid of Fog of War. Unfortunately, this value seems to have a limit of around 400.	SightDistance=90;
    SonarDistance	            The distance given to you as sonar, on the mini map.	SonarDistance=650;
    SonarDistanceJam	        This is how far the unit jams sonar on the mini map.	SonarDistanceJam=650;
    sortbias		            sortbias=0;
    SoundCategory	            The "sound category" the unit uses. Sound categories are typically described in TDF files in the gamedata directory. (The sounds.tdf file is a good place to start). It is used to describe a group of sounds to associate with a unit, such as what sounds does it make when it starts, stops, arrives at a destination, is activated, is deactivated, etc.	SoundCategory=VIPE;
    SpanishDescription	        As description, in Spanish.	SpanishDescription=Vehículo todoterreno de ataque;
    SpanishName	                As Name, but in Spanish	SpanishName=Zipper;
    StandingFireOrder	        This is the initial fire order the unit starts with. 0 = Hold Fire; 1 = Return Fire; 2 = Fire at Will.	StandingFireOrder=0;

    StandingMoveOrder	        this is the initial movement order the unit starts with. 0 = Hold Position; 1 = Move; 2 = Roam	StandingMoveOrder=1;
    Stealth	                    Is this unit inivisible on sonar and radar.	Stealth=1;
    SteeringMode	            The way in which the unit turns. See totala1.hpi for options.	SteeringMode=2;
    TEDClass	                Important...I think. Define what type of unit it is.	TEDClass=WATER;
    teleporter	                Is this unit a teleporter. The two galatic gates have this = 1.	teleporter=1;
    ThreeD	                    Is the unit 3D.	ThreeD=1;
    TidalGenerator	            Is the unit a Tidal generator?	TidalGenerator=1;
    TransMaxUnits	            Maximum number of units that can be transported.	TransMaxUnits=1;
    transportcapacity	        Like TransMaxUnits I guess. The number of units that can be transported.	transportcapacity=5;
    transportsize	            How big the transport is. I don't quite understand.	transportsize=3;
    TurnRate	                How quickly the unit turns.	TurnRate=999;
    UnitName	                This is the name of your unit, (what I refer to as the "short name" and the name your files you decided on. e.g.. your file in this case would be called coralpha.fbi.	UnitName=CORWIN;
    UnitNumber	                The ID# for the unit. If this is the same as some other unit, your unit may not work. VERY IMPORTANT. All IDs from 0-about 400 have been used. Use other ones > 10000 is the best. The more digits, the more unlikely you'll have a ID conflict with someone else.	UnitNumber=9;
    Upright	                    Is the unit upright? For kbots - this keeps the unit upgright when climbing hills. In my case for a flying unit, my unit "layed down" on the ground whenever it landed (air unit). By setting upright=1, it solved my problem.	Upright=1;
    Version	                    The version of TA the unit will work under. Set this to 1.	Version=1;
    WaterLine	                How high up the 3d model to put the water line. For ships.	WaterLine=43;
    Weapon1	                    The unit's primary weapon. The name specified is the name of a weapon described in any of the number of TDF files found in the weapon subdirectories.	Weapon1=crblmssl;
    Weapon2	                    The unit's secondary weapon. The name specified is the name of a weapon described in any of the number of TDF files found in the weapon subdirectories.	Weapon2=coramph_weapon2;
    Weapon3	                    The unit's third weapon. The name specified is the name of a weapon described in any of the number of TDF files found in the weapon subdirectories.	Weapon3=CORSEAP_WEAPON3;
    WindGenerator	            The amount of energy generated by the wind by the unit.	WindGenerator=30;
    WorkerTime	                How quickly the unit nanolathes.	WorkerTime=80;
    wpri_badTargetCategory	    A bad target (lower chance of hitting) for the primary weapon. The value specified identifies all units that have that value specified in their own "Category" settings.	wpri_badTargetCategory=VTOL;
    wsec_badTargetCategory	    A bad target for the secondry weapon.	wsec_badTargetCategory=VTOL;
    YardMap	                    Defines in more detail the "footprint" of a construction yard (or any stationary building). As an example, the ARM Adv. Air Plant data at the right has 6 groups of 7 values defining an X-Z coordinate "footprint" for the construction yard. The following values are available:








f indicates the space is occupied by a feature (e.g. Dragons teeth)

o indicates occupied points on ground where a unit may not pass. By default, all values are o.

O occupied when building is open - never used.

c defines the "hole" (typically in construction plant units) where the units are built and where they enter or exit. For land buildings.

C same as c but for water buildings.

w seems to indicate those parts of a ship yard that are above water

g (or G) indicates that the space can operate over a geothermal vent. Otherwise, operates just like an O. Created specifically for the geothermal plant

y - standard yard - no footprint on land

Y - standard water yard - no footprint on water. Y is simply a location that will never have a footprint, no matter what.
As you know, footprints are square, but your units aren't always.
This allows you to shape the footprint a little. (i.e. ARMLAB, the corners
are always "footprintless")

If the unit doesn't use "OpenYard()" and "CloseYard()" in the BOS you can simply state "YardMap=o" no matter the size of the footprint. You could also do the opposite by stating "YardMap=c", and the whole footprint will appear and disappear no matter the footprint size.
// For ARM Adv. Air Plant
// FootprintX=7;
// FootprintZ=6;
YardMap=ooooooo ooooooo occccco occccco occccco occccco;
// Thus, the "South" end
// of the plant is open
// while the other sides
// are blocked.


// For ARM Kbot Lab
// FootprintX=6;
// FootprintZ=6;
YardMap=yoccoy ooccoo ooccoo ooccoo ooccoo yoccoy;
// The corners are always
// open, but the middle
// opens and closes
// depending on the unit
// script.
ZBuffer	Does the unit have a z buffer. (All units have this = 1)	ZBuffer=1;

"""