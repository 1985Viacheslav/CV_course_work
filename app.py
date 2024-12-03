import os
import cv2
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from typing import Generator
from ultralytics import YOLO

app = FastAPI()
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
model = YOLO('yolov5su.pt')


# функция для классификации кадра
def classify_frame_yolo(frame):
    results = model(frame)
    labels = model.names
    for i in range(len(results[0].boxes)):
        box = results[0].boxes[i]
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = float(box.conf[0])
        class_id = int(box.cls[0])

        # фильтрация только животных
        if labels[class_id] in ["cat", "dog", "bird"]:
            class_name = labels[class_id]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{class_name} ({confidence:.2f})", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame


# главная страница для загрузки
@app.get("/", response_class=HTMLResponse)
async def upload_page():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Классификация животных</title>
    </head>
    <body>
        <h1>Загрузите видео для классификации</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept="video/*" required>
            <button type="submit">Загрузить</button>
        </form>
        <h1>Загрузите фото для классификации</h1>
        <form action="/upload-image" method="post" enctype="multipart/form-data">
            <input type="file" name="image" accept="image/*" required>
            <button type="submit">Загрузить</button>
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# загрузка видео
@app.post("/upload")
async def upload_file(file: UploadFile):
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # сохранение загруженного файла
    with open(input_path, "wb") as f:
        f.write(file.file.read())

    # страница с ссылкой на поток
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Результат классификации</title>
    </head>
    <body>
        <h1>Загруженный файл</h1>
        <video controls width="480">
            <source src="/files/{file.filename}" type="{file.content_type}">
        </video>
        <h2>Обработанное видео с классификацией</h2>
        <img src="/stream/{file.filename}" width="480" />
        <br><br>
        <a href="/">Загрузить другой файл</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# загрузка изображения
@app.post("/upload-image")
async def upload_image(image: UploadFile):
    input_path = os.path.join(UPLOAD_FOLDER, image.filename)

    # сохранение изображения
    with open(input_path, "wb") as f:
        f.write(image.file.read())

    # загрузка и обработка изображения
    frame = cv2.imread(input_path)
    processed_frame = classify_frame_yolo(frame)

    # сохранение обработанного изображения
    output_path = os.path.join(UPLOAD_FOLDER, f"processed_{image.filename}")
    cv2.imwrite(output_path, processed_frame)

    # страница с обработанным изображением
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Результат классификации</title>
    </head>
    <body>
        <h1>Загруженное изображение</h1>
        <img src="/files/{image.filename}" width="480" />
        <h2>Обработанное изображение с классификацией</h2>
        <img src="/files/processed_{image.filename}" width="480" />
        <br><br>
        <a href="/">Загрузить другой файл</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# Потоковое воспроизведение обработанного видео
@app.get("/stream/{filename}")
async def stream_video(filename: str):
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(input_path):
        return HTMLResponse(content="File not found", status_code=404)

    return StreamingResponse(video_stream(input_path), media_type="multipart/x-mixed-replace; boundary=frame")


# Генератор для потоковой передачи кадров
def video_stream(input_path: str) -> Generator:
    cap = cv2.VideoCapture(input_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Обрабатываем кадр
        processed_frame = classify_frame_yolo(frame)

        # Кодируем кадр в JPEG
        _, buffer = cv2.imencode(".jpg", processed_frame)

        # Формируем HTTP-ответ с кадром
        frame_data = (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
        )
        yield frame_data

    cap.release()


# Статические файлы для исходных данных
@app.get("/files/{filename}")
async def static_files(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return HTMLResponse(content="File not found", status_code=404)
    return FileResponse(file_path)
