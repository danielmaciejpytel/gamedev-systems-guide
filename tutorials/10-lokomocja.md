# Lokomocja: intencja, rzeczywisty ruch i faza kroku

## Dane wejściowe
Rozdziel prędkość żądaną, rzeczywistą i filtrowaną. Postać może chcieć sprintować, ale stać przy ścianie. Animacja oparta wyłącznie na intencji pokaże bieg w miejscu.

```text
horizontalSpeed = length(vec2(velocity.x, velocity.z))
verticalSpeed = velocity.y
desiredSpeed = inputMagnitude * selectedMaxSpeed
```

Przykład zakłada oś Y w górę. W innym silniku zmień adapter osi. Długość wektora 3D zawiera ruch pionowy; nie używaj jej bezrefleksyjnie do doboru chodu.

## Kierunek i kontekst
Wylicz kierunek ruchu względem facing. Dla wektora bliskiego zeru zachowaj poprzedni kierunek albo ustaw jawny stan idle, zamiast normalizować zero. Oddziel nachylenie podłoża, nachylenie ścieżki i krzywiznę zakrętu.

## Planowanie
Rozdziel start, pętlę i zatrzymanie. Przejście dobieraj również do fazy stopy, żeby uniknąć przeskoku podporowej nogi. Playback rate i skala przemieszczenia root motion to osobne parametry: szybsze odtwarzanie nie jest równoważne dłuższemu krokowi.

## Sprawdź w grze
Przetestuj ścianę, cofanie, strafe, schody, nagły stop i lądowanie. Loguj intencję oraz rzeczywistą prędkość. Dobra lokomocja wyraża decyzję gracza, a jednocześnie pasuje do ruchu fizycznego.

---

[Spis treści](../README.md) · [Poprzedni tutorial](09-rig-i-kontrakty-danych.md) · [Następny tutorial](11-dobor-animacji.md)
