import pygame
from bar import Bar
import dataGenerator
import math
import algorithms
class Graph():

    PADDING = 50
    BAR_EDGE_PADDING = 10

    def __init__(self, width, height, algorithm):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.__window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.xaxis_width = (self.WINDOW_WIDTH - self.PADDING * 2)
        self.xaxis_x = (self.WINDOW_WIDTH - self.xaxis_width) / 2
        self.xaxis_y = self.WINDOW_HEIGHT - self.PADDING
        self.sorting_algorithm = algorithm()
        self.current_bar = None
        self.is_sorting = False

    def DrawBars(self):
        num_bars = len(Bar.bars)
        bar_width = (self.WINDOW_WIDTH - (self.BAR_EDGE_PADDING * 2) - (self.PADDING * 2)) // num_bars
        for i in range(num_bars):
            if Bar.max_val > 0:
                color = Color.WHITE if i == self.current_bar else Color.GREEN
                bar_height = (Bar.bars[i].val / Bar.max_val) * (self.WINDOW_HEIGHT - self.PADDING * 2)
                pygame.draw.rect(self.__window, color, ((self.xaxis_x + self.BAR_EDGE_PADDING) + (i * bar_width) + 10, self.xaxis_y - bar_height, bar_width, bar_height))


    def Run(self):
        pygame.init()
        pygame.font.init()

        pygame.display.set_caption("Algorithm Visualizer")

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and not self.is_sorting:
                        dataGenerator.DataGenerator.GenerateDataSet(50)

            self.__window.fill(Color.BLACK)
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = font.render(f"{self.sorting_algorithm.__name__} - Time elapsed:  ", True, Color.WHITE)
            self.__window.blit(text_surface, dest=(50, 50))
            xaxis = pygame.draw.rect(self.__window, Color.WHITE, (self.xaxis_x, self.xaxis_y, self.xaxis_width, 2))
            try:
                self.current_bar = next(self.sorting_algorithm)
                self.is_sorting = True
            except StopIteration:
                self.current_bar = None
                self.is_sorting = False
            self.DrawBars()

            clock.tick(60)
            pygame.display.update()
        pygame.quit()

class Color():
    GREEN = (27, 207, 33)
    BLUE = (17, 84, 217)
    WHITE = (255, 255, 255)
    PURPLE = (213, 20, 219)
    BLACK = (0, 0, 0)