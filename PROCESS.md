# Procesboek Django

Laura Koelewijn

13217704

**Do 3 nov. 22**

Ik heb net het hoorcollege gekeken en ik vond het heel fijn om even een uitgebreidere uitleg te krijgen over HTML en CSS. Ik herinner me nog van een paar weken geleden dat we ook een site moesten maken in HTML, alleen dat het hoorcollege daarover totaal niet in de diepte ging, wat er tot leidde dat ik heel veel "basic" kennis over HTML op moest zoeken op het internet. Echter, in dit hoorcollege ging het allemaal wat dieper. Ten eerste; heel fijn om te weten dat je gewoon alleen de *width attribute* van een afbeelding kan aanpassen om de afbeelding te herschalen zonder dat de afbeelding uit verhouding wordt gehaald. Voorheen ging ik namelijk elke keer uitrekenen hoe hoog de hoogte moest zijn om de afbeelding in verhouding te laten. Ook heb ik nieuwe dingen geleerd zoals hoe je een tabel kan maken, en dat je de *style* van een HTML-document ook in de *head* kan zetten. Wat betreft het laatste, dit is denk ik niet iets dat ik veel zal gaan gebruiken, aangezien ik het wel fijn vind voor de overzichtelijkheid om een los *stylesheet* document te hebben en te linken. Daarnaast, ik wist helemaal niet dat een .class algemeen is, en een #id uniek! Ook cool om te weten hoe flex werkt; bijna alles flext wel mee tegenwoordig (denk ook omdat sites moeten werken op desktop én op mobiel).

            Na het hoorcollege heb ik een start gemaakt aan de search website.

**Vr 4 nov. 22**

Vandaag heb ik search opdracht afgemaakt. Het ging me wel aardig af, al moet ik zeggen dat dit soort dingen toch altijd meer tijd kosten dan dat je verwacht. Dit komt voornamelijk door het onderzoeken van zaken waar je nog geen kennis over hebt. Bijvoorbeeld het CSS-document, af en toe werkte het gewoon niét. Op dat soort momenten was Stack Overflow mijn beste vriend. Ik heb geleerd dat je "!important" kan gebruiken in de CSS om alle andere *attributes* te overriden. Dit was handig om te kijken waar in de *stylesheet* het fout ging waardoor de veranderingen die ik wilde maken niet verschenen.
    Nu ben ik van plan om de laatste twee hoorcolleges te kijken; Git en Django.

**Ma 7 nov. 22**

Afgelopen vrijdag had ik niet meer genoeg concentratie om het Django hoorcollege af te kijken, dus ik heb vanochtend het laatste uurtje gekeken. Het is ook best veel nieuwe informatie natuurlijk. Vanmiddag had ik het mentoruur van Django en heb ik mijn idee voor mijn website doorgesproken; een site voor een vriendin van mij waarop ze haar eigen gemaakte kleding kan verkopen. Max leek het wel een leuk en goed idee dus daar ben ik blij mee. Het enige punt waar ik tegen aan zou kunnen gaan lopen is het implementeren van een betaalsysteem op de site. Max weet niet hoe moeilijk of makkelijk dat kan zijn. Ik kan me best voorstellen dat dat een lastig dingetje kan worden. Max stelde voor dat ik ook de site in zou kunnen leveren zonder betaalsysteem als het niet lukt, om het eventueel later wel te implementeren in mijn eigen tijd

**Za 19 nov. 22**

Ik heb het op dit moment erg druk met Programmeren2 en ik merk dat ik weinig tijd over hou voor het project. Ik geef Progammeren2 nu ook voorrang omdat ik er opdrachten voor in moet leveren die gelijk beoordeeld worden met een cijfer. Ik hoop dat het binnenkort weer iets rustiger wordt zodat ik meer tijd kan besteden aan Django, want anders ben ik bang dat het me niet gaat lukken.

            De tijd die ik er afgelopen twee weken wel aan besteed heb bestond vooral uit het proberen te begrijpen van het Django *framework* zodat ik echte stappen kan gaan maken met de Wiki opdracht. Alhoewel er best wat in het hoorcolleges uitgelegd wordt vind ik het allemaal een beetje verwarrend wanneer ik de opdracht open; zoveel files waarvan ik niet goed begrijp wat erin staat en wat ze doen.

            Vandaag heb ik wel mijn project *proposal* geschreven, want de tijd dringt. Dit ging overigens prima omdat ik een aardig helder idee heb van wat mijn site gaat inhouden.

-- vanaf hier samen met Martijn besloten dat ik geen zelf gedefinieerd project meer ga doen --

**Di 29 nov. 22**

Eindelijk begrijp ik hoe Git werkt! Ik was vergeten om te *committen* terwijl ik bezig was met Wiki, en toen ik het vervolgens wilde doen wist ik helemaal niet meer hoe het moest. Het kijken van het hoorcollege is dan ook weer een tijdje geleden... Ik heb delen ervan opnieuw bekeken om het weer een beetje terug te halen. Nog begreep ik de volgorde van de Git *commands* niet helemaal, en wat welke *command* precies doet. Ik vroeg het aan een medestudent aan mijn tafel. Zij kon mij precies uitleggen hoe alles in elkaar stak. Nu weet ik dat je eerst moet *adden*, vervolgens moet *committen* en een message erbij kan toevoegen, om als laatste alle veranderingen te *pushen* naar GitHub. Een paar uur later was ik degene die dit kon uitleggen aan een andere medestudent :).

            Nu ik Git begrijp en nu ik het gevoel heb dat ik ongeveer weet wat files zoals views.py (ik zie het als een soort document met functies) en urls.py (paden voor de urls) doen, voel ik me zekerder om echte stappen te gaan maken in deze opdracht. Ik ben net begonnen aan het toevoegen van twee HTML-pagina's: entry.html en error.html. Dit leek mij wel een goed begin, niet al te ingewikkeld en goed te over zien. Op dit moment laat de entry.html nog geen entry zien, maar dit ga ik later implementeren. Stapje voor stapje. De error page heb ik wel gevuld; gewoon met een simpele error *message* in een *header* en een *paragraph*. Ik wil zo meteen nog schetsen maken en het *design-document* afronden en uploaden, omdat ik dat anders sowieso ga vergeten.

            Aan het einde van de dag heb ik de links aan de linkerkant van de layout.html werkend gemaakt. Ik wist nog hoe dit moest van de search opdracht. Ook heb ik de HTML-pagina's voor die links aangemaakt. Vervolgens heb ik aan de hand van het hoorcollege "<str:title>" geplaatst in mijn urls.py zodat de site nu naar de pagina gaat die je achter de slash intypt.

**Vr 2 dec. 22**

Vandaag heb ik heel veel tijd besteed aan het lezen van markdown2 documentatie. Toen ik begreep hoe het eenmaal in elkaar zat heb ik mijn convert_markdown functie in views.py toegevoegd. Ook heb ik in mijn entry functie ervoor gezorgd dat Django mijn error pagina rendert als een user een titel van een entry intypt in achter de slash in de URL die niet bestaat. Dit was makkelijk omdat ik door mijn convert_markdown functie gelijk een manier had om bestaande markdown content aan te roepen waardoor ik kon checken of het "not None" is. Als het dus wel "None" is, moet er een error renderen. Als laatste heb ik nog even gauw links gemaakt van de entries in de index pagina.

**Za 3 dec. 22**

Ik ben van plan om even in het weekend door te werken. Ik wil graag Wiki afmaken vóór maandag aangezien ik denk dat ik ook nog aardig wat tijd nodig ga hebben voor Commerce.

            Vandaag ben ik begonnen met het implementeren van de search bar. Dit was wel even een klusje. Eerst ben ik op papier wat ideeën uit gaan schrijven. Ik kwam er niet helemaal uit. Aangezien ik dit weekend toch bij mijn ouders ben greep ik mijn kans en vroeg ik mijn vader, die in ICT werkt, om hulp. Ik liet hem zien wat ik probeerde te doen, en toen zijn we samen gaan zoeken naar een oplossing. Uiteindelijk zijn we met het idee gekomen om te loopen door een lijst met alle entries. Als dan de eerste letters van een entry uit de lijst overeenkomt met de letters van de entry die de user intypt bij in de searchbar, voegen we deze entry toe aan een andere lijst. Vervolgens rendert Django een pagina met deze lijst van overeenkomstige zoekopdrachten. De links werken nu nog niet; de search.html is nu gewoon een pagina met een lijst. Maar voor nu kan ik verder.

            Daarna ben ik bezig geweest met het implementeren van de newpage.html. Aanvankelijk ging dit prima, omdat er best veel over *forms* uitgelegd werd in het hoorcollege. Toen ik dacht dat ik klaar was werkte het helaas niet. Ik kon wel dingen in de *form* invullen, alleen er werd geen nieuwe pagina aangemaakt. Wat er gebeurde was dat er één keer een nieuwe pagina aangemaakt werd, en deze vervolgens elke keer geëdit werd. Ik stopte voor vandaag, omdat ik moe was en er toch niet meer uit ging komen vandaag. Ik heb nog wel even snel een *edit button* toegevoegd in de entry.html, maar deze knop werkt voor nu nog niet.

**Zo 4 dec. 22**

Ik ben erachter gekomen waarom mijn newpage niet werkte! Het werkte niet omdat ik geen *if-statement* had toegevoegd in mijn functie. Waar de new_page functie voorheen niet checkte of de pagina al bestond en dus elke keer dezelfde pagina editte, check de functie het nu wel en rendert een error als de pagina al bestaat! Als de pagina nog niet bestaat maakt 'ie een nieuwe pagina aan. Eindelijk werkt het!

            Alleen search werkt niet meer... Maar ook hier: ik vergat *if*- en *else-statements* toe te voegen om te kijken of pagina's bestaan. Snel gefikst!

            Ook heb ik nog linkjes toegevoegd aan de search.html pagina zodat er niet meer een saaie lijst staat, maar zodat users op bepaalde pagina's kunnen klikken als ze ernaar zoeken.

**Ma 5 dec. 22**

Ik heb gister een screenshot gemaakt van mijn newpage view, omdat ik dacht: Hey, dit is precies hoe de edit moet functioneren! Vandaag heb ik dit dus voor een groot deel opnieuw geschreven in een edit functie in views.py. Mijn knopje bestond al, dus ik heb alles aan elkaar verbonden.

            Daarnaast heb ik random page functionaliteit geïmplementeerd. Dit had ik echt in een halfuurtje af omdat ik al eerder met de random module van Python gewerkt heb en ik hier de kans zag om het opnieuw te gebruiken. Ik heb even op het internet gezocht wat het beste was om te gebruiken om een random element uit een lijst te selecteren, en dat bleek random.choice() te zijn (Dankjewel W3schools). Wiki is nu af!

**Di 6 dec. 22**

Ik liet net aan een medestudent mijn Wiki site zien, en natuurlijk ontdekte ik toen een bug: De linkjes op de bestaande markdown pagina's werken nog niet (Dus bijvoorbeeld de link naar de HTML-pagina op de CSS-pagina). Ik heb het natuurlijk gauw opgelost. Toch best handig om er op deze manier achter te komen of er nog bugs in je code zitten!

            In de middag heb ik het grootste gedeelte van het Commerce hoorcollege gekeken, maar niet volledig want ik vond het nogal lang.

**Wo 7 dec. 22**

Vandaag heb ik de laatste 45 minuten van het Commerce hoorcollege gekeken. Dit keer ben ik hierna gelijk schetsen en class diagrams gaan maken, omdat ik nog weet van de vorige keer dat ik vergeet hoe alles werkt als ik niet gelijk aan de slag ga. Ik heb alles van het design-document afgerond en gelijk gepusht naar GitHub.

            Toen ben ik begonnen aan Commerce. Ik moet zeggen dit een stuk soepelere start was dan met Wiki omdat ik nu wél begrijp hoe Django werkt. Ik begon met het maken van een AuctionListings model omdat we op dit moment ook bezig zijn met classes in Python met Programmeren2 en ik dit er verdacht veel op vind lijken. Ik heb hierna de active listings geïmplementeerd en mijn admin page geactiveerd. Voor de admin page heb ik weer even het hoorcollege erbij gepakt. Dit ging allemaal vrij snel.

            Uiteindelijk heb ik nog cards gemaakt voor op m'n index page om alle listings te presenteren. Ik heb op internet gezocht naar "Professional bootstrap cards" (haha) en kwam op een hele vage website terecht, waar ik er een van gekopieerd en geplakt heb in mijn index pagina. Er zat ook een enorme hoeveelheid aan CSS bij. Het werkte helaas nog niet. Ik had het idee dat dit kwam doordat de CSS niet werkte, omdat zo'n card natuurlijk voornamelijk CSS is. Ik veranderde het lettertype in mijn CSS en het veranderde niet op mijn pagina. Toen wist ik zeker dat de CSS niet werkte en heb ik het internet geraadpleegd. Iemand op Stack Overflow zei dat het kan liggen aan de cache van je browser en dat het soms helpt om de cache en geschiedenis van je browser te verwijderen en het opnieuw te proberen. *That did the trick!*

**Do 8 dec. 22**

Ik heb vandaag een listing pagina gemaakt waar een user op kan klikken om alle details van de listing te zien. Ik heb een lange tijd zitten gestruggled met het weergeven van de juiste pagina want ik begreep niet helemaal hoe ik de ID van een listing mee kan geven aan de pagina voor die listing. Na delen van het hoorcollege terug te kijken lukte het me wel.

            Ook heb ik de view functie van create afgemaakt en de site nog wat mooier gemaakt. Ik vond het namelijk lelijk dat alle tekststukken verschillende *margins* hadden. Ik wilde de *margins* aanpassen zodat de stukken tekst precies onder elkaar kwamen te staan, maar dit ging niet zo makkelijk; de tekst bewoog namelijk niet. Op internet heb ik gevonden dat dit kwam doordat ik een *label* probeerde te verplaatsen, en om dat te doen moest ik eerst de *inline block* voor dat label aanzetten en daarna kon ik pas de *margin* aanpassen.

**Za 10 dec. 22**

Op zaterdag (helaas weer in het weekend) heb ik mijn AuctionListings model aangepast omdat ik bids moest toevoegen. Dit was nog best een gedoe omdat ik al listings had toegevoegd aan mijn site en ik daardoor met de makemigrations en migrate allemaal errors kreeg (omdat er voor die listings nog geen bids bestaan dus). Ik heb uiteindelijk al mijn bestaande listings verwijdert, het AuctionListings model aangepast, en weer nieuwe listings toegevoegd. Zo ging alles goed.

            Vervolgens wilde ik ervoor zorgen dat users kunnen bieden op listings, en ik ben me hier toch eens lang mee bezig geweest. Ik begreep wel dat ik een Bid model moest aanmaken, en vervolgens code moest aanpassen van wat ik nu al had, maar ik voelde me overweldigd door de hoeveelheid werk die ik moest doen. Het is me helaas niet gelukt om het bieden vandaag helemaal af te maken, en omdat het weekend is heb ik ook niemand die mij er mee kan helpen. Daarom zet ik dit even op halt en ga ik er later mee verder.

            Ondanks alle *struggles* heb ik wel veel geleerd vandaag:

                - Ik heb geleerd dat je meerdere *formatted strings* kan *returnen* in een model in plaats van slechts één door middel van bijvoorbeeld een \__str__ of een \__repr__\.
                - Ook heb ik geleerd dat ik de prijs van een listing met 2 decimalen kan formatteren door .2f % te gebruiken.
                - Als laatste heb ik met bootstrap een handige error pop-up kunnen implementeren voor wanneer een user een bod invoert dat te laag is.

Laat op de avond ben ik nog even bezig geweest met het toevoegen van een functie waarmee *users comments* kunnen toevoegen op *listings.* Dit lukte vrij snel omdat ik het de request.POST["..."]-methode onder de knie had door het implementeren van forms in de vorige opdracht.

**Zo 11 dec. 22**

Vandaag wilde ik het graag mogelijk maken dat verkopers hun *auction* kunnen sluiten én dat users *listings* toe kunnen voegen aan hun *watchlist*.

            's Middags heb ik het *auction closing* geïmplementeerd. Wat mij hierbij hielp was het opschrijven van schemaatjes voor mezelf om duidelijk te krijgen wat ik nou precies moest doen in de *views, urls*, en wat voor *templates* ik moest creëren. Dit lukte vrij goed.

            's Avonds heb ik de *watchlist* toegevoegd. Dit was weer een kwestie van informatie van de user extraheren van de *backend*, om dit vervolgens naar de *frontend* te sturen. Wel had ik nog een beetje moeite met het *redirecten* van pagina's. Ik wilde dit graag doen omdat dit mij logischer leek dan elke keer nieuwe pagina's te renderen. Logischerwijze probeerde ik het op dezelfde manier te doen als in de source-code (bijvoorbeeld zo: return HttpResponseRedirect(reverse("index"))), maar op de een of andere manier werkte dit niet. Op internet zocht ik alternatieve manieren om HttpResponseRedirect te gebruiken en heb het vervolgens op de volgende manier gedaan: return HttpResponseRedirect(reverse("listing",args=(id, ))). Toen werkte het wel, geen idee waarom.

**Ma 12 dec. 22**

Aangezien alles van Commerce nu werkt met uitzondering van bids, heb ik vandaag een student assistent gevraagd om hulp. Nu is het mij gelukt om Commerce helemaal af te ronden!

**Do 15 dec. 22**

Vandaag heb ik de laatste checks gedaan, om te kijken of alles werkt van Wiki en Commerce, en heb ik de *final* versies gepusht naar GitHub.

            Ik merkte net nog gauw een bug op in Commerce: wanneer ik een listing toe voeg door middel van mijn create listing link op de site, werd alles goed opgeslagen behalve de categorie; die was leeg als ik de listing bekeek op de *admin* pagina. Toen kwam ik erachter dat ik in de code van mijn createlisting functie bij het creëren van een nieuw AuctionListing object vergat om de categorie toe te voegen. In de HTML stond al wel dat de user een categorie kon kiezen, en ik kon dus wel een categorie kiezen uit een drop-down menu, alleen het werd niet opgeslagen. Ik heb net dus de categorie toegevoegd in mijn view functie.

            Als allerlaatste heb ik nog wat leuke CSS toegevoegd aan beide sites: een foto van een kiwi als icoon bovenaan de wiki site en naast het wiki logo aan de linkerkant. Toen heb ik wiki veranderd naar kiwi :) Ook heb ik nog een icoon toegevoegd aan de Commerce site.
