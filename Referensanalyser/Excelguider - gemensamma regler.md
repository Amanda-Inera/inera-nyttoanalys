# Excelguider - gemensamma regler

Syfte: gemensamma regler för återanvändbar, fältnära vägledning i referensanalysernas Excelmallar.

## 1. Dokumentets roll

Den gemensamma guiden beskriver sådan mall- och metodkunskap som gäller för samtliga referensanalysernas Excelmallar:

- hur fältens synliga sökvägar och statusar ska förstås
- vilka typer av underlag som kan användas för olika fält
- hur lokala uppgifter, uppskattningar, erfarenheter från andra kommuner och Ineras kalkylfaktorer förhåller sig till varandra
- hur källor, enheter, tidsperioder och osäkerhet hanteras
- hur återkommande Excelblock och resultatfält fungerar
- hur nettonytta per investerad krona ska förstås.

Den analysspecifika Excelguiden är master för:

- analysens jämförelse och avgränsning
- den exakta fältkartan
- status och guidningsordning för varje fält
- analysspecifika värden, erfarenheter och bedömningsstöd
- analysspecifika samband och kontrolltriggers
- förifyllt analysspecifikt innehåll.

## 2. Grundprinciper för underlaget

Lokala uppgifter, priser och leverantörskostnader ska komma från användaren eller från ett angivet underlag. Generella ersättningsvärden används bara när den gemensamma eller analysspecifika guiden uttryckligen anger att ett sådant värde finns.

Grå fält är låsta delar av Excelmallen. De ska inte ersättas med egna beräkningar eller behandlas som inmatningsfält.

Guiden innehåller fält-, mall- och metodkunskap. 

## 3. Öppna arbetsboken

Excelmallen laddas ner från appen och öppnas lokalt i Excel på PC. Referensmallarna fungerar inte på Mac.

När mallen öppnas kan användaren behöva klicka på **Aktivera redigering** och **Aktivera innehåll**. Det kan också visas säkerhetsmeddelanden som behöver godkännas. Sådana meddelanden innebär inte i sig att något är fel med mallen.

Användaren fyller själv i och sparar Excelmallen. Assistenten kan ge stöd om fältens innebörd, vilka lokala uppgifter som behövs och vilka kontroller som är relevanta.

## 4. Fältguidens struktur

Den analysspecifika guiden har en fältguide med följande struktur:

`Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger`

Fältkartan återger alla relevanta vita och grå fält i samma ordning som de förekommer i Excelmallen. Den gemensamma ordningen gör att assistenten kan förstå var ett grått fält ligger mellan två vita fält och hur inmatning, hämtning och beräkning hänger ihop. Grå fält har status **Grått** och guidningsordningen **Förklara vid behov – ingen inmatning** i fältkartan.

Dokumentordningen och dialogordningen är inte samma sak:

- **Dokumentordning:** Assistenten läser hela fältkartan i Excelordning.
- **Dialogordning:** Assistenten guidar bara i vita fält. Grå fält noteras och hoppas över, om de inte behöver förklaras.

### 4.1 Flik, block och fält

- Varje fältguide ligger under en rubrik med **Flik** som anger vilken Excelflik fälten återfinns i.
- **Block** återger den synliga sökvägen i Excel: `blockrubrik / underblock` när alla nivåer finns.
- Flik-, block-, underblock- och fältnamn återger det som användaren ser i Excel och ska inte ersättas med sammanfattande benämningar.

### 4.2 Status

Status beskriver vilken typ av fält cellen är.

| Status | Innebörd |
| --- | --- |
| **Vitt (tomt)** | Ett redigerbart fält utan ett giltigt förifyllt värde. En platshållare, exempelvis `<Kommunens namn>`, behandlas som tom eftersom den måste ersättas med en lokal uppgift. |
| **Vitt (förifyllt)** | Ett redigerbart fält med ett verkligt synligt värde eller innehåll som kan behållas eller ändras. |
| **Grått** | Ett låst fält som användaren inte kan uppdatera. Det kan vara hämtat, beräknat eller informativt. |

### 4.3 Guidningsordning

Fältets status visar om det är tomt, förifyllt eller låst. Guidningsordningen anger hur assistenten ska hantera fältet.

#### 4.3.1 Vitt (tomt)

| Guidningsordning | Assistentens handling |
| --- | --- |
| **Ta fram lokalt – uppskatta försiktigt vid behov** | Börja med lokala uppgifter. Hjälp användaren att göra en försiktig uppskattning om säkrare underlag saknas. |
| **Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov** | Börja med lokala uppgifter. Om underlag saknas kan assistenten berätta vad SKR Kompetenscenter har sett i arbetet med andra kommuner och hjälpa användaren pröva om det passar lokalt. |
| **Ta fram lokalt – annars använd en av Ineras kalkylfaktorer** | Börja med lokala uppgifter. Om sådant underlag saknas kan användaren använda den av Ineras kalkylfaktorer för timkostnad eller drivmedel som anges för fältet. |
| **Ta fram lokalt – inget ersättningsvärde** | Be om den lokala uppgiften. Om den inte är tillgänglig, markera att den återstår och fortsätt guidningen. Hitta inte på eller erbjud något generellt ersättningsvärde. |
| **Välj efter lokal situation i lista** | Hjälp användaren att välja det alternativ som bäst motsvarar den lokala situationen från en lista med flera val. |

Vilken typ av underlag som är relevant anges i den analysspecifika guiden eller från kontexten. Det kan exempelvis vara lokal statistik, mätning, forskning, avtal, offert eller verksamhetens uppskattning.

#### 4.3.2 Vitt (förifyllt)

| Guidningsordning | Assistentens handling |
| --- | --- |
| **Pröva lokalt – annars behåll förifyllt** | Lyft fältet aktivt och hjälp användaren att bedöma om det förifyllda innehållet passar den lokala situationen. Behåll det om det saknas skäl eller underlag för att ändra det. |
| **Behåll normalt – ändra vid behov** | Utgå från det förifyllda innehållet utan att aktivt pröva det med användaren. Ändra det om användaren tar upp frågan eller om det framkommer ett tydligt skäl. |

Skillnaden mellan ordningarna är alltså om det förifyllda innehållet ska **prövas aktivt** eller **normalt behållas**.

#### 4.3.3 Grått (låst)

Grå fält finns med i fältkartan på sin rätta plats i Excelordningen, så att assistenten känner till dem. De utgör däremot inte steg i den normala guidningen.

| Guidningsordning | Assistentens handling |
| --- | --- |
| **Förklara vid behov – ingen inmatning** | Hoppa normalt över fältet i dialogen. Förklara vad det innehåller, visar eller beräknar om användaren frågar eller om det behövs för att förstå mallen eller resultatet. Be aldrig användaren fylla i, ändra eller bedöma fältet. |

## 5. Fältkartans användning

Fältkartan är ordnad på samma sätt som Excelmallen. Den kan användas både för en fullständig genomgång och för stöd om ett enskilt fält.

Vita fält är inmatningsfält. Fältets status och guidningsordning visar om en lokal uppgift behöver tas fram, om en försiktig uppskattning kan användas eller om ett förifyllt värde normalt kan behållas.

Grå fält är låsta, beräknade eller informativa. De ingår inte som inmatningsfält men kan behöva förklaras för att användaren ska förstå mallen eller resultatet.

Hur genomgången presenteras, hur många fält som behandlas åt gången och när flödet går vidare styrs i referensflödets beteendelager.

## 6. Hantering av uppgifter

### 6.1 Vad ett värde kan bygga på

| Begrepp | Innebörd |
| --- | --- |
| **Lokala uppgifter** | Uppgifter som är relevanta för den lokala situationen. De kan exempelvis bygga på statistik, mätningar, verksamhetskunskap, forskning, avtal, offerter eller gemensamma uppskattningar. |
| **Erfarenheter från andra kommuner** | SKR Kompetenscenter har genom arbetet med kommuner sett hur andra har bedömt vissa fält. Sådana exempel eller spann kan hjälpa användaren att pröva en lokal nivå när det egna underlaget är osäkert. De är inte nationell statistik, rekommenderade nivåer eller facit. |
| **Ineras kalkylfaktorer** | Inera tillhandahåller några vanliga kalkylfaktorer för timkostnader och drivmedel. De kan användas när en relevant lokal uppgift saknas och fältets guidningsordning tillåter det. Värdet kan vara förifyllt i Excel eller hämtas från kunskapsbasen. |

### 6.2 Källa eller motivering

För varje vitt fält finns ett tillhörande fält med rubriken **Källa**. Där dokumenteras kort var uppgiften kommer ifrån eller vad en uppskattning bygger på.

Exempel:

- `Uppskattning från verksamheten`
- `Ineras kalkylfaktor för undersköterska`
- `Erfarenheter från andra kommuners analyser, SKR Kompetenscenter`
- `Kommunens avtal med leverantören`
- `Statistik från verksamhetssystemet`.

För grå fält ska användaren inte fylla i någon källa.

### 6.3 Ett värde för flera år

Om mallen bara har ett inmatningsfält för ett antagande som förändras över tid ska ett rimligt och försiktigt genomsnitt för hela analysperioden användas. En möjlig nivå mot slutet av perioden ska inte automatiskt användas som genomsnitt för samtliga år.

Genomsnittet kan bedömas genom att jämföra en rimlig nivå i början av perioden med en rimlig nivå mot slutet.

### 6.4 Ineras kalkylfaktorer för timkostnader och drivmedel

Inera tillhandahåller ett begränsat antal kalkylfaktorer för timkostnader och drivmedel. En kalkylfaktor kan vara förifylld i Excelmallen eller hämtas från kunskapsbasen när fältets guidningsordning tillåter det.

En uppdaterad kalkylfaktor är relevant när användaren vill:

- kontrollera om ett förifyllt värde fortfarande är aktuellt
- uppdatera en förifylld timkostnad eller drivmedelskostnad
- jämföra ett lokalt eller förifyllt värde med Ineras aktuella kalkylfaktor.

Lokala uppgifter går före Ineras kalkylfaktorer när de lokala uppgifterna är relevanta och tillräckligt tillförlitliga.

## 7. Gemensamma specialfall

### 7.1 Startår

För fältet **Vilket år vill ni räkna från?** används i första hand det verkliga lokala startåret.

Om startåret är okänt eller inte behöver motsvara ett kalenderår kan det förifyllda värdet `1` behållas. Föregående, innevarande eller något annat kalenderår ska inte antas utan underlag.

### 7.2 Timkostnader

Det finns både tomma och förifyllda timkostnadsfält. Den analysspecifika guiden anger status och guidningsordning för varje fält.

När en lokal timkostnad ska tas fram används månadslönen i kommunen för den yrkesgrupp som fältet gäller:

**(månadslön / 142 arbetstimmar per månad) × 1,54**

### 7.3 Drivmedel

Drivmedel förekommer både i en tabell med kalkylfaktorer och som ett val i nyttoberäkningen. Den analysspecifika guiden anger fältens status och guidningsordning.

Valet i nyttoberäkningen ska motsvara den lokala fordonsanvändningen. Om flera drivmedel används väljs ett försiktigt representativt antagande som inte överskattar nyttan. Grunden för valet dokumenteras i **Källa**.

### 7.4 Transporter

Transportuppgifter ska bygga på faktisk lokal användning, inte på idealfall eller enstaka exempel.

- **Andel som görs med bil:** andelen ska avse de berörda besök eller insatser som faktiskt genomförs med bil.
- **Körsträcka:** använd ett relevant genomsnitt och skilj den resa som påverkas från hela arbetsrutten.
- **Snitthastighet:** använd faktisk genomsnittlig körning, inte hastighetsgränsen.
- **Restid:** använd den resa och period som fältet efterfrågar.
- **Andra färdsätt:** ta bara med dem när de faktiskt är relevanta.

Bedömningen gäller normalt kommunen eller verksamheten som helhet, om analysen inte uttryckligen gäller en avgränsad grupp.

### 7.5 Leverantörspriser och avtal

Kostnader för produkt, tjänst, licens, abonnemang, införande, installation, drift och support ska i första hand bygga på offert, avtal, upphandlat pris, lokalt budgetunderlag eller annan faktisk lokal kostnadsuppgift.

Ett pris kontrolleras genom att undersöka:

- vad som ingår
- vilken enhet och period priset gäller
- om engångskostnader tillkommer
- om priset gäller köp, hyra, abonnemang eller tjänst
- om hårdvara, licens, plattform, drift, support, installation eller tillägg ingår.

Om priset behöver uppskattas ska det framgå i **Källa** vad uppskattningen bygger på. Guiden ger inte generella riktvärden för lokala leverantörspriser.

## 8. Gemensamma grå fält utanför den ordinarie inmatningen

### 8.1 Osäkerhetsvariationer och lägst/högst

Vissa värden har inbyggda osäkerhetsvariationer i grå fält till höger om de vita inmatningsfälten. De grå fälten är låsta och ingår inte i den ordinarie inmatningen.

Variationerna bygger på vad SKR Kompetenscenter välfärdsteknik har sett i arbetet med kommuner. Användaren fyller normalt i det troliga lokala värdet i det vita fältet. Viktiga osäkerheter i den egna uppgiften kan dokumenteras i **Källa**.

Om de inbyggda variationerna behöver ändras krävs en anpassad mall eller en analys från grunden.

### 8.2 Årsvisa faktorrader

Årsvisa faktorrader styr hur nyttor och kostnader fördelas över analysperioden. De är förifyllda av SKR Kompetenscenter välfärdsteknik och ingår inte i den ordinarie inmatningen.

En faktor på `1` betyder att 100 procent av nyttan eller kostnaden förväntas det aktuella året.

### 8.3 Fliken Fler nyttor & kostnader

Fliken **Fler nyttor & kostnader** är låst och fungerar som ett informationssteg. Den visar andra nyttor och kostnader som SKR Kompetenscenter har identifierat tillsammans med kommuner men som inte värderas i pengar i kalkylen.

Användaren kan inte ändra, godkänna eller komplettera innehållet på fliken. Lokala nyttor och kostnader som har identifierats exempelvis i en workshop kan ingå i helhetsbilden, men de kan inte skrivas in på den låsta fliken.

## 9. Fliken Resultat nyttokalkyl

När användaren har arbetat igenom alla vita fält ska assistenten markera övergången:

> Nu har vi fyllt i alla uppgifter och är redo att titta på resultatet. Det är dags att gå till fliken Resultat nyttokalkyl och uppdatera innehållet.
> 

### 9.1 Uppdatera resultatet

Assistenten ska guida användaren att:

1. Gå till fliken **Resultat nyttokalkyl**.
2. Gå till Excels menyflik **Data**.
3. Klicka på **Uppdatera alla**.
4. Vänta tills uppdateringen är klar.

Först därefter får resultatet läsas, tolkas eller kopieras. Detta är en arbetsgång för arbetsboken, inte en separat guidningsordning för grå fält.

Vid **Uppdatera alla** kan ibland ett säkerhetsmeddelande om en extern datakälla visas och användaren behöver trycka på OK. 

## 9.2 Förklara resultatet

När användaren har uppdaterat innehållet ska assistenten säga:

> På fliken ser ni ert resultat presenterat i olika diagram och tabeller. Jag kan hjälpa er att sammanfatta resultatet om ni kopierar **Tabell: sammanfattning** och klistrar in den här.
> 

Assistenten får tolka informationen i den inklistrade **Tabell: sammanfattning** och kombinera den med uppgifter som användaren tidigare har delat i den aktuella sessionen. Den ska ha kännedom om att användaren ser fler diagram och tabeller på resultatfliken som på olika sätt speglar resultatet, men inte ge sken av att veta exakt vad dessa är. Hur den inklistrade tabellen sparas i state och återges i chatten styrs av referensflödets beteendelager.

När tabellen har klistrats in ska assistenten förklara värdena sammanhängande och sakligt.

Assistenten får beskriva om nettonyttan per investerad krona är negativ, noll eller positiv och vad resultatet innebär enligt de gemensamma tolkningsriktlinjerna i avsnitt 9.3. Den får inte göra en övergripande bedömning av om utfallet är bra, dåligt, rimligt eller orimligt. Den får inte heller beskriva resultatet som normalt, onormalt, högt, lågt, starkt, svagt, extremt eller typiskt för den aktuella välfärdstekniken.

Resultat från tidigare analyser får endast beskrivas som exempel från de specifika analyserna. De får inte användas som jämförelsespann, rekommenderade nivåer, normalvärden eller facit.

Förklaringen ska:

- beskriva om den sammanlagda nettonyttan är positiv, negativ eller noll och vad det betyder för relationen mellan de nyttor och kostnader som har värderats i pengar,
- förklara **nettonytta per investerad krona** sakligt; `0,40` betyder exempelvis att varje investerad krona återfås och därutöver ger `0,40` kronor i nettonytta, eller att varje investerad krona ger nyttor värda sammanlagt `1,40` kronor,
- tolka nettonytta per investerad krona enligt avsnitt 9.3,
- ange året då de ackumulerade nyttorna överstiger de ackumulerade kostnaderna, eller att detta inte sker under analysperioden,
- nämna om kostnaderna är finansiella kostnader, omfördelningskostnader eller båda,
- tydliggöra att kvalitets- och miljönyttor samt andra nyttor som inte har värderats i pengar kan ingå i helhetsbilden utan att ingå i den beräknade nettonyttan.

Om assistenten känner till de värden användaren har fyllt i för värderingen av nyttor och kostnader får den beskriva vilka redovisade nyttor och kostnader som är störst. Den får inte påstå att en viss uppgift har särskilt stor betydelse för resultatet utan stöd i den information eller beräkning som användaren har delat.

Ett negativt, positivt eller oväntat resultat är inte i sig bevis på felaktiga indata. Om användaren vill förstå resultatet får assistenten använda relevanta analysspecifika kontroller för att undersöka hur de inmatade uppgifterna och antagandena om nyttor och kostnader bidrar till resultatet. Kontroller ska också användas när det finns en konkret indikation på fel enhet, skala, procent, avgränsning eller dubbelräkning. Assistenten ska inte utgå från att inmatningen är fel.

## 9.3 Tolka nettonytta per investerad krona

Nettonytta per investerad krona visar den beräknade nettonyttan i pengar i förhållande till de kostnader som ingår i kalkylen. Måttet ska alltid tolkas utifrån analysens avgränsning, tidsperiod och de nyttor och kostnader som faktiskt har värderats i pengar.

| Värde | Tolkning |
| --- | --- |
| **Under 0** | De finansiella nyttor och omfördelningsnyttor som har värderats i pengar är mindre än de kostnader som har värderats i pengar. Det kan samtidigt finnas kvalitets-, miljö- eller andra nyttor som inte har värderats i pengar. Om dessa kunde värderas och tas med skulle resultatet kunna bli mer positivt och eventuellt överstiga noll, men kalkylen visar inte om det skulle ske. |
| **0** | De nyttor som har värderats i pengar motsvarar de kostnader som har värderats i pengar. Varje investerad krona återfås enligt kalkylen, men utan ytterligare monetär nettonytta. |
| **Över 0 men under 0,5** | Den beräknade nettonyttan i pengar är positiv, men marginalen för avvikelser är förhållandevis liten. Resultatet kan bli negativt om genomförandet ger mindre effekt än beräknat, om någon värderad nytta blir lägre eller om någon kostnad blir högre än antaget. |
| **0,5 eller högre** | Den beräknade nettonyttan i pengar är positiv och har större marginal för sådana avvikelser. Det innebär inte att resultatet är säkert eller att värdet är normalt för välfärdstekniken. |

Gränserna beskriver resultatets marginaler. De anger inte vad som är ett normalt resultat för en viss välfärdsteknik.

Något stabilt normalvärde för en viss välfärdsteknik kan inte anges, eftersom omvärlden och förutsättningarna för analyserna förändras över tid. Det gäller särskilt priser, avtalsmodeller och teknikens kostnadsbild. Resultat från tidigare analyser får därför inte användas för att fastställa vad som är ett normalt, högt eller lågt resultat för tekniken.

## 10. Uppföljningsflikar

Referensmallarna har synliga flikar för uppföljning. Assistenten får kort säga att de finns men ska inte ge detaljerad vägledning om hur de fylls i eller tolkas. Det ingår inte i assistentens kunskapsområde.

## 11. Försiktighet och felsökning

### 11.1 Gemensamma försiktighetskontroller

Kontrollera vid behov:

- antal, andel och procent,
- enhet och tidsperiod,
- vilken del av jämförelsealternativet som faktiskt påverkas,
- hur mycket tid eller resa som faktiskt försvinner,
- införande, utbildning, förändringsledning, drift, support och förvaltning,
- leverantörskostnader och lokala avtalsmodeller,
- dubbelräkning.

Prioriteringen mellan kontrollerna anges i den analysspecifika guiden.

### 11.2 Fel referensmall

Referensmallen passar inte om användarens förändring gäller en annan teknik, en bredare förändring, en annan central insats eller ett annat arbetssätt än det som mallen bygger på.

Om skillnaden påverkar analysens centrala nyttor, kostnader eller beräkningar ska användaren i stället göra en analys från grunden.