---
description: "SQL dla testera: zapytania SELECT, filtrowanie, agregacja, rodzaje JOIN, pułapki z NULL i weryfikacja danych w bazie podczas testów aplikacji."
---

# SQL

**SQL (Structured Query Language)** to język do zarządzania danymi w **relacyjnych bazach danych**. Umożliwia pobieranie, dodawanie, aktualizowanie i usuwanie danych oraz definiowanie struktury bazy (tabele, klucze, relacje).

## Zastosowanie w pracy testera

- weryfikacja danych po testach **API / ETL**,
- sprawdzanie, czy akcja w aplikacji **zapisała się poprawnie** w bazie,
- szukanie niespójności (duplikaty, brakujące relacje, wartości `NULL`),
- porównywanie danych między środowiskami (testowym i produkcyjnym),
- przygotowywanie **danych testowych** (`INSERT`, `UPDATE`).

!!! note "Dialekty SQL"
    Składnia różni się między bazami. `LIMIT 10` działa w MySQL, PostgreSQL i SQLite (w SQL Server: `SELECT TOP 10`, w Oracle: `FETCH FIRST 10 ROWS ONLY`), `AUTO_INCREMENT` to MySQL (PostgreSQL: `GENERATED ... AS IDENTITY`), a `FULL JOIN` nie istnieje w MySQL. Sprawdzaj dokumentację bazy używanej w projekcie.

## Podstawowe operacje (CRUD)

=== "SELECT"

    ```sql
    SELECT imie, nazwisko FROM pracownicy WHERE miasto = 'Kraków';
    SELECT DISTINCT kraj FROM klienci;   -- unikalne wartości
    SELECT * FROM produkty ORDER BY cena DESC LIMIT 10;
    ```

=== "INSERT"

    ```sql
    INSERT INTO pracownicy (imie, nazwisko, stanowisko)
    VALUES ('Jan', 'Kowalski', 'Tester');
    ```

=== "UPDATE"

    ```sql
    UPDATE pracownicy SET stanowisko = 'Senior Tester' WHERE id = 7;
    ```

=== "DELETE"

    ```sql
    DELETE FROM pracownicy WHERE id = 7;
    ```

!!! danger "Zawsze z `WHERE`"
    `UPDATE` i `DELETE` bez `WHERE` zmienią **wszystkie** wiersze w tabeli. Najpierw uruchom `SELECT` z tym samym warunkiem.

!!! warning "Bezpieczna zmiana danych"
    Przed `UPDATE` lub `DELETE` uruchom ten sam warunek w `SELECT`, a zmianę wykonaj w transakcji: `BEGIN; UPDATE ...; SELECT ...;`, a potem `COMMIT` albo `ROLLBACK`. Na produkcji używaj tylko konta do odczytu.

## Filtrowanie

| Operator | Znaczenie | Przykład |
|---|---|---|
| `=` | równe | `WHERE miasto = 'Kraków'` |
| `<>` / `!=` | różne | `WHERE wiek <> 30` |
| `> < >= <=` | porównania | `WHERE wiek > 25` |
| `BETWEEN … AND …` | zakres | `WHERE wiek BETWEEN 20 AND 30` |
| `IN (...)` | należy do zbioru | `WHERE stanowisko IN ('Tester', 'Developer')` |
| `LIKE` | wzorzec (`%` dowolny ciąg, `_` jeden znak) | `WHERE nazwisko LIKE 'Kow%'` |
| `IS NULL` / `IS NOT NULL` | wartości puste | `WHERE email IS NULL` |
| `AND`, `OR`, `NOT` | logika | `WHERE miasto = 'Kraków' AND stanowisko = 'Tester'` |

!!! warning "NULL to nie wartość"
    - `WHERE email = NULL` nigdy nic nie zwraca; używaj `IS NULL`.
    - `WHERE wiek <> 30` pomija wiersze, w których `wiek` jest `NULL`.
    - `NOT IN (podzapytanie)` zwraca pusty wynik, jeśli podzapytanie zawiera `NULL`; bezpieczniej użyć `NOT EXISTS`.
    - `COUNT(kolumna)` pomija `NULL`, a `COUNT(*)` liczy wszystkie wiersze.

## Agregacja

```sql
SELECT COUNT(*)    FROM produkty;
SELECT SUM(cena)   FROM produkty;
SELECT AVG(cena)   FROM produkty;
SELECT MIN(cena), MAX(cena) FROM produkty;

-- grupowanie + warunek na grupie
SELECT stanowisko, COUNT(*) AS liczba
FROM pracownicy
GROUP BY stanowisko
HAVING COUNT(*) > 2;
```

## JOIN-y

| Typ | Zwraca |
|---|---|
| `INNER JOIN` | tylko dopasowane rekordy z obu tabel |
| `LEFT JOIN` | wszystkie z lewej + dopasowane z prawej |
| `RIGHT JOIN` | wszystkie z prawej + dopasowane z lewej |
| `FULL JOIN` | wszystkie z obu (brak dopasowania daje `NULL`) |

!!! example "INNER JOIN a LEFT JOIN na danych"

    Tabela `pracownicy`:

    | id | imie | id_dzialu |
    |---|---|---|
    | 1 | Anna | 10 |
    | 2 | Piotr | 20 |
    | 3 | Ewa | `NULL` |

    Tabela `dzialy`:

    | id | nazwa |
    |---|---|
    | 10 | QA |
    | 20 | Backend |
    | 30 | Frontend |

    ```sql
    SELECT p.imie, d.nazwa AS dzial          -- aliasy p i d
    FROM pracownicy p
    INNER JOIN dzialy d ON p.id_dzialu = d.id;
    ```

    | imie | dzial |
    |---|---|
    | Anna | QA |
    | Piotr | Backend |

    Ten sam warunek z `LEFT JOIN` zwraca też Ewę, która nie ma działu:

    | imie | dzial |
    |---|---|
    | Anna | QA |
    | Piotr | Backend |
    | Ewa | `NULL` |

    Dział *Frontend* nie pojawia się w żadnym wyniku, bo nie ma w nim pracowników. Zwróciłby go `RIGHT JOIN` lub `FULL JOIN`.

## Przydatne zapytania testerskie

```sql
-- duplikaty adresów e-mail
SELECT email, COUNT(*) FROM uzytkownicy GROUP BY email HAVING COUNT(*) > 1;

-- zamówienia bez istniejącego klienta (osierocone rekordy)
SELECT z.* FROM zamowienia z
LEFT JOIN klienci k ON z.id_klienta = k.id
WHERE k.id IS NULL;

-- czy zamówienie z testu zapisało się poprawnie
SELECT status, suma FROM zamowienia WHERE id = 1234;
```

## Definiowanie struktury

```sql
-- składnia MySQL; w PostgreSQL: id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
CREATE TABLE pracownicy (
  id         INT PRIMARY KEY AUTO_INCREMENT,
  imie       VARCHAR(50) NOT NULL,
  email      VARCHAR(100) UNIQUE,
  id_dzialu  INT,
  FOREIGN KEY (id_dzialu) REFERENCES dzialy(id) ON DELETE CASCADE
);
```

`ON DELETE CASCADE` sprawia, że usunięcie rekordu nadrzędnego usuwa również **wszystkie powiązane rekordy**, nie tylko sam podmiot.
