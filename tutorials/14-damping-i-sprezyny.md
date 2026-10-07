# Damping, interpolacja i sprężyny

## Dobierz mechanizm do celu
Lerp o stałej wadze na klatkę zmienia odpowiedź wraz z FPS. Damping wykładniczy używa:

```text
alpha = 1 - exp(-response * dt)
value += (target - value) * alpha
```

Stałe tempo ogranicza maksymalną zmianę na sekundę. Sprężyna przechowuje również prędkość i może dawać bezwładność lub oscylacje. Te mechanizmy nie są zamienne.

## Sprężyna
Przykładowy integrator półjawny:

```text
acceleration = (stiffness * (target - value) - damping * velocity) / mass
velocity += acceleration * step
value += velocity * step
```

Wymagaj dodatniej masy oraz nieujemnego tłumienia i sztywności. Rozbijaj duży `dt` na małe podkroki, ale ogranicz koszt przy zacięciu klatki. Parametry i metoda integracji wspólnie decydują o stabilności. Krytyczne tłumienie ciągłego modelu wynosi `2 * sqrt(stiffness * mass)`; dyskretny integrator nadal wymaga sprawdzenia.

## Kąty
Wybieraj najkrótszą różnicę kątową przez wrap do przedziału wokół zera. Dla kwaternionów używaj interpolacji rotacji i pamiętaj, że `q` oraz `-q` opisują tę samą orientację.

## Sprawdź w grze
Wykonaj skok celu, sinusoidalny ruch i zacięcie klatki. Porównaj czas dojścia i przeregulowanie przy różnych FPS. Funkcja `exponential_follow` jest w przykładzie Python.

---

[Spis treści](../README.md) · [Poprzedni tutorial](13-maszyna-stanow-i-inercja.md) · [Następny tutorial](15-root-motion-i-korekta-kroku.md)
