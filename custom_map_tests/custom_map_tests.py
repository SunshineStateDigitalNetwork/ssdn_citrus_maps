import os
import unittest
import json
from datetime import date
from pathlib import Path
from citrus.cli import transform

test_dir_path = os.path.abspath(os.path.dirname(__file__))

def stand_up(self):
    with open(os.path.join(test_dir_path, 'transformation_test_data/transformation_verification.json')) as fp:
        self.data = [json.loads(line) for line in fp]
    self.config = {'ssdn': {'InFilePath': os.path.join(test_dir_path, 'transformation_test_data'),
                            'OutFilePath': os.path.join(test_dir_path, 'transformation_test_data'),
                            'Provider': 'Sunshine State Digital Network',
                            'CustomMapPath': os.path.split(test_dir_path)[0]}}
    return self

def clean():
    os.remove(Path(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')))

"""
2 = Broward College Archives & Special Collections
4 = Florida Atlantic University
5 = Florida Gulf Coast University Library
8 = Florida State College at Jacksonville
16 = Miami-Dade Public Library System
18 = University of South Florida Libraries
"""    


class FSUCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()
    
    def test_fsu_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'Florida State University Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'fsu', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[13])
        
        
class FBCTLHCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()
        
    def test_fbctlh_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'First Baptist Church of Tallahassee',
                               'IntermediateProvider': 'Florida State University Libraries',
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'fbctlh', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[9])
        
        
class LeonHighCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()
        
    def test_fbctlh_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'First Baptist Church of Tallahassee',
                               'IntermediateProvider': 'Florida State University Libraries',
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'leon', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[12])        
        
        
class GodbyHighCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()
        
    def test_fbctlh_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'First Baptist Church of Tallahassee',
                               'IntermediateProvider': 'Florida State University Libraries',
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'godby', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[10])   


class HavanaHHSCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)
                                                            
    def tearDown(self):
        clean()
        
    def test_fbctlh_mods_custom_map(self):
        transformation_info = {'Map': 'fsu_mods_map',
                               'DataProvider': 'First Baptist Church of Tallahassee',
                               'IntermediateProvider': 'Florida State University Libraries',
                               'Scenario': 'SSDNMODS'}
        transform(self.config, transformation_info, 'havana', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[11])


class FIUCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_fiu_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Florida International University Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'fiu', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[7])


class BoyntonBeachCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_boynton_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Boynton Beach City Library Archives',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'boynton', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[0])
        


class BrockwayCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_boynton_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Miami Shores Village Archives at Brockway Memorial Library',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'brockway', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[1])
        
        
class CoralGablesCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_boynton_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'City of Coral Gables',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'coral_gables', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[3])


class MBVMCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_boynton_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Miami Design Preservation League, Closeup Productions',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'mbvm', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[6])


class GNMHSCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_boynton_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Greater North Miami Historical Society',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'gnmhs', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[14])


class VaclavCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_boynton_dc_custom_map(self):
        transformation_info = {'Map': 'fiu_dc_map',
                               'DataProvider': 'Vaclav Havel Library Foundation',
                               'IntermediateProvider': 'Florida International University Libraries',
                               'Scenario': 'SSDNDC'}
        transform(self.config, transformation_info, 'vhlf', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[19])
        
        
class UMCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()

    def test_boynton_dc_custom_map(self):
        transformation_info = {'Map': 'um_qdc_map',
                               'DataProvider': 'University of Miami Libraries',
                               'IntermediateProvider': None,
                               'Scenario': 'SSDNQDC'}
        transform(self.config, transformation_info, 'um', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[17])
        
"""        
class IR_FIUCustomMapTestCase(unittest.TestCase):

    def setUp(self):
        self = stand_up(self)

    def tearDown(self):
        clean()
    
    def test_fsu_mods_custom_map(self):
        transformation_info = {'Map': '',
                               'DataProvider': 'Florida International University Libraries',
                               'IntermediateProvider': None,
                               'Scenario': ''}
        transform(self.config, transformation_info, 'fsu', verbosity=1)
        with open(os.path.join(test_dir_path, 'transformation_test_data', f'SSDN_TMP-{date.today()}.jsonl')) as fp:
            test_data = json.load(fp)
        self.assertEqual(test_data, self.data[])        
"""


if __name__ == '__main__':
    unittest.main()
