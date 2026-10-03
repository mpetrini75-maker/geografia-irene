/* Geografia di Irene — utilità condivise */
function toggleSol(id, btn){
  var el = document.getElementById(id);
  if(!el) return;
  var open = el.classList.toggle("open");
  if(btn) btn.textContent = open ? "🙈 Nascondi soluzioni" : "🔑 Mostra soluzioni";
}

/* 🔊 Ascolta: ogni riquadro con un titolo si può far leggere a voce.
   Irene impara meglio ascoltando che leggendo (profilo DSA): il tasto è su ogni card. */
(function(){
  if(!("speechSynthesis" in window)) return;
  var attivo = null;

  function voceItaliana(){
    var voci = speechSynthesis.getVoices().filter(function(v){ return /^it/i.test(v.lang); });
    return voci.find(function(v){ return /google|natural|neural|alice|elsa|federica/i.test(v.name); }) || voci[0] || null;
  }

  function testoDa(card){
    var copia = card.cloneNode(true);
    copia.querySelectorAll(".ascolta, .solbtn, .sol, script, figure, pre").forEach(function(n){ n.remove(); });
    return copia.innerText.replace(/[\u{1F300}-\u{1FAFF}☀-➿]/gu, " ").replace(/\s+/g, " ").trim();
  }

  function ferma(){
    speechSynthesis.cancel();
    if(attivo){ attivo.classList.remove("on"); attivo.textContent = "🔊 Ascolta"; attivo = null; }
  }

  function parla(btn, card){
    if(attivo === btn){ ferma(); return; }
    ferma();
    var u = new SpeechSynthesisUtterance(testoDa(card));
    u.lang = "it-IT"; u.rate = 0.95;
    var v = voceItaliana(); if(v) u.voice = v;
    u.onend = u.onerror = function(){ if(attivo === btn) ferma(); };
    attivo = btn; btn.classList.add("on"); btn.textContent = "⏹ Ferma";
    speechSynthesis.speak(u);
  }

  function aggiungi(){
    document.querySelectorAll(".card h2").forEach(function(h){
      var card = h.closest(".card");
      if(!card || card.hasAttribute("data-no-voce")) return;
      var b = document.createElement("button");
      b.className = "ascolta"; b.type = "button"; b.textContent = "🔊 Ascolta";
      b.addEventListener("click", function(){ parla(b, card); });
      h.parentNode.insertBefore(b, h);
    });
  }
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", aggiungi); else aggiungi();
  window.addEventListener("pagehide", ferma);
})();
