# Wejście, pauza i różne zegary

## Problem
Ta sama czułość zachowuje się inaczej przy niskim FPS, slow motion i pauzie.

## Rozdziel jednostki
Mysz zwykle dostarcza przemieszczenie zebrane między klatkami. Drążek opisuje wychylenie, które zamieniasz na prędkość kątową. Nie mnoż delty myszy przez czas ponownie, jeśli backend już dostarczył przemieszczenie.

```text
mouseAngle = mouseDelta * degreesPerMouseUnit
stickAngle = stickAxis * degreesPerSecond * realDt
simulationDt = realDt * timeScale
```

Zegar rzeczywisty pasuje do reakcji interfejsu i sterowania podczas spowolnienia. Zegar symulacji pasuje do ruchu świata. To decyzja projektowa: podczas pauzy możesz zablokować gameplay, ale nadal pozwalać obracać kamerę podglądu.

Przed obliczeniem prędkości `angleDelta / dt` obsłuż `dt <= epsilon`. Nie zastępuj każdego zera sztucznym krokiem bez zastanowienia: może to wygenerować ogromną prędkość. Wybierz pominięcie aktualizacji albo zachowanie poprzedniej wartości.

## Kolejność ma znaczenie
Zapisz pipeline: filtr urządzenia, wspomaganie celowania, look-at, odrzut, ograniczenia, finalna orientacja. Rozróżnij korektę dodawaną do wejścia od przejęcia sterowania, które usuwa wejście użytkownika.

## Sprawdź w grze
Odtwórz tę samą sekwencję wejścia przy 30, 60 i 144 FPS, w pauzie oraz przy `timeScale = 0.25`. Porównaj końcowy kąt, a także opóźnienie reakcji. Jednostki każdego parametru zapisz przy jego definicji.

---

[Spis treści](../README.md) · [Poprzedni tutorial](01-wlasnosc-kamery.md) · [Następny tutorial](03-katy-limity-i-resety.md)
