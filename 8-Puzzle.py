import pygame
import sys
import random

pygame.init()

# Constants
TILE_SIZE = 80
FONT_SIZE = TILE_SIZE // 2


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the game window
def initialize_game(n):
    WIDTH = n * TILE_SIZE
    HEIGHT = n * TILE_SIZE
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"{n}-Puzzle Game")
    return screen, WIDTH, HEIGHT

# Initialize the tiles
def initialize_tiles(n):
    tiles = [[y * n + x + 1 for x in range(n)] for y in range(n)]
    tiles[n - 1][n - 1] = 0
    return tiles

# Shuffle the tiles
def shuffle_tiles(tiles, empty_tile, shuffle_count):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for _ in range(shuffle_count):
        dx, dy = random.choice(directions)
        new_x, new_y = empty_tile[0] + dx, empty_tile[1] + dy
        if 0 <= new_x < len(tiles[0]) and 0 <= new_y < len(tiles):
            tiles[empty_tile[1]][empty_tile[0]], tiles[new_y][new_x] = tiles[new_y][new_x], tiles[empty_tile[1]][empty_tile[0]]
            empty_tile[0], empty_tile[1] = new_x, new_y

# Main game loop
def game_loop(screen, WIDTH, HEIGHT, n):
    tiles = initialize_tiles(n)
    empty_tile = [n - 1, n - 1]
    shuffle_tiles(tiles, empty_tile, shuffle_count=n * 100)

    FONT = pygame.font.Font(None, FONT_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP and empty_tile[1] > 0:
                    tiles[empty_tile[1]][empty_tile[0]], tiles[empty_tile[1] - 1][empty_tile[0]] = \
                        tiles[empty_tile[1] - 1][empty_tile[0]], tiles[empty_tile[1]][empty_tile[0]]
                    empty_tile[1] -= 1
                elif event.key == pygame.K_DOWN and empty_tile[1] < n - 1:
                    tiles[empty_tile[1]][empty_tile[0]], tiles[empty_tile[1] + 1][empty_tile[0]] = \
                        tiles[empty_tile[1] + 1][empty_tile[0]], tiles[empty_tile[1]][empty_tile[0]]
                    empty_tile[1] += 1
                elif event.key == pygame.K_LEFT and empty_tile[0] > 0:
                    tiles[empty_tile[1]][empty_tile[0]], tiles[empty_tile[1]][empty_tile[0] - 1] = \
                        tiles[empty_tile[1]][empty_tile[0] - 1], tiles[empty_tile[1]][empty_tile[0]]
                    empty_tile[0] -= 1
                elif event.key == pygame.K_RIGHT and empty_tile[0] < n - 1:
                    tiles[empty_tile[1]][empty_tile[0]], tiles[empty_tile[1]][empty_tile[0] + 1] = \
                        tiles[empty_tile[1]][empty_tile[0] + 1], tiles[empty_tile[1]][empty_tile[0]]
                    empty_tile[0] += 1

        # Clear the screen
        screen.fill(BLACK)

        # Draw the tiles
        for y in range(n):
            for x in range(n):
                value = tiles[y][x]
                if value != 0:
                    pygame.draw.rect(screen, WHITE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
                    text = FONT.render(str(value), True, BLACK)
                    text_rect = text.get_rect(center=(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2))
                    screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

        if tiles == [[y * n + x + 1 for x in range(n)] for y in range(n)]:
            running = False

    pygame.time.wait(2000)

# Initialize and run the game
def main():
    n = int(input("Enter the puzzle size: "))
    if n < 2:
        print("Puzzle size must be at least 2.")
        return

    screen, WIDTH, HEIGHT = initialize_game(n)
    game_loop(screen, WIDTH, HEIGHT, n)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
