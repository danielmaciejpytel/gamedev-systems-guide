# Wygładzanie parametrów i częściowe aktualizacje

## Problem
Przejście FOV nigdy nie dociera do celu, bo setter w każdej klatce rozpoczyna je od nowa.

## Rozwiązanie
Rozpoczynaj przejście przy zmianie celu. Przechowuj wartość początkową, docelową, czas trwania i postęp. Dla zerowego czasu ustaw cel od razu.

```text
if requestedTarget != target:
    start = current
    target = requestedTarget
    elapsed = 0
t = clamp(elapsed / duration, 0, 1)
current = lerp(start, target, t * (2 - t))
```

Porównywanie floatów może wymagać tolerancji albo identyfikatora żądania. Jeśli cel naprawdę porusza się co klatkę, użyj filtra śledzącego, a nie nieustannie restartowanego przejścia o zadanym czasie.

## Dwie wagi
Złożenie `lerp(base, lerp(base, sceneValue, sceneWeight), overrideWeight)` daje `base + sceneWeight * overrideWeight * (sceneValue - base)`. Waga 0.5 w obu miejscach oznacza 0.25 całkowitego wpływu.

## Patch i reset
Zdarzenie z opcjonalnymi polami powinno zmieniać tylko przekazane wartości. Brak pola nie oznacza zera. Zdefiniuj oddzielne polecenie resetu i snapshot bazy. Rozróżnij zapis stanu, oznaczenie go jako zmienionego i przekazanie odbiorcy animacji.

## Sprawdź w grze
Powtarzaj identyczne żądanie przez sekundę, wyślij patch zawierający tylko zoom i przerwij przejście nowym celem. FOV powinien zachować się przewidywalnie.

---

[Spis treści](../README.md) · [Poprzedni tutorial](05-fov-i-projekcja.md) · [Następny tutorial](07-glebia-ostrosci.md)
