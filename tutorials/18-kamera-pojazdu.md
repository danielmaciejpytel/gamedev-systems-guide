# Kamera pojazdu: boom, autocenter i kolizje

## Model
Punkt obserwacji i ramię kamery rozdziel od finalnej pozycji po kolizji. Preset określa zamierzony dystans; geometria świata może go skrócić.

## Kolizja
Wykonaj sphere sweep od bezpiecznego punktu przy pojeździe do docelowej kamery. Odfiltruj własny pojazd. Uwzględnij osobno przypadek, w którym początek testu już znajduje się w przeszkodzie.

```text
allowedDistance = collisionQuery(pivot, desiredPosition, probeRadius)
if allowedDistance < currentDistance:
    currentDistance = allowedDistance
else:
    currentDistance = follow(currentDistance, allowedDistance, returnRate, dt)
```

Natychmiastowe skracanie chroni przed przejściem przez ścianę. Wygładzony powrót ogranicza pompowanie kamery. Sweep i overlap mogą mieć różne promienie, bo odpowiadają na inne pytania; nazwij je osobno.

## Autocenter
Po ręcznym ruchu odczekaj określony czas. Potem zwiększaj siłę centrowania wraz z prędkością pojazdu. Osobne ustawienia dla myszy i gamepada pomagają uzyskać oczekiwane odczucie. Obrót yaw pojazdu nie musi oznaczać kopiowania pitch i roll.

## Sprawdź w grze
Cofaj przy ścianie, przejedź pod mostem, minąć słup i skacz z rampy. Sprawdź, czy kolizja skraca ramię od razu, a wyjazd z przeszkody nie powoduje nagłego odsunięcia.

---

[Spis treści](../README.md) · [Poprzedni tutorial](17-sceny-i-przejecie-kontroli.md) · [Następny tutorial](19-perspektywy-i-proxy.md)
