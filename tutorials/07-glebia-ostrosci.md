# Głębia ostrości i dynamiczny cel

## Kontrakt
Przechowuj granice w jednej jednostce świata i pilnuj relacji:

```text
0 <= nearBlur <= nearFocus <= farFocus <= farBlur
```

Nazwy oznaczają odpowiednio koniec pełnego bliskiego rozmycia, początek ostrego zakresu, koniec ostrego zakresu i początek pełnego dalekiego rozmycia. Definicja zależy od renderera, więc dopasuj adapter.

## Cel ruchomy
Oblicz odległość celu od kamery. Następnie zbuduj zakres z offsetów:

```text
d = length(targetPosition - cameraPosition)
nearBlur  = max(0, d - outerNearOffset)
nearFocus = max(0, d - innerNearOffset)
farFocus  = d + innerFarOffset
farBlur   = d + outerFarOffset
```

Waliduj porządek offsetów i skończoność wartości. Zdecyduj, czy używasz dystansu euklidesowego, czy głębokości w osi widoku; renderer może oczekiwać drugiej konwencji.

## Brak celu
Provider może utracić aktora, slot albo komponent podczas streamingu. Zwróć jawny brak wyniku. Polityka kamery może zachować ostatni zakres, wygasić DOF albo przejść na bazowe ustawienia. Nie wybieraj przypadkowego celu.

## Sprawdź w grze
Przesuwaj cel przez kamerę, usuń go w trakcie sceny i ustaw odległość bliską zeru. Sprawdź brak skoków oraz zgodność jednostek. W [camera_math.py](../examples/camera_math.py) jest funkcja budująca uporządkowany zakres.

---

[Spis treści](../README.md) · [Poprzedni tutorial](06-blend-parametrow.md) · [Następny tutorial](08-warstwy-ruchu-kamery.md)
