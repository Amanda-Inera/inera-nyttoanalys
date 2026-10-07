# Förvaltning – revidering av kunskapsbasen

## Administrativt stöd – ingår inte i KB

Den här filen styr arbetet med KB-revidering. Den ska **inte porteras till appens kunskapsbas, indexeras för KB-sökning eller ingå i `KB06-samlad.md`**. Förvara förvaltningsdokument i `admin/`, utanför artikelmapparna. Samlingsfilens byggskript utesluter redan denna mapp.

## Källor, ansvar och avgränsning

- Använd detta repos godkända artiklar som metodkälla. Ange vilken branch eller version som granskas; skilj arbetsförslag från godkänd text. Använd inklistrad arbetsversion om Amanda anger det. Fråga om versionen är oklar.
- Kontrollera de senaste relevanta filerna i [appens repo](https://github.com/fabian-von-tiedemann/inera-nyttoanalys-v2) för vad appen faktiskt använder: grafer, scopes, gemensamma artiklar och instruktioner.
- Amanda beslutar om metoden. Formuleringar i issues, tekniska förslag och appbeteenden är inte metodbeslut utan hennes bekräftelse. Anpassa inte KB till felaktigt appbeteende.
- Ge textförslag för granskning. Ändra filer, skapa PR:er eller publicera issues och kommentarer endast när Amanda har bett om det. Ändra originalartiklarna, aldrig den genererade samlingsfilen.

## Arbeta ett scope i taget

Börja med det scope Amanda anger. Om inget anges, fråga. Ge först en kort nulägesanalys: relevanta artiklar och issues samt metodfrågor som behöver avgöras.

Kontrollera relevanta issues, kommentarer, tidigare beslut och guldcase, även utan etiketten `KB`. Sök på nytt innan scopet avslutas. Skilj testobservationer, bekräftade metodbeslut och tekniska hypoteser. Visa om ett förslag redan stöds av KB, behöver förtydligande eller innebär en ändrad riktning.

Ta med de `shared`-scopes som noden faktiskt hämtar. Ändra en gemensam artikel bara om ändringen fungerar i alla dess sammanhang. Föreslå ändrad artikelindelning när det behövs; beakta även publika länkar. Stäm av motsägelser mellan KB, tidigare beslut och appen med Amanda. Gå vidare först när aktuellt scope är genomgånget och godkänt.

## Skrivregler för KB-artiklar

Läs de sju skrivprinciperna i [#235 ordagrant](https://github.com/fabian-von-tiedemann/inera-nyttoanalys-v2/issues/235#issuecomment-5396322697) före revidering. De [antogs av Amanda](https://github.com/fabian-von-tiedemann/inera-nyttoanalys-v2/issues/235#issuecomment-5396578741):

- En rubrik motsvarar en hämtbar enhet. All brödtext ska ligga under en egen H2-rubrik, även ingressen.
- Varje sektion ska omfatta **200–1 200 tecken**; sikta på 400–800. Högst sex sektioner per artikel.
- Håll varje tabell inom en sektion och under 1 200 tecken.
- Använd rubriker som beskriver läsarens situation med bekanta ord. Lägg poängen i första meningen. Varje sektion ska kunna förstås fristående.

Skriv direkt och användarnära, gärna i imperativ. Tilltala läsaren med `du`, `dig` och `din`. Använd `ni` bara för en uttalad grupp, exempelvis ”ni i analysgruppen”. Skriv ”organisationen” eller ”er organisation” när hela organisationen avses. Nämn ”assistenten” i tredje person vid behov. Undvik ”man”, otydliga ”vi” och ”användaren” i användarriktad text. Använd centrala begrepp konsekvent.

Beskriv metodens facit och avgränsningar. Lägg appflöden, tekniska lösningar, sparinstruktioner och rapportimplementation i separat utvecklingsåterkoppling.

## Kontrollera före godkännande

Kontrollera att relevant innehåll från föregående version finns kvar och redovisa medvetna borttagningar. Undvik dubbleringar inom artikeln; kontrollerad upprepning mellan artiklar är tillåten. Kontrollera skrivregler, metodbeslut, relevanta issues och sökbarhet för varje färdigt scope.

Kontrollera aktuell hämtning och chunkning i appen. Använd `npm run kb:chunkprofil <scope>` i apprepot när de reviderade texterna finns tillgängliga där, eller be Fabian om mätningen. Redovisa varningar och sådant som ännu inte kunnat verifieras. Ändra inte metoden för att få en teknisk kontroll att passera.

## Avsluta och överlämna

När Amanda säger att revideringen är klar, skapa en kort ändringslogg, högst cirka en sida, och lägg den i biblioteket. Ange datum, artiklar/scope, viktigaste innehållsförändringar och medvetet borttaget innehåll. Skriv uttryckligen om inget har tagits bort. Lägg till avgränsningar endast när sådana finns.

När ett metodsteg är färdigreviderat, skapa ett kort porteringsunderlag med tre rubriker:

1. **Vad som ändrats** – berörda artiklar och vad som gäller nu.
2. **Metodbeslut som appen ska följa** – metodens regler.
3. **Vad som inte har ändrats men lätt kan förväxlas** – viktiga avgränsningar; ange om inga finns.

Ta inte med appbeteenden, kodfiler, lösningsförslag eller testfall i porteringsunderlaget. Fabian och utvecklingsagenten härleder implementation och tester. Gå sist igenom vilka issues revideringen hanterar och vad som återstår.

Denna förvaltningsfil och administrativa ändringsloggar följer inte med innehållsporteringen.
