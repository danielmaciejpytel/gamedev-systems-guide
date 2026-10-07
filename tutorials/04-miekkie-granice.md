# Miękkie granice obrotu i powrót do środka

## Cel
Twardy clamp nagle zatrzymuje kamerę. Miękka strefa wcześniej osłabia ruch na zewnątrz i może sprężyście sprowadzać widok do dozwolonego zakresu.

```text
distanceToEdge = maxYaw - yaw
outwardScale = smoothstep(0, softMargin, distanceToEdge)
if inputYaw > 0:
    inputYaw *= outwardScale
```

`smoothstep` jest tutaj pedagogicznym wyborem krzywej. Symetrycznie obsłuż lewą granicę. Ruch do środka powinien pozostać responsywny. Szerokość strefy ogranicz do połowy dostępnego zakresu; przy zerowym zakresie zablokuj oś bez dzielenia przez zero.

Oddziel trzy rzeczy: limit kąta, tłumienie wejścia i prędkość powrotu. Dzięki temu projektant może uzyskać miękkie zatrzymanie bez silnego autocentrowania. Gdy zmieniasz limity w locie, wygładzaj je i uwzględnij sytuację, w której bieżący kąt znajduje się poza nowym zakresem.

## Proporcje ekranu
Zmiana aspect ratio zmienia widoczny obszar. Jeśli zakres patrzenia ma chronić kadr sceny, oblicz go z rzeczywistej projekcji. Przybliżenie poziomego FOV przez `verticalFov * aspect` nie jest dokładnym przeliczeniem perspektywy.

## Sprawdź w grze
Przytrzymaj drążek na granicy, odwróć kierunek i zawęź zakres podczas ruchu. Porównaj 16:9 z szerokim ekranem. Oceń odczucie sterowania oraz kadrowanie.

---

[Spis treści](../README.md) · [Poprzedni tutorial](03-katy-limity-i-resety.md) · [Następny tutorial](05-fov-i-projekcja.md)
