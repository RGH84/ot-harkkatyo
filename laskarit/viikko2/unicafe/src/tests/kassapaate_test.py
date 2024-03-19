import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti_rahaa_on = Maksukortti(1000)
        self.kortti_rahaa_ei = Maksukortti(200)

    def test_kassan_saldo_alussa_oikein(self):
    
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_lounaiden_maara_alussa_oikein(self):
        #Sen verran selkeä, että voinee kummankin tarkistaa kerralla.
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullisella_lounaalla_maksu_riittävä_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_toimii_edullisella_lounaalla_maksu_riittävä_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(vaihtoraha, 260)

    def test_kateisosto_toimii_edullisella_lounaalla_maksu_riittävä_myydyt_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullisella_lounaalla_maksu_ei_riittävä_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_edullisella_lounaalla_maksu_ei_riittävä_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(vaihtoraha, 200)

    def test_kateisosto_toimii_edullisella_lounaalla_maksu_ei_riittävä_myydyt_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_maukkaalla_lounaalla_maksu_riittävä_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_toimii_maukkaalla_lounaalla_maksu_riittävä_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_toimii_maukkaalla_lounaalla_maksu_riittävä_myydyt_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_toimii_maukkaalla_lounaalla_maksu_ei_riittävä_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_maukkaalla_lounaalla_maksu_ei_riittävä_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(vaihtoraha, 200)

    def test_kateisosto_toimii_maukkaalla_lounaalla_maksu_ei_riittävä_myydyt_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_rahaa_riittavasti_raha_lahtee_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_rahaa_on)

        self.assertEqual(str(self.kortti_rahaa_on), "Kortilla on rahaa 7.60 euroa")

    def test_korttiosto_edullinen_rahaa_riittavasti_palauttaa_true(self):
    
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti_rahaa_on))

    def test_korttiosto_edullinen_rahaa_riittavasti_lounaiden_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_rahaa_on)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_rahaa_riittavasti_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_rahaa_on)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_edullinen_rahaa_ei_riittavasti_raha_lahtee_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_rahaa_ei)

        self.assertEqual(str(self.kortti_rahaa_ei), "Kortilla on rahaa 2.00 euroa")

    def test_korttiosto_edullinen_rahaa_ei_riittavasti_palauttaa_false(self):
    
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti_rahaa_ei))

    def test_korttiosto_edullinen_rahaa_ei_riittavasti_lounaiden_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_rahaa_ei)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_rahaa_ei_riittavasti_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_rahaa_ei)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_rahaa_riittavasti_raha_lahtee_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_rahaa_on)

        self.assertEqual(str(self.kortti_rahaa_on), "Kortilla on rahaa 6.00 euroa")

    def test_korttiosto_maukas_rahaa_riittavasti_palauttaa_true(self):
    
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti_rahaa_on))

    def test_korttiosto_maukas_rahaa_riittavasti_lounaiden_maara_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_rahaa_on)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_maukas_rahaa_riittavasti_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_rahaa_on)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_rahaa_ei_riittavasti_raha_lahtee_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_rahaa_ei)

        self.assertEqual(str(self.kortti_rahaa_ei), "Kortilla on rahaa 2.00 euroa")

    def test_korttiosto_maukas_rahaa_ei_riittavasti_palauttaa_false(self):
    
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.kortti_rahaa_ei))

    def test_korttiosto_maukas_rahaa_ei_riittavasti_lounaiden_maara_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_rahaa_ei)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_maukas_rahaa_ei_riittavasti_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_rahaa_ei)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti_rahaa_ei, 500)

        self.assertEqual(str(self.kortti_rahaa_ei), "Kortilla on rahaa 7.00 euroa")

    def test_lataa_rahaa_kortille_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti_rahaa_ei, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_lataa_rahaa_kortille_ei_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti_rahaa_ei, -500)

        self.assertEqual(str(self.kortti_rahaa_ei), "Kortilla on rahaa 2.00 euroa")

    def test_kassassa_rahaa_euroina_palauttaa_oikein(self):

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    

