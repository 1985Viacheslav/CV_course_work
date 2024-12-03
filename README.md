# CV_course_work

# В данном репозитории находится Курсовая работа по курсу CV

# Выполнил студент группы М80-209М-23 Брежнев Вячеслав Александрович

Работа представляет собой приложение по распознаванию кошек собак и птиц на фото и видео.

# Запуск и развёртывание

1. Скачать данный репозиторий.
2. Установить необходимые зависимости (requirements.txt) (pip install ultralytics fastapi uvicorn python-multipart opencv-python).
3. Прописать в терминале команду python -m uvicorn app:app --reload (или uvicorn app:app --reload может по разному работать на разных версиях).
4. В терминале появится ссылка на http://127.0.0.1:8000/ перейти по ней и далее открывается окно для загрузки фото и видео, после загрузки выводится результат детекции.
5. Папка uploads создаётся автоматически.

# Пример использования программы:

*Интерфейс*
![interface](https://github.com/user-attachments/assets/caec3db5-443f-41c8-a4ef-abd09082dee9)

*Детекция на видео*
![video1](https://github.com/user-attachments/assets/ac222980-0807-4263-b8b3-2e13702b8241)
![video2](https://github.com/user-attachments/assets/17348717-4c32-49aa-b499-cd19c0442dc5)

*Детекция на фото*

![image1](https://github.com/user-attachments/assets/af38ffdb-4542-407a-b216-eb5ec4c577b8)
![image4](https://github.com/user-attachments/assets/54f314e1-2e98-44f9-8e27-dde6fd1714bf)


Примеры, когда на фото присутствуют животные кроме собак кошек и птиц, т.е. один из классов не должен быть обнаружен:

![image0](https://github.com/user-attachments/assets/359774ac-4f7b-4538-978d-647cac1686f0)
![image3](https://github.com/user-attachments/assets/16c82f13-9af8-4039-8ca8-b5b2f65a7b85)

Пример, когда на фото присутствуют сразу несколько классов:

![image5](https://github.com/user-attachments/assets/2c6ffb7b-a30d-44c6-9600-d4828ca4ae57)
![image2](https://github.com/user-attachments/assets/a63ce2f4-3983-4811-83b8-5110c4b41619)

*Примеры, когда на закруженных данных нет класса для обнаружения, детекция отсутствует*

![not_detected1](https://github.com/user-attachments/assets/8e5f6980-eb2a-439e-8b22-a8d18c0d42da)

![not_detected2](https://github.com/user-attachments/assets/aaaba311-950a-49a9-bf84-a20079816afc)






