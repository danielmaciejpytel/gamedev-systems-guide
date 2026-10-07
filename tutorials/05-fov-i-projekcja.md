# FOV: poziomy, pionowy i zależny od ekranu

## Problem
Liczba wpisana w ustawieniach nie zawsze odpowiada liczbie oczekiwanej przez kamerę. Jedna może oznaczać FOV poziomy, druga pionowy.

Dla proporcji `aspect = width / height`:

```text
vertical = 2 * atan(tan(horizontal / 2) / aspect)
horizontal = 2 * atan(tan(vertical / 2) * aspect)
```

Funkcje trygonometryczne używają radianów. Dopiero wynik przelicz na stopnie. Nie dodawaj ukrytego offsetu do ustawienia użytkownika; jeśli projekt wymaga kalibracji, nazwij ją i wyjaśnij w konfiguracji.

## Implementacja
Ustal jedną konwencję wewnętrzną, np. pionowy FOV. Przyjmuj tylko skończone wartości w otwartym zakresie między 0 a 180 stopni i dodatnie proporcje obrazu. Zakres suwaka edytora nie chroni settera wywoływanego z kodu.

Przykład wykonywalny znajduje się w [camera_math.py](../examples/camera_math.py). Funkcja `horizontal_to_vertical` wykonuje przeliczenie i waliduje argumenty.

## Ciało i broń
Szerszy kadr może odsłaniać barki i ręce. Traktuj korektę pozycji kamery względem ciała jako osobny system z ograniczonym wpływem. Nie mieszaj ustawienia projekcji z przypadkowym przesunięciem transformacji. Osobna projekcja broni wymaga jawnej konfiguracji płaszczyzn i renderowania.

## Sprawdź w grze
Zmieniaj aspect ratio bez zmiany pionowego FOV, a potem bez zmiany poziomego FOV. Oba warianty zachowają inny fragment kadru. Sprawdź celowanie, widoczność ciała i clipping broni.

---

[Spis treści](../README.md) · [Poprzedni tutorial](04-miekkie-granice.md) · [Następny tutorial](06-blend-parametrow.md)
