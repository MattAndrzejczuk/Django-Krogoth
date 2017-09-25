from LazarusII.models import Damage, WeaponTDF, FeatureTDF, UnitFbiData, DownloadTDF, SoundSetTDF, UnitFbiData_v2

from rest_framework import serializers, exceptions


class UnitFbiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitFbiData
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.save()
        return instance


class WeaponTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponTDF
        fields = '__all__'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(WeaponTDFDataSerializer, self).get_serializer(*args, **kwargs)


class FeatureTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureTDF
        fields = '__all__'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(FeatureTDFDataSerializer, self).get_serializer(*args, **kwargs)


class DownloadTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadTDF
        fields = '__all__'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DownloadTDFDataSerializer, self).get_serializer(*args, **kwargs)


class SoundTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundSetTDF
        fields = ()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(SoundTDFDataSerializer, self).get_serializer(*args, **kwargs)


#### Fields were printed using:
# >>> str_fields = ''
# >>>
# >>> for (key, value) in data.items():
# ...     str_fields += '"' + key + '",'

class UnitFbiDataSerializer_v2(serializers.ModelSerializer):
    class Meta:
        model = UnitFbiData_v2
        fields = ("norestrict", "SpanishDescription", "canhover", "YardMap", "NoAutoFire", "transportsize", "ShootMe",
                  "MinWaterDepth",
                  "GermanDescription", "HealTime", "MakesMetal", "IsFeature", "MaxDamage", "Builddistance", "CloakCost",
                  "Description",
                  "ImmuneToParalyzer", "MetalStorage", "HideDamage", "Scale", "transportcapacity", "PigLatinName",
                  "Builder", "MaxWaterDepth",
                  "RadarDistance", "CloakCostMoving", "EnergyStorage", "RadarDistanceJam", "WorkerTime",
                  "SelfDestructAs", "PitchScale",
                  "TidalGenerator", "ExtractsMetal", "BMcode", "altfromsealevel", "SightDistance",
                  "Designation",
                  "ItalianDescription", "canstop", "FootprintX", "selfdestructcountdown", "MoveRate1", "BankScale",
                  "Acceleration",
                  "ItalianName", "FrenchName", "FootprintZ", "HoverAttack", "MaxVelocity",
                  "Ovradjust", "canguard",
                  "Name", "canmove", "Commander", "JapaneseName", "ZBuffer", "Side", "mincloakdistance", "MetalMake",
                  "firestandorders",
                  "SteeringMode", "ShowPlayerName", "Canfly", "EnergyMake", "ExplodeAs", "Floater",
                  "canload",
                  "ActiveWhenBuild", "UnitName", "attackrunlength", "FrenchDescription", "maneuverleashlength",
                  "BadTargetCategory",
                  "Stealth", "IsAirBase", "Category", "SoundCategory", "id", "BrakeRate", "ThreeD",
                  "SonarDistanceJam",
                  "Copyright", "SpanishName", "MaxSlope", "TurnRate", "onoffable", "sortbias", "NoShadow", "BuildTime",
                  "NoChaseCategory",
                  "wsec_badTargetCategory", "UnitNumber", "SonarDistance", "StandingFireOrder", "Downloadable",
                  "Corpse", "WaterLine",
                  "BuildCostEnergy", "DefaultMissionType", "canpatrol", "BuildCostMetal", "istargetingupgrade",
                  "CanCapture", "EnergyUse",
                  "teleporter", "antiweapons", "Weapon3", "JapanesDescription", "TEDClass", "ai_limit", "WindGenerator",
                  "CanDgun",
                  "DamageModifier", "kamikazedistance", "PigLatinDescription", "ai_weight", "cruisealt", "GermanName",
                  "Version",
                  "MovementClass", "amphibious", "Objectname", "kamikaze", "BuildAngle", "Weapon1",
                  "wpri_badTargetCategory",
                  "TransMaxUnits", "CanReclamate", "cantbetransported", "Weapon2", "MobileStandOrders", "init_cloaked",
                  "digger",
                  "StandingMoveOrder", "canattack", "Upright", )

    def update(self, instance, validated_data):
        instance.save()
        return instance
