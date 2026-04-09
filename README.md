# CherryPy Base — базовый шаблон для приложений на CherryPy
CherryPy — это объектно-ориентированный веб-фреймворк для Python со встроенным HTTP-сервером.
Он хорошо подходит для несложных сайтов и встраиваемых веб-интерфейсов.

## 🔧 В шаблоне реализовано:
- Базовая структура проекта
- Конфигурация через `config/app.conf` и настройки из `.env`
- Точка входа `run.py` и монтирование маршрутов `tree.mount`
- Плагин БД и инструмент авторизации как заготовки

## 📦 Структура проекта
```
├── app/                              # пакет приложения CherryPy
│   ├── controllers/                  # классы-обработчики и монтирование tree.mount
│   │   ├── api/                      # ветка REST API
│   │   │   └── v1/                   # ресурсы API версии 1
│   │   │       └── health.py
│   │   └── root.py
│   ├── models/                       # доменные модели (заготовка)
│   ├── plugins/                      # плагины движка CherryPy (например, БД)
│   ├── services/                     # бизнес-логика (заготовка)
│   ├── templates/                    # шаблоны Jinja2
│   └── tools/                        # инструменты CherryPy (хуки, авторизация)
├── config/                           # настройки из переменных окружения и app.conf
│   ├── app.conf
│   └── settings.py
├── tests/                            # pytest
├── env.example
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── run.py
└── uv.lock
```

## ⚙️ Установка и запуск
#### uv
```bash
git clone https://gitverse.ru/Rockdukan/cherrypy-base.git
cd cherrypy-base
uv venv
uv sync
uv run python run.py
```

#### venv
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

## 🧪 Тестирование
```bash
uv run pytest -q
```

## 🌐 Маршруты

- `GET /`  
  HTML-страница из шаблона `index.html`.

- `GET /api/v1/health`  
  Проверка работоспособности. Возвращает JSON:

  ```json
  {"status": "ok"}
  ```
