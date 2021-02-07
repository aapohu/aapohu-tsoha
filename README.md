Tämä projekti on harjoitustyö [Tsoha](https://hy-tsoha.github.io/materiaali/index
)-kurssille 

Palautus 7.2.21:
Tässä vaiheessa ei ole vielä koeajovalmista versiota herokussa. 

Uusien käyttäjien rekisteröintitoiminnon toteuttamisessa tuli ongelmia joten varsinaisesti toimivia ominaisuuksia on vasta 
viestien lähettäminen olemassaoleviin keskusteluihin ja sisäänkirjautuminen valmiille käyttäjälle. 

Tällä hetkellä tietokannassa on neljä taulua, Käyttäjät, alueet, keskustelut ja viestit. Näihin tauluihin tulee muutoksia ja tauluja tulee myös lisää sitä mukaa kun saan lisättyä niitä vaativia ominaisuuksia. 

Sovellus on vielä toistaiseksi yksittäinen app.py-tiedosto. Ensi viikolla on tarkoitus mm. eriyttää sovelluksen toiminnot eri tiedostoihin.



Tavoitteena on tehdä keskustelusovellus/foorumi, jossa on seuraavat ominaisuudet:
   - Foorumilla on useita alueita
      - Alueilla on viestiketjuja, jotka koostuvat niihin lähetetyistä viesteistä
          
   - Foorumilla on kahden tasoisia käyttäjiä (peruskäyttäjä, ylläpitäjä)
       - Ylläpitäjä voi:
          - Luoda uusia keskustelualueita
          - Muokata peruskäyttäjien käyttölupia
          - Tehdä kaiken, minkä peruskäyttäjäkin voi
       - Peruskäyttäjä voi:
          - Selata niitä alueita, joihin hänellä on lupa
          - Aloittaa uuden viestiketjun
          - Lähettää viestin ketjuun
          - Muokata tai poistaa lähettämänsä viestin
          - Tykätä toisten käyttäjien viesteistä
          
   - Viestejä voi etsiä hakutoiminnolla, haun voi rajata tietylle alueelle
