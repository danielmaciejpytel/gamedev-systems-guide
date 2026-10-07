# Maszyna stanów i płynne przejścia przez inercję

## Reguły stanów
Określ stan domyślny, priorytety przejść oraz to, czy przejście globalne może przerwać lokalne. Zdarzenia enter/exit powinny wystąpić dokładnie raz. Zabezpiecz pętlę przejść w jednej klatce.

## Inercjalizacja
Zwykły crossfade liczy dwie pozy i miesza je. Inercjalizacja przełącza się na nową animację i wygasza różnicę od poprzedniego ruchu, uwzględniając również jego prędkość.

```text
outputPose = newPose + decayingOffset
```

To zapis koncepcyjny: rotacje wymagają reprezentacji delta quaternion albo osi i kąta, a nie dodawania macierzy. Zachowaj historię poprzednich próbek, wylicz błąd i prędkość, a następnie wygaszaj je funkcją o gładkim zakończeniu. Prosty lerp nie zachowuje tej samej ciągłości prędkości.

## Cykl życia
Teleport powinien zresetować historię, żeby stara poza nie „ciągnęła” postaci do poprzedniego miejsca. Ragdoll i zmiana riga wymagają osobnej polityki. Przy ograniczeniu LOD pamiętaj, że aktywny efekt może potrzebować aktualizacji mimo zwykłego pomijania animacji.

Zerowy czas przejścia w maszynie stanów nie musi oznaczać skoku wizualnego, jeśli wygładzanie realizuje następny etap.

## Sprawdź w grze
Przerywaj start biegu zatrzymaniem, wykonaj teleport w trakcie przejścia i zmień LOD. Oceniaj nie tylko pozycję, ale również skoki prędkości kończyn.

---

[Spis treści](../README.md) · [Poprzedni tutorial](12-klipy-blend-i-zdarzenia.md) · [Następny tutorial](14-damping-i-sprezyny.md)
