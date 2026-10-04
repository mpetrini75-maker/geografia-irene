const CACHE = 'geografia-irene-v5';

const ASSETS = [
  './',
  './alert.js',
  './allenamento.js',
  './app.js',
  './carta.html',
  './carta-allenamento.html',
  './clima.html',
  './clima-allenamento.html',
  './economia.html',
  './economia-allenamento.html',
  './icon-180.png',
  './icon-192.png',
  './icon-512.png',
  './img/carta/fisica-muta.jpg',
  './img/carta/fiumi.jpg',
  './img/carta/laghi.jpg',
  './img/carta/passi.jpg',
  './img/carta/politica-muta-colori.jpg',
  './img/carta/politica-muta.jpg',
  './img/carta/province.jpg',
  './img/carta/rilievi.jpg',
  './img/carta/subregioni.jpg',
  './img/carta/valli.jpg',
  './img/clima-carta.jpg',
  './img/clima-schema.jpg',
  './img/eco-p01.jpg',
  './img/eco-p02.jpg',
  './img/eco-p03.jpg',
  './img/eco-p04.jpg',
  './img/eco-p05.jpg',
  './img/eco-p06.jpg',
  './img/eco-p07.jpg',
  './img/industria-carta-gruppo.jpg',
  './img/lombardia-acque.jpg',
  './img/lombardia-alpi.jpg',
  './img/lombardia-fasce.jpg',
  './img/lombardia-province.jpg',
  './img/storia/p03.jpg',
  './img/storia/p06.jpg',
  './img/storia/p07.jpg',
  './img/storia/p08.jpg',
  './img/storia/p09.jpg',
  './img/storia/p10.jpg',
  './img/storia/p12.jpg',
  './img/storia/p16.jpg',
  './img/storia/p17.jpg',
  './img/storia/p18.jpg',
  './img/storia/p19.jpg',
  './img/storia/p20.jpg',
  './img/storia/p22.jpg',
  './img/storia/p23.jpg',
  './img/storia/p25.jpg',
  './img/storia/p26.jpg',
  './img/storia/p30.jpg',
  './index.html',
  './lombardia.html',
  './lombardia-allenamento.html',
  './manifest.json',
  './storia.html',
  './storia-allenamento.html',
  './style.css',
];

// Installazione: pre-carica tutte le pagine locali
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

// Attivazione: elimina le cache vecchie
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: cache-first per i font Google, network-first per le pagine HTML,
// stale-while-revalidate per il resto.
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);

  // Font Google: cache-first (raramente cambiano)
  if (url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    e.respondWith(
      caches.open(CACHE).then(cache =>
        cache.match(e.request).then(cached => {
          const network = fetch(e.request).then(res => {
            cache.put(e.request, res.clone());
            return res;
          });
          return cached || network;
        })
      )
    );
    return;
  }

  // Pagine HTML: network-first → prende sempre l'ultima versione se online,
  // ricade sulla cache solo offline. Evita di servire codice vecchio.
  const isHTML = e.request.mode === "navigate" || url.pathname.endsWith(".html") || url.pathname.endsWith("/");
  if (url.origin === self.location.origin && isHTML) {
    e.respondWith(
      caches.open(CACHE).then(cache =>
        fetch(e.request).then(res => {
          cache.put(e.request, res.clone());
          return res;
        }).catch(() => cache.match(e.request))
      )
    );
    return;
  }

  // Altre risorse locali (immagini, css, js): stale-while-revalidate
  if (url.origin === self.location.origin) {
    e.respondWith(
      caches.open(CACHE).then(cache =>
        cache.match(e.request).then(cached => {
          const network = fetch(e.request).then(res => {
            cache.put(e.request, res.clone());
            return res;
          }).catch(() => {});
          return cached || network;
        })
      )
    );
  }
});
