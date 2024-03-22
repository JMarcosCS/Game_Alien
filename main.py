import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

# Função para incializar o jogo e criar objeto


def run_game():
    pygame.init()
    # Utilizando as configurações
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Cria a espaçonave
    ship = Ship(ai_settings, screen)
    # Armazenamento de projéteis:
    bullets = Group()
    # Cor do plano de fundo
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Início do laço principaç
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


    # Tela mais visível
run_game()
