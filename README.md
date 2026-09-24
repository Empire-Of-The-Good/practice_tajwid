<div align="center">
<img src="logo.png" alt="Practice Tajwid Banner" width="400">

[![Version 0.0.2](https://img.shields.io/badge/Version-0.0.2-red.svg)](https://github.com/Empire-Of-The-Good/practice_tajwid)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-green.svg?logo=python)](https://www.python.org/downloads/)
[![PyQt6 6.11.0](https://img.shields.io/badge/PyQt6-6.11.0-orange.svg?logo=pypi)](https://pypi.org/project/PyQt6/)
[![OS](https://img.shields.io/badge/OS-Linux-purple.svg?logo=linux&logoColor=white)](https://kernel.org/)

</div>

<div align="center">
	<h1>
		Practice Tajwid — Практика базовых правил
	</h1>
</div>

## 📌 О проекте
Здесь собраны (будут) базовые правила по таджвиду. Проект решает проблему с неправильным чтением.

> [!NOTE]
> Проект продуман не до конца: возможно, это будут лишь тесты с ответами, а может, и наоборот.

### 🔥 Ключевые Особенности
* **Оффлайн** — учитесь на своем ПК/ноутбуке без интернета.
* **Бесплатно** — проект абсолютно бесплатен, не нужно за что-либо платить.
* **Наглядность** — сразу после ответа можно увидеть выделением, как читать правильно.

## 🔧 Стек технологий
* **Язык:** `Python 3.12`
* **Фреймворки/Библиотеки:** `Pygame`

## ⚙️ Установка
> [!TIP]
> Для работы советуется установленный `uv` (быстрый менеджер пакетов).

### Linux
```bash
# 1. Клонируем репозиторий с проектом к себе на компьютер
git clone git@github.com:Empire-Of-The-Good/practice_tajwid.git

# 2. Переходим в корневую директорию скачанного проекта
cd practice_tajwid

# 3. Скачиваем, изолируем и обновляем все необходимые зависимости через uv
uv sync

# 4. Запускаем приложение в изолированном окружении
uv run python src/practice_tajwid/main.py
```

#### Если вы не хотите использовать uv
```bash
# 1. Создание виртуального окружения и активация
python -m venv .venv && source .venv/bin/activate

# 2. Установка зависимостей
pip install -r requirements.txt

# 3. Запуск
python src/practice_tajwid/main.py
```

## 🗺️ Roadmap
- [ ] Сделать колонку с выбором нужной темы для теста
- [ ] Составить тест
