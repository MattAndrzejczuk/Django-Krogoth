from django.test import TestCase
from LazarusV.super_hpi.hpi_I_dependency_gatherer import TotalACompileManager
# Create your tests here.

class SuperHPITestCase(TestCase):
    def setUp(self):
        test_path = '/usr/src/persistent/media/Processed_HPI_Archives/root/ArmPrime_1.0_mattsAbel/'
        ta_compile_manager = TotalACompileManager(root_fbi_path=test_path)

    def test_basic_disassembler_units(self):
        test_path = '/usr/src/persistent/media/Processed_HPI_Archives/root/ArmPrime_1.0_mattsAbel/'
        ta_compile_manager = TotalACompileManager(root_fbi_path=test_path)
        print(ta_compile_manager.superHPI.disassembled_units)



"""
from LazarusV.super_hpi.hpi_I_dependency_gatherer import TotalACompileManager
test_path = '/usr/src/persistent/media/Processed_HPI_Archives/root/ArmPrime_1.0_mattsAbel/'
ta_compile_manager = TotalACompileManager(root_fbi_path=test_path)
print(ta_compile_manager.superHPI.disassembled_units)
"""

"""
from LazarusV.super_hpi.hpi_Z_debug import logged_disassembler

"""