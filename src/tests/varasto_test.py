import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):

    def test_normaali(self):
        self.varasto = Varasto(10)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    ##Vaara alkutilavuus
    def test_setUpVaara(self):
        self.varasto = Varasto(-2)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    ##Vaara alkutilavuus ja saldo
    def test_setUpVaaraVaara(self):
        self.varasto = Varasto(-2, -2)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    #Alkusaldo 5
    def test_alkuSaldo(self):
        self.varasto = Varasto(10, 5)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    #Alkusaldo liian suuri
    def test_alkuSaldo(self):
        self.varasto = Varasto(10, 11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    #Alkusaldo neg
    def test_alkuSaldoNeg(self):
        self.varasto = Varasto(10, -2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #Alkusaldo sama
    def test_alkuSaldoSama(self):
        self.varasto = Varasto(10, 10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def setUp(self):
        self.varasto = Varasto(10)


    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    #Lisätään täsmälleen oikea määrä
    def test_lisataan(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    #laitetaan negatiivinen
    def test_laitetaanNeg(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    ##laitetaan liikaa
    def test_laitetaanLiikaa(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    ##laitetaan sama
    def test_laitetaanSama(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    ##Otetaan liikaa
    def test_otetaanLiikaa(self):
        self.varasto.lisaa_varastoon(10)
        otettu = self.varasto.ota_varastosta(11)
        self.assertAlmostEqual(otettu, 10)

    ##Otetaan neg määrä
    def test_otetaanVaara(self):
        otettu = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(otettu, 0)

    ##Otetaan nollasta
    def test_otetaanNollasta(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(2), 0)

    ##Otetaan sama määrä
    def test_otetaanSama(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(otettu, 5)

    ##str
    def test_tulostus(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_tulostus_rikki(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10.0")
