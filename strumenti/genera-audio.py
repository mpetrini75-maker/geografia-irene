r"""Registra con una voce naturale (edge-tts, neurale) il testo di ogni riquadro delle lezioni.
Marco, 03/10/2026: la sintesi vocale del telefono era "estremamente robotica".
Ogni riquadro con un titolo <h2> diventa audio/<pagina>-<n>.mp3 (n = ordine dei titoli nella pagina,
lo stesso che usa app.js per il tasto Ascolta). Si rilancia dopo ogni modifica al testo di una lezione.
Uso:  py strumenti\genera-audio.py            (rifa' solo gli audio il cui testo e' cambiato)
      py strumenti\genera-audio.py --tutto    (li rifa' tutti)
"""
import asyncio, hashlib, json, re, sys
from pathlib import Path
from bs4 import BeautifulSoup
import edge_tts

R = Path(__file__).resolve().parent.parent
AUDIO = R / "audio"
VOCE = "it-IT-ElsaNeural"   # provino "tre" scelto da Marco il 03/10: piu' veloce e piu' acuta, da ragazzina sveglia
RATE, PITCH = "+0%", "+15Hz"   # era +20%: Marco il 04/10 "troppo veloce", rallentata come in Tedesco
LEZIONI = ["lombardia", "storia", "economia", "clima", "carta", "piano-lombardia"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️‍]")


def testo_card(card):
    for n in card.select(".solbtn, .sol, script, figure, pre, button"):
        n.decompose()
    for td in card.select("td, th"):          # le celle di tabella si leggono separate
        td.append(". ")
    for li in card.select("li"):
        li.append(". ")
    t = card.get_text(" ")
    t = EMOJI.sub(" ", t)
    t = t.replace("km²", "chilometri quadrati").replace("m²", "metri quadrati").replace("–", " - ")
    t = re.sub(r"\s*\.\s*(\.\s*)+", ". ", t)
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"^\.\s*", "", t)
    return t


async def main():
    tutto = "--tutto" in sys.argv
    AUDIO.mkdir(exist_ok=True)
    indice_f = AUDIO / "indice.json"
    vecchio = json.loads(indice_f.read_text(encoding="utf-8")) if indice_f.exists() else {}
    nuovo = {}
    fatti = saltati = 0
    for slug in LEZIONI:
        soup = BeautifulSoup((R / f"{slug}.html").read_text(encoding="utf-8"), "html.parser")
        cards = [h.find_parent(class_="card") for h in soup.select(".card h2")]
        for i, card in enumerate(cards):
            if card.has_attr("data-no-voce"):
                continue
            testo = testo_card(card)
            nome = f"{slug}-{i}.mp3"
            impronta = hashlib.sha1((VOCE + RATE + PITCH + testo).encode()).hexdigest()
            nuovo[nome] = impronta
            if not tutto and vecchio.get(nome) == impronta and (AUDIO / nome).exists():
                saltati += 1
                continue
            await edge_tts.Communicate(testo, VOCE, rate=RATE, pitch=PITCH).save(str(AUDIO / nome))
            fatti += 1
            print(f"  {nome}: {len(testo)} caratteri")
    for f in AUDIO.glob("*.mp3"):
        if f.name not in nuovo:
            f.unlink()
            print("  tolto", f.name)
    indice_f.write_text(json.dumps(nuovo, indent=1), encoding="utf-8")
    print(f"audio registrati: {fatti} · gia' a posto: {saltati} · totale: {len(nuovo)}")

asyncio.run(main())
