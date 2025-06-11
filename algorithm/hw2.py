import queue
import time
import threading
import random

# Глобальна черга заявок
request_queue = queue.Queue()

# Лічильник для генерації унікальних ID
request_id_counter = 1

# Генерація нової заявки
def generate_request():
    global request_id_counter
    request_data = {
        'id': request_id_counter,
        'timestamp': time.strftime("%H:%M:%S"),
        'details': f"Заявка №{request_id_counter}"
    }
    request_queue.put(request_data)
    print(f"[{request_data['timestamp']}] Додано: {request_data['details']}")
    request_id_counter += 1

# Обробка заявки з черги
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[{time.strftime('%H:%M:%S')}] Обробка: {request['details']}")
        time.sleep(random.uniform(0.5, 1.5))  # Імітація часу обробки
        print(f"[{time.strftime('%H:%M:%S')}] Завершено: {request['details']}")
    else:
        print(f"[{time.strftime('%H:%M:%S')}] Черга пуста. Очікування нових заявок...")

# Основний цикл програми
def main_loop():
    try:
        while True:
            generate_request()
            time.sleep(random.uniform(0.5, 1.0))  # Імітація паузи між заявками
            process_request()
            time.sleep(random.uniform(0.2, 0.5))  # Пауза між обробками
    except KeyboardInterrupt:
        print("\n Завершення програми за запитом користувача.")

if __name__ == "__main__":
    main_loop()