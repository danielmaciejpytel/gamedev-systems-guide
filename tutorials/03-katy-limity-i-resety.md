# Kąty, korekty i resety bez niespodzianek

## Model
Utrzymuj oddzielnie kąt gracza i kąt korekty. Nazwij wynik `finalYaw`, żeby odbiorca nie dodał korekty drugi raz.

```text
playerYaw = clamp(wrap(playerYaw + inputYaw), minYaw, maxYaw)
correctionYaw += externalYaw
finalYaw = playerYaw + correctionYaw
```

Ten model ogranicza wejście, ale pozwala korekcie wyjść poza zakres. Jeśli potrzebujesz bezwzględnej granicy bezpieczeństwa, ogranicz również sumę. Zdecyduj świadomie, czy nadpisanie orientacji omija zwykłe limity.

## Reset proporcjonalny
Reset `x *= max(0, 1 - speed * dt)` zwalnia blisko zera. Stała prędkość `moveTowards(x, 0, degreesPerSecond * dt)` daje inną odpowiedź. Wariant wykładniczy `x *= exp(-speed * dt)` zachowuje ten sam współczynnik zaniku przy różnych krokach czasu. Ustal mały próg kończący reset, jeśli potrzebujesz dokładnego zera.

## Polecenia jednej klatki
Jeśli orientację można wymusić tylko raz w klatce, określ regułę: pierwsze żądanie, ostatnie żądanie albo najwyższy priorytet. Nie ukrywaj jej w przypadkowej kolejności wywołań. Zbierz żądania i rozstrzygnij je przed aktualizacją pozy.

## Sprawdź w grze
Podaj korektę przekraczającą zakres, wykonaj reset przy aktywnym wejściu i zgłoś dwa wymuszenia w jednej klatce. Obserwuj oddzielnie kąt gracza, korektę i wynik. Testuj przejście przez -180/180 stopni.

---

[Spis treści](../README.md) · [Poprzedni tutorial](02-wejscie-i-czas.md) · [Następny tutorial](04-miekkie-granice.md)
