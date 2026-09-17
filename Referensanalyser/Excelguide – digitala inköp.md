# Excelguide – digitala inköp

Syfte: Beskriva Excelmallens fältlogik, fältordning, analysspecifika kunskap och kontrollpunkter för digitala inköp.

## 1. Analysens ram

### Jämförelse

- **Alternativ A:** Hemtjänstpersonal handlar dagligvaror fysiskt i butik.
- **Alternativ B:** Brukaren handlar dagligvaror online med stöd av hemtjänstpersonal och butiken ansvarar för hemleverans.

### Avgränsning

- Analysen gäller digitala inköp i äldreomsorg/hemtjänst där brukaren får stöd att handla dagligvaror digitalt och butiken levererar varorna hem.
- Om hemtjänsten fortfarande hämtar eller kör ut varor behöver jämförelsen och transportnyttan kontrolleras.
- Analysen gäller inte digitalt videostöd under inköpet. Om användaren avser skärmstöd eller digitalt besök ska referensanalysen för digitala besök eller en analys från grunden övervägas.

### Vad som främst driver resultatet

- skillnaden mellan fysisk och digital tidsåtgång,
- andelen brukare som får digitala inköp,
- antalet inköp per brukare och vecka,
- transport, grupphandling och vilka resor som faktiskt försvinner,
- lokalt arbetssätt och ansvar för hemleverans.

## 2. Fältguide

Fältkartan återger alla relevanta vita och grå fält i Excelordning. Guidningen följer den gemensamma guidens regler för status, guidningsordning och hantering av grå fält.

Varje tabell ligger under namnet på den Excelflik där fälten finns. Kolumnen **Block / underblock** visar innehållsstrukturen inom fliken.

### Flik: Nyttokalkyl start

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| — | Namn på förändringen | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med `Digitala inköp`. | Om användaren beskriver videostöd, egen utkörning eller annan modell än hemleverans från butik: kontrollera om rätt referensmall används. |
| — | Vilket år vill ni räkna från? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Följ den gemensamma regeln för startår. | — |
| — | Diskonteringsränta | Grått | Förklara vid behov – ingen inmatning | Förinställd på 3 %. Förklara diskontering kort om användaren frågar. Fältet är låst och kan inte ändras av användaren. | — |
| Lista intressenterna | <Kommunens namn> | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Platshållaren är inte ett giltigt värde. Ersätt den med den aktuella kommunens namn. Kommunnamnet återanvänds automatiskt på andra flikar. | — |
| Lista intressenterna | Brukare; Samhället; Personal | Grått | Förklara vid behov – ingen inmatning | Förifyllda och låsta intressenter. | Om användaren behöver lägga till breda nya intressenter: kontrollera om referensmallen fortfarande passar. |

### Flik: Räkna på nyttor

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Faktorer som används i flera beräkningar / Beräkning av antal personer som kan ha digitala inköp | Antal personer som får hjälp med inköp | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd verksamhets-, planerings- eller bistånds/insatsstatistik. Ge inget generellt riktvärde. | Kontrollera om antalet felaktigt avser alla äldre, alla med hemtjänst eller andra än dem som faktiskt får hjälp med inköp. |
| Faktorer som används i flera beräkningar / Beräkning av antal personer som kan ha digitala inköp | Andel av de som får hjälp med inköp som skulle kunna få digitala inköp | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 70 %. SKR Kompetenscenter har tillsammans med kommuner använt det som en möjlig ambitionsnivå vid ett förändrat arbetssätt. Pröva om nivån passar lokalt och beakta brukare som behöver annan insatsform. | Vid låg andel: fråga om arbetssättet verkligen ska ändras eller om införandet är begränsat. Vid mycket hög andel: kontrollera att undantag för särskilda behov har beaktats. |
| Faktorer som används i flera beräkningar / Beräkning av antal personer som kan ha digitala inköp | Antal brukare som skulle kunna få digitala inköp | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen utifrån antal personer och andel. | — |
| Faktorer som används i flera beräkningar / Beräkning av antal inköp | Antal inköp per brukare och vecka | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | Lokal insatsfrekvens går först. SKR Kompetenscenter har i arbetet med andra kommuner sett att ett inköp per brukare och vecka ofta används i analysen. Pröva om det passar lokalt. | Vid fler än ett inköp per vecka: kontrollera att värdet avser biståndsbeslutade/personalförlagda inköp, inte privata kompletteringsinköp eller undantag. |
| Faktorer som används i flera beräkningar / Beräkning av antal inköp | Antal inköp per år, totalt; Antal digitala inköp per år, totalt | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen. | — |
| Faktorer som används i flera beräkningar / Timkostnader | Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr) | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med 359 kr. Följ gemensam regel för förifyllda timkostnader. | — |
| Faktorer som används i flera beräkningar / Timkostnader | Timkostnad enhetschef (nivå 2) (kr) | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med 551 kr. Följ gemensam regel för förifyllda timkostnader. | — |
| Faktorer som används i flera beräkningar / Timkostnader | Timkostnad personal som arbetar med förändringsledning (kr) | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Följ gemensam regel för tomma timkostnadsfält. | — |
| Faktorer som används i flera beräkningar / Timkostnader | Timkostnad systemadministratör, offentlig sektor (kr) | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Följ gemensam regel för tomma timkostnadsfält. | — |
| Faktorer som används i flera beräkningar / Drivmedel | Bensin; Etanol E85; Diesel; HVO100; El; Fordonsgas | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för informationstabellen med drivmedelskostnader. | — |
| Frigjorda resurser till omvårdnad istället för serviceinsatser / Tidsåtgång för fysiska inköp idag | Tidsåtgång per inköpstillfälle, exklusive restid (min) | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | Använd faktisk lokal tid. Vid grupphandling ska total butikstid delas på de brukare som handlas åt. SKR Kompetenscenter har i arbetet med kommuner sett 20–45 minuter per brukare; omkring 30 minuter är vanligt. Pröva vad som passar lokalt. | Vid 45 minuter eller mer: kontrollera att det är tid per brukare, inte total grupphandlingstid. Vid 60 minuter per brukare: kontrollera särskilt. |
| Frigjorda resurser till omvårdnad istället för serviceinsatser / Tidsåtgång för fysiska inköp idag | Tidsåtgång för resa till och från butik (min) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd lokal restid för inköpsresan. Vid grupphandling ska restiden fördelas på de brukare som ingår i rundan. | Om tiden räknas från varje brukares bostad: kontrollera om grupphandlingen i praktiken utgår från hemtjänstlokal eller annan startpunkt. |
| Frigjorda resurser till omvårdnad istället för serviceinsatser / Tidsåtgång för fysiska inköp idag | Total tidsåtgång för fysiska inköp i snitt per inköpstillfälle (min); Antal inköp per år, totalt; Total tidsåtång för fysiska inköp per år (timmar) | Grått | Förklara vid behov – ingen inmatning | Hämtas eller beräknas av mallen. | — |
| Frigjorda resurser till omvårdnad istället för serviceinsatser / Tidsåtgång när en del av inköpen görs digitalt | Tidsåtgång per digitalt inköpstillfälle, exlusive transport (min) | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Bedöm faktisk tid för att stödja brukaren. Digitalt inköp kan ta ungefär lika lång tid som fysiskt inköp när brukaren är aktivt delaktig och väljer varor. | Om digital tid är mycket lägre än fysisk tid: fråga om brukaren verkligen deltar eller om personalen bara matar in en inköpslista. |
| Frigjorda resurser till omvårdnad istället för serviceinsatser / Tidsåtgång när en del av inköpen görs digitalt | Antal digitala inköp per år, totalt; Total tidsåtgång för digitala inköp per år, totalt (timmar) | Grått | Förklara vid behov – ingen inmatning | Hämtas eller beräknas av mallen. | — |
| Frigjorda resurser till omvårdnad istället för serviceinsatser / Frigjord tid | Antal inköp som fortsatt görs fysiskt; Total tidsåtgång för de inköp som fortsatt görs fysiskt; Total tidsåtgång för digitala och fysiska inköp (timmar); Frigjord tid när vissa inköp görs digitalt (timmar); Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr) | Grått | Förklara vid behov – ingen inmatning | Mallen räknar samman fysisk och digital tidsåtgång och hämtar timkostnaden. | Vid oväntat hög frigjord tid: kontrollera fysisk tid, digital tid, andel digitala inköp och grupphandlingslogik. Kontrollera att hela den fysiska tiden inte har räknats bort när stöd fortfarande behövs digitalt. |
| Minskade transportkostnader / Antal bilresor som undviks | Andel inköp som görs med bil idag (procent) | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Fråga hur stor andel av inköpen som görs med bil, inte hur stor andel av hemtjänstens resor generellt som görs med bil. Inköp görs ofta med bil eftersom varor kan vara tunga, men använd ingen generell procentsats. | Vid låg andel som görs med bil: fråga hur varor faktiskt hämtas eller transporteras. Kontrollera att procent inte matas in som heltal på fel sätt. |
| Minskade transportkostnader / Antal bilresor som undviks | Antal digitala inköp per år, totalt; Antal av digitala inköp som annars hade gjorts med bil | Grått | Förklara vid behov – ingen inmatning | Hämtas eller beräknas av mallen. | — |
| Minskade transportkostnader / Antal mil som undviks | Transportsträcka med bil per inköpstillfälle (km) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd körsträckan för de inköpsresor som faktiskt försvinner. Vid grupphandling ska sträckan fördelas på brukarna i rutten. | Räkna inte hela hemtjänstrutten om bara inköpsresan påverkas. Kontrollera tur/retur, grupphandling och eventuell dubbelräkning. |
| Minskade transportkostnader / Antal mil som undviks | Antal sparade mil per år | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen. | — |
| Minskade transportkostnader / Drivmedelskostnader | Typ av drivmedel | Vitt (tomt) | Välj efter lokal situation i lista | Välj i rullistan det drivmedel som bäst motsvarar de berörda resorna. Vid osäkerhet eller flera drivmedel: välj försiktigt så att nyttan inte överskattas; det billigaste relevanta alternativet kan användas som försiktigt antagande. | — |
| Minskade transportkostnader / Drivmedelskostnader | Kostnad för drivmedel per mil | Grått | Förklara vid behov – ingen inmatning | Hämtas från den kalkylfaktor från Inera som valts för drivmedlet. | — |

### Flik: Räkna på kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Kostnad för digital teknik | En (1) surfplatta täcker såhär många personer | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 15 eftersom flera brukare kan dela en surfplatta. Hjälp användaren pröva om det passar det lokala arbetssättet. | Vid mycket lägre antal: fråga om fler surfplattor verkligen behövs eller om de kan delas. |
| Kostnad för digital teknik | Antal brukare som skulle kunna få digitala inköp; Antal surfplattor som behövs | Grått | Förklara vid behov – ingen inmatning | Hämtas eller beräknas av mallen. | — |
| Kostnad för digital teknik | Leasingskostnad för surfplatta inkl. abonnemang, per år (kr) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd avtal, upphandlad standardkostnad eller lokal kostnadsmodell. Ge inget prisintervall. Kontrollera vad som ingår: surfplatta, abonnemang, SIM-kort, support, försäkring, MDM eller annat. | — |
| Förändringsledning | Antal timmar för förändringsledning totalt | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | Utgå från lokal införandeplan. Om en lokal bedömning saknas kan assistenten berätta att SKR Kompetenscenter i arbetet med kommuner har sett analyser som använder 3 timmar per brukare som ska få insatsen. Pröva om det passar lokalt. Tiden avser arbetssätt, organisation, rutiner och stöd till brukare och personal. | Vid lågt värde: kontrollera att rutiner, rollfördelning, information, stöd och införande i verksamheten ingår. |
| Förändringsledning | Timkostnad personal som arbetar med förändringsledning (kr) | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet på fliken Räkna på nyttor. | — |
| Utbildning av personal under införandet | Antal personer som behöver utbildning | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Räkna den personal som ska kunna stödja digitala inköp. Det kan vara all berörd hemtjänstpersonal eller en lokalt avgränsad grupp. | Vid mycket få personer: kontrollera att all personal som behöver kunna ge stödet finns med. |
| Utbildning av personal under införandet | Tidsåtgång för utbildning per person (timmar) | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 1,5 timmar. Behåll om lokal utbildningsplan saknas; höj om lösningen kräver mer. Antalet personer är ofta mer resultatdrivande än exakt tid per person. | — |
| Utbildning av personal under införandet | Totalt antal timmar för utbildning; Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr) | Grått | Förklara vid behov – ingen inmatning | Beräknas eller hämtas av mallen. | — |
| Tidsåtgång för information till brukare | Antal brukare som skulle kunna få digitala inköp | Grått | Förklara vid behov – ingen inmatning | Hämtas från fliken Räkna på nyttor. | — |
| Tidsåtgång för information till brukare | Tidsåtgång för att informera hos brukare (min) | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 20 minuter. Avser första informationen och motivationen, inte det löpande stödet vid varje inköp. | Vid oro, motstånd eller större informationsbehov: pröva om tiden behöver höjas. Blanda inte ihop den med inköpstiden. |
| Tidsåtgång för information till brukare | Totalt antal timmar för att informera hos brukare; Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr) | Grått | Förklara vid behov – ingen inmatning | Beräknas eller hämtas av mallen. | — |
| Kostnader för drift, förvaltning och support | Tidsåtgång för drift, support och förvaltning per surfplatta och år (timmar) | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 1 timme per surfplatta och år. Avser återkommande drift/support, inte införande, utbildning eller förändringsledning. | Vid högt värde: kontrollera om andra aktiviteter har blandats in eller dubbelräknats. |
| Kostnader för drift, förvaltning och support | Antal surfplattor som behövs; Timkostnad systemadministratör, offentlig sektor (kr) | Grått | Förklara vid behov – ingen inmatning | Hämtas från tidigare fält. | — |

### Flik: Fler nyttor & kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Nyttor som inte värderats i pengar | Ökad delaktighet för brukaren; Ökad självständighet för brukaren; Ökad trygghet för brukaren; Förbättrad arbetsmiljö för personal | Grått | Förklara vid behov – ingen inmatning | Säg: ”Här ser ni andra nyttor som SKR Kompetenscenter har identifierat tillsammans med kommuner. De värderas inte i pengar i kalkylen, men de förväntas också finnas och är värdefulla i helhetsbilden.” Om en tidigare workshop gav fler nyttor kan de bekräftas, men de kan inte skrivas in på den låsta fliken. | — |
| Kostnader som inte värderats i pengar | Inga förifyllda kostnader | Grått | Förklara vid behov – ingen inmatning | Det finns inga förifyllda kostnader som inte värderas i pengar. Fliken är låst och innehåller inget som användaren ska fylla i eller bedöma. | — |

### Flik: Resultat nyttokalkyl

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Tabell: sammanfattning | Sammanlagd nettonytta efter 6 år (kr); Nettonytta per investerad krona efter 6 år (kr); Nyttorna överstiger kostnaderna år:; Finansiell nytta (%); Omfördelningsnytta (%); Finansiell kostnad (%); Omfördelningskostnad (%); Nyttor som inte värderats i pengar | Grått | Förklara vid behov – ingen inmatning | Följ den gemensamma regeln för att uppdatera och förklara resultatet. | Om användaren vill förstå utfallet eller om det finns en konkret indikation på fel: använd relevanta kontroller i avsnitt 4. |

## 3. Analyskunskap och viktiga samband

Använd kunskapen i detta avsnitt när den hjälper användaren att förstå analysens avgränsning och hur nyttorna och kostnaderna hänger samman. Använd fältguiden för stöd om enskilda fält, förifyllda värden och rimlighetsnivåer.

| Tema | Kunskap att kunna förklara |
| --- | --- |
| Analysens avgränsning | Analysen jämför ett arbetssätt där hemtjänstpersonal handlar dagligvaror fysiskt i butik med ett arbetssätt där brukaren handlar online med stöd av hemtjänstpersonal och butiken ansvarar för hemleveransen. Om hemtjänsten fortfarande hämtar eller kör ut varorna ska endast den tid och transport som faktiskt försvinner räknas som nytta. Analysen omfattar inte digitalt videostöd under inköpet. |
| Nyttor som värderas i pengar | Den finansiella nyttan är minskade drivmedelskostnader. Omfördelningsnyttan är frigjord arbetstid genom minskad tid för fysiska inköp och resor, efter att tiden för det digitala inköpsstödet har räknats med. |
| Kostnader | Den finansiella kostnaden är kostnaden för den digitala tekniken. Omfördelningskostnaderna omfattar förändringsledning, utbildning, information till brukare samt drift och support. En eventuell leveransavgift för brukaren kan behöva synliggöras i helhetsbilden, men har inget eget värderat fält i den aktuella Excelmallen. |
| Nyttor som inte värderas i pengar | Mallen visar förväntade kvalitetsnyttor som ökad delaktighet, självständighet och trygghet för brukaren samt förbättrad arbetsmiljö för personal. De värderas inte i pengar i kalkylen men kan ha ett värde även när värdet inte uttrycks i pengar. Ytterligare nyttor som kommunen redan har identifierat kan bekräftas men kan inte läggas till i denna Excelmall. |

## 4. Analysspecifika kontroller och vanliga feltolkningar

Använd relevanta kontroller när flera inmatningar behöver bedömas tillsammans eller när det finns risk för felaktig avgränsning eller dubbelräkning. Använd fältguiden för kontroller av enskilda värden och enheter. Kontrollerna ska inte genomföras som en obligatorisk extra genomgång.

| Kontrollområde | Kontrollera eller förklara |
| --- | --- |
| Analysens omfattning | Kontrollera att förändringen innebär att brukaren handlar digitalt med stöd av hemtjänstpersonal och att butiken ansvarar för hemleveransen. Om hemtjänsten fortfarande hämtar eller kör ut varorna, eller om förändringen gäller digitalt videostöd, behöver analysens avgränsning prövas. |
| Målgrupp och inköpsvolym | Kontrollera att antalet personer med inköpshjälp, andelen som kan få digitala inköp och antalet inköp bygger på samma målgrupp och period. Fysiska och digitala inköp ska inte båda räknas som om de omfattar hela volymen. |
| Fysisk och digital tidsåtgång | Kontrollera att fysisk och digital tidsåtgång bedöms tillsammans. Vid grupphandling ska gemensam butiks- och restid fördelas mellan berörda brukare. Den digitala tiden ska omfatta det stöd som fortfarande behövs för att brukaren ska kunna genomföra inköpet och vara delaktig. |
| Transport och hemleverans | Kontrollera att restid, andel bilresor och körsträcka endast avser inköpsresor som faktiskt försvinner. Vid gemensamma inköpsrutter ska tid och sträcka fördelas så att samma transport inte räknas en gång per brukare. |
| Teknik, införande och förvaltning | Kontrollera att antalet tekniska enheter är förenligt med det lokala arbetssättet för delning och att kostnaden motsvarar avtalets omfattning. Samma aktivitet eller kostnad ska inte räknas flera gånger som exempelvis förändringsledning, utbildning, information, löpande stöd vid inköpet eller drift och support. |

## 5. Analysspecifikt stöd när resultatet förklaras

Följ den gemensamma regeln för att förklara resultatet. Använd stödet nedan för att koppla resultatet till kommunens inmatningar och till dokumenterade erfarenheter av digitala inköp.

- Om fysisk och digital inköpstid är ungefär lika kan den värderade nyttan främst bestå av den restid som försvinner och de minskade drivmedelskostnaderna. Använd relevanta kontroller i avsnitt 4 och den fältspecifika vägledningen för att förklara kommunens resultat.
- När resultatet huvudsakligen består av omfördelningsnytta, förklara att en stor del av värdet utgörs av frigjord arbetstid och att nyttan realiseras när tiden används på nya sätt.
- Påminn vid behov om att resultatet i pengar inte omfattar de kvalitetsnyttor som beskrivs i avsnitt 3. Om brukaren får en leveransavgift som inte har värderats i mallen behöver även den synliggöras separat i helhetsbilden.