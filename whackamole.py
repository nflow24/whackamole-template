import pygame, random

def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-mole")

        clock = pygame.time.Clock()
        # initialize game interface
        # fills screen with color
        screen.fill("light green")

        # draws vertical lines
        for i in range(0, 20):
            pygame.draw.line(screen, (0, 0, 0), (i * 32, 0), (i * 32, 640))
        # draws horizontal lines
        for i in range(0, 16):
            pygame.draw.line(screen, (0, 0, 0), (0, i * 32), (640, i * 32))

        # initializes mole position
        mole = screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        pygame.display.flip()
        clock.tick(60)

        running = True
        while running:

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mole.collidepoint(event.pos):
                        # generates random coordinates and updates event.pos
                        new_x_pos = random.randrange(0, 640, 32)
                        new_y_pos = random.randrange(0, 512, 32)
                        event.pos = new_x_pos, new_y_pos

                        # redraws entire screen with new mole position
                        screen.fill("light green")
                        for i in range(0, 20):
                            pygame.draw.line(screen, (0, 0, 0), (i * 32, 0), (i * 32, 640))
                        for i in range(0, 16):
                            pygame.draw.line(screen, (0, 0, 0), (0, i * 32), (640, i * 32))
                        mole = screen.blit(mole_image, mole_image.get_rect(topleft=event.pos))
                        pygame.display.update()

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
