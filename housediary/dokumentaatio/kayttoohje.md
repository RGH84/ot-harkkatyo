# Käyttöohje

Voit ladata projektin uusimman version lähdekoodin suoraan GitHubista. Siirry projektin [releases](https://github.com/RGH84/ot-harkkatyo/releases/tag/viikko6)-sivulle ja valitse Assets-kohdasta Source code ladataksesi tiedostot.

## Ohjelman asennus ja käynnistäminen

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

## Kirjautuminen

Sovellus avautuu suoraan kirjautumisnäkymään:

**Kuva tulee lopullisesta versiosta**

Kirjautua voit syöttämällä voimassa olevan käyttäjätunnuksen ja salasanan vastaaviin kenttiin ja klikkaamalla "Kirjaudu"-painiketta.

## Uuden käyttäjän luominen

Voit siirtyä kirjautumisnäkymästä uuden käyttäjän luontinäkymään napsauttamalla "Luo käyttäjä" -painiketta.

Luo uusi käyttäjäprofiili täyttämällä vaaditut tiedot ja painamalla "Luo"-painiketta:

**Kuva tulee lopullisesta versiosta**

Onnistuneen rekisteröinnin jälkeen ohjelma palauttaa sinut kirjautumisnäkymään.

## Etusivu

Kirjautumisen jälkeen pääset etusivulle, joka esittelee kaikki keskeneräiset tehtäväsi:

**Kuva tulee lopullisesta versiosta**

Tässä näkymässä voit lisätä uusia tehtäviä, merkitä olemassaolevia tehtäviä valmiiksi sekä tarkastella suoritettuja tehtäviä.

## Tehdyt tehtävät

Aikataulutetuille ja aikatauluttomille tehtäville on omat näkymänsä, joissa voit tarkastella valmiita tehtäviä ja poistaa niitä tarpeen mukaan.

**Yksityiskohtaisemmat ohjeet sisällytetään lopulliseen versioon**

