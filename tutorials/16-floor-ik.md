# Floor IK i stabilny kontakt z podłożem

## Pipeline
Najpierw próbkuj animację bazową, potem wykryj podłoże, dopasuj miednicę i na końcu rozwiąż IK nóg. Ustal, czy trace korzysta z pozy przed korektą czy po niej, aby uniknąć sprzężenia zwrotnego.

```text
baseFeet = animatedPose.feet
contacts = traceGround(baseFeet)
pelvisOffset = limitedPelvisCorrection(contacts)
pose = applyPelvisOffset(animatedPose, pelvisOffset)
pose = solveTwoBoneLegs(pose, contacts)
```

## Kontakt
Normalna powierzchni wyznacza orientację stopy, ale ogranicz maksymalny przechył. Wygładzaj wejście i wyjście kontaktu. Blokuj stopę podporową względem podłoża; na ruchomej platformie przechowuj punkt w przestrzeni tej platformy.

Miednica powinna pomagać obu nogom. Ogranicz pionowy offset i rozciąganie kończyny. Nie traktuj każdego trafienia trace jako odpowiedniego podłoża: sprawdź warstwę, nachylenie i zasięg.

## Odporność
Waliduj kości, długości segmentów oraz kierunek zgięcia. Brak trafienia powinien zmniejszać wagę IK. Teleport resetuje cache kontaktu. Przy niskim LOD można ograniczyć częstotliwość trace, zachowując płynne wygaszanie.

## Sprawdź w grze
Przejdź po schodach, krawędzi, pochyłości i ruchomej platformie. Testuj lądowanie i utratę podłoża. Rysuj trace, punkt kontaktu, normalną i końcowy cel IK.

---

[Spis treści](../README.md) · [Poprzedni tutorial](15-root-motion-i-korekta-kroku.md) · [Następny tutorial](17-sceny-i-przejecie-kontroli.md)
