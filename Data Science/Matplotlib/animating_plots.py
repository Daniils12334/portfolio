import matplotlib.pyplot as plt
import random
import pygame

# Инициализируем звук
pygame.mixer.init()
# Замените этот путь на путь к любому короткому .wav-файлу (например, щелчок)
# Можно скачать звуки с https://freesound.org
SOUND_FILE = "/home/danbar/Desktop/great_sound.mp3"  # положи этот файл рядом со скриптом
try:
    sound = pygame.mixer.Sound(SOUND_FILE)
except:
    sound = None  # если файл не найден — работаем без звука

# Данные
subjects = [0, 0, 0, 0, 0, 0, 0]
labels = ["Rust", "C++", "Java", "Python", "Go", "JavaScript", "Bash"]
colors = ["red", "green", "black", "brown", "yellow", "purple", "blue"]

plt.ion()
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(300):
    winner = random.randint(0, 6)
    subjects[winner] += 5

    ax.clear()
    bars = ax.bar(labels, subjects, color=colors)

    # Добавляем очки над столбцами
    for bar, score in zip(bars, subjects):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 20,
                str(score), ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Выделим лидера цветом или границей
    max_value = max(subjects)
    for bar, val in zip(bars, subjects):
        if val == max_value:
            bar.set_edgecolor("gold")
            bar.set_linewidth(3)

    ax.set_title("🔥 Best Programming Language Voting 🔥", fontsize=16)
    ax.set_ylim(0, max(subjects) + 200)


    plt.pause(0.05)

if sound:
    sound.play()
plt.ioff()
plt.show()
