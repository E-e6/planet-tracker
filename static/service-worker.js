self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open("planet-tracker-cache").then((cache) => {
      return cache.addAll(["/", "/static/manifest.json", "/static/icons/icon-192.png"]);
    })
  );
  self.skipWaiting();
});

self.addEventListener("fetch", (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => response || fetch(e.request))
  );
});
