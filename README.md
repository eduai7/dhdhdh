# Зелёный мир / Yashil dunyo

Сайт о природе и о том, как её сохранить. 7 страниц, языки RU / UZ, болотная палитра.

## Как запустить на GitHub Pages
1. Создайте новый репозиторий на GitHub (например `eco-site`), сделайте его **Public**.
2. Загрузите в него все файлы из этой папки (Add file → Upload files), чтобы `index.html` лежал в корне.
3. Settings → Pages → Source: **Deploy from a branch** → Branch: `main`, папка `/ (root)` → Save.
4. Через 1–2 минуты сайт будет доступен по адресу `https://<ваш-логин>.github.io/eco-site/`.

## Структура
- `index.html` — Главная
- `ecosystems.html` — Экосистемы
- `threats.html` — Угрозы
- `protect.html` — Как сохранить
- `uzbekistan.html` — Природа Узбекистана
- `habits.html` — Эко-привычки (чек-лист, сохраняется в браузере)
- `about.html` — О проекте + тест
- `css/style.css`, `js/main.js`, `img/` — фотографии (Wikimedia Commons, свободные лицензии; список авторов на странице «О проекте»)
- `build.py` — генератор страниц (необязательно). Тексты можно править прямо в HTML
  или в `build.py` и пересобрать: `python3 build.py .`

## Переключение языка
Каждый текст записан дважды: `data-l="ru"` и `data-l="uz"`. Кнопка RU/UZ меняет `<html lang>`,
выбор запоминается.
