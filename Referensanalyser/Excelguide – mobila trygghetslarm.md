# Excelguide – mobila trygghetslarm

# Excelguide – mobila trygghetslarm

Syfte: Beskriva Excelmallens fältlogik, fältordning, analysspecifika kunskap och kontrollpunkter för mobila trygghetslarm.

## 1. Analysens ram

### Jämförelse

- **Alternativ A:** Brukaren har stationärt trygghetslarm och kan larma och få hjälp i den egna bostaden.
- **Alternativ B:** Brukaren har mobilt trygghetslarm och kan larma och få hjälp både i och utanför den egna bostaden.

### Avgränsning

- Analysen gäller mobila trygghetslarm som ersätter eller kompletterar stationära trygghetslarm.
- Nyttorna uppstår främst om brukare kan genomföra vissa insatser mer självständigt, särskilt promenad, ledsagning och inköp.
- Mobilt trygghetslarm tar inte i sig bort omsorgsbehov. Det ger trygghet och möjlighet att vara aktiv utanför bostaden; nyttan uppstår först om det leder till färre eller kortare fysiska insatser.
- Mallen värderar vissa direkta nyttor i pengar: frigjord tid, minskad restid, minskade drivmedelskostnader och minskade kostnader för stationära trygghetslarm.

### Vad som främst driver resultatet

- antal brukare som ska använda mobila trygghetslarm i snitt,
- andel brukare som klarar promenad, ledsagning eller inköp självständigt med mobilt trygghetslarm,
- tidsåtgång per insats,
- restid och körsträcka,
- kostnad för mobila trygghetslarm per månad och brukare,
- ersatta stationära trygghetslarm,
- tilläggstjänster, exempelvis fallarm,
- förändringsledning, utbildning, information samt drift/support.

## 2. Fältguide

Fältkartan återger alla relevanta vita och grå fält i Excelordning. Guidningen följer den gemensamma guidens regler för status, guidningsordning och hantering av grå fält.

Varje tabell ligger under namnet på den Excelflik där fälten finns. Kolumnen **Block / underblock** visar innehållsstrukturen inom fliken.

### Flik: Nyttokalkyl start

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| — | Namn på förändringen | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med `Mobila trygghetslarm`. | Om användaren beskriver annan GPS-/sensorteknik eller bredare larmkedja än mobilt trygghetslarm: kontrollera om referensmallen passar. |
| — | Vilket år vill ni räkna från? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Följ den gemensamma regeln för startår. | — |
| — | Diskonteringsränta | Grått | Förklara vid behov – ingen inmatning | Förinställd på 3 %. Förklara diskontering kort om användaren frågar. Fältet är låst och ingår inte i den ordinarie guidningen. | — |
| Lista intressenterna | <Kommun> | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Platshållaren är inte ett giltigt värde. Ersätt den med den aktuella kommunens namn. Kommunnamnet återanvänds automatiskt på andra flikar. | — |
| Lista intressenterna | Brukare; Samhället; Personal | Grått | Förklara vid behov – ingen inmatning | Förifyllda och låsta intressenter. | Om användaren behöver lägga till breda nya intressenter: kontrollera om referensmallen fortfarande passar. |

### Flik: Räkna på nyttor

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Faktorer som används i flera beräkningar | Totalt antalet brukare som ska använda mobila trygghetslarm i snitt | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal plan, uppskattning eller målgruppsbedömning. Värdet ska avse genomsnittlig användning under analysperioden. | Om införandet sker gradvis: mallen har ett värde, så använd periodgenomsnitt. Ange inte startnivå som om den gäller alla år. |
| Faktorer som används i flera beräkningar | Timkostnad för omsorgspersonal (exempelvis undersköterska) | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för timkostnader. Förifyllt värde kan normalt användas om lokalt värde saknas. | Lokala uppgifter går före Ineras förifyllda kalkylfaktor. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| Drivmedel | kalkylfaktorer för drivmedel: Bensin, Etanol E85, Diesel, HVO100, El, Fordonsgas | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för drivmedel. Förifyllda värden kan normalt användas om lokala uppgifter saknas. | Assistenten ska inte proaktivt föreslå uppdaterade drivmedelsvärden. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| 1. Frigjord tid för personal - minskad tid promenad | Antal brukare med insatsen promenad | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal uppgift om hur många brukare som har promenad som insats. | Om användaren anger alla brukare med mobilt trygghetslarm: kontrollera att alla verkligen har promenadinsats i jämförelsealternativet. |
| 1. Frigjord tid för personal - minskad tid promenad | Andel brukare som kan promenera självständigt med mobilt trygghetslarm (%) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Hjälp användaren bedöma vilka brukare som faktiskt kan promenera självständigt med larm som trygghetsstöd. | Om andelen är hög: fråga om det gäller brukare som klarar promenaden fysiskt/kognitivt och främst behöver trygghet, inte praktiskt stöd eller ledsagning. |
| 1. Frigjord tid för personal - minskad tid promenad | Antal promenader per brukare i snitt per vecka | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Mallen är förifylld med 1, en nivå som SKR Kompetenscenter har sett i arbetet med kommuner. Pröva om den passar den lokala planeringen. | Om kommunen har annan bistånds-/planeringsfrekvens: använd lokal uppgift. |
| 1. Frigjord tid för personal - minskad tid promenad | Antal promenadinsatser som inte behöver genomföras per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 1. Frigjord tid för personal - minskad tid promenad | Tid i minuter för insatsen promenad i snitt | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | SKR Kompetenscenter har i arbetet med kommuner sett 60 minuter användas för promenad. Pröva om det passar lokalt. | Kontrollera att hela promenadtiden verkligen frigörs och att personal inte fortfarande behöver följa med under hela eller delar av insatsen. |
| 1. Frigjord tid för personal - minskad tid promenad | Total frigjord tid och årlig nytta | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Timkostnad hämtas från fältet med Ineras kalkylfaktor. | Be inte användaren fylla i beräknade/hämtade fält. |
| 2. Frigjord tid för personal - minskad ledsagning | Antal brukare med insatsen ledsagning | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal uppgift om antal brukare med ledsagning som insats. | Räkna inte brukare där ledsagningen har annat syfte än trygghet/stöd vid utevistelse och därför inte påverkas av mobilt larm. |
| 2. Frigjord tid för personal - minskad ledsagning | Andel brukare som med stöd av mobilt trygghetslarm klarar sig utan ledsagning (%) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren skilja mellan brukare som kan gå/resa själva med trygghetsstöd och brukare som behöver faktisk ledsagning. | Om andelen är hög: fråga om det finns risk att trygghetslarmet ersätter socialt eller praktiskt stöd som brukaren fortfarande behöver. |
| 2. Frigjord tid för personal - minskad ledsagning | Antal ledsagningar per brukare i snitt per vecka | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | SKR Kompetenscenter har i arbetet med kommuner sett 0,5 ledsagningar per brukare och vecka användas. Jämför med den lokala planeringen. | Om lokal frekvens varierar mycket: använd försiktigt genomsnitt. |
| 2. Frigjord tid för personal - minskad ledsagning | Antal ledsagningar som inte behöver genomföras per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 2. Frigjord tid för personal - minskad ledsagning | Tid i minuter för insatsen ledsagning i snitt | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | SKR Kompetenscenter har i arbetet med kommuner sett 90 minuter användas för ledsagning. Pröva om det passar lokalt. | Kontrollera att tidsvärdet avser den del av ledsagningen som faktiskt kan försvinna, inte hela stödbehovet om personal fortfarande behövs. |
| 2. Frigjord tid för personal - minskad ledsagning | Total frigjord tid och årlig nytta | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Timkostnad hämtas från fältet med Ineras kalkylfaktor. | Be inte användaren fylla i beräknade/hämtade fält. |
| 3. Frigjord tid för personal - minskad tid inköp | Antal brukare med insatsen inköp | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal uppgift om brukare med inköpsinsats. | Räkna inte brukare där inköp redan görs digitalt, av närstående eller av annan aktör om personalens insats inte påverkas. |
| 3. Frigjord tid för personal - minskad tid inköp | Andel brukare som kan hantera inköp självständigt med mobilt trygghetslarm (%) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Hjälp användaren bedöma om larmet faktiskt gör att brukaren kan klara inköp själv. | Var extra försiktig: mobilt trygghetslarm kan öka trygghet vid utevistelse, men ersätter inte hjälp med beställning, betalning, bärande eller planering. |
| 3. Frigjord tid för personal - minskad tid inköp | Antal inköpsinsatser per brukare i snitt per vecka | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Mallen är förifylld med 1, en nivå som SKR Kompetenscenter har sett i arbetet med kommuner. Kontrollera mot lokal insatsfrekvens. | Om användaren räknar fler inköp per vecka: fråga om detta gäller biståndsbeslutade/personalförlagda inköpsinsatser. |
| 3. Frigjord tid för personal - minskad tid inköp | Antal inköpsinsatser som inte behöver genomföras per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 3. Frigjord tid för personal - minskad tid inköp | Tid i minuter för insatsen inköp i snitt | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal tid för personalens inköpsinsats. | Kontrollera att tiden verkligen försvinner genom mobilt trygghetslarm, inte bara flyttas till annan form av stöd. |
| 3. Frigjord tid för personal - minskad tid inköp | Total frigjord tid och årlig nytta | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Timkostnad hämtas från fältet med Ineras kalkylfaktor. | Be inte användaren fylla i beräknade/hämtade fält. |
| 4. Frigjord tid för personal - "ange insats" | Antal brukare med insatsen "ange insats"; Andel brukare som kan hantera "ange insats" självständigt med mobilt trygghetslarm (%); Antal "ange insats" per brukare i snitt per vecka; Tid i minuter för insatsen "ange insats" i snitt | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Använd bara blocket om kommunen redan har identifierat en tydlig annan insats där mobilt trygghetslarm kan ersätta eller minska personalstöd. Utgå från lokala uppgifter och dokumentera grunden. | Uppmuntra inte aktivt till nya stora nyttor. Om insatsen är central men inte stöds av mallen kan en analys från grunden passa bättre. |
| 4. Frigjord tid för personal - "ange insats" | Antal "ange insats" som inte behöver genomföras per år; Total frigjord tid i timmar per år; Timkostnad för omsorgspersonal (exempelvis undersköterska); Årlig nytta (kr) | Grått | Förklara vid behov – ingen inmatning | Beräknas eller hämtas av mallen. | — |
| 5. Frigjord tid - minskad restid med bil | Andel i procent av besöken (för nedan insatser) görs med bil idag | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal uppskattning för de insatser som faktiskt minskar: promenad, ledsagning, inköp och eventuell egen insats. | Om användaren använder all hemtjänstkörning: styr tillbaka till berörda insatser. |
| 5. Frigjord tid - minskad restid med bil | Antal insatser totalt som kan tas bort per år totalt; antal insatser totalt som kan tas bort per år som görs med bil | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen utifrån insatsblocken och hur stor andel av insatserna som görs med bil. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 5. Frigjord tid - minskad restid med bil | Antal minuter i snitt för resa (tur och retur) som genomförs med bil | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal restid för resor kopplade till de insatser som kan minska. | Räkna inte restid för besök som fortfarande sker. Om besöket delvis kvarstår ska restidsnyttan bedömas försiktigt. |
| 5. Frigjord tid - minskad restid med bil | Frigjord tid, timkostnad och årlig nytta | Grått | Förklara vid behov – ingen inmatning | Beräknas/hämtas i mallen. | Be inte användaren fylla i beräknade/hämtade fält. |
| 6. Minskade kostnader för drivmedel | Antal körda km i snitt per besök (tur och retur) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal kördata/ruttkunskap för berörda insatser. | Kontrollera att kilometer avser resor som faktiskt försvinner, inte all körning till brukaren. |
| 6. Minskade kostnader för drivmedel | Antal körda mil som kan undvikas per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 6. Minskade kostnader för drivmedel | Vilken typ av drivmedel använder ni? | Vitt (tomt) | Välj efter lokal situation i lista | Fältet är en rullista med drivmedel från drivmedelstabellen. Använd faktisk lokal fordonsanvändning. Om osäkert: välj försiktigt, ofta billigaste alternativet, för att inte överskatta nyttan. | Använd Ineras förifyllda kalkylfaktorer, lokalt värde eller uppdaterad kalkylfaktor från Inera i kunskapsbasen om användaren uttryckligen efterfrågar det. |
| 6. Minskade kostnader för drivmedel | Kostnad för drivmedel per mil | Grått | Förklara vid behov – ingen inmatning | Hämtas från den kalkylfaktor från Inera som valts för drivmedlet. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält. |
| 7. Frigjord tid - minskad restid med annat färdsätt än bil | Andel besök som görs med annat färdsätt än bil | Grått | Förklara vid behov – ingen inmatning | Fältet räknar utifrån andelen som inte görs med bil. Förklara vid behov sambandet med andelen som görs med bil. | Använd bara om annat färdsätt faktiskt förekommer. Specialfall ska bedömas separat. |
| 7. Frigjord tid - minskad restid med annat färdsätt än bil | Antal besök som görs med annat färdsätt än bil per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 7. Frigjord tid - minskad restid med annat färdsätt än bil | Tid i snitt per besök (tur och retur) för resa med annat färdsätt än bil (min) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal restid för gång, cykel, kollektivtrafik eller annat. | Om andra färdsätt inte är relevanta: lämna/0 enligt mallens logik. Räkna inte restid för insatser som fortfarande sker. |
| 7. Frigjord tid - minskad restid med annat färdsätt än bil | Frigjord tid, timkostnad och årlig nytta | Grått | Förklara vid behov – ingen inmatning | Beräknas/hämtas i mallen. | Be inte användaren fylla i beräknade/hämtade fält. |
| 8. Minskade kostnader för stationärt larm | Antal brukare som kommer ersätta stationärt trygghetslarm med mobilt trygghetslarm | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal uppgift om hur många stationära larm som faktiskt tas bort. | Räkna inte alla mobila larm om vissa brukare behåller stationärt larm parallellt. |
| 8. Minskade kostnader för stationärt larm | Kostnad för stationärt larm per månad och brukare | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd lokal avtals-/kostnadsuppgift. | Kontrollera vad som ingår: larm, larmmottagning, installation, service eller annan avgift. |
| 8. Minskade kostnader för stationärt larm | Minskad kostnad per år för stationära larm | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |

### Flik: Räkna på kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Faktorer som används i flera beräkningar | Totalt antalet brukare som ska använda mobila trygghetslarm i snitt | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Förklara vid behov att värdet bara ska fyllas i en gång. | Be inte användaren fylla i hämtade fält här. |
| Faktorer som används i flera beräkningar | Timkostnad för omsorgsorgspersonal | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 1. Kostnad för mobila trygghetslarm | Kostnad för mobila trygghetslarm per månad och brukare | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd lokalt avtal, offert eller upphandlingsunderlag. | Ge inget prisintervall. Kontrollera om priset gäller larm, plattform, licens, SIM/uppkoppling, larmmottagning eller support. |
| 1. Kostnad för mobila trygghetslarm | Total kostnad för mobila trygghetslarm per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 2. Införandekostnad leverantör | Införande kostnad till leverantör (engångskostnad) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd leverantörsavtal/offert. | Kontrollera att kostnaden inte redan ingår i månadskostnaden per brukare. |
| 3. Övriga kostnader till leverantör | Extra månadskostnad för tilläggstjänst, t.ex. fallarm | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd bara om kommunen köper tilläggstjänst utöver mobilt trygghetslarm. | Kontrollera att tilläggstjänsten inte redan ingår i grundpriset. |
| 3. Övriga kostnader till leverantör | Hur stor andel av brukaren har ovan tilläggstjänst | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal bedömning av vilka brukare som faktiskt behöver tilläggstjänsten. | Om andelen är hög: fråga om det verkligen gäller alla eller bara en riskgrupp. |
| 3. Övriga kostnader till leverantör | Årlig kostnad för tilläggstjänst | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 4. Förändringsledning | Tidsåtgång för arbete med förändringsledning | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren tänka på målgruppsbedömning, bistånds-/verksamhetsrutiner, larmkedja utanför bostaden, information, personalens arbetssätt och samverkan med larmmottagning. | Om värdet är lågt: fråga om förändrat ansvar vid larm utanför bostaden, rutiner för laddning/användning och kommunikation till brukare/närstående finns med. |
| 4. Förändringsledning | Timkostnad personal som arbetar med förändringsledning (kr) | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Använd lokal timkostnad eller en av Ineras kalkylfaktorer. | I Källa kan användaren kort ange om värdet är lokalt eller en av Ineras kalkylfaktorer. |
| 5. Utbildning av personal | Hur många personer ska gå utbildning? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Räkna berörd personal: hemtjänst, larmhantering, administratörer och eventuellt bistånd/planering beroende på arbetssätt. | Om bara några få räknas: fråga om all personal som ska hantera larm eller svara på frågor behöver känna till rutinerna. |
| 5. Utbildning av personal | Hur lång tid tar utbildningen (timmar)? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal utbildningsplan eller uppskattning. | SKR Kompetenscenters arbete med kommuner ger inget generellt tidsspann. Utbildningen varierar med teknik, larmkedja och arbetssätt. |
| 5. Utbildning av personal | Timkostnad omsorgspersonal | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 6. Informera och utbilda brukare | Hur många brukare ska ha mobila trygghetslarm | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält här. |
| 6. Informera och utbilda brukare | Hur lång tid tar det att informera och utbilda brukare (h)? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Hjälp användaren tänka på instruktion, laddning, hur larmet används utanför bostaden, integritet och förväntningar på vad larmet ska användas till. | Om tiden är låg: fråga om brukaren faktiskt behöver kunna hantera laddning, bära larmet och förstå när det ska användas. |
| 6. Informera och utbilda brukare | Timkostnad omsorgspersonal | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 7. Kommunens drift och support | Antal timmar med drift, support, förvaltning av plattform per år | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal bedömning av administration, användarstöd, felanmälan, kontakt med leverantör, uppföljning och hantering av borttappade/trasiga larm. | Om lågt värde: fråga om löpande support, batteri/laddning, abonnemang och larm som inte fungerar finns med. |
| 7. Kommunens drift och support | Timkostnad systemadministratör, offentlig sektor (kr) | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Följ den gemensamma regeln för timkostnader. | Lokala uppgifter går före Ineras kalkylfaktor. |

### Flik: Fler nyttor & kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Nyttor som inte värderas i pengar | Brukare blir mer självständig; Brukare blir mer trygg; Brukare blir mer aktiv; Anhörig blir mer trygg; Bättre arbetsmiljö för personal; Bättre möjlighet till kompetensförsörjning för kommunen; Frigjord tid genom senareläggning av fysisk hemtjänst; Frigjord tid genom senareläggning av flytt till SÄBO; Minskad miljöpåverkan för samhället; Brukare får förbättrat socialt liv | Grått | Förklara vid behov – ingen inmatning | Säg: ”Här ser ni andra nyttor som SKR Kompetenscenter har identifierat tillsammans med kommuner. De värderas inte i pengar i kalkylen, men de förväntas också finnas och är värdefulla i helhetsbilden.” Om en tidigare workshop gav fler nyttor kan de bekräftas, men de kan inte skrivas in på den låsta fliken. | — |
| Kostnader som inte värderats i pengar | Inga analysspecifika kostnader är förifyllda i aktuell Excelversion. | Grått | Förklara vid behov – ingen inmatning | Det finns inga förifyllda kostnader som inte värderas i pengar. Fliken är låst och innehåller inget som användaren ska fylla i eller bedöma. | — |

### Flik: Resultat nyttokalkyl

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Tabell: sammanfattning | Sammanlagd nettonytta efter 6 år (kr); Nettonytta per investerad krona efter 6 år (kr); Nyttorna överstiger kostnaderna år:; Finansiell nytta (%); Omfördelningsnytta (%); Finansiell kostnad (%); Omfördelningskostnad (%); Nyttor som inte värderats i pengar | Grått | Förklara vid behov – ingen inmatning | Följ den gemensamma regeln för att uppdatera och förklara resultatet. | Om användaren vill förstå utfallet eller om det finns en konkret indikation på fel: använd relevanta kontroller i avsnitt 4.  |

## 3. Analyskunskap och viktiga samband

Använd kunskapen i detta avsnitt när den hjälper användaren att förstå analysens avgränsning och hur nyttorna och kostnaderna hänger samman. Använd fältguiden för stöd om enskilda fält, förifyllda värden och rimlighetsnivåer.

| Tema | Kunskap att kunna förklara |
| --- | --- |
| Analysens avgränsning | Analysen jämför stationärt trygghetslarm, som fungerar i den egna bostaden, med mobilt trygghetslarm, som fungerar både i och utanför bostaden. Mallen värderar nyttor som kan uppstå när brukare med stöd av larmet kan genomföra promenad, ledsagning, inköp eller en tydligt avgränsad egen insats mer självständigt. Larmet ger trygghet men ersätter inte i sig behovet av fysisk, praktisk eller social hjälp. |
| Nyttor som värderas i pengar | De finansiella nyttorna är minskade drivmedelskostnader och minskade kostnader för stationära trygghetslarm. Omfördelningsnyttan är frigjord arbetstid genom insatser och resor som inte längre behöver genomföras av personal. |
| Kostnader | De finansiella kostnaderna omfattar mobila trygghetslarm, leverantörens införandekostnad och eventuella tilläggstjänster, exempelvis fallarm. Omfördelningskostnaderna omfattar förändringsledning, utbildning av personal, information och utbildning till brukare samt kommunens drift, support och förvaltning. |
| Nyttor som inte värderas i pengar | Mallen visar förväntade nyttor som ökad självständighet, trygghet, aktivitet och förbättrat socialt liv för brukaren, ökad trygghet för närstående, förbättrad arbetsmiljö och kompetensförsörjning, senarelagd fysisk hemtjänst eller flytt till SÄBO samt minskad miljöpåverkan. De värderas inte i pengar i kalkylen men kan ha ett värde även när värdet inte uttrycks i pengar. Ytterligare nyttor som kommunen redan har identifierat kan bekräftas men kan inte läggas till på den låsta fliken. |

## 4. Analysspecifika kontroller och vanliga feltolkningar

Använd relevanta kontroller när flera inmatningar behöver bedömas tillsammans eller när det finns risk för felaktig avgränsning eller dubbelräkning. Använd fältguiden för kontroller av enskilda värden och enheter. Kontrollerna ska inte genomföras som en obligatorisk extra genomgång.

| Kontrollområde | Kontrollera eller förklara |
| --- | --- |
| Analysens omfattning och berörda insatser | Kontrollera att nyttan gäller insatser som brukaren faktiskt kan genomföra mer självständigt med mobilt trygghetslarm. Promenad, ledsagning och inköp ska bedömas var för sig. En eventuell egen insats ska vara tydligt avgränsad och bygga på lokala uppgifter om vilket personalstöd som kan minska. |
| Målgrupp och insatsvolym | Kontrollera att det totala antalet brukare, antalet brukare med respektive insats, andelen som kan klara insatsen självständigt och insatsfrekvensen avser samma målgrupp och period. Utgå inte från att alla brukare med mobilt trygghetslarm har samtliga insatser. Samma insats ska inte räknas i flera nyttoblock. |
| Kvarvarande stöd, tid och transport | Kontrollera att endast den personal- och restid som faktiskt försvinner räknas som nytta. Ett mobilt trygghetslarm ersätter inte fysisk ledsagning eller hjälp med exempelvis planering, betalning och bärande. Restid, färdsätt och körsträcka ska endast avse de berörda insatser som inte längre behöver genomföras. |
| Mobila och stationära larm | Kontrollera att kostnaden för mobila trygghetslarm motsvarar avtalets omfattning och att tilläggstjänster inte redan ingår i grundpriset. Minskad kostnad för stationära trygghetslarm ska endast räknas för brukare där larmet faktiskt tas bort eller kommunens kostnad minskar. |
| Införande, förvaltning och larmkedja | Stäm av leverantörens åtaganden mot kommunens kostnader för förändringsledning, utbildning, information, drift och support så att samma aktivitet inte räknas flera gånger. Beakta även hur mobiltäckning, laddning, korrekt användning, larmmottagning och ansvar för utryckning utanför bostaden påverkar arbetssättet och möjligheten att realisera nyttorna. |

## 5. Analysspecifikt stöd när resultatet förklaras

Följ den gemensamma regeln för att förklara resultatet. Använd stödet nedan för att koppla resultatet till kommunens inmatningar och till dokumenterade samband för mobila trygghetslarm.

- Den värderade nyttan påverkas av hur många brukare som faktiskt kan genomföra berörda insatser mer självständigt, hur mycket personal- och restid som försvinner samt hur många stationära trygghetslarm som faktiskt ersätts. Kostnaderna påverkas bland annat av antalet mobila larm, den lokala avtalsmodellen, tilläggstjänster samt kommunens införande och förvaltning. Använd relevanta kontroller i avsnitt 4 och den fältspecifika vägledningen för att förklara kommunens resultat.
- Skilj mellan frigjord arbets- och restid, som är omfördelningsnytta, och minskade kostnader för drivmedel och stationära trygghetslarm, som är finansiella nyttor. Omfördelningsnyttan realiseras när den frigjorda tiden används på nya sätt.
- Påminn vid behov om att resultatet i pengar inte omfattar nyttorna som beskrivs som ej värderade i avsnitt 3. Senarelagd fysisk hemtjänst eller flytt till SÄBO ska inte beskrivas som en säker effekt av det mobila trygghetslarmet eller räknas in i nettonyttan.