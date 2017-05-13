# Анализ тональности отзывов

## Как запустить

Требования: `python 3`(3.5.1) with `flask`(0.11.1) module, `scikit-learn`(0.18.1), `nltk`(3.2.2) and `numpy`(1.11.2)

Для запуска приложения нужно просто выполнить `Controller.py`:
```
$ python Controller.py
```

Папка `models` содержит notebook (`kaggle.ipynb`) и сохраненную модель `cnt_log.pkl`

`Controller.py` - flask app

`SentimentAnalyzer.py` - класс-обертка для работы с моделью

Папка `templates` содержит шаблоны, используемые Web UI; их заполнение происходит в `Controller.py`

`log` - папка для логов приложения

`static` - статический контент приложения (стили, картинки)

`screens` - папка со скриншотами работающего приложения

Дополнительную информацию можно найти в `static/ABOUT.MD` (достпна в Web UI по кнопке `Помощь`)
