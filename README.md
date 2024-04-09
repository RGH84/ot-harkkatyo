# HouseDiary

## Sovelluksen tarkoitus

Tämä sovellus on suunniteltu helpottamaan omakotitalojen ylläpitoa tarjoamalla käyttäjille mahdollisuuden luoda ja hallita henkilökohtaista huoltopäiväkirjaa. Sovellus palvelee erityisesti pientaloasujia. Se on kuitenkin käyttökelpoinen kaiken tyyppisten kiinteistöjen ylläpidossa. Jokainen rekisteröitynyt käyttäjä saa käyttöönsä oman huoltopäiväkirjan, mikä tekee kodin huoltotoimenpiteiden seurannasta ja suunnittelusta vaivatonta. 

## Huomio Python-versiosta ja suoritusympäristöstä

Sovelluksen Python-version vähimmäisvaatimus on `3.8`. Sovelluksen toiminta on testattu Ubuntu 22.04.4 LTS ja Cubbli Linux järjestelmillä.

## Muita huomioita

Sovelluksen kehityksen alkuvaiheessa sovellukseen on otettu runsaasti vaikutteita kurssin referenssisovelluksesta, ToDoAppista, jotta kehitystyö pääsi jouhevasti käyntiin. Tämän seurauksena sovellus muistuttaa monin osin kyseistä referenssisovellusta tässä vaiheessa. Nyt, kun sovelluksen perustoimintalogiikka alkaa olla selvillä, siiryn vahvemmin kohti oman näköistä koodia. Ohjaajaa antanee palautetta, mikäli hän katsoo, että sovellus muistuttaa liikaa referenssisovellusta tässä vaiheessa.

Sovellus on vielä kehityksen alkutaipaleella. Tällä hetkellä sovelluksessa voi luoda käyttäjän, tarkastella muita käyttäjiä ja ns. kirjautua sisään/ulos. Sovelluksen käyttö tapahtuu tällä hetkellä teksipohjaisesti. 

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

1. Asenna tarvittavat riippuvuudet suorittamalla seuraava komento:

```bash
poetry install
```

2. Tee tarpeelliset alustavat toimenpiteet käyttämällä komentoa:

```bash
poetry run invoke build
```

3. Käynnistä sovellus antamalla komento:

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




