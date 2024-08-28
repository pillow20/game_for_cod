import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Создание окна
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Шрифт для текста
font = pygame.font.SysFont("Arial", 24)

# Словарь с характеристиками уровней сложности
levels = {
    "beginner": {"text_length": 50, "text_difficulty": 1, "typing_speed": 20},
    "medium": {"text_length": 100, "text_difficulty": 2, "typing_speed": 40},
    "advanced": {"text_length": 200, "text_difficulty": 3, "typing_speed": 60},
    "expert": {"text_length": 500, "text_difficulty": 4, "typing_speed": 80}
}

# Выбор уровня сложности
level = input("Выберите уровень сложности (beginner, medium, advanced, expert): ")

# Генерация текста для набора
text_to_type = ""
for i in range(levels[level]["text_length"]):
    text_to_type += random.choice("абвгдежзиклмнопрстйэюя ")

# Переменные для хранения состояния
correct_keys = 0
incorrect_keys = 0
typing_speed = 0
accuracy = 0
time_taken = 0

# Основной цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Проверка нажатой клавиши
            if event.unicode == text_to_type[0]:
                correct_keys += 1
                text_to_type = text_to_type[1:]
            else:
                incorrect_keys += 1

    # Обновление статистики
    typing_speed = correct_keys / (time_taken+1 / 60)
    accuracy = correct_keys / (correct_keys + incorrect_keys+1) * 100

    # Отрисовка текста
    window.fill((255, 255, 255))
    text_surface = font.render(text_to_type, True, (0, 0, 0))
    window.blit(text_surface, (100, 100))

    # Отрисовка статистики
    stats_surface = font.render(f"Правельно: {correct_keys}, Неправельно: {incorrect_keys}, Скорость: {typing_speed:.2f} wpm, Accuracy: {accuracy:.2f}%", True, (0, 0, 0))
    window.blit(stats_surface, (100, 200))

    # Обновление экрана
    pygame.display.flip()
    pygame.time.Clock().tick(60)