import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_saldo_vahenee_oikein_jos_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(15000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_palauttaa_true_jos_rahat_riittavat(self):

        self.assertTrue(self.maksukortti.ota_rahaa(1000))

    def test_palauttaa_false_jos_rahat_ei_riita(self):

        self.assertFalse(self.maksukortti.ota_rahaa(1500))

    def test_saldo_euroina_oikein(self):
        self.maksukortti.saldo_euroina()

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
