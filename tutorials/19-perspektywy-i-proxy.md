# Przełączanie perspektywy i blend pełnego widoku

## Stany
Rozróżnij perspektywę żądaną, docelową i faktycznie aktywną. Zmiana może czekać na zasób, zakończenie sceny albo widoczność modelu postaci.

```text
requestedMode -> policy -> targetMode -> readiness -> activeMode
```

## Proxy
Na czas przejścia aktywuj widok pośredni. Interpoluj pozycję, rotację przez Slerp i jawnie wybrane parametry optyczne. Proxy mieszające tylko transformację nie zapewnia automatycznie blendu FOV czy DOF.

Kiedy gracz odwraca przejście, użyj aktualnego wyniku jako początku nowego blendu. Nie wracaj do starej pozy początkowej. Zadbaj o brak obu uczestników albo utratę jednego z nich. Kolizję sprawdzaj również dla pośredniej pozycji, żeby tor kamery nie przecinał karoserii.

## Reprezentacja postaci
Kamera pierwszoosobowa może ukrywać głowę, a trzecioosobowa jej potrzebować. Przygotuj reprezentację przed aktywacją widoku. Po powrocie ukryj ją w odpowiednim momencie przejścia.

## Typ czasu
```cpp
const float transitionSeconds = enteringFirstPerson ? 0.0f : configuredSeconds;
```

Zapis czasu do `bool` sprowadzi każdą niezerową wartość do prawdy. Po konwersji z powrotem otrzymasz 1 zamiast np. 0.3. Używaj nazw z jednostką i włącz ostrzeżenia konwersji.

## Sprawdź w grze
Przełączaj tryb szybko, podczas streamingu i tuż przy pojeździe. Śledź aktywny widok, optykę oraz widoczność głowy.

---

[Spis treści](../README.md) · [Poprzedni tutorial](18-kamera-pojazdu.md) · [Następny tutorial](20-konfiguracja-i-debugowanie.md)
