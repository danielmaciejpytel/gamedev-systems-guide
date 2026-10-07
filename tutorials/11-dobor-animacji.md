# Tabele doboru animacji, wildcardy i fallback

## Problem
Ogólna reguła przechwytuje przypadek, dla którego przygotowano konkretny klip.

## Jawna polityka dopasowania
W tabeli typu „pierwszy pasujący wygrywa” kolejność jest częścią logiki:

```text
action      stance      clip
vault       crouched    vault_low
vault       *           vault_default
*           *           idle_safe
```

Umieść szczegółowe reguły przed ogólnymi. Alternatywnie oblicz ranking szczegółowości i zdefiniuj rozstrzyganie remisu. Nie mieszaj obu polityk przypadkowo.

## Schemat i fallback
Waliduj liczbę wejść i nazwane kolumny. Nie polegaj na komentarzu opisującym inną kolejność niż parser. Rozróżnij brak pasującej reguły, brak klipu i klip jeszcze niegotowy po streamingu.

Fallback może być wyborem platformy, alternatywą jakościową albo zasobem ratunkowym. Zapisz, kiedy jest wybierany. Jeśli wybór klipu następuje przy aktywacji węzła, zmiana wejść podczas Update nie wymusi automatycznie nowego wyszukania.

## Cache
Cache powinien znać generację bazy i zasobów. Po hot reload odśwież wynik lub jawnie wymagaj reaktywacji. W przeciwnym razie edytor pokazuje nową tabelę, a runtime korzysta ze starego wrappera.

## Sprawdź w grze
Przetestuj przesłoniętą regułę, złą liczbę wejść, brak zasobu oraz zmianę tabeli podczas działania. Debugger powinien pokazać wybrany wiersz i powód fallbacku.

---

[Spis treści](../README.md) · [Poprzedni tutorial](10-lokomocja.md) · [Następny tutorial](12-klipy-blend-i-zdarzenia.md)
