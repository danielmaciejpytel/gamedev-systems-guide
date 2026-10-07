# Konfiguracja, cache i dowody poprawnego działania

## Konfiguracja
Zestaw parametrów może być buforowany. Ponowne wybranie tej samej nazwy nie musi odświeżyć danych. Użyj identyfikatora generacji albo jawnego `reload`, a brak zestawu obsłuż opisanym błędem lub presetem bazowym.

```text
if active.name != requested.name or active.revision != requested.revision:
    validate(requested)
    active = buildRuntimeParameters(requested)
```

Zdefiniuj jednostki, zakresy i wartości domyślne. Waga użyta jako próg logiczny nie jest płynnym blendem. Jeżeli pole ma zachowywać się binarnie, użyj nazwy i typu opisujących przełącznik.

## Debugger
Pokazuj intencję wejścia, stan przed ograniczeniami, wkłady proceduralne, aktywny preset, właściciela i wynik dla renderera. Odczyt pola lub obecność settera nie dowodzi, że końcowy solver go używa. Prześledź drogę aż do konsumenta.

## Plan weryfikacji
Sprawdź walidację danych, testy matematyki, integrację grafu i zachowanie runtime. Zielony test funkcji przeliczającej FOV nie potwierdza komfortu kamery w gotowej scenie.

Testuj pauzę, skrajne kroki czasu, brak zasobów, zmianę riga, teleport oraz przerwanie przejścia. Powtarzaj scenariusze na docelowej platformie i w konfiguracji wydania. Funkcje debugowe oraz komentarze nie stanowią dowodu działania funkcji w buildzie gracza.

## Ćwiczenie końcowe
Zbuduj małą scenę: postać, schody, pojazd i krótka scena dialogowa. Połącz mechanizmy z poprzednich rozdziałów. Zapisz oczekiwane zachowanie i porównaj je z nagraniem oraz logiem aktywnych systemów.

---

[Spis treści](../README.md) · [Poprzedni tutorial](19-perspektywy-i-proxy.md)
