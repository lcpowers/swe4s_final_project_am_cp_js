"""Unit testing for functions in fpho_setup
"""
import fpho_setup
import unittest
import random


class TestImportFiberphoData(unittest.TestCase):

    def test_column_assignments_one_fiber(self):
        fTime, f1Red, f1Green = fpho_setup.import_fpho_data('1FiberTest.csv')
        test_time = ['52111503.5648', '52111528.4224', '52111553.6768',
                     '52111579.1104', '52111603.6736', '52111628.608',
                     '52111653.696', '52111678.848', '52111704.256',
                     '52111729.792', '52111754.176', '52111779.0592',
                     '52111804.0832', '52111829.1584', '52111855.296',
                     '52111879.296', '52111904.3712', '52111929.4336',
                     '52111954.9312', '52111979.5456']
        self.assertEqual(fTime, test_time)

        test_red = ['1360.02593259583', '1543.68695652174', '1888.49759025813',
                    '1379.57643426807', '1544.10860132064', '1883.40917588543',
                    '1379.09578938341', '1543.43963639482', '1881.64479890232',
                    '1379.13064059686', '1543.77490781237', '1881.50361032501',
                    '1378.9618729097', '1543.00722065003', '1880.44435297144',
                    '1379.31223737244', '1542.8058657062', '1880.79807906698',
                    '1379.1495755081', '1542.52636995112']
        self.assertEqual(f1Red, test_red)

        test_green = ['1510.66266506603', '1649.64105642257',
                      '1540.86554621849', '1511.04921968788',
                      '1649.37254901961', '1539.86634653862',
                      '1510.93917567027', '1648.68547418968',
                      '1540.050020008', '1510.9443777511',
                      '1648.91356542617', '1540.14965986395',
                      '1511.02521008403', '1648.08083233293',
                      '1539.74429771909', '1510.95918367347',
                      '1647.96798719488', '1540.39575830332',
                      '1511.10444177671', '1647.51860744298']
        self.assertEqual(f1Green, test_green)
        
        def test_column_assignments_one_fiber(self):
            fTime, f1Red, f1Green, f2Red, f2Green = fpho_setup.import_fpho_data(
                                                                '1FiberTest.csv')
            test_time = ['57887085.8496', '57887107.8144',
                         '57887132.3904', '57887157.6448',
                         '57887182.5664', '57887207.8336',
                         '57887232.704', '57887257.5616',
                         '57887282.7008', '57887308.032',
                         '57887333.1712', '57887358.0288',
                         '57887382.9632', '57887407.9232',
                         '57887433.3952', '57887458.0352',
                         '57887483.136', '57887508.9536',
                         '57887533.4016', '57887558.3104']
            self.assertEqual(fTime, test_time)
            
            test_red1 = ['644.744558543487', '678.416060082934',
                         '647.206535086939', '644.814607841392',
                         '678.270266422253', '647.262916229155',
                         '644.723486803467', '678.379611667764',
                         '647.031696595419', '644.656285037997',
                         '678.365943512075', '647.200270515581',
                         '644.59420883091', '678.557867198206',
                         '647.119970100909', '644.794675114346',
                         '678.310701382833', '647.334674046522',
                         '644.818024880315', '678.212746267063']
            self.assertEqual(f1Red, test_red1)
            
            test_green1 = ['712.658962090541', '706.853029076187',
                           '714.173102686787', '712.524225248436',
                           '706.683430253957', '714.162738314317',
                           '712.601486934118', '706.846433566434',
                           '714.076996687523', '712.630695620169',
                           '706.940655134339', '714.133529628267',
                           '712.506323150534', '706.897313213103',
                           '714.293706293706', '712.506323150534',
                           '706.771056312109', '714.288995215311',
                           '712.807832167832', '706.860566801619']
            self.assertEqual(f1Green, test_green1)

            test_red2 = ['661.240182347449', '702.872228630014',
                         '663.797440544845', '661.14175866425',
                         '703.062045733326', '663.734168177075',
                         '661.214990571392', '703.00814704967',
                         '663.732410611303', '661.227293531792',
                         '703.05911645704', '663.754087255817',
                         '661.062668204537', '703.013419746984',
                         '663.687299756504', '661.326888925505',
                         '702.928470734699', '663.968510279929',
                         '661.102506362022', '703.291700994123']
            self.assertEqual(f2Red, test_red2)
            
            test_green2 = ['479.767687953734', '456.4006398425',
                           '515.287149829785', '479.69746934088',
                           '456.525983347689', '515.158525081006',
                           '479.75784422296', '456.437389770723',
                           '514.962962962963', '479.951437594848',
                           '456.417702309175', '514.988556662975',
                           '480.10959353595', '456.319265001435',
                           '514.76740084492', '480.127968500062',
                           '456.411139821992', '515.082400229687',
                           '479.812969115295', '456.644108116976']
            self.assertEqual(f2Green, test_green2)
            

if __name__ == '__main__':
    unittest.main()
