# Excelguide – digitala lås

Syfte: Beskriva Excelmallens fältlogik, fältordning, analysspecifika kunskap och kontrollpunkter för digitala lås.

## 1. Analysens ram

### Jämförelse

- **Alternativ A:** Personal inom ordinärt boende använder analoga nycklar för att öppna brukarens bostad.
- **Alternativ B:** Personal inom ordinärt boende använder digitala nycklar för att öppna brukarens bostad.

### Avgränsning

- Analysen gäller digitala lås i äldreomsorg/hemtjänst, inte ett generellt passersystem för alla kommunala lokaler.
- Nyttorna uppstår främst genom minskad fysisk nyckelhantering, färre byten av lås/låscylindrar, mindre tid för nyckelöverlämning och mindre omväg för att hämta nyckel vid larm.
- Digitala lås tar normalt inte bort själva omsorgsbesöket. Nyttan ligger i att personalen slipper nyckelhantering, omvägar och vissa praktiska hinder.
- Resultatet drivs starkt av hur nyckelhanteringen fungerar i dag: antal nyckelöverlämningar, larm där nyckel behöver hämtas, extra körning och kostnader för borttappade nycklar/låsbyten.

### Vad som främst driver resultatet

- vald kostnadsmodell: köp, hyra eller köp som tjänst,
- pris per lås och/eller kostnad per lås och månad,
- totalt antal brukare och extralås,
- nyckelöverlämningar under arbetspass,
- larm där nyckel behöver hämtas,
- extra körsträcka för nyckelöverlämning och nyckelhämtning,
- installation: leverantör eller kommun,
- förändringsledning, utbildning, information och drift/support.

## 2. Fältguide

Fältkartan återger alla relevanta vita och grå fält i Excelordning. Guidningen följer den gemensamma guidens regler för status, guidningsordning och hantering av grå fält.

Varje tabell ligger under namnet på den Excelflik där fälten finns. Kolumnen **Block / underblock** visar innehållsstrukturen inom fliken.

### Flik: Nyttokalkyl start

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| — | Namn på förändringen | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med `Digitala lås`. | Om användaren beskriver bredare passersystem eller annan teknik än digitala lås för hemtjänstens åtkomst: kontrollera om referensmallen passar. |
| — | Vilket år vill ni räkna från? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Följ den gemensamma regeln för startår. | — |
| — | Diskonteringsränta | Grått | Förklara vid behov – ingen inmatning | Förinställd på 3 %. Förklara diskontering kort om användaren frågar. Fältet är låst och ingår inte i den ordinarie guidningen. | — |
| Lista intressenterna | <Kommun> | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Platshållaren är inte ett giltigt värde. Ersätt den med den aktuella kommunens namn. Kommunnamnet återanvänds automatiskt på andra flikar. | — |
| Lista intressenterna | Brukare; Samhället; Personal | Grått | Förklara vid behov – ingen inmatning | Förifyllda och låsta intressenter. | Om användaren behöver lägga till breda nya intressenter: kontrollera om referensmallen fortfarande passar. |

### Flik: Räkna på nyttor

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Faktorer som används i flera beräkningar | Totalt antal brukare som ska ha digitala lås | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal plan, inventering eller uppskattning av hur många brukare som ska omfattas. | Om användaren anger alla hemtjänstbrukare: fråga om alla verkligen behöver digitalt lås eller bara brukare där personal behöver åtkomst. |
| Faktorer som används i flera beräkningar | Timkostnad omvårdnadspersonal | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för timkostnader. Förifyllt värde kan användas om lokalt värde saknas. | Lokala uppgifter går före Ineras förifyllda kalkylfaktor. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| Faktorer som används i flera beräkningar | Antal extralås (t.ex till port eller tvättstuga) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Hjälp användaren tänka på lås utöver brukarens huvuddörr som krävs för att lösningen ska fungera i praktiken. | Om värdet är högt: fråga om alla extralås verkligen krävs eller om vissa entréer redan har annan åtkomstlösning. |
| Drivmedel | kalkylfaktorer för drivmedel: Bensin, Etanol E85, Diesel, HVO100, El, Fordonsgas | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för drivmedel. Förifyllda värden kan normalt användas om lokala uppgifter saknas. | Assistenten ska inte proaktivt föreslå uppdaterade drivmedelsvärden. Om användaren frågar efter nyare värden kan assistenten slå upp uppdaterade kalkylfaktorer från Inera i kunskapsbasen om sådana finns. |
| 1. Minskad kostnad för ersättning av lås | Antal lås som behöver bytas ut per månad (vid användning av fysiska lås, t.ex vid borttappade nycklar) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal statistik eller uppskattning från nyckelhantering, fastighet, hemtjänst eller incidentrapportering. | Räkna bara lås/låscylindrar som digitala lås rimligen minskar behovet av att ersätta. Räkna inte all normal låsservice. |
| 1. Minskad kostnad för ersättning av lås | Kostnad för nytt lås | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd lokal kostnad från avtal, fastighet, låssmed, bostadsbolag eller intern debitering. | Ge inget riktvärde. Om kostnaden avser större åtgärd än lås/låscylinder, be användaren kontrollera vad som ingår. |
| 1. Minskad kostnad för ersättning av lås | Total kostnad för utbyta av lås per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 2. Frigjord tid p.g.a minskad tid för överlämning av fysiska nycklar under arbetspass | Antal överlämningar av fysiska nycklar mellan personal per dag under pågående arbetspass | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren kartlägga hur nycklar lämnas över i nuläget: mellan personal, grupper, turer eller geografiska områden. | Om kommunen redan har nyckelfria rutiner eller fasta nycklar per personalgrupp kan värdet vara lågt. Räkna bara överlämningar som faktiskt försvinner med digitala lås. |
| 2. Frigjord tid p.g.a minskad tid för överlämning av fysiska nycklar under arbetspass | Total tidsåtgång vid överlämnande för en person i minuter inklusive restid | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om faktisk genomsnittstid per överlämning för en person, inklusive eventuell omväg/restid. Mallen räknar upp tidsåtgången för båda parter i överlämningen. | Om värdet avser hela mötet för flera personer eller hela arbetsrutten: be användaren bryta ned till rätt enhet. |
| 2. Frigjord tid p.g.a minskad tid för överlämning av fysiska nycklar under arbetspass | Total tidsåtgång per dag och per år för överlämning av nycklar | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 2. Frigjord tid p.g.a minskad tid för överlämning av fysiska nycklar under arbetspass | Timkostnad omvårdnadspersonal | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 3. Frigjord tid vid larm hos brukare | Antal larm som kräver fysiskt besök hos brukare per dag | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal larmstatistik. Räkna bara larm där personal faktiskt behöver åka till brukaren. | Räkna inte larm som hanteras per telefon eller på distans. |
| 3. Frigjord tid vid larm hos brukare | Snittid för att hämta nyckel per larm i minuter | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren uppskatta den extra tid som uppstår för att hämta fysisk nyckel innan personal kan åka till brukaren. | Om personal redan har nyckel med sig eller kan gå direkt till brukaren ska värdet vara lågt eller 0. Räkna inte hela larmbesöket, bara nyckelhämtningsdelen. |
| 3. Frigjord tid vid larm hos brukare | Totalt frigjord tid per dag och per år pga att personal inte måste hämta nyckel vid larm | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 3. Frigjord tid vid larm hos brukare | Timkostnad omvårdnadspersonal | Grått | Förklara vid behov – ingen inmatning | Hämtas från timkostnadsfältet. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 4. Minskad drivmedelskostnader p.g.a av minskade överlämningar av nycklar | Antal överlämningar av fysiska nycklar mellan personal per dag under pågående arbetspass | Grått | Förklara vid behov – ingen inmatning | Hämtas från tidigare fält. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält här. |
| 4. Minskad drivmedelskostnader p.g.a av minskade överlämningar av nycklar | Andel överlämningar som sker med bil per dag | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Fråga hur stor andel av nyckelöverlämningarna som innebär extra bilkörning. | Om överlämning sker på samma plats där personal ändå befinner sig ska andelen som görs med bil eller den extra körningen inte överdrivas. |
| 4. Minskad drivmedelskostnader p.g.a av minskade överlämningar av nycklar | Antal extra körda km totalt per dag p.g.a av överlämning av nyckel en person | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om genomsnittlig extra körsträcka som orsakas av nyckelöverlämning för en person. Mallen räknar upp körningen för båda parter. | Räkna bara extra kilometer som försvinner med digitala lås, inte hela körsträckan under arbetspasset. |
| 4. Minskad drivmedelskostnader p.g.a av minskade överlämningar av nycklar | Antal körda mil som kan undvikas per år | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 4. Minskad drivmedelskostnader p.g.a av minskade överlämningar av nycklar | Vilken typ av drivmedel använder ni | Vitt (tomt) | Välj efter lokal situation i lista | Fältet är en rullista med drivmedel från drivmedelstabellen. Använd faktisk lokal fordonsanvändning. Om osäkert: välj försiktigt, ofta billigaste alternativet, för att inte överskatta nyttan. | Använd Ineras förifyllda kalkylfaktorer, lokalt värde eller uppdaterad kalkylfaktor från Inera i kunskapsbasen om användaren uttryckligen efterfrågar det. |
| 4. Minskad drivmedelskostnader p.g.a av minskade överlämningar av nycklar | Kostnad för drivmedel per mil | Grått | Förklara vid behov – ingen inmatning | Hämtas från den kalkylfaktor från Inera som valts för drivmedlet. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält. |
| 5. Minskad drivmedelskostnad p.g.a minskade hämtningar av nycklar vid larm | Antal larm som kräver fysiskt besök hos brukare per dag | Grått | Förklara vid behov – ingen inmatning | Hämtas från tidigare fält. Förklara bara vid behov. | Be inte användaren fylla i hämtade fält här. |
| 5. Minskad drivmedelskostnad p.g.a minskade hämtningar av nycklar vid larm | Andel larm som åtgärdas med bil | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren avgränsa till larm där personal behöver fysisk utryckning med bil och där extra körning för nyckelhämtning faktiskt försvinner. | Kontrollera att samma larm inte räknas flera gånger. |
| 5. Minskad drivmedelskostnad p.g.a minskade hämtningar av nycklar vid larm | Antal extra körda km för att hämta nyckel vid larm per dag | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal uppskattning av extra omväg för att hämta nyckel före larmbesök. | Räkna inte hela resan till brukaren om den fortfarande behöver göras. Räkna bara omvägen/extra sträckan som digitala lås tar bort. |
| 5. Minskad drivmedelskostnad p.g.a minskade hämtningar av nycklar vid larm | Antal körda mil som kan undvikas per år; typ av drivmedel; kostnad för drivmedel per mil | Grått | Förklara vid behov – ingen inmatning | Hämtas eller beräknas i mallen. Följ gemensam regel för drivmedel. | Be inte användaren fylla i hämtade/beräknade fält. |

### Flik: Räkna på kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Faktorer som används i flera beräkningar | Totalt antal brukare som ska ha digitala lås | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Förklara vid behov att värdet bara ska fyllas i en gång. | Be inte användaren fylla i grå/hämtade fält. |
| Faktorer som används i flera beräkningar | Timkostnad omvårdnadspersonal | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| Faktorer som används i flera beräkningar | Antal extralås (t.ex till port eller tvättstuga) | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Förklara vid behov att extralås bara ska fyllas i en gång. | Be inte användaren fylla i hämtade fält här. |
| 1. Investering (engångskostnad) vid köp av digitala lås | Pris per lås | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd lokalt avtal, offert eller upphandlingsunderlag. | Om kommunen köper lås som tjänst eller hyr: kontrollera om inköpspris ska vara 0 och om kostnaden i stället ska ligga i blocket Kostnad per lås. |
| 1. Investering (engångskostnad) vid köp av digitala lås | Total kostnad för alla lås | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 1. Investering (engångskostnad) vid köp av digitala lås | Övriga kostnader som exempelvis nyckelgömmor (om ej aktuell ange noll) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd bara om sådana kostnader faktiskt tillkommer och inte ingår i priset per lås eller leverantörsavtalet. | Om kostnaden redan ingår i leverantörens helhetspris ska den inte läggas här. |
| 2. Kostnad per lås (drift & support eller vid köp av tjänst) | Kostnad per lås och månad | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd vid drift/support per lås eller köp som tjänst. Be om avtal/offert. | Undvik dubbelräkning mot engångsinvestering om månadskostnaden redan inkluderar lås/hårdvara. Kontrollera vad som ingår. |
| 2. Kostnad per lås (drift & support eller vid köp av tjänst) | Månatlig kostnad för digitala lås gällande drift/support eller vid köp som tjänst | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 3. Införandekostnad leverantör | Kostnad för införande till levertantör (engångskostnad) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd leverantörsavtal/offert. | Kontrollera om kostnaden redan ingår i pris per lås, tjänstekostnad eller separat införandeavtal. |
| 3. Införandekostnad leverantör | Kostnad för att leverantören installerar ett digitalt lås | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd om leverantören installerar låsen. | Om kommunen installerar själv: använd kommunens installationsblock i stället och undvik dubbelräkning. |
| 3. Införandekostnad leverantör | Kostnad för installation av digitala lås av leverantören | Grått | Förklara vid behov – ingen inmatning | Beräknas i mallen. Förklara bara vid behov. | Be inte användaren fylla i beräknade fält. |
| 4. Eventuella övriga kostnader till leverantör | Ange eventuellt övriga kostnad till leverantör per år | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd bara för återkommande leverantörskostnader som inte fångas i andra block. | Om kostnaden är en licens/drift/support per lås ska den normalt ligga i kostnad-per-lås-blocket. |
| 5. Förändringsledning | Tidsåtgång för arbete med förändringsledning (timmar) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren tänka på rutiner, behörigheter, informationsarbete, samverkan med fastighetsägare/hyresvärdar, larmrutiner, installation och förändrat arbetssätt. | Om värdet är mycket lågt: fråga om behörighetsadministration, rutinförändring, utbildning, larmflöden och samordning med fastighetsägare finns med. |
| 5. Förändringsledning | Timkostnad personal som arbetar med förändringsledning (kr) | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Använd lokal timkostnad eller en av Ineras kalkylfaktorer. | I Källa kan användaren kort ange om värdet är lokalt eller en av Ineras kalkylfaktorer. |
| 6. Utbildning av personal | Hur många omvårdnadspersonal ska gå utbildning för att kunna använda digitala lås? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Räkna berörd personal som behöver kunna använda låsen i vardagen. | Om bara ett fåtal räknas: fråga om all berörd personal verkligen kan använda låsen säkert. |
| 6. Utbildning av personal | Hur lång tid tar utbildningen (timmar)? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal utbildningsplan eller uppskattning. SKR Kompetenscenters arbete med kommuner ger inget generellt tidsspann för utbildningen. | Om tiden är mycket låg: fråga om både teknik, rutiner, behörighet och avvikelse-/larmrutiner täcks. |
| 6. Utbildning av personal | Timkostnad omvårdnadspersonal | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 6. Utbildning av personal | Hur många personal ska gå utbildning för att kunna installera digitala lås? (Om leverantören installerar så ange noll) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd bara om kommunen installerar låsen själv. | Om leverantören installerar ska detta normalt vara 0. |
| 6. Utbildning av personal | Hur lång tid tar utbildningen (timmar)? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal utbildningsplan för installationspersonal. | Om installation görs av leverantör ska detta normalt vara 0. |
| 6. Utbildning av personal | Timkostnad installationspersonal | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Använd lokal timkostnad eller en relevant kalkylfaktor från Inera om lokal uppgift saknas. | I Källa kan användaren kort ange om värdet är lokalt eller en av Ineras kalkylfaktorer. |
| 7. Informera brukare och hyresvärdar | Hur lång tid tar det att informera brukare i snitt (h) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be användaren tänka på information, samtycke/förankring, praktiska frågor och trygghet. | Om värdet är 0: fråga om brukare inte behöver informeras alls. |
| 7. Informera brukare och hyresvärdar | Timkostnad omvårdnadspersonal | Grått | Förklara vid behov – ingen inmatning | Hämtas från Räkna på nyttor. Följ den gemensamma regeln för timkostnader. | Be inte användaren fylla i hämtade fält här. |
| 7. Informera brukare och hyresvärdar | Kostnad för att informera hyresvärdar (totalt) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd om kommunen behöver samordna med fastighetsägare, bostadsbolag eller hyresvärdar. | Om kommunen äger bostäderna eller redan har etablerad process kan kostnaden vara låg, men den bör inte glömmas om många fastighetsägare berörs. |
| 8. Kommunens drift och support | Antal timmar med drift, support, förvaltning av digitala lås per år | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Be om lokal bedömning av total årlig tid för behörighetsadministration, användarstöd, felanmälan, batteribyten/underhåll och leverantörskontakt. Mallen frågar inte efter antal administratörer; summera i stället den totala tidsåtgången för alla berörda. | Om värdet är mycket lågt: fråga om löpande behörighetsändringar, personalomsättning, supportflöden och driftstörningar finns med. |
| 8. Kommunens drift och support | Timkostnad systemadministratör, offentlig sektor (kr) | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Följ den gemensamma regeln för timkostnader. | Lokala uppgifter går före Ineras kalkylfaktor. |
| 9. Installation av lås (kommun) | Tid för kommunens personal att istallera ett digitalt lås | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd om kommunen installerar själv. | Om leverantören installerar ska detta normalt vara 0 eller lämnas enligt mallens arbetssätt. |
| 9. Installation av lås (kommun) | Timkostnad för installationspersonal | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Använd lokal timkostnad eller en relevant kalkylfaktor från Inera om lokal uppgift saknas. | I Källa kan användaren kort ange om värdet är lokalt eller en av Ineras kalkylfaktorer. |

### Flik: Fler nyttor & kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Nyttor som inte värderas i pengar | Ökad trygghet för brukare; Ökad säkerhet för brukare; Minskad kostnad för brukare; Förbättrad arbetsmiljö; Förbättrad schemaplanering; Ökad möjlighet till samarbete mellan olika arbetsgrupper; Ökad krisberedskap; Minskad miljöpåverkan | Grått | Förklara vid behov – ingen inmatning | Säg: ”Här ser ni andra nyttor som SKR Kompetenscenter har identifierat tillsammans med kommuner. De värderas inte i pengar i kalkylen, men de förväntas också finnas och är värdefulla i helhetsbilden.” Om en tidigare workshop gav fler nyttor kan de bekräftas, men de kan inte skrivas in på den låsta fliken. | — |
| Kostnader som inte värderats i pengar | Inga analysspecifika kostnader är förifyllda i aktuell Excelversion. | Grått | Förklara vid behov – ingen inmatning | Det finns inga förifyllda kostnader som inte värderas i pengar. Fliken är låst och innehåller inget som användaren ska fylla i eller bedöma. | — |

### Flik: Resultat nyttokalkyl

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Tabell: sammanfattning | Sammanlagd nettonytta efter 6 år (kr); Nettonytta per investerad krona efter 6 år (kr); Nyttorna överstiger kostnaderna år:; Finansiell nytta (%); Omfördelningsnytta (%); Finansiell kostnad (%); Omfördelningskostnad (%); Nyttor som inte värderats i pengar | Grått | Förklara vid behov – ingen inmatning | Följ den gemensamma regeln för att uppdatera och förklara resultatet. | Om användaren vill förstå utfallet eller om det finns en konkret indikation på fel: använd kontrollordningen i avsnitt 4. |

## 3. Analyskunskap och viktiga samband

Använd kunskapen i detta avsnitt när den hjälper användaren att förstå analysens avgränsning, vilka uppgifter och lokala förutsättningar som påverkar resultatet och varför kommunen behöver göra en egen lokal värdering.

| Tema | Kunskap att kunna förklara |
| --- | --- |
| Analysens avgränsning | Analysen gäller digitala lås för personalens åtkomst till bostäder inom äldreomsorg och hemtjänst. Den gäller inte generella passersystem för kommunala lokaler. Digitala lås tar normalt inte bort omsorgsbesöket; nyttan uppstår genom minskad fysisk nyckelhantering. |
| Nyttor som värderas i pengar | De huvudsakliga nyttorna är frigjord tid och minskad körning vid nyckelöverlämning och nyckelhämtning, minskade drivmedelskostnader samt minskat behov av att ersätta borttappade nycklar och låscylindrar. |
| Kostnader | Kostnader kan uppstå för lås, införande och leverantör, förändringsledning, utbildning, information, installation, drift och support. Vad som ska tas med beror på kommunens avtal och arbetssätt. |
| Lokala uppgifter och antaganden | Resultatet påverkas framför allt av antal brukare och extralås, hur nyckelhanteringen fungerar i nuläget, antal nyckelöverlämningar och relevanta larm, extra tid och körsträcka samt kostnader för lås, införande, drift och support. Lokala uppgifter ska användas där sådana finns. |
| Referensanalysens status | Referensanalysen innehåller ingen värdering i pengar. Kommunen ska därför göra en egen lokal värdering i Excelmallen. Referensanalysen ger inget normalt nettonyttespann för digitala lås. |
| Nyttor som inte värderas i pengar | Mallen visar vissa förväntade kvalitetsnyttor i låsta fält, exempelvis trygghet, säkerhet, arbetsmiljö, schemaplanering, samarbete och krisberedskap. De värderas inte i pengar i kalkylen men är trots det värdefulla. Ytterligare nyttor som kommunen redan har identifierat, exempelvis i en workshop, kan bekräftas men kan inte läggas till i denna Excelmall. |

## 4. Analysspecifika kontroller och vanliga feltolkningar

Använd relevanta kontroller när en uppgift behöver prövas, när användaren vill förstå resultatet eller när det finns en konkret risk för felaktig avgränsning eller dubbelräkning. Kontrollerna ska inte genomföras som en obligatorisk extra genomgång.

| Kontrollområde | Kontrollera eller förklara |
| --- | --- |
| Analysens omfattning | Kontrollera att förändringen gäller digitala lås för hemtjänstens eller äldreomsorgens åtkomst till bostäder. Om förändringen gäller ett bredare passersystem kan en annan analys behövas. |
| Brukare och extralås | Räkna bara brukare där personal behöver åtkomst till bostaden. Håll antal brukare och antal extralås åtskilda. Fråga om port, tvättstuga eller andra utrymmen kräver ytterligare lås. |
| Nyckelöverlämningar | Använd lokal kartläggning eller uppskattning. Räkna bara överlämningar som faktiskt försvinner med digitala lås. Digitala lås ska inte räknas som att själva omsorgsbesöken försvinner. |
| Larm | Räkna bara larm som kräver fysiskt besök. Tids- och környttan ska endast avse larm där personalen slipper hämta en fysisk nyckel. Om ingen extra nyckelhämtning krävs ska tiden och körsträckan för nyckelhämtning vara 0. Samma larm ska inte räknas flera gånger. |
| Tid och körsträcka | Räkna endast den extra tid och körsträcka som orsakas av nyckelhanteringen, inte hela larmbesöket, resan till brukaren eller arbetsrutten. Kontrollera att värdet avser rätt person och enhet enligt fältguiden. |
| Köp, tjänst eller hyra | Använd kommunens avtal eller offert för att avgöra om kostnaden ska ligga som engångsinvestering, kostnad per lås och månad eller båda. Kontrollera vad som ingår så att samma lås eller hårdvara inte räknas både som köp och som full tjänstekostnad. |
| Installation | Utgå från vem som faktiskt installerar låsen. Räkna inte både leverantörens och kommunens installation för samma lås. |
| Införande, drift och support | Kontrollera att relevanta kostnader och arbetsinsatser för leverantör, förändringsledning, utbildning, information till brukare och hyresvärdar, behörighetsadministration, drift, support och underhåll finns med. |
| Parallella system | Om vissa brukare eller fastigheter fortfarande kräver analoga nycklar behöver den kvarvarande nyckelhanteringen och administrationen vägas in i bedömningen av nyttan. |

## 5. Analysspecifikt stöd när resultatet förklaras

Följ den gemensamma regeln för att förklara resultatet. Använd stödet nedan för att koppla resultatet till kommunens inmatningar och förutsättningarna för digitala lås.

- Ange inte att ett visst nettonyttespann är normalt eller beskriv nivån som hög, låg, stark, svag eller ovanlig. Referensanalysen innehåller ingen värdering i pengar och ger inget stöd för sådana bedömningar.
- Om användaren vill förstå ett oväntat resultat, använd relevanta kontroller i avsnitt 4 utan att utgå från att inmatningen är fel.
- För nyttovärderingen kan relevanta samband och kontroller gälla antal brukare och extralås, nyckelöverlämningar, relevanta larm samt den extra tid och körsträcka som faktiskt försvinner.
- För kostnadsvärderingen kan relevanta samband och kontroller gälla vald avtalsmodell, vad som ingår i priset samt kostnader för införande, installation, drift och support. Kontrollera också om samma kostnad kan ha räknats flera gånger.
- Om nettonyttan är negativ, eller om användaren själv uppfattar den som svag, kan möjliga förklaringar vara begränsad eller redan effektiv nyckelhantering, få relevanta larm, liten extra körning eller höga lokala kostnader. Pröva förklaringarna mot kommunens faktiska inmatningar och beskriv hur nyttorna och kostnaderna tillsammans ger resultatet.
- Påminn vid behov om att siffrorna inte omfattar hela bilden. De kvalitetsnyttor som visas i mallen och eventuella ytterligare nyttor eller kostnader som kommunen redan har identifierat hör också till helhetsbilden, men kan inte läggas till i denna Excelmall.
