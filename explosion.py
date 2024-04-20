import pygame
snd_dir = 'media/snd/' # Путь до папки со звуками
img_dir = 'media/img/' # Путь до папки со спрайтами
width = 1366 # ширина игрового окна
height = 768 # высота игрового окна
# Создаем класс игрока
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.anim_speed = 4  # Скорость анимации
        self.frame = 0  # Текущий кадр анимации
        self.anim = [pygame.transform.scale(
            pygame.image.load(img_dir + f'./explosion/{i}.png'),
            (100, 100)) for i in range(9)]
        self.image = self.anim[0]  # Стартовая картинка спрайта
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.image = self.anim[self.frame // self.anim_speed]  # следующая картинка
        self.frame += 1
        if self.frame >= self.anim_speed * len(self.anim):
            self.kill()
