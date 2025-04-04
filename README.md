# Server Status Dashboard

Ein einfaches Dashboard zur Anzeige der Serverauslastung (CPU, RAM, Disk, Uptime) auf einer externen Website.

## 📦 Struktur

- `server/` – Python-Skript auf dem Heimserver
- `web/` – PHP-Empfänger & HTML-Dashboard auf Webhosting

## 🖥️ Server einrichten

1. Python-Pakete installieren:
    pip install psutil requests

2. `server_status_push.py` anpassen (URL deiner Website eintragen)

3. Starten:
    python3 server_status_push.py

Optional als systemd-Dienst einrichten.

## 🌐 Website einrichten

- `receive.php` und `dashboard.html` auf deinen Webspace kopieren
- Stelle sicher, dass `status.json` beschreibbar ist

Fertig! Alle 5 Sekunden werden aktuelle Werte auf deiner Website angezeigt.
