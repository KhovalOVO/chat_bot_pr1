# Консольный чат-бот на Python

Простой консольный чат-бот, использующий локальную LLM модель (`gemma3:12b`) через [Ollama](https://ollama.com) и библиотеку [LangChain](https://www.langchain.com/).

---
Выполнил студент группы БСМО-31-24 Коваленко Артём
---
## ⚙️ Технологии

- Python 3.10
- LangChain
- LangChain Ollama integration
- Модель: `gemma3:12b` (запускается локально через Ollama)

---

## 🚀 Установка

1. Установи зависимости:

```bash
pip install -r requirements.txt
```

2. Установи и запусти [Ollama](https://ollama.com/), затем скачай [модель](https://ollama.com/library/gemma3:12b):

```bash
ollama pull gemma3:12b
```

3. Запусти бота

```bash
python bot_console.py
```