# Sceny, kolejki żądań i oddawanie sterowania

## Problem
Po scenie zostaje zmieniony FOV albo zablokowane patrzenie. Przejęcie kamery nie ma kompletnego cyklu życia.

## Transakcja sterowania
Na wejściu zapisz stan bazy: właściciel widoku, optyka, ograniczenia, wagi proceduralne i blokady. Przejęcie ma identyfikator, żeby stary koniec sceny nie zwolnił blokady należącej do nowszej sceny.

```text
token = director.acquire(ScenePriority)
snapshot = captureViewState()
playScene(token)
blendBackToGameplay(token, snapshot)
director.release(token)
```

Snapshot nie musi przywracać każdej starej wartości bezwarunkowo. Ustawienie komfortu zmienione przez gracza podczas sceny powinno zwykle przetrwać. Określ, które pola są własnością sceny, a które użytkownika.

## Kolejka i streaming
Żądanie aktywacji nie oznacza natychmiast gotowej kamery. Przetwarzaj kolejkę w ustalonym etapie klatki. Deduplikuj żądania i zapewnij anulowanie, limit oczekiwania oraz retry dla zasobów jeszcze niegotowych.

Blokada zmian powinna jasno określać, czy dotyczy aktywacji, optyki i ruchu. Markowanie cięcia jest osobną decyzją, która może resetować historię renderera.

## Sprawdź w grze
Przerwij scenę, wykonaj seek, wyłącz aktora po streamingu i uruchom drugą scenę przed końcem pierwszej. Po oddaniu kontroli sprawdź ciało, kamerę i blokady wejścia.

---

[Spis treści](../README.md) · [Poprzedni tutorial](16-floor-ik.md) · [Następny tutorial](18-kamera-pojazdu.md)
