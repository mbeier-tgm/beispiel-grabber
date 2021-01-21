# Beispiel Grabber

<details open="open">
  <summary>Inhaltsverzeichnis</summary>
  <ol>
    <li>
      <a href="#über-das-projekt">Über das Projekt</a></li>
    <li>
      <a href="#erste-schritte">Erste Schritte</a>
      <ul>
        <li><a href="#voraussetzungen">Voraussetzungen</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#verwendung">Verwendung</a></li>
    <li><a href="#lizenz">Lizenz</a></li>
  </ol>
</details>

## Über das Projekt

Der Beispiel Grabber ist ein Python-Script, welches alle Aufgaben der Angewandten Mathematik von [aufgabenpool.at](https://aufgabenpool.at) automatisch herunterladet. Aktuell sind die Beispiele als Ganzes nur schwer zu finden, da jedes einzelne über eine Suchanfrage gesucht werden muss und die Download-Funktion ermöglicht jeweils nur den Download von einzelnen Beispielangaben. Dieses Script hingegen durchläuft die hinterliegenden Dateistruktur, in der alle Beispiele inklusive Angaben-PDF aufgelistet sind, und ladet die betreffenden Dateien herunter.

## Erste Schritte

Um den Beispiel Grabber verwenden zu können, müssen folgende Schritte durchgeführt werden.

### Voraussetzungen

Als Vorraussetzung für das Deployment, die Installation und die Verwendung des Beispiel Grabbers muss Python 3.x installiert werden. Für mehr Informationen diesbezüglich, siehe [hier](https://www.python.org/downloads/).

### Installation

Das Deployment des Beispiel Grabbers und die Installation der benötigten Modules funktioniert wie folgt:

In der Bash und Zsh:
```bash
git clone https://github.com/mbeier-tgm/beispiel-grabber.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Verwendung

Um den Beispiel Grabber zu starten muss das Python Virtual Environment aktiviert werden. Aus dieser heraus kann das BeispielGrabber-Skript einfach gestartet werden. Abhängig von der benutzten Shell funktioniert die Verwendung wie folgt:

Bash und Zsh
```bash
source venv/bin/activate
python BeispielGrabber.py
```

Die Beispiele werden dann in den `./Beispiele/` - Ordner heruntergeladen.

Um das Virtual Environment wieder zu beenden, kann folgender Befehl verwendet werden:

```bash
deactivate
```

## Lizenz

Dieses Projekt ist unter der MIT Lizenz veröffentlicht (siehe [LICENSE](LICENSE)). 
