import pygame
import sys
from player import Player
from bullet import Bullet
from explosion import Explosion
from enemytop import EnemyTop
from enemyleft import EnemyLeft
from enemyright import EnemyRight
from enemybottom import EnemyBottom

pygame.init()                                       # Инициализируем модуль pygame

width = 1366                                        # ширина игрового окна
height = 768                                        # высота игрового окна
fps = 30                                            # частота кадров в секунду
game_name = "Shooter"                               # название нашей игры

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
COSMO = "#003b59"


snd_dir = 'media/snd/'                              # Путь до папки со звуками
img_dir = 'media/img/'                              # Путь до папки со спрайтами

# Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)               # Заголовок окна

icon = pygame.image.load(img_dir + 'icon.png')      # Загружаем файл с иконкой
pygame.display.set_icon(icon)                       # Устанавливаем иконку в окно

bg = pygame.image.load(img_dir + 'bg.jpg')      # Загружаем фон


def get_hit_sprite(hits_dict):
    for hit in hits_dict.values():
        return hit[0]

def draw_hp(screen, x, y, hp, hp_width, hp_height): # Функция для рисования hp
    color = "#32CD32" # Зеленый цвет
    white = "#FFFFFF" # Белый цвет
    rect = pygame.Rect(x, y, hp_width, hp_height) # Создаем рамку
    fill = (hp / 500) * hp_width # Считаем ширину полосы для hp
    fill_rect = pygame.Rect(x, y, fill, hp_height) # Cоздаем полосу для hp
    pygame.draw.rect(screen, color, fill_rect) # Рисуем полосу для hp
    pygame.draw.rect(screen, white, rect, 1) # Рисуем рамку

# Функция отображения текста на экране
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Функция для отображения меню
def show_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Shooter", 100, WHITE, width // 2, height // 4)
        draw_text("Press ENTER to Start", 50, WHITE, width // 2, height // 2)
        draw_text("Press ESC to Quit", 50, WHITE, width // 2, height * 3 // 4)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Если нажата клавиша Enter, выходим из меню и начинаем игру
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

all_sprites = pygame.sprite.Group()                 # Создаем группу для спрайтов
mobs_sprites = pygame.sprite.Group()                # Создаем группу для спрайтов мобов
bullets_sprites = pygame.sprite.Group()             # Создаем группу для спрайтов пуль
players_sprites = pygame.sprite.Group()             # Создаем группу для спрайтов игроков

player = Player()                                   # Создаём объект класса Player
all_sprites.add(player)                             # Добавляем player группу всех спрайтов
players_sprites.add(player)                         # Добавляем игрока в группу игроков

enemybottom = EnemyBottom()                        # Создаём объект класса EnemyBottom
all_sprites.add(enemybottom)                       # Добавляем enemy_bottom группу всех спрайтов
mobs_sprites.add(enemybottom)                      # Добавляем enemy_bottom группу врагов
enemyright = EnemyRight()                          # Создаём объект класса EnemyRight
all_sprites.add(enemyright)                        # Добавляем enemy_right группу всех спрайтов
mobs_sprites.add(enemyright)                       # Добавляем enemy_bottom группу врагов
enemyleft = EnemyLeft()                            # Создаём объект класса EnemyLeft
all_sprites.add(enemyleft)                         # Добавляем enemy_left группу всех спрайтов
mobs_sprites.add(enemyleft)                        # Добавляем enemy_bottom группу врагов
enemytop = EnemyTop()                              # Создаём объект класса EnemyTop
all_sprites.add(enemytop)                          # Добавляем enemy_top группу всех спрайтов
mobs_sprites.add(enemytop)                         # Добавляем enemy_bottom группу врагов

timer = pygame.time.Clock()                         # Создаем таймер pygame
'''
# Иногда нужно добавлять pygame.mixer.init()
pygame.mixer.music.load(snd_dir + "music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)'''

run = True



def main():
    while True:
        show_menu()  # Показываем меню перед началом игры
        player = Player()                                   # Создаём объект класса Player
        all_sprites.add(player)                             # Добавляем player группу всех спрайтов
        players_sprites.add(player)                         # Добавляем игрока в группу игроков

        enemybottom = EnemyBottom()                        # Создаём объект класса EnemyBottom
        all_sprites.add(enemybottom)                       # Добавляем enemy_bottom группу всех спрайтов
        mobs_sprites.add(enemybottom)                      # Добавляем enemy_bottom группу врагов
        enemyright = EnemyRight()                          # Создаём объект класса EnemyRight
        all_sprites.add(enemyright)                        # Добавляем enemy_right группу всех спрайтов
        mobs_sprites.add(enemyright)                       # Добавляем enemy_bottom группу врагов
        enemyleft = EnemyLeft()                            # Создаём объект класса EnemyLeft
        all_sprites.add(enemyleft)                         # Добавляем enemy_left группу всех спрайтов
        mobs_sprites.add(enemyleft)                        # Добавляем enemy_bottom группу врагов
        enemytop = EnemyTop()                              # Создаём объект класса EnemyTop
        all_sprites.add(enemytop)                          # Добавляем enemy_top группу всех спрайтов
        mobs_sprites.add(enemytop)                         # Добавляем enemy_bottom группу врагов

        timer = pygame.time.Clock()                         # Создаем таймер pygame

        # Иногда нужно добавлять pygame.mixer.init()
        pygame.mixer.music.load(snd_dir + "music.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        run = True

        while run:                                          # Начинаем бесконечный цикл
            timer.tick(fps)			                        # Контроль времени (обновление игры)
            all_sprites.update()                            # Выполняем действия всех спрайтов в группе

            for event in pygame.event.get():                # Обработка ввода (события)
                if event.type == pygame.QUIT:               # Проверить закрытие окна
                    run = False                             # Завершаем игровой цикл
                if event.type == pygame.KEYDOWN:            # Проверить нажатие клавиш
                    if event.key == pygame.K_SPACE:         # Если нажат пробел
                        player.snd_shoot.play()             # Воспроизводим звук выстрела
                        bullet = Bullet(player)             # Создаем пулю передавая внутрь игрока
                        all_sprites.add(bullet)             # Добавляем пулю ко всем спрайтам
                        bullets_sprites.add(bullet)         # Добавляем пулю ко всем пулям

            shots = pygame.sprite.groupcollide(bullets_sprites, mobs_sprites, True, False)
            if shots:
                sprite = get_hit_sprite(shots)  # Получаем спрайт из второй группы
                sprite.hp -= 30
                if sprite.hp <= 0:
                    sprite.snd_expl.play()  # Воспроизводим звук взрыва
                    expl = Explosion(sprite.rect.center)
                    all_sprites.add(expl)
                    sprite.kill()

            scratch = pygame.sprite.groupcollide(mobs_sprites, players_sprites, False, False)
            if scratch:
                sprite = get_hit_sprite(scratch)            # Получаем спрайт из второй группы
                sprite.snd_scratch.play()   # Воспроизводим звук скрежета
                player.hp -= 1
                if player.hp <= 0:
                    run = False
            screen.blit(bg, (0, 0))
            all_sprites.draw(screen)                        # Отрисовываем все спрайты
            draw_hp(screen, 50, 50, player.hp, 200, 20)
            pygame.display.update()                         # Переворачиваем экран

if __name__ == "__main__":
    main()  # Запуск игры
