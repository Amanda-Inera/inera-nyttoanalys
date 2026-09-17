# Excelguide – digital nattillsyn

# Excelguide – digital nattillsyn

Syfte: Beskriva Excelmallens fältlogik, fältordning, analysspecifika kunskap och kontrollpunkter för digital nattillsyn.

## 1. Analysens ram

### Jämförelse

- **Alternativ A:** Nattillsyn görs genom fysiska personalbesök i bostaden.
- **Alternativ B:** Brukaren får digital nattillsyn på distans via kamera i bostaden.

### Avgränsning

- Analysen gäller digital nattillsyn via kamera i bostaden.
- Om användaren vill analysera sensorbaserad nattillsyn, bredare trygghetspaket eller nattillsyn där sensorer är huvudlösningen ska denna referensanalys inte användas. Hänvisa till från-grunden-flödet.
- Värderade nyttor uppstår främst när fysiska tillsynsbesök kan ersättas och restid/körtid minskar.
- Digital nattillsyn ersätter bara besök som enbart gäller tillsyn. Besök med toalettbesök, personlig omvårdnad eller andra insatser ska inte räknas som ersatta tillsynsbesök.

### Vad som främst driver resultatet

- kostnad för kamera/välfärdsteknik per månad,
- antal brukare med digital nattillsyn,
- antal besök per natt med enbart nattillsyn,
- restid, körsträcka och andel besök med bil,
- antal personal vid fysiska nattillsynsbesök,
- egen personal eller extern leverantör för digital nattillsyn,
- tid för digital nattillsyn med egen personal,
- drift/support/förvaltning.

## 2. Fältguide

Fältkartan återger alla relevanta vita och grå fält i Excelordning. Guidningen följer den gemensamma guidens regler för status, guidningsordning och hantering av grå fält.

Varje tabell ligger under namnet på den Excelflik där fälten finns. Kolumnen **Block / underblock** visar innehållsstrukturen inom fliken.

### Flik: Nyttokalkyl start

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| — | Namn på förändringen | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med `Digital nattillsyn`. | Om användaren beskriver sensorer eller bredare trygghetsteknik: kontrollera om referensmallen passar. |
| — | Vilket år vill ni räkna från? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Följ den gemensamma regeln för startår. | — |
| — | Diskonteringsränta | Grått | Förklara vid behov – ingen inmatning | Förinställd på 3 %. Förklara diskontering kort om användaren frågar. Fältet är låst och ingår inte i den ordinarie guidningen. | — |
| Lista intressenterna | <Kommunens namn> | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Platshållaren är inte ett giltigt värde. Ersätt den med den aktuella kommunens namn. Kommunnamnet återanvänds automatiskt på andra flikar. | — |
| Lista intressenterna | Brukare; Samhället; Personal | Grått | Förklara vid behov – ingen inmatning | Förifyllda och låsta intressenter. | Om användaren behöver lägga till breda nya intressenter: kontrollera om referensmallen fortfarande passar. |

### Flik: Räkna på nyttor

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Faktorer som används i flera beräkningar | Hur många brukare kommer ha digital nattillsyn i kommunen? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal uppgift eller uppskattning. Förklara vid behov att en majoritet av brukare med nattillsyn ofta kan ha digital nattillsyn, men att kommunens beslut och registrering av nattinsatser påverkar. | Ge ingen generell siffra. Om användaren räknar alla med nattbesök: fråga om alla verkligen har enbart tillsyn eller om vissa har personlig omvårdnad/toalettbesök. |
| Faktorer som används i flera beräkningar | Hur många besök får varje brukare per natt i snitt, med enbart nattillsyn? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Hjälp användaren avgränsa till besök som bara gäller tillsyn. Det kan kräva manuell kontroll i verksamheten om besluten inte skiljer på tillsyn och omvårdnad. | Om användaren inkluderar alla nattbesök: stoppa och förklara att bara rena tillsynsbesök ska räknas här. |
| Faktorer som används i flera beräkningar | Antal besök med enbart digital nattillsyn per natt och per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen utifrån antal brukare och besök per natt. Förklara bara vid behov. | Be inte användaren fylla i beräknade/hämtade fält. |
| Timkostnader | Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för timkostnader. | Lokala uppgifter går före Ineras förifyllda kalkylfaktor. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| Timkostnader | timkostnad grundutbildad sjuksköterska | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för timkostnader. | Lokala uppgifter går före Ineras förifyllda kalkylfaktor. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| Timkostnader | timkostnad personal som arbetar med förändringsledning | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Följ den gemensamma regeln för timkostnader. | Lokala uppgifter går före Ineras förifyllda kalkylfaktor. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| Timkostnader | timkostnad systemadministratör | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Följ den gemensamma regeln för timkostnader. | Lokala uppgifter går före Ineras förifyllda kalkylfaktor. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| Drivmedel | kalkylfaktorer för drivmedel: Bensin, Etanol E85, Diesel, HVO100, El, Fordonsgas | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för drivmedel. Förifyllda värden kan normalt användas om lokala uppgifter saknas. | Assistenten ska inte proaktivt föreslå uppdaterade drivmedelsvärden. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| 1. Minskade kostnader för drivmedel | Hur stor andel av nattillsynsbesöken gör ni med bil idag (procent)? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal bedömning för kommunen/verksamheten som helhet. Väg in landsbygd, glesbygd, tätort, storstad, nattpatruller och faktisk organisering. | Om användaren utgår från en enskild nattpatrull/hemtjänstgrupp: fråga om analysen gäller hela kommunen och om snittet behöver breddas. |
| 1. Minskade kostnader för drivmedel | Antal besök med enbart digital nattillsyn per år | Grått | Förklara vid behov – ingen inmatning | Hämtas från tidigare beräkning. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält. |
| 1. Minskade kostnader för drivmedel | Hur många km kör ni per besök i snitt, tur och retur? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal kördata, ruttplanering eller sammanvägd verksamhetsbedömning. Det ska avse genomsnittlig körsträcka tur och retur per fysiskt tillsynsbesök som ersätts. | Om värdet bygger på ytterfall: be användaren tänka genomsnitt. Kontrollera att värdet inte avser hela nattpatrullens rutt om fältet avser per besök. |
| 1. Minskade kostnader för drivmedel | Typ av drivmedel | Vitt (tomt) | Välj efter lokal situation i lista | Fältet är en rullista med drivmedel från drivmedelstabellen. Använd faktisk lokal fordonsanvändning. Om osäkert: välj försiktigt, ofta billigaste alternativet, för att inte överskatta nyttan. | Använd inte färska externa drivmedelspriser i v1. Använd Ineras förifyllda kalkylfaktorer, lokala uppgifter eller uppdaterad kalkylfaktor från Inera i kunskapsbasen om användaren uttryckligen efterfrågar det. |
| 1. Minskade kostnader för drivmedel | Kostnad för drivmedel per mil | Grått | Förklara vid behov – ingen inmatning | Hämtas från den kalkylfaktor från Inera som valts för drivmedlet. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält. |
| 2. Frigjord tid för omvårdnadspersonal genom färre besök | Antal besök med enbart digital nattillsyn per år | Grått | Förklara vid behov – ingen inmatning | Hämtas från tidigare beräkning. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält. |
| 2. Frigjord tid för omvårdnadspersonal genom färre besök | Hur lång tid tar ett besök med enbart nattillsyn i snitt för en person (exklusive restiden)? (min) | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Mallen är förifylld med 5 minuter, en nivå som SKR Kompetenscenter har sett användas för rena tillsynsbesök. Personalen tittar då ofta bara till att brukaren sover eller är okej. Hjälp användaren bedöma om 5 minuter passar lokalt. | Om användaren anger betydligt längre tid: fråga om besöket egentligen innehåller andra insatser än tillsyn. Sådana besök ska inte räknas som enbart nattillsyn. |
| 2. Frigjord tid för omvårdnadspersonal genom färre besök | Hur lång tid tar resan till och från brukaren, i snitt, för en person? (min) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokalt snitt. Värdet ska avse restid kopplad till tillsynsbesöket, inte hela nattens rutt. | Om restiden verkar mycket hög/låg: fråga om den speglar kommunen som helhet och nattens rutter. |
| 2. Frigjord tid för omvårdnadspersonal genom färre besök | Hur många personal brukar oftast vara med vid fysiska nattillsyns-besök? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren ange hur arbetet faktiskt görs. Ofta är det 1 eller 2 personer. Detta styrs ofta av arbetsmiljö/trygghet för personal, område och lokal policy, inte bara brukarens behov. | Om värdet är 2: påminn att tidsnyttan multipliceras med antal personal. Om kommunen varierar mellan 1 och 2: be om försiktigt genomsnitt. |
| 2. Frigjord tid för omvårdnadspersonal genom färre besök | Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 3. Frigjord tid för personal som arbetar med arbets- och schemaplanering | Hur många personer arbetar med arbets-och schemaplanering, per år? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Fråga hur kommunen organiserar planering: centralt eller per grupp. | Om användaren är osäker: håll det enkelt. Denna nytta brukar inte vara den största resultatdrivaren. |
| 3. Frigjord tid för personal som arbetar med arbets- och schemaplanering | Hur många timmar frigörs för varje person som arbetar med arbets- och schemaplanering, per år, tack vare digital nattillsyn? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal uppskattning. Digital nattillsyn kan förenkla planering genom färre fysiska nattbesök. | Lägg inte oproportionerligt mycket tid på exakt uppskattning om användaren saknar underlag. |
| 3. Frigjord tid för personal som arbetar med arbets- och schemaplanering | Timkostnad grundutbildad sjuksköterska | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |

### Flik: Räkna på kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| 1. Kostnad för kameror | Hur många brukare kommer ha digital nattillsyn i kommunen? | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Förklara vid behov att värdet bara ska fyllas i en gång. | Be inte användaren fylla i hämtade fält här. |
| 1. Kostnad för kameror | Kostnad för en kamera per månad (kr) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd lokalt avtal, offert eller upphandlingsunderlag. Förklara att analysen gäller kamera. | Ge inget prisintervall och säg inte att ett visst pris verkar rimligt. Om kostnaden gäller sensor, sensorpaket eller bredare trygghetspaket: stoppa och förklara att mallen gäller kamera. Vid sensorlösning bör användaren börja från grunden. |
| 2. Kostnad för förändringsledning | Hur många timmar behöver ni lägga på förändringsledning under införandet för att lyckas med nyttorna? | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | SKR Kompetenscenter har sett en kommun använda 400 timmar för 90 brukare. Pröva om det hjälper den lokala bedömningen. Digital nattillsyn är ofta enklare än läkemedelsautomater, men förändringsledning behövs ändå. Hjälp användaren tänka på nya rutiner, beslut, tillit till kameratillsyn, arbetsledning, nattpersonal och samspel med eventuell leverantör. | Om värdet är mycket lågt: fråga om tid för rutiner, informationsarbete, förankring hos personal, brukare och närstående samt hantering av oro finns med. |
| 2. Kostnad för förändringsledning | Timkostnad personal som arbetar med förändringsledning | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 3. Kostnad för utbildning under införandet | Hur många personer behöver utbildas under införandet? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Beror på om kommunen gör digital tillsyn själv eller om extern leverantör gör tillsynen. Om egen personal utför tillsynen: räkna berörd nattpersonal. Om extern leverantör utför tillsynen: intern personal kan ändå behöva känna till kamera, rutiner och larmflöden. | Om användaren bara tar med ett fåtal: fråga om alla berörda roller kan hantera rutiner och tryggt svara på frågor. |
| 3. Kostnad för utbildning under införandet | Tidsåtgång per person (timmar) | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Mallen är förifylld med 1 timme. SKR Kompetenscenter har sett den nivån användas i kommunernas analyser av digital nattillsyn. Pröva om den lokala utbildningsplanen kräver mer eller mindre tid. | Normalt ingen stark kontrolltrigger; antal personer är oftare viktigare än tiden per person. |
| 3. Kostnad för utbildning under införandet | Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 4. Installation, information och registrering av brukare år 1 | Hur många brukare kommer ha digital nattillsyn i kommunen? | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält här. |
| 4. Installation, information och registrering av brukare år 1 | Tidsåtgång för information, installation och registrering av brukare (timmar) | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Mallen är förifylld med 2 timmar per brukare, en nivå som SKR Kompetenscenter har sett användas i kommunernas analyser. Pröva om den passar den lokala processen. | Om kommunen har tungt informations- eller trygghetsskapande arbete med brukare och närstående kan tiden behöva höjas. |
| 4. Installation, information och registrering av brukare år 1 | Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 5. Övrig kostnad för drift, support, m.m. | Hur många timmar tror ni att ni kommer lägga på drift, support och förvaltning av digital nattillsyn, per år? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Beror på antal kameror och ansvarsfördelning. Om kommunen gör mycket själv kan tiden bli högre; om leverantören ansvarar för drift kan intern tid bli lägre. Vid behov kan assistenten berätta att SKR Kompetenscenter har sett 25–400 timmar per år i kommunernas analyser. | Om användaren lägger mycket lågt trots egen drift/egen tillsyn: fråga om support, felhantering, uppföljning och leverantörskontakt finns med. |
| 5. Övrig kostnad för drift, support, m.m. | Timkostnad systemadministratör, offentlig sektor | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 6. Personal som arbetar med digital nattillsyn | Hur många personer kommer att arbeta med digital nattillsyn, i snitt, varje natt? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Används om kommunen använder egen personal för digital nattillsyn. Det kan vara en person på kontor eller flera personer som gör digital tillsyn löpande/mobilt under arbetspass. | Om kommunen använder extern leverantör: lämna detta block och använd blocket Extern leverantör av digital nattillsyn i stället. Undvik dubbelräkning. |
| 6. Personal som arbetar med digital nattillsyn | Hur många timmar kommer personerna arbeta enbart med digital nattillsyn i snitt, varje natt? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren skilja tid som faktiskt ägnas åt digital nattillsyn från annan nattpersonalstid. | Om digital tillsyn sker löpande bland andra uppgifter: hjälp användaren uppskatta bara den andel av tiden som avser digital nattillsyn. |
| 6. Personal som arbetar med digital nattillsyn | Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 7. Extern leverantör av digital nattillsyn | Hur mycket kostar varje tillsynsbesök som leverantören utför? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd leverantörsavtal/offert. Detta är en finansiell kostnad. | Ge inget prisintervall. Om kommunen inte har extern leverantör: lämna detta block och räkna i stället på egen personal. Undvik dubbelräkning. |
| 7. Extern leverantör av digital nattillsyn | Antal besök med enbart digital nattillsyn per år | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält här. |

### Flik: Fler nyttor & kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Nyttor som inte värderas i pengar | Förbättrad arbetsmiljö för personal genom färre resor; Förbättrad arbetsmiljö för personalen genom bättre balans; Ökad trygghet för brukare; Bättre hälsa hos brukaren; Minskad miljöpåverkan för samhället | Grått | Förklara vid behov – ingen inmatning | Säg: ”Här ser ni andra nyttor som SKR Kompetenscenter har identifierat tillsammans med kommuner. De värderas inte i pengar i kalkylen, men de förväntas också finnas och är värdefulla i helhetsbilden.” Om en tidigare workshop gav fler nyttor kan de bekräftas, men de kan inte skrivas in på den låsta fliken. | — |
| Kostnader som inte värderats i pengar | Inga analysspecifika kostnader är förifyllda i aktuell Excelversion. | Grått | Förklara vid behov – ingen inmatning | Det finns inga förifyllda kostnader som inte värderas i pengar. Fliken är låst och innehåller inget som användaren ska fylla i eller bedöma. | — |

### Flik: Resultat nyttokalkyl

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Tabell: sammanfattning | Sammanlagd nettonytta efter 6 år (kr); Nettonytta per investerad krona efter 6 år (kr); Nyttorna överstiger kostnaderna år:; Finansiell nytta (%); Omfördelningsnytta (%); Finansiell kostnad (%); Omfördelningskostnad (%); Nyttor som inte värderats i pengar | Grått | Förklara vid behov – ingen inmatning | Följ den gemensamma regeln för att uppdatera och förklara resultatet. | Om användaren vill förstå utfallet eller om det finns en konkret indikation på fel: använd relevanta kontroller i avsnitt 4. |

## 3. Analyskunskap och viktiga samband

Använd kunskapen i detta avsnitt när den hjälper användaren att förstå analysens avgränsning och hur nyttorna och kostnaderna hänger samman. Använd fältguiden för stöd om enskilda fält, förifyllda värden och rimlighetsnivåer.

| Tema | Kunskap att kunna förklara |
| --- | --- |
| Analysens avgränsning | Analysen jämför fysisk nattillsyn genom personalbesök i bostaden med digital nattillsyn på distans via kamera. Den digitala tillsynen kan utföras av kommunens personal eller en extern leverantör. Endast besök som enbart gäller tillsyn och kan ersättas helt ska räknas som ersatta. Sensorbaserad nattillsyn och bredare sensor- eller trygghetspaket omfattas inte av analysen. |
| Nyttor som värderas i pengar | Den finansiella nyttan är minskade drivmedelskostnader genom färre resor. Omfördelningsnyttorna är frigjord arbetstid för omvårdnadspersonal genom färre fysiska besök och minskad restid samt frigjord tid för arbets- och schemaplanering. Den tid som kommunens personal fortfarande använder för digital nattillsyn ska räknas som en kostnad. |
| Kostnader | De finansiella kostnaderna är kostnaden för kameror och, när det är aktuellt, kostnaden per tillsynsbesök från en extern leverantör. Omfördelningskostnaderna omfattar förändringsledning, utbildning, information, installation och registrering av brukare, drift, support och förvaltning samt arbetstid för egen personal som utför digital nattillsyn. |
| Nyttor som inte värderas i pengar | Mallen visar förväntade nyttor som förbättrad arbetsmiljö genom färre resor och bättre balans, ökad trygghet och bättre hälsa eller nattsömn för brukaren samt minskad miljöpåverkan. De värderas inte i pengar i kalkylen men kan ha ett värde även när värdet inte uttrycks i pengar. Ytterligare nyttor som kommunen redan har identifierat kan bekräftas men kan inte läggas till i denna Excelmall. |

## 4. Analysspecifika kontroller och vanliga feltolkningar

Använd relevanta kontroller när flera inmatningar behöver bedömas tillsammans eller när det finns risk för felaktig avgränsning eller dubbelräkning. Använd fältguiden för kontroller av enskilda värden och enheter. Kontrollerna ska inte genomföras som en obligatorisk extra genomgång.

| Kontrollområde | Kontrollera eller förklara |
| --- | --- |
| Analysens omfattning | Kontrollera att förändringen gäller digital nattillsyn via kamera. Om lösningen huvudsakligen bygger på sensorer eller ingår i ett bredare sensor- eller trygghetspaket behöver analysens avgränsning prövas. |
| Målgrupp och tillsynsbesök | Kontrollera att antalet brukare och antalet besök per natt avser samma målgrupp och endast besök som enbart gäller tillsyn. Kommunens beslut eller registrering kan benämna insatsen ”nattbesök” även när personlig omvårdnad, toalettbesök eller andra fysiska insatser ingår. Sådana besök ska inte räknas som ersatta tillsynsbesök. |
| Fysiska besök och transporter | Kontrollera att besökstid, restid, antal personal, andel bilresor och körsträcka avser samma fysiska tillsynsbesök som faktiskt försvinner. Restid och körsträcka ska avse ett genomsnitt per besök och inte hela nattpatrullens rutt. Om flera personer deltar i besöket ska den beräknade tidsnyttan vara förenlig med antalet personal. |
| Egen personal eller extern leverantör | Kontrollera om den digitala tillsynen utförs av kommunens personal eller en extern leverantör. Vid egen personal ska endast den tid som faktiskt används för digital nattillsyn räknas. Vid extern leverantör ska den avtalade kostnaden användas. Samma digitala tillsynsbesök ska inte räknas i båda kostnadsblocken. |
| Teknik, införande och förvaltning | Kontrollera att kamerapriset motsvarar den teknik och de tjänster som ingår i avtalet. Stäm av leverantörens åtaganden mot kommunens egen tid för förändringsledning, utbildning, information, installation, registrering, drift, support och förvaltning så att samma aktivitet eller kostnad inte räknas flera gånger. |

## 5. Analysspecifikt stöd när resultatet förklaras

Följ den gemensamma regeln för att förklara resultatet. Använd stödet nedan för att koppla resultatet till kommunens inmatningar och till dokumenterade erfarenheter av digital nattillsyn.

- Den värderade nyttan påverkas av hur många rena tillsynsbesök som faktiskt ersätts, hur mycket besöks- och restid som försvinner, hur många personer som deltar i de fysiska besöken samt resor och körsträckor. Kostnaderna påverkas av kamerakostnaden, valet mellan egen personal och extern leverantör samt den lokala ansvarsfördelningen. Använd relevanta kontroller i avsnitt 4 och den fältspecifika vägledningen för att förklara kommunens resultat.
- När resultatet huvudsakligen består av omfördelningsnytta, förklara att en stor del av värdet utgörs av frigjord arbetstid och att nyttan realiseras när tiden används på nya sätt. Påminn vid behov om att resultatet i pengar inte omfattar de kvalitets- och miljönyttor som beskrivs i avsnitt 3.