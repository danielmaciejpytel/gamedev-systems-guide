# Root motion, dopasowanie celu i długość kroku

## Rozdziel ruch bazowy i korektę
Wyciągnij root motion z klipu, przelicz go do świata, a potem policz oddzielną korektę do celu. Dzięki temu możesz ograniczyć korektę bez niszczenia charakteru animacji.

```text
animatedDeltaWorld = actorRotation * animatedDeltaLocal
correction = clampLength(targetError, correctionSpeed * dt)
proposedDelta = animatedDeltaWorld + correction
actualDelta = characterCollision.solve(proposedDelta)
```

To pseudokod przemieszczenia; rotację składaj właściwą operacją na transformacjach. Po kolizji użyj rzeczywistego ruchu do dalszego dopasowania stóp.

## Skala kroku
Stosunek długości ruchu rzeczywistego do animowanego pomaga dobrać korektę kroku. Dla małego mianownika użyj jawnego fallbacku, zamiast dzielić przez niemal zero. Ogranicz wynik do rozsądnego zakresu i uwzględnij nogę podporową.

Skalowanie XYZ zmienia również ruch pionowy. Jeśli projekt wymaga wyłącznie zmiany długości kroku na podłożu, skaluj składowe poziome oddzielnie. Playback rate reguluj osobno.

## Cel zdarzeniowy
Dopasowanie do kontaktu, np. dłoni z uchwytem, potrzebuje czasu do konkretnego znacznika. Brak znacznika powinien wyłączyć korektę lub użyć opisanej polityki zastępczej. Zero nie powinno udawać poprawnie znalezionego eventu.

## Sprawdź w grze
Podejdź do celu na różnych dystansach, zablokuj ruch kolizją i usuń znacznik kontaktu. Obserwuj ślizganie stóp, przeskok root i zgodność momentu kontaktu.

---

[Spis treści](../README.md) · [Poprzedni tutorial](14-damping-i-sprezyny.md) · [Następny tutorial](16-floor-ik.md)
