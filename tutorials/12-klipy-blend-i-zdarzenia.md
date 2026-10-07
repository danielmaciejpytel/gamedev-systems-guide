# Odtwarzanie klipów, blend i zdarzenia

## Przycinanie czasu
Po przycięciu początku i końca klipu efektywna długość wynosi `max(0, duration - trimStart - trimEnd)`. Zdarzenia próbkuj w tym samym przekształconym przedziale, którego używasz do pozy. Wznowienie i restart mają różne znaczenie.

## Poza i events
Blend pozy można zapisać jako `blend(A, B, weight)`, ale dźwięków kroków nie należy bezmyślnie emitować z obu klipów. Jedna prosta polityka wybiera events A przy wadze poniżej 0.5, a B w przeciwnym razie. Inna synchronizuje wspólne znaczniki i usuwa duplikaty.

## Faza
Klipsy o różnych długościach mogą dzielić znormalizowaną fazę:

```text
timeA = phase * durationA
timeB = phase * durationB
```

W blend space wagi mogą pochodzić z interpolacji barycentrycznej. Waliduj duplikaty punktów i zerowe zakresy osi. Brak próbki powinien mieć jawny wynik: poza referencyjna dla zwykłej animacji, neutralna delta dla additive.

## Additive
Additive opisuje różnicę względem pozy bazowej. Zdefiniuj pozę odniesienia i przestrzeń rotacji; zwykły klip nie staje się poprawną deltą wyłącznie przez zmianę flagi.

## Sprawdź w grze
Blenduj chód i bieg o różnych długościach. Nasłuchuj podwójnych kroków przy przejściu przez 0.5. Testuj pętlę, seek i duży krok czasu obejmujący koniec klipu.

---

[Spis treści](../README.md) · [Poprzedni tutorial](11-dobor-animacji.md) · [Następny tutorial](13-maszyna-stanow-i-inercja.md)
