# CV_course_work

# В данном репозитории находится Курсовая работа по курсу CV

# Выполнил студент группы М80-209М-23 Брежнев Вячеслав Александрович

Работа представляет собой приложение по классификации животных на фото и видео. Модель способна распознавать следующие классы - кошки, собаки, птицы, лошади, овцы, коровы, слоны, медведи, зебры, жирафы (классы, существующие в датасете COCO).

Для реализации поставленной задачи выбрана предобученная модель YOLO (https://docs.ultralytics.com/ru/models/yolov5/#performance-metrics) yolov5su как пример для достижения оптимального баланса между скоростью и точностью. Для повышения точности можно взять модель yolov5x6u или, к примеру, более новую модель yolov10x - при этом повысится точность, но понизится скорость. Для еще более точного результата, расширения распознаваемых классов и минимизации ошибок необходимо провести дообучение модели на собственном датасете, однако это требует значительных вычислительных ресурсов и временных затрат на обучение.

# Запуск и развёртывание

1. Скачать данный репозиторий.
2. Установить необходимые зависимости (requirements.txt) (pip install ultralytics fastapi uvicorn python-multipart opencv-python).
3. Прописать в терминале команду python -m uvicorn app:app --reload (или uvicorn app:app --reload может по разному работать на разных версиях).
4. В терминале появится ссылка на http://127.0.0.1:8000/ перейти по ней и далее открывается окно для загрузки фото и видео, после загрузки выводится результат классификации.

## Пример использования программы:

# *Интерфейс*

![главный экран](https://github.com/user-attachments/assets/f2258ac2-3031-4430-a9d1-c13fb1108e93)


# *Детекция на видео*
![видео](https://github.com/user-attachments/assets/fe6f4d19-addf-4609-9f6b-257cf26597cc)
![видео 2](https://github.com/user-attachments/assets/d2f73845-3d77-4f64-9538-b822ee26d68b)

# *Детекция на фото*

![пингвин](https://github.com/user-attachments/assets/a02ed05c-6e30-48dd-9c0e-75d6bf3ee9eb)
![Зебра](https://github.com/user-attachments/assets/8c293e97-014f-4d4f-97dd-398f6dd633da)
![птицы](https://github.com/user-attachments/assets/f28b3b00-5556-4b15-b1f6-3beaa1685678)
![кошки1](https://github.com/user-attachments/assets/359fbd5e-0ec8-4959-bb22-537799baab14)


# *Примеры, когда на фото присутствуют животные кроме классифицируемых т.е. один из классов не должен быть обнаружен:*
![один не распознан](https://github.com/user-attachments/assets/8ae20acf-7bf6-4ad8-9cab-959c8985f9b6)

# *Примеры, когда на фото присутствуют сразу несколько классов:*
![много классов](https://github.com/user-attachments/assets/d17bdaf9-de12-4cd1-ada8-b12871d7314c)

![животные](https://github.com/user-attachments/assets/f0b42c4d-c83e-40ff-a7c9-a3f4c3a7d030)


# *Пример, когда на закруженных данных нет класса для обнаружения, детекция отсутствует:*

![не найдено](https://github.com/user-attachments/assets/112cb938-065e-4940-b882-b03f5cff3628)

# *Пример когда на изображении присутствует "шум":*

![шум1](https://github.com/user-attachments/assets/79c8a4ca-8a3c-4457-99c9-bef0e65406c0)





