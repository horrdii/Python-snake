import pygame
import json

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

LEADERBOARD_FILE = 'leaderboard.json'

def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            leaderboard = json.load(f)
            if not isinstance(leaderboard, list):
                raise ValueError("Invalid leaderboard format")
            return leaderboard
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return []

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(leaderboard, f)

def update_leaderboard(name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({'name': name, 'score': score})
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    leaderboard = leaderboard[:5]
    save_leaderboard(leaderboard)
    return leaderboard

def display_leaderboard(screen, leaderboard):
    pygame.init()
    font = pygame.font.SysFont(None, 50)
    text = font.render("Leaderboard", True, WHITE)
    screen.blit(text, [SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 + 50])

    font = pygame.font.SysFont(None, 35)
    for index, entry in enumerate(leaderboard):
        text = font.render(f"{index + 1}. {entry['name']} - {entry['score']}", True, WHITE)
        screen.blit(text, [SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 + 100 + index * 40])

    pygame.display.flip()
    pygame.time.wait(3000)
