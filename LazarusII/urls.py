from django.conf.urls import url, include
from LazarusII import views
from LazarusII.views import UnitFbiData, ApiNavigationUrls, LazarusListUnits, \
    CustomToastGenerator, ExecuteBash, AutoCollectStatic, OpenTotalAnnihilationFBIFile, OpenTotalAnnihilationTDFFile, \
    UserAgentTracker, ExecuteBash_LS_AllCustomModFiles, OpenTotalAnnihilationFBIFileII, UnitFBIViewset

# Pure Python Stuff:
from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair





urlpatterns = [

    url(r'^help_api/$', ApiNavigationUrls.as_view()),

    # userAgentTracker
    url(r'^UserAgentTracker', UserAgentTracker.as_view()),

    url(r'^unit_fbi/$', views.getUnitFbiUsingId),
    # url(r'^UnitFbiData/$', UnitFbiData.as_view(), name='UnitFbiData'),
    url(r'^LazarusListUnits/', LazarusListUnits.as_view(), name='LazarusListUnits'),
    url(r'^ExecuteBash/', ExecuteBash.as_view(), name='ExecuteBash'),
    url(r'^AutoCollectStatic/', AutoCollectStatic.as_view(), name='AutoCollectStatic'),
    url(r'^CustomToast/', CustomToastGenerator.as_view(), name='CustomToast'),

    url(r'^OpenTotalAnnihilationFBIFile/', OpenTotalAnnihilationFBIFile.as_view(), name='OpenTotalAnnihilationFBIFile'),
    url(r'^OpenTotalAnnihilationTDFFile/', OpenTotalAnnihilationTDFFile.as_view(), name='OpenTotalAnnihilationTDFFile'),

    url(r'^OpenTotalAnnihilationFBIFileII/', OpenTotalAnnihilationFBIFileII.as_view(), name='OpenTotalAnnihilationFBIFileII'),

    url(r'^UnitFBIViewset/', UnitFBIViewset.as_view(), name='UnitFBIViewset'),
    # url(r'^UnitFBIViewset/', include(router.urls)),

    url(r'^ExecuteBash_LS_AllCustomModFiles/', ExecuteBash_LS_AllCustomModFiles.as_view(), name='ExecuteBash_LS_AllCustomModFiles'),
]









# = models.CharField(max_length=100)
# = models.FloatField(null=True, blank=True)
# = models.IntegerField()
# = models.BooleanField(default=False)

"""
    Acceleration	            How fast the unit acceleration
    ActivateWhenBuilt	        Is the default state of this unit ACTIVATED (or ON) when built.
    ai_limit	                Limit of number the AI will build of this unit.
    ai_weight	                The weighting (ie. what % of these to to build. I don't know what the units are)
    altfromsealevel	            Altitude from sea. For flying units. Don't quite understand this one myself.
    amphibious	                Is the unit amphibious (can go under water, & on land.
    antiweapons	                Does this unit shoot at the weapons of other units eg. Missile defence systems
    attackrunlength	            For planes. The distance they must travel before being able to drop their bombs/shoot their missiles. HoverAttack is like attackrunlength=0, I think
    BMcode	                    A BMcode. Every unit has a value of 1, except for contstruction plants (eg. Air Craft Plant, Vehical Plants). So do likewise.
    BadTargetCategory	        The type of target that is not good for that low accuracy at this type of unit. In general. The value specified identifies all units that have that value specified in their own "Category" settings.
    BankScale	                The Scale (see Scale) of the unit when banking (ie. turning if its an aircraft)
    BrakeRate	                The rate at which the unit can slow down
    BuildAngle	                No idea. Here's a possibility: Random angle to build unit on, example is the solar panel some times facing 180 degrees from the solar panel next to it.
    BuildCostEnergy	            The amount of energy that will be consumed during the building of this unit. I think value < 0 generate errors, but I've never tried.
    BuildCostMetal	            Same as above, but amount of metal.
    BuildTime	                The time is takes to build this unit. On average, 10000 is medium time, things like fusion plants are more like 100000, and krogoth like 300000
    Builddistance	            The distance at which a unit can build if it is a builder.
    Builder	                    Can this unit build other units.
    canattack	                Can the unit attack.
    CanCapture	                Can this unit capture other units.
    CanDgun	                    Can the unit DGUN (ie. has a gun like the commander)
    Canfly	                    Can this unit fly.
    canguard	                Can this unit guard.
    canhover	                Can this unit hover
    canload	                    Can this unit load other units.
    canmove	                    Can this unit move.
    canpatrol	                Can this unit patrol.
    CanReclamate	            Can this unit reclaim things.
    canstop	                    Can this unit stop.
    cantbetransported	        Is this a unit that transports cannot load eg. Ships, krogoth
    Category	                A category class. Look at some of the FBI files in totala1.hpi for examples. Essentially, this places the unit in several named catagories that can be named in other variables such as "wpri_badTargetCategory" described below, and in the AI Text files as well.
    CloakCost	                The energy cost of this unit remaining cloaked when standing still.
    CloakCostMoving 	        The energy cost of this unit remaining cloaking while moving.
    Commander	                Is this unit the (a?) commander.
    Copyright	                The copyright of this unit. Must be as shown to the right, or won't work. (Most people copy this line as a comment, and put their own copyright infomation in the commented-out version.
    Corpse	                    The name of the feature the unit turns into when the unit dies. If the unit is a feature (Dragons Teeth) the unit instantly turns into this feature, when it is finished being built. (this is not the 3do file of the feature, the feature entry tells the 3do file to use in the feautres OBJECT variable).
    cruisealt	                The altitude at which the unit flys
    DamageModifier	            The rate at which this unit heals itself.
    DefaultMissionType	        The default orders of this unit for missions.
    Description	                The description of the unit seen at the bottom of the screen when you hold the cursor over it in the game.
    Designation	                The designation. This is unimportant and can have virtually any value (there may be a limit to the number of character it will except)
    digger	                    Does this unit have pieces which extend under ground. I think thats what it means. Things like the pop-up heavy cannon have this = 1.
    Downloadable	            Is this a unit which has been downloaded off the internet. If you want to be able to use the unit, put 1.
                                (12/28/98) Note from The Raptor: Not true. I haven't included this variable in all of my units, and they work just fine. It's just one that we started seeing in the Cavedog weekly units, so assumed that's what it meant. It really seems to do nothing.
    EnergyMake	                The energy this unit produces when ACTIVE.
    EnergyStorage	            The amount added to the maximum amount of energy you can store while the unit is alive.
    EnergyUse	                The amount of energy the unit uses while it is ACTIVE.
    ExplodeAs	                The explosion ID of the explosion that will happen if the unit explodes. See totala1.hpi for other examples.
    ExtractsMetal	            The rate at which the unit extracts metal. (Yes, the MOHOmine only extracts at like 0.01)
    firestandorders	            Can this unit give firestandorders. You know as much as me.
    Floater	                    Does this unit float on water.
    FootprintX	                The X axis footprint. Should correlate with the unit model's actual size. The footprint helps control how close units can get to one another.
    FootprintZ	                As with FootprintX, but the Z axis (ie. up and down on the screen while playing TA). Should correlate with the unit model's actual size.

    FrenchDescription	        As description, but in French.
    FrenchName	                As Name, but in French	FrenchName=Zeus;
    GermanDescription	        As description, but in German	GermanDescription=Überschwerer Gefechtspanzer;
    GermanName	                As Name, but in german	GermanName=A.K.;

    HealTime	                The time it take for this unit to heal itself. (Typically used by commanders)
    HideDamage	                Whether or not to show the amount of damage done to this unit to the opponent(s). Commanders have this value set.
    HoverAttack	                Will this attack while remaining in the same spot, even though it is an aircraft. Like the brawler.
    ImmuneToParalyzer	        Is this unit immune to being paralyzed.
    init_cloaked	            When built this unit is cloaked.
    IsAirBase	                Is this unit an airbase. Only the air repair pad and aircraft carriers have this as 1
    IsFeature	                Is this unit a feature. eg. The dragons teeth. Features do not appear on radar.
    istargetingupgrade	        Does this unit upgrade the targeting so that units shoot at things on radar like at things seen by that unit.
    ItalianDescription	        As description, but in Italian	ItalianDescription=Veicolo veloce da attacco;
    ItalianName	                As Name, but in Italian	ItalianName=Zipper;
    JapanesDescription	        As description, but in Japanese	JapaneseDescription=XXXX;
    JapaneseName	            As Name, but in Japanese	JapaneseName=Jeffysan;
    kamikaze	                Does this unit kill itself to attack its target eg. The roach/invader
    kamikazedistance	        How far from the target must the unit be to do a kamikaze attack
    MakesMetal	                Does this unit make metal. eg. Metal Maker NS
    maneuverleashlength	        How far from the course that the unit is patrolling / moving on will it vary if it is attacked / distracted.
    MaxDamage	                Amount of damage unit can take before dying (i.e "Hit Points"). Kbots have about 600, Tanks have about 2000, Planes have about 500, Commander has 3000
    MaxSlope	                What is the maximum slope this unit can go on.
    MaxVelocity	                What is the maximum speed of this unit. Commander is 1.07, Core Storm is 1.25, Arm Hawk is 12
    MaxWaterDepth	            What is maximum depth of water this unit can go in
    MetalMake	                The amount of metal generated by construction units
    MetalStorage	            The amound added to your maximum metal storage while this unit is alive	MetalStorage=900;
    mincloakdistance	        The distance the unit must have on every side to remain cloaked. If another unit moves into this area, the unit uncloaks.	mincloakdistance=90;
    MinWaterDepth	            The minimum depth of water this unit can be in	MinWaterDepth=8;
    MobileStandOrders	        Basically, I think, can this unit hold position of all mobile units, only the transports (all of them) have this equal to 0.	MobileStandOrders=1;
    MoveRate1	                Planes seem to use this. For example, all planes except the air transports have values of 8, the transports have values of 1.	MoveRate1=1;

    MovementClass	            How the unit moves. See totala1.hpi for examples. Movement classes are typically described in TDF files in the gamedata directory. (The moveinfo.tdf file is a good guess). It is used as a shortcut way of setting certain parameters (such as those listed here) by grouping them and giving them a name.
    Name	                    The name that appears on the bottom of the screen when you select a unit.
    NoAutoFire	                Double negative. 1 means this unit will not automatically fire at other units. 0 means it will.
    NoChaseCategory	            Category the unit will not chase. The value specified identifies all units that have that value specified in their own "Category" settings.	NoChaseCategory=VTOL;
    norestrict	                If the unit apears in the multiplayer Unit Restrictions menu. For example, the way the commander does not apear in the list.
    NoShadow	                Does this unit not have a shadow (most water units don't)
    Objectname	                This is the name of your 3do file.
    onoffable	                Can this unit be turned on and off. On is ACTIVE, OFF is INACTIVE
    Ovradjust	                No idea. Some units just have this
    PigLatinDescription	        As description but in Pig Latin.	PigLatinDescription=Astfay attackay Outingscay Ehiclevay;
    PigLatinName	            As Name but in Pig Latin.	PigLatinName=Effyjay;
    PitchScale

    RadarDistance	            Distance that shown to you on radar by your unit
    RadarDistanceJam	        Distance that is jammed by unit.
    Scale	                    The size modifier from 3DO file into the game. I think. I don't actually know.
    SelfDestructAs	            The explosion that happens when a unit self desctructs. See totala1.hpi for examples.
    selfdestructcountdown	    The number the self-destruct count down starts at.
    ShootMe	                    Does this unit broadcast itself as a target? (eg. Dragons's Teeth has this as 0, all other units as 1) If this is 0, then enemy units will not choose to attack this unit regardless of their orders.

    ShowPlayerName	            Show the players name as a description (like the commander)
    Side	                    Which side does the unit belong to ARM, CORE.
    SightDistance	            The distance from the unit that everything is shown in. ie. Distance it gets rid of Fog of War. Unfortunately, this value seems to have a limit of around 400.
    SonarDistance	            The distance given to you as sonar, on the mini map.
    SonarDistanceJam	        This is how far the unit jams sonar on the mini map.
    sortbias
    SoundCategory	            The "sound category" the unit uses. Sound categories are typically described in TDF files in the gamedata directory. (The sounds.tdf file is a good place to start). It is used to describe a group of sounds to associate with a unit, such as what sounds does it make when it starts, stops, arrives at a destination, is activated, is deactivated, etc.
    SpanishDescription	        As description, in Spanish.	SpanishDescription=Vehículo todoterreno de ataque;
    SpanishName	                As Name, but in Spanish	SpanishName=Zipper;
    StandingFireOrder	        This is the initial fire order the unit starts with. 0 = Hold Fire; 1 = Return Fire; 2 = Fire at Will.

    StandingMoveOrder	        this is the initial movement order the unit starts with. 0 = Hold Position; 1 = Move; 2 = Roam
    Stealth	                    Is this unit inivisible on sonar and radar.
    SteeringMode	            The way in which the unit turns. See totala1.hpi for options.
    TEDClass	                Important...I think. Define what type of unit it is.
    teleporter	                Is this unit a teleporter. The two galatic gates have this = 1.
    ThreeD	                    Is the unit 3D.
    TidalGenerator	            Is the unit a Tidal generator?
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

"""