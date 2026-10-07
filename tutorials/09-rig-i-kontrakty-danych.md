# Rig, refleksja i stabilne kontrakty

## Problem
Zmiana nazwy kości lub pola może zerwać graf, nawet jeśli typ danych i wygląd modelu pozostają takie same.

## Waliduj przed użyciem
Przykładowy solver wymaga kości `ViewPivot`, `ChestAnchor`, `ViewAim` i `MotionRoot`. Sprawdź istnienie wszystkich indeksów przed odczytem rodziców. Dopiero potem zweryfikuj relację `ViewAim -> ViewPivot -> ChestAnchor`.

```text
indices = resolveRequiredBones(rig)
if anyMissing(indices):
    return DisabledSolver("missing bone")
if parent(indices.viewAim) != indices.viewPivot:
    return DisabledSolver("invalid hierarchy")
```

Stan błędu musi blokować zarówno aktualizację, jak i próbkowanie. Samo pole `initialized = false` nie zapewnia ochrony, jeśli nikt go nie odczytuje.

## API i serializacja
Metoda publiczna w języku natywnym nie musi być dostępna w skryptach. Refleksja, widoczność w edytorze i uprawnienie do zapisu to osobne kontrakty. Rejestruj API świadomie, a przy zmianie nazw dodaj migrację zapisanych grafów i danych.

Inicjalizuj każde pole pakietu animacji. Asercje pomagają w development, ale walidacja wejścia runtime powinna działać niezależnie od konfiguracji kompilacji.

## Sprawdź w grze
Usuń wymaganą kość, podmień rodzica i wczytaj starszy asset. Oczekuj czytelnego komunikatu oraz bezpiecznej pozy zastępczej. Nie oczekuj, że identyczny układ pamięci naprawi niezgodne nazwy.

---

[Spis treści](../README.md) · [Poprzedni tutorial](08-warstwy-ruchu-kamery.md) · [Następny tutorial](10-lokomocja.md)
