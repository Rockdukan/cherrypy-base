# CherryPy Base — базовый шаблон для приложений на CherryPy
CherryPy — это объектно-ориентированный веб-фреймворк для Python со встроенным HTTP-сервером.
Он хорошо подходит для несложных сайтов и встраиваемых веб-интерфейсов.
![screenshot](screenshot.jpg)

## 🔧 В шаблоне реализовано:
- Базовая структура проекта
- Конфигурация через `config/app.conf` и настройки из `.env`
- Точка входа `server.py` и монтирование маршрутов `tree.mount`
- HTML через Jinja2 и REST-ресурс `/api/v1/users` с `MethodDispatcher`
- Плагин БД и инструмент авторизации как заготовки

## 📦 Структура проекта
```
├── app/
│   ├── controllers/
│   ├── plugins/
│   ├── tools/
│   ├── templates/
│   ├── models/
│   └── services/
├── config/
│   ├── app.conf
│   └── settings.py
├── tests/
├── server.py
├── env.example
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## ⚙️ Установка и запуск
```bash
git clone https://gitverse.ru/Rockdukan/cherrypy-base.git
cd cherrypy-base
uv venv
uv sync  # ставит зависимости из pyproject.toml
uv run python server.py
```

Если вы предпочитаете устанавливать зависимости из `requirements.txt`, можно сделать так:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python server.py
```

## 🧪 Тестирование
```bash
uv sync --extra dev
uv run pytest -q
```

## 🌐 Маршруты

- `GET /`  
  HTML-страница из шаблона `index.html`.

- `GET /api/v1/users`  
  Возвращает JSON:

  ```json
  {"items": []}
  ```

- `POST /api/v1/users`  
  Принимает JSON в теле запроса и возвращает JSON с перечнем принятых ключей.
