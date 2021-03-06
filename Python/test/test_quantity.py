# encoding: utf-8
from unittest import TestCase
import src.quantity as quantity
from decimal import Decimal


class TestQuantityBaseUnitConversion(TestCase):

    def test_length(self):
        l = quantity.Length(1.0, 'm')

        self.assertEqual(l('Em'), Decimal('1e-18'))
        self.assertEqual(l('Pm'), Decimal('1e-15'))
        self.assertEqual(l('Tm'), Decimal('1e-12'))
        self.assertEqual(l('Gm'), Decimal('1e-9'))
        self.assertEqual(l('Mm'), Decimal('1e-6'))
        self.assertEqual(l('km'), Decimal('1e-3'))
        self.assertEqual(l('hm'), Decimal('1e-2'))
        self.assertEqual(l('dam'), Decimal('0.1'))
        self.assertEqual(l('dm'), Decimal('10.'))
        self.assertEqual(l('cm'), Decimal('100.'))
        self.assertEqual(l('mm'), Decimal('1000.'))
        self.assertEqual(l('μm'), Decimal('1e6'))
        self.assertEqual(l('nm'), Decimal('1e9'))
        self.assertEqual(l('pm'), Decimal('1e12'))
        self.assertEqual(l('fm'), Decimal('1e15'))
        self.assertEqual(l('am'), Decimal('1e18'))

    def test_mass(self):
        m = quantity.Mass(1.0, 'kg')
        self.assertEqual(m('Eg'), Decimal('1e-15'))
        self.assertEqual(m('Pg'), Decimal('1e-12'))
        self.assertEqual(m('Tg'), Decimal('1e-9'))
        self.assertEqual(m('Gg'), Decimal('1e-6'))
        self.assertEqual(m('Mg'), Decimal('1e-3'))
        self.assertEqual(m('kg'), Decimal('1'))
        self.assertEqual(m('hg'), Decimal('10'))
        self.assertEqual(m('dag'), Decimal('100'))
        self.assertEqual(m('dg'), Decimal('10000.'))
        self.assertEqual(m('cg'), Decimal('100000.'))
        self.assertEqual(m('mg'), Decimal('1000000.'))
        self.assertEqual(m('μg'), Decimal('1e9'))
        self.assertEqual(m('ng'), Decimal('1e12'))
        self.assertEqual(m('pg'), Decimal('1e15'))
        self.assertEqual(m('fg'), Decimal('1e18'))
        self.assertEqual(m('ag'), Decimal('1e21'))

    def test_time(self):
        t = quantity.Time(1.0, 's')

        self.assertEqual(t('ms'), Decimal('1000.'))
        self.assertEqual(t('μs'), Decimal('1e6'))
        self.assertEqual(t('ns'), Decimal('1e9'))
        self.assertEqual(t('ps'), Decimal('1e12'))
        self.assertEqual(t('fs'), Decimal('1e15'))
        self.assertEqual(t('as'), Decimal('1e18'))

    def test_time_from_s(self):
        t = quantity.Time(1.0, "s")
        self.assertEqual(t('s'), Decimal('1'))


    def test_aos(self):
        n = quantity.AmountOfSubstance(1.0, 'kmol')
        self.assertEqual(n('mol'), 1000.0)

    def test_temperature_from_K(self):
        t = quantity.Temperature(0.0, 'K')
        self.assertEqual(t('K'), Decimal('0.0'))
        self.assertEqual(t('°C'), Decimal('-273.15'))
        self.assertEqual(t('°F'), Decimal('-459.67'))

    def test_temperature_from_C(self):
        t = quantity.Temperature(-40.0, '°C')
        self.assertEqual(t('°C'), Decimal('-40.0'))
        self.assertEqual(t('K'), Decimal('233.15'))
        self.assertAlmostEqual(t('°F'), Decimal('-40.0'), delta=1e-9)

    def test_temperature_from_F(self):
        t = quantity.Temperature(-40.0, '°F')
        self.assertAlmostEqual(t('K'), Decimal('233.15'), delta=1e-9)
        self.assertEqual(t('°C'), Decimal('-40.0'))


class TestQuantityBaseUnitComparison(TestCase):

    def test_comparing_base_to_base_equal(self):
        m1 = quantity.Mass(1., 'g')
        m2 = quantity.Mass(1., 'g')
        self.assertTrue(m1 == m2)
        self.assertTrue(m1 <= m2)
        self.assertTrue(m1 >= m2)
        self.assertFalse(m1 > m2)
        self.assertFalse(m1 < m2)
        self.assertFalse(m1 != m2)

    def test_comparing_base_to_base_greater(self):
        m1 = quantity.Mass(2., 'g')
        m2 = quantity.Mass(1., 'g')
        self.assertFalse(m1 == m2)
        self.assertFalse(m1 <= m2)
        self.assertTrue(m1 >= m2)
        self.assertTrue(m1 > m2)
        self.assertFalse(m1 < m2)
        self.assertTrue(m1 != m2)

    def test_comparing_base_to_base_less(self):
        m1 = quantity.Mass(1., 'g')
        m2 = quantity.Mass(2., 'g')
        self.assertFalse(m1 == m2)
        self.assertTrue(m1 <= m2)
        self.assertFalse(m1 >= m2)
        self.assertFalse(m1 > m2)
        self.assertTrue(m1 < m2)
        self.assertTrue(m1 != m2)

    def test_comparing_none_base_to_base_equal(self):
        l1 = quantity.Length(1000., 'mm')
        l2 = quantity.Length(1., 'm')
        self.assertTrue(l1 == l2)
        self.assertTrue(l1 <= l2)
        self.assertTrue(l1 >= l2)
        self.assertFalse(l1 > l2)
        self.assertFalse(l1 < l2)
        self.assertFalse(l1 != l2)

    def test_comparing_none_base_to_base_greater(self):
        l1 = quantity.Length(10000., 'mm')
        l2 = quantity.Length(1., 'm')
        self.assertFalse(l1 == l2)
        self.assertFalse(l1 <= l2)
        self.assertTrue(l1 >= l2)
        self.assertTrue(l1 > l2)
        self.assertFalse(l1 < l2)
        self.assertTrue(l1 != l2)

    def test_comparing_none_base_to_base_less(self):
        l1 = quantity.Length(100., 'mm')
        l2 = quantity.Length(1., 'm')
        self.assertFalse(l1 == l2)
        self.assertTrue(l1 <= l2)
        self.assertFalse(l1 >= l2)
        self.assertFalse(l1 > l2)
        self.assertTrue(l1 < l2)
        self.assertTrue(l1 != l2)

    def test_comparing_none_base_to_none_base(self):
        m1 = quantity.Mass(100., 'dag')
        m2 = quantity.Mass(1., 'kg')
        self.assertTrue(m1 == m2)

    def test_comparing_base_to_base_temperature(self):
        t1 = quantity.Temperature(273.15, 'K')
        t2 = quantity.Temperature(273.15, 'K')
        self.assertTrue(t1 == t2)