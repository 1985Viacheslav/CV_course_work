# CV_course_work

# В данном репозитории находится Курсовая работа по курсу CV

# Выполнил студент группы М80-209М-23 Брежнев Вячеслав Александрович

Работа представляет собой приложение по распознаванию кошек собак и птиц на фото и видео.

# Запуск и развёртывание

1. Скачать данный репозиторий.
2. Установить необходимые зависимости (requirements.txt) (pip install ultralytics fastapi uvicorn python-multipart opencv-python).
3. Прописать в терминале команду python -m uvicorn app:app --reload (или uvicorn app:app --reload может по разному работать на разных версиях).
4. В терминале появится ссылка на http://127.0.0.1:8000/ перейти по ней и далее открывается окно для загрузки фото и видео, после загрузки выводится результат детекции.
5. Папка static создаётся автоматически.

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


# Примеры, когда на фото присутствуют животные кроме собак кошек и птиц, т.е. один из классов не должен быть обнаружен:

![image0](https://github.com/user-attachments/assets/359774ac-4f7b-4538-978d-647cac1686f0)
![image3](https://github.com/user-attachments/assets/16c82f13-9af8-4039-8ca8-b5b2f65a7b85)

# Пример, когда на фото присутствуют сразу несколько классов:
![много классов](https://github.com/user-attachments/assets/d17bdaf9-de12-4cd1-ada8-b12871d7314c)

![животные](https://github.com/user-attachments/assets/f0b42c4d-c83e-40ff-a7c9-a3f4c3a7d030)


# *Примеры, когда на закруженных данных нет класса для обнаружения, детекция отсутствует*

![не найдено](https://github.com/user-attachments/assets/112cb938-065e-4940-b882-b03f5cff3628)







