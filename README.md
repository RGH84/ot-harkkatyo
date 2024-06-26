# HouseDiary

## Sovelluksen tarkoitus

Tämä sovellus on suunniteltu helpottamaan omakotitalojen ylläpitoa tarjoamalla käyttäjille mahdollisuuden luoda ja hallita henkilökohtaista huoltopäiväkirjaa. Sovellus palvelee erityisesti pientaloasujia. Se on kuitenkin käyttökelpoinen kaiken tyyppisten kiinteistöjen ylläpidossa. Jokainen rekisteröitynyt käyttäjä saa käyttöönsä oman huoltopäiväkirjan, mikä tekee kodin huoltotoimenpiteiden seurannasta ja suunnittelusta vaivatonta. 

## Huomio Python-versiosta ja suoritusympäristöstä

Sovelluksen Python-version vähimmäisvaatimus on `3.8`. Sovelluksen toiminta on testattu Ubuntu 22.04.4 LTS ja Cubbli Linux järjestelmillä.

## Dokumentaatio

- [Vaatimusmäärittely](./housediary/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./housediary/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./housediary/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./housediary/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./housediary/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](./housediary/dokumentaatio/testausdokumentti.md)

## Asennus

1. Kloonattuasi tämän projektin, mene hakemistoon housediary komennolla:
   
```bash
cd housediary
```

2. Asenna tarvittavat riippuvuudet suorittamalla seuraava komento:

```bash
poetry install
```

3. Tee tarpeelliset alustavat toimenpiteet käyttämällä komentoa:

```bash
poetry run invoke build
```

4. Käynnistä sovellus antamalla komento:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman voi suorittaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

Raportti tallentuu _htmlcov_-hakemistoon.

### Koodin laatu

Pylint testit voi ajaa komennolla:

```bash
poetry run invoke lint
```

Automaattisen formatoinnin voi ajaa komennolla:

```bash
poetry run invoke autoformat
```







