# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AssetAttributeTestCase(ModuleTestCase):
    'Test Asset Attribute module'
    module = 'asset_attribute'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AssetAttributeTestCase))
    return suite
