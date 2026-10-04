r"""Genera le 5 pagine -allenamento di Geografia di Irene da un unico modello.
Le domande stanno qui sotto (prima opzione = quella giusta: l'app le mescola).
Uso:  py strumenti\genera-allenamenti.py
"""
import json
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent

MODELLO = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#FAF6EE">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Geografia di Irene">
<script src="alert.js"></script>
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<title>__TITOLO__ — Allenamento</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#FAF6EE; --card:#FFFFFF; --ink:#2F2A24;
    --accent:#2F7A55; --accent-soft:#DDEFE3;
    --green:#3E8E5A; --green-soft:#E2F0E6;
    --red:#C2492F; --red-soft:#F6E1DB;
    --blue:#3B6EA5; --blue-soft:#E2ECF5;
  }
  *{box-sizing:border-box;}
  body{margin:0; font-family:"Lexend","Trebuchet MS",Verdana,sans-serif;
    background:var(--bg); color:var(--ink); line-height:1.7; letter-spacing:0.3px; padding:24px 14px 60px;}
  .wrap{max-width:620px;margin:0 auto;}
  .back{display:inline-block;background:var(--accent-soft);color:var(--accent);text-decoration:none;border-radius:12px;padding:8px 16px;font-size:0.98rem;font-weight:bold;margin:0 8px 14px 0;}
  h1{color:var(--accent);font-size:1.6rem;text-align:center;margin:0 0 6px;}
  .sub{text-align:center;color:#8a7f70;margin:0 0 26px;font-size:1rem;}
  .card{background:var(--card);border-radius:18px;padding:22px 20px;margin-bottom:22px;
    box-shadow:0 4px 14px rgba(0,0,0,0.06);border:1px solid #efe7da;}
  .card h2{margin:0 0 10px;font-size:1.25rem;color:var(--accent);}
  .card .lead{color:#8a7f70;margin:0 0 12px;font-size:0.97rem;}
  .levelbar{margin:0 0 12px;}
  .lvrow{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:0.98rem;color:var(--accent);}
  .lvdots{display:inline-flex;gap:6px;}
  .lvdot{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;
    background:var(--bg);border:2px solid var(--accent-soft);color:#b9ad9c;font-size:0.85rem;font-weight:bold;}
  .lvdot.on{background:var(--accent-soft);border-color:var(--accent);color:var(--accent);}
  .ex{margin:14px 0;}
  .qnum{font-weight:bold;color:var(--accent);}
  .qtext{font-size:1.1rem;margin:6px 0 8px;}
  .options{display:flex;flex-direction:column;gap:10px;}
  .opt{background:var(--bg);border:2px solid var(--accent-soft);
    border-radius:12px;padding:13px 14px;font-size:1.05rem;cursor:pointer;
    text-align:left;font-family:inherit;color:var(--ink);transition:all .15s;}
  .opt:hover{border-color:var(--accent);}
  .opt.correct{background:var(--green-soft);border-color:var(--green);color:var(--green);font-weight:bold;}
  .opt.wrong{background:var(--red-soft);border-color:var(--red);color:var(--red);}
  .feedback{margin-top:10px;font-size:1.02rem;font-weight:bold;min-height:24px;}
  .feedback.ok{color:var(--green);}
  .feedback.no{color:var(--red);}
  .progress{text-align:center;font-size:1.05rem;margin:12px 0 0;color:#8a7f70;}
  .star{font-size:1.4rem;}
  .match-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:6px;}
  .match-col{display:flex;flex-direction:column;gap:10px;}
  .match-btn{background:var(--bg);border:2px solid var(--accent-soft);border-radius:12px;
    padding:12px;font-size:0.98rem;cursor:pointer;font-family:inherit;color:var(--ink);
    display:flex;align-items:center;justify-content:center;text-align:center;gap:6px;transition:all .15s;}
  .match-btn:hover{border-color:var(--accent);}
  .match-btn.sel{border-color:var(--blue);background:var(--blue-soft);color:var(--blue);font-weight:bold;}
  .match-btn.done{background:var(--green-soft);border-color:var(--green);color:var(--green);font-weight:bold;cursor:default;opacity:0.85;}
  .match-btn.flash{border-color:var(--red);background:var(--red-soft);}
  .restart{display:inline-block;margin:12px auto 0;background:var(--accent);color:#fff;border:none;
    border-radius:12px;padding:11px 22px;font-size:1rem;cursor:pointer;font-family:inherit;}
</style>
</head>
<body>
<div class="wrap">
  <a class="back" href="index.html">&larr; Indice</a><a class="back" href="__LEZIONE__.html">📖 Ripassa la lezione</a>
  <h1>🏋️ __TITOLO__ — Allenamento</h1>
  <p class="sub">Mattoncino __NUM__ · 3 sezioni · 3 livelli ciascuna 💪</p>

  <div class="card">
    <h2>🧠 1. Domande</h2>
    <p class="lead">Scegli la risposta giusta. Puoi riprovare finché non la trovi!</p>
    <div class="levelbar" id="quiz-level"></div>
    <div id="quiz-box"></div>
    <div class="progress" id="quiz-prog"></div>
  </div>

  <div class="card">
    <h2>✅ 2. Vero o falso</h2>
    <p class="lead">Leggi la frase e tocca Vero o Falso. Dopo ti dico perché.</p>
    <div class="levelbar" id="vf-level"></div>
    <div id="vf-box"></div>
    <div class="progress" id="vf-prog"></div>
  </div>

  <div class="card">
    <h2>🔗 3. Abbina</h2>
    <p class="lead">Tocca una casella a sinistra, poi la sua coppia a destra. Collega tutte le coppie!</p>
    <div class="levelbar" id="abbina-level"></div>
    <div class="match-grid" id="abbina-grid"></div>
    <div class="progress" id="abbina-prog"></div>
  </div>
</div>
<script>
window.ALLENAMENTO = __DATI__;
</script>
<script src="allenamento.js"></script>
<script>
  if ('serviceWorker' in navigator) { navigator.serviceWorker.register('./service-worker.js'); }
</script>
</body>
</html>
"""


def Q(q, *opts):
    return {"q": q, "opts": list(opts)}


def V(q, v, perche):
    return {"q": q, "v": v, "perche": perche}


def A(*coppie):
    return [{"l": l, "r": r} for l, r in coppie]


MATTONCINI = {
    "lombardia": {
        "num": 1, "titolo": "La Lombardia: il territorio",
        "quiz": [
            [Q("Qual è il capoluogo della Lombardia?", "Milano", "Bergamo", "Brescia"),
             Q("Quanti abitanti ha la Lombardia, più o meno?", "10 milioni", "1 milione", "50 milioni"),
             Q("Quante province ha la Lombardia?", "12", "5", "20"),
             Q("Con quale Stato straniero confina?", "Svizzera", "Francia", "Austria"),
             Q("Quale regione c'è a SUD della Lombardia?", "Emilia-Romagna", "Piemonte", "Veneto")],
            [Q("Qual è la fascia più grande della Lombardia?", "la pianura (47%)", "la collina (12%)", "la montagna (41%)"),
             Q("Qual è la fascia più piccola?", "la collina", "la pianura", "la montagna"),
             Q("Il punto più alto della Lombardia è il…", "Bernina", "Monte Bianco", "Etna"),
             Q("L'unico parco nazionale lombardo è il parco…", "dello Stelvio", "del Gran Paradiso", "d'Abruzzo"),
             Q("Dove si va a sciare soprattutto?", "Sondrio, Bergamo, Brescia", "Milano, Lodi, Pavia", "Cremona e Mantova")],
            [Q("Quale fiume segna il confine a sud?", "il Po", "l'Adda", "il Ticino"),
             Q("Quante acque dolci italiane ci sono in Lombardia?", "l'80%", "il 10%", "il 50%"),
             Q("Il lago più grande d'Italia è il…", "Garda", "lago di Como", "lago d'Iseo"),
             Q("Il lago più profondo d'Italia è il…", "lago di Como", "Garda", "lago Maggiore"),
             Q("Quali laghi sono TUTTI lombardi?", "Como e Iseo", "Garda e Maggiore", "Maggiore e Lugano")],
        ],
        "vf": [
            [V("Il Veneto si trova a est della Lombardia.", True, "Sulla cartina è a destra, cioè a est."),
             V("La Lombardia confina con la Francia.", False, "Confina con la Svizzera, non con la Francia."),
             V("Milano è il capoluogo della Lombardia.", True, "Milano è anche città metropolitana."),
             V("La Lombardia ha 5 province.", False, "Le province sono 12."),
             V("A sud c'è l'Emilia-Romagna.", True, "E il Po fa da confine.")],
            [V("Quasi metà della Lombardia è pianura.", True, "La pianura è il 47%."),
             V("La collina è la fascia più grande.", False, "La collina è la più piccola: 12%."),
             V("Il Parco dello Stelvio è uno dei più grandi d'Europa.", True, "Sta intorno all'Ortles-Cevedale."),
             V("Le aree protette sono il 27% della regione.", True, "Ci sono 24 parchi regionali e 20 foreste."),
             V("In Lombardia non ci sono montagne sopra i 4000 m.", False, "Il Bernina supera i 4000 m.")],
            [V("Il Ticino è un affluente del Po.", True, "È il primo e il più importante."),
             V("Il Garda è tutto in Lombardia.", False, "È diviso tra Lombardia, Veneto e Trentino."),
             V("Il lago di Como ha la forma di una Y rovesciata.", True, "I tre rami si incontrano a Bellagio."),
             V("I laghi lombardi sono di origine glaciale.", True, "Li hanno scavati gli antichi ghiacciai."),
             V("Il lago Maggiore si chiama anche Lario.", False, "Il Lario è il lago di Como; il Maggiore è il Verbano.")],
        ],
        "abbina": [
            A(("Milano", "capoluogo 🏙️"), ("Svizzera", "confine a nord-ovest"), ("Veneto", "confine a est"),
              ("Emilia-Romagna", "confine a sud"), ("Piemonte", "confine a ovest")),
            A(("Montagna", "41%"), ("Collina", "12%"), ("Pianura", "47%"),
              ("Bernina", "punto più alto"), ("Stelvio", "parco nazionale")),
            A(("Garda", "il più grande d'Italia"), ("Como (Lario)", "il più profondo d'Italia"),
              ("Maggiore", "anche detto Verbano"), ("Iseo", "anche detto Sebino"), ("Po", "confine a sud 🌊")),
        ],
    },
    "storia": {
        "num": 2, "titolo": "La storia della Lombardia",
        "quiz": [
            [Q("Qual è lo stemma della Lombardia?", "la rosa camuna", "il leone di San Marco", "l'aquila"),
             Q("Dove ci sono le incisioni sulle rocce dei Camuni?", "in Val Camonica", "sul lago di Garda", "a Milano"),
             Q("Quale città fondarono gli Etruschi?", "Mantova", "Milano", "Como"),
             Q("Quale poeta romano nacque a Mantova?", "Virgilio", "Dante", "Manzoni"),
             Q("Milano diventò capitale…", "dell'Impero romano d'Occidente", "del Regno di Francia", "dei Longobardi")],
            [Q("Dove misero la capitale i Longobardi?", "a Pavia", "a Milano", "a Roma"),
             Q("Chi sconfisse i Longobardi?", "Carlo Magno", "Napoleone", "Garibaldi"),
             Q("La Lega Lombarda vinse la battaglia di…", "Legnano", "Waterloo", "Solferino"),
             Q("Contro quale imperatore combatteva la Lega Lombarda?", "Federico Barbarossa", "Carlo Magno", "Augusto"),
             Q("Quale famiglia comandava Mantova?", "i Gonzaga", "gli Sforza", "i Medici")],
            [Q("Chi riunì la Lombardia nel 1797?", "Napoleone", "Carlo Magno", "Garibaldi"),
             Q("Dopo Napoleone l'Austria creò il…", "Regno Lombardo-Veneto", "Ducato di Milano", "Regno d'Italia"),
             Q("Nel 1848 a Milano ci furono…", "le Cinque giornate", "le Dieci giornate", "i Mille"),
             Q("In che anno nacque il Regno d'Italia?", "1861", "1815", "1915"),
             Q("Quale grande evento ci fu a Milano nel 2015?", "l'Expo", "le Olimpiadi", "i Mondiali")],
        ],
        "vf": [
            [V("La rosa camuna è un antico simbolo del sole.", True, "È incisa sulle rocce della Val Camonica."),
             V("I Galli fondarono i villaggi che diventarono Milano e Bergamo.", True, "Anche Brescia e Como."),
             V("Gli Etruschi fondarono Pavia.", False, "Gli Etruschi fondarono Mantova."),
             V("Plinio era di Como.", True, "Era un naturalista romano."),
             V("Milano fu capitale dell'Impero romano d'Occidente.", True, "Si chiamava Mediolanum.")],
            [V("Il nome Lombardia viene dai Longobardi.", True, "Il nord si chiamava Longobardia Maior."),
             V("La Lega Lombarda perse a Legnano.", False, "Vinse! Sconfisse il Barbarossa."),
             V("I Visconti e gli Sforza comandavano Milano.", True, "Erano le Signorie."),
             V("Con le Signorie comandava una sola famiglia.", True, "Prima, nei Comuni, si governavano le città."),
             V("Bergamo e Brescia furono per secoli di Venezia.", True, "Fino al 1797.")],
            [V("Il Regno Lombardo-Veneto era austriaco.", True, "Lo creò l'Austria nel 1815."),
             V("Le Cinque giornate furono a Brescia.", False, "Furono a Milano. A Brescia ci furono le Dieci giornate."),
             V("Nel 1861 nacque il Regno d'Italia.", True, "E la Lombardia ne fece parte."),
             V("Il fascismo nacque a Milano nel 1919.", True, "Con i Fasci di combattimento."),
             V("Nel 2023 Bergamo e Brescia furono capitali della cultura.", True, "Capitali italiane della cultura.")],
        ],
        "abbina": [
            A(("Camuni", "incisioni sulle rocce 🪨"), ("Etruschi", "fondano Mantova"), ("Galli", "villaggi di Milano e Bergamo"),
              ("Romani", "Milano capitale"), ("Virgilio", "poeta di Mantova")),
            A(("Longobardi", "capitale a Pavia"), ("Carlo Magno", "re dei Franchi"), ("Lega Lombarda", "vince a Legnano ⚔️"),
              ("Gonzaga", "Signori di Mantova"), ("Sforza", "Signori di Milano")),
            A(("1797", "Napoleone riunisce la Lombardia"), ("1815", "Regno Lombardo-Veneto"), ("1848", "Cinque giornate di Milano"),
              ("1861", "nasce il Regno d'Italia"), ("2015", "Expo a Milano")),
        ],
    },
    "economia": {
        "num": 3, "titolo": "Popolazione ed economia",
        "quiz": [
            [Q("Quanti italiani vivono in Lombardia?", "il 16%", "il 50%", "il 2%"),
             Q("Dove vive la maggior parte dei lombardi?", "in pianura", "in montagna", "in collina"),
             Q("Che cos'è il saldo naturale?", "nati meno morti", "arrivati meno partiti", "uomini meno donne"),
             Q("Dal 2012 in Lombardia…", "muoiono più persone di quante ne nascano", "nascono più bambini di prima", "non cambia niente"),
             Q("Perché gli abitanti continuano ad aumentare?", "per l'immigrazione", "per le tante nascite", "perché nessuno muore")],
            [Q("Quanta ricchezza italiana produce la Lombardia?", "circa 1/5", "la metà", "quasi niente"),
             Q("In quale settore lavora più gente?", "terziario (servizi)", "primario (agricoltura)", "secondario (industria)"),
             Q("Quanti lavorano nell'agricoltura?", "l'1%", "il 30%", "il 68%"),
             Q("Il settore secondario è…", "l'industria", "l'agricoltura", "il turismo"),
             Q("Milano è una delle sei capitali…", "economiche d'Europa", "dello sport", "della moda antica")],
            [Q("La Lombardia produce il 42% del…", "riso italiano", "vino francese", "petrolio"),
             Q("Dove sono soprattutto le industrie?", "in pianura, da Varese a Brescia", "sulle Alpi", "solo a Mantova"),
             Q("In montagna, a Sondrio, ci sono soprattutto…", "centrali idroelettriche", "raffinerie", "fabbriche di auto"),
             Q("Che cosa c'è a Milano?", "la Borsa Italiana", "il Parlamento", "il Vaticano"),
             Q("Il turismo d'affari (fiere, congressi) è forte soprattutto…", "a Milano", "a Sondrio", "a Livigno")],
        ],
        "vf": [
            [V("In Lombardia vivono più di 10 milioni di persone.", True, "È la regione più popolata d'Italia."),
             V("La maggior parte dei lombardi vive in montagna.", False, "2 su 3 vivono in pianura."),
             V("Gli stranieri sono circa l'11% degli abitanti.", True, "Più di un milione di persone."),
             V("Oggi in Lombardia nascono più bambini di quante persone muoiano.", False, "Dal 2012 è il contrario."),
             V("La popolazione cresce grazie all'immigrazione.", True, "Arriva gente da altre regioni e paesi.")],
            [V("La Lombardia è la prima regione d'Italia per economia.", True, "Produce circa 1/5 della ricchezza."),
             V("Quasi 7 lavoratori su 10 sono nei servizi.", True, "Il terziario è il 68,6%."),
             V("Nell'industria lavora il 90% delle persone.", False, "Nell'industria lavora circa il 30%."),
             V("Il primario è l'agricoltura e l'allevamento.", True, "In Lombardia ci lavora solo l'1%."),
             V("Le imprese lombarde sono quasi tutte grandissime.", False, "Più del 99% sono piccole.")],
            [V("La Lombardia è la prima regione agricola d'Italia.", True, "Latte, riso, carne di maiale."),
             V("Il riso si coltiva soprattutto verso Pavia.", True, "Nella pianura irrigua."),
             V("Le industrie sono soprattutto sulle Alpi.", False, "Sono soprattutto in pianura."),
             V("Bormio e Livigno sono località di montagna.", True, "Ci si va a sciare."),
             V("Sirmione e Desenzano sono sul lago di Garda.", True, "Turismo sui laghi.")],
        ],
        "abbina": [
            A(("Saldo naturale", "nati meno morti"), ("Immigrazione", "gente che arriva da fuori"), ("Pianura", "ci vivono 2 su 3"),
              ("16%", "italiani che vivono in Lombardia"), ("11%", "stranieri in Lombardia")),
            A(("Primario", "agricoltura 🌾"), ("Secondario", "industria 🏭"), ("Terziario", "servizi 🏦"),
              ("1%", "chi lavora nei campi"), ("68,6%", "chi lavora nei servizi")),
            A(("Pavia", "riso 🍚"), ("Sondrio", "centrali idroelettriche"), ("Milano", "Borsa Italiana"),
              ("Bormio", "turismo di montagna ⛷️"), ("Sirmione", "turismo sul lago")),
        ],
    },
    "clima": {
        "num": 4, "titolo": "Il clima",
        "quiz": [
            [Q("Il clima è…", "il tempo normale di un luogo, che si ripete ogni anno", "il tempo di oggi", "la temperatura di un giorno"),
             Q("La neve ad agosto in pianura sarebbe…", "un'eccezione", "normale", "un elemento del clima"),
             Q("Gli ELEMENTI del clima dicono…", "com'è il clima", "perché il clima è così", "dove piove"),
             Q("I FATTORI del clima dicono…", "perché il clima è così", "com'è il clima", "che ore sono"),
             Q("Quanti sono gli elementi climatici?", "8", "10", "3")],
            [Q("Se sali in montagna la temperatura…", "diminuisce", "aumenta", "resta uguale"),
             Q("Quale di questi è un ELEMENTO?", "la temperatura", "l'altitudine", "le correnti marine"),
             Q("Quale di questi è un FATTORE?", "l'altitudine", "le precipitazioni", "l'umidità"),
             Q("Il versante di una montagna esposto al sole si chiama…", "solatìo", "bacìo", "nivale"),
             Q("Un lago profondo rende il clima…", "più mite", "più freddo", "più secco")],
            [Q("Il clima di quasi tutta la Lombardia è…", "continentale", "mediterraneo", "tropicale"),
             Q("Il clima continentale ha estati…", "calde e afose", "fresche", "fredde con neve"),
             Q("Dove c'è il microclima mediterraneo?", "sulle rive dei grandi laghi", "sulle Alpi", "in mezzo alla pianura"),
             Q("Quale pianta cresce sulle rive del Garda?", "l'ulivo", "il pino mugo", "il muschio"),
             Q("Nel clima di alta montagna gli inverni sono…", "lunghi e freddissimi", "miti e corti", "caldi")],
        ],
        "vf": [
            [V("Il clima si ripete ogni anno in modo simile.", True, "Per esempio la nebbia torna ogni autunno."),
             V("Il clima è il tempo di un solo giorno.", False, "Quello è il tempo atmosferico; il clima è la media."),
             V("Gli elementi climatici sono 8.", True, "Temperatura, umidità, pressione, sole, precipitazioni..."),
             V("I fattori climatici sono 3.", False, "Sono 10."),
             V("La temperatura è un elemento del clima.", True, "Si misura, quindi è un elemento.")],
            [V("Più si sale, più fa freddo.", True, "È il fattore altitudine."),
             V("Più si va verso nord, più fa caldo.", False, "Fa più freddo: è il fattore latitudine."),
             V("Il versante in ombra si chiama bacìo.", True, "Quello al sole si chiama solatìo."),
             V("I boschi rendono il clima più umido.", True, "È il fattore copertura vegetale."),
             V("L'uomo non può cambiare il clima.", False, "Può: disboscamento, anidride carbonica.")],
            [V("La Lombardia ha tre climi diversi.", True, "Alta montagna, continentale, mediterraneo."),
             V("In pianura d'inverno c'è spesso la nebbia.", True, "È il clima continentale."),
             V("Il microclima mediterraneo è sulle Alpi.", False, "È sulle rive dei grandi laghi."),
             V("Sui laghi gli inverni sono miti.", True, "I laghi profondi scaldano l'aria."),
             V("In alta montagna le piante cambiano a fasce.", True, "Conifere, pascoli, muschi, ghiacciai.")],
        ],
        "abbina": [
            A(("Elementi", "com'è il clima"), ("Fattori", "perché è così"), ("Clima", "tempo normale che si ripete"),
              ("Stato medio", "adatto alla stagione"), ("Neve ad agosto", "un'eccezione ❄️")),
            A(("Altitudine", "salendo fa più freddo"), ("Latitudine", "verso nord fa più freddo"), ("Solatìo", "versante al sole ☀️"),
              ("Bacìo", "versante in ombra"), ("Lago profondo", "clima più mite")),
            A(("Alta montagna", "inverni lunghi e neve"), ("Continentale", "nebbia ed estati afose"), ("Mediterraneo", "ulivi sui laghi 🫒"),
              ("Conifere", "alberi con gli aghi"), ("Latifoglie", "alberi con foglie larghe")),
        ],
    },
    "carta": {
        "num": 5, "titolo": "La Lombardia sulla carta",
        "quiz": [
            [Q("Quali sono i tre gruppi delle Alpi lombarde?", "Lepontine, Retiche, Orobiche", "Marittime, Cozie, Graie", "Dolomiti, Carniche, Giulie"),
             Q("Dove sono le Alpi Orobiche?", "nel mezzo, sopra Bergamo", "in basso, sotto Pavia", "a sinistra, vicino al Piemonte"),
             Q("Quale montagna è nell'Appennino lombardo?", "il Monte Lesima", "il Bernina", "il Resegone"),
             Q("Grigna e Resegone sono vicino a…", "Lecco", "Mantova", "Pavia"),
             Q("Che cos'è un passo?", "il punto più basso per attraversare una montagna", "la cima più alta", "un lago di montagna")],
            [Q("Quale passo è nell'Appennino?", "il Penice", "lo Stelvio", "lo Spluga"),
             Q("Il passo all'angolo nord-est è…", "lo Stelvio", "il Penice", "la Presolana"),
             Q("Qual è la valle più lunga?", "la Valtellina", "la Val Sabbia", "la Val Cavallina"),
             Q("Nella Val Brembana scorre il…", "Brembo", "Serio", "Mincio"),
             Q("Nella Val Camonica scorre l'…", "Oglio", "Adda", "Ticino")],
            [Q("Il secondo nome del lago di Como è…", "Lario", "Benaco", "Verbano"),
             Q("Il Benaco è il lago…", "di Garda", "Maggiore", "d'Iseo"),
             Q("Brembo e Serio si gettano nell'…", "Adda", "Oglio", "Ticino"),
             Q("Quale fiume esce dal lago di Garda?", "il Mincio", "il Lambro", "l'Olona"),
             Q("Oltrepò vuol dire…", "oltre il Po: sotto il fiume", "sopra il lago", "vicino a Milano")],
        ],
        "vf": [
            [V("Le Alpi Lepontine sono in alto a sinistra.", True, "Ci trovi il Pizzo Stella."),
             V("L'Appennino è in alto, vicino alla Svizzera.", False, "È in basso, nella punta sotto Pavia."),
             V("Il Bernina è nelle Alpi Retiche.", True, "Lungo il confine nord."),
             V("Il Passo della Presolana è vicino al Pizzo della Presolana.", True, "Hanno lo stesso nome."),
             V("Lo Spluga è un fiume.", False, "È un passo, verso la Svizzera.")],
            [V("La Valtellina va da sinistra a destra.", True, "È la valle più lunga, in alto."),
             V("Nella Val Seriana scorre il Serio.", True, "Il nome te lo dice da solo."),
             V("La Val Cavallina è vicino al lago d'Endine.", True, "Guarda la carta delle valli."),
             V("I laghi della prof sono 13 perché ci sono 13 laghi.", False, "Sono 8 laghi più 5 secondi nomi."),
             V("Il lago d'Iseo si chiama anche Sebino.", True, "Come il Garda si chiama Benaco.")],
            [V("Il Po fa da confine in basso.", True, "Scorre da sinistra a destra."),
             V("Il Ticino esce dal lago di Como.", False, "Esce dal lago Maggiore. Dal lago di Como esce l'Adda."),
             V("Monza e Brianza è proprio sopra Milano.", True, "È la provincia più piccola."),
             V("La Lomellina è sotto il Po.", False, "È sopra il Po; sotto ci sono i due Oltrepò."),
             V("Le province lombarde sono 12.", True, "Sondrio è quella tutta di montagna.")],
        ],
        "abbina": [
            A(("Alpi Lepontine", "Pizzo Stella"), ("Alpi Retiche", "Bernina"), ("Alpi Orobiche", "Pizzo Coca"),
              ("Appennino", "Monte Lesima"), ("Lecco", "Grigna e Resegone")),
            A(("Val Brembana", "Brembo"), ("Val Seriana", "Serio"), ("Valtellina", "Adda"),
              ("Val Camonica", "Oglio"), ("Val Trompia", "Mella")),
            A(("Maggiore", "Verbano"), ("Lugano", "Ceresio"), ("Como", "Lario"),
              ("Iseo", "Sebino"), ("Garda", "Benaco")),
        ],
    },
}

for slug, m in MATTONCINI.items():
    dati = {k: m[k] for k in ("quiz", "vf", "abbina")}
    for k, livelli in dati.items():
        assert len(livelli) == 3 and all(len(x) == 5 for x in livelli), (slug, k)
    html = (MODELLO.replace("__TITOLO__", m["titolo"]).replace("__NUM__", str(m["num"]))
            .replace("__LEZIONE__", slug).replace("__DATI__", json.dumps(dati, ensure_ascii=False)))
    (RADICE / f"{slug}-allenamento.html").write_text(html, encoding="utf-8")
    print("scritto", f"{slug}-allenamento.html")
