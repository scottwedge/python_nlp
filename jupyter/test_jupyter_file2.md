### Демонстрационный файл

> Программа выполняет полный анализ текстового корпуса:
> извлечение признаков, фильтрация текста, обработка слов,
> составление вектора. Полученные данные сохраняются в БД.
> Далее, выполняется классификация выбранного корпуса текстов
> на основе полученных входных и выходных векторов.
> Все параметры для настройки системы анализа текстовой 
> информации задаются файлом param.json


**Подключение внешних библиотек:**

**Инициализация работы с БД:**

**Получение списка используемых текстов и отправка имени текста, 
имени темы и исходного текста в БД:**

**Обновление таблицы БД со списком тем для отчётности:**

**Фильтрация исходных текстов. Отправка обработанных текстов в БД:**

**Фомирование общего словаря для всех текстов и отправка
словаря в БД:**

**Обновление общей информации, для отчётности:**

**Фомирование входных и выходных векторов к каждому тексту,
отправка их в БД:**

**Настройка объекта для последовательного извлечения 
входных и выходных данных:**

**Разделение данных на обучающую и тестовую:**

**Формирование и подготовка нейронной сети:**

**Начало процесса обучения сети:**

**Построение графиков для отчета:**