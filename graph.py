import pygame
from bar import Bar
import dataGenerator
import algorithms
import time
class Graph():

    PADDING = 100
    BAR_EDGE_PADDING = 10
    MAX_FPS = 240
    VALUES_STEP = 100
    MIN_VALUES = 100
    MAX_VALUES = 1000

    def __init__(self, width, height):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.__window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.xaxis_width = (self.WINDOW_WIDTH - self.PADDING * 2)
        self.xaxis_x = (self.WINDOW_WIDTH - self.xaxis_width) / 2
        self.xaxis_y = self.WINDOW_HEIGHT - self.PADDING
        self.num_values = 100
        self.sorting_algorithm_index = 0
        self.sorting_algorithm = algorithms.Algorithm.algorithms[self.sorting_algorithm_index]
        self.sorting_algorithm_generator = None # holds the current sorting algorithm to be executed once only
        self.current_bar = None
        self.is_sorting = False
        self.start_time = 0
        self.elapsed_time = 0
        self.compare = 0
        self.swaps = 0

    def DrawBars(self):
        num_bars = len(Bar.bars)
        bar_width = (self.WINDOW_WIDTH - (self.BAR_EDGE_PADDING * 2) - (self.PADDING * 2)) // num_bars
        for i in range(num_bars):
            if Bar.max_val > 0:
                color = Color.WHITE if i == self.current_bar else Color.GREEN
                bar_height = (Bar.bars[i].val / Bar.max_val) * (self.WINDOW_HEIGHT - self.PADDING * 2)
                pygame.draw.rect(self.__window, color, ((self.xaxis_x + self.BAR_EDGE_PADDING) + (i * bar_width), self.xaxis_y - bar_height, bar_width, bar_height))
                


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
                        dataGenerator.DataGenerator.GenerateDataSet(self.num_values)
                    elif event.key == pygame.K_RIGHT and not self.is_sorting:
                        self.sorting_algorithm_index += 1
                        if self.sorting_algorithm_index >= len(algorithms.Algorithm.algorithms):
                            self.sorting_algorithm_index = 0
                        self.sorting_algorithm = algorithms.Algorithm.algorithms[self.sorting_algorithm_index]
                    elif event.key == pygame.K_LEFT and not self.is_sorting:
                        self.sorting_algorithm_index -= 1
                        if self.sorting_algorithm_index < 0:
                            self.sorting_algorithm_index = len(algorithms.Algorithm.algorithms) - 1
                        self.sorting_algorithm = algorithms.Algorithm.algorithms[self.sorting_algorithm_index]
                    elif event.key == pygame.K_SPACE and not self.is_sorting:
                        self.is_sorting = True
                        self.sorting_algorithm_generator = self.sorting_algorithm()
                        self.start_time = time.time()
                        self.elapsed_time = 0
                        self.compare = 0
                        self.swaps = 0
                    elif event.key == pygame.K_UP and not self.is_sorting:
                        self.num_values += self.VALUES_STEP
                        if self.num_values > self.MAX_VALUES:
                            self.num_values = self.MAX_VALUES
                        dataGenerator.DataGenerator.GenerateDataSet(self.num_values)
                    elif event.key == pygame.K_DOWN and not self.is_sorting:
                        self.num_values -= self.VALUES_STEP
                        if self.num_values < self.MIN_VALUES:
                            self.num_values = self.MIN_VALUES
                        dataGenerator.DataGenerator.GenerateDataSet(self.num_values)
                    

            self.__window.fill(Color.BLACK)
            font = pygame.font.SysFont('Comic Sans MS', 30)
            
            xaxis = pygame.draw.rect(self.__window, Color.WHITE, (self.xaxis_x, self.xaxis_y, self.xaxis_width, 2))

            try:
                if self.is_sorting:
                    self.current_bar, self.compare, self.swaps = next(self.sorting_algorithm_generator)
                    self.is_sorting = True
                    self.elapsed_time = time.time() - self.start_time
            except StopIteration:
                self.current_bar = None
                self.is_sorting = False
                self.sorting_algorithm_generator = None
            text_surface = font.render(f"{self.sorting_algorithm.__name__} - Time elapsed:  {self.elapsed_time:.2f}s, Comparisons = {self.compare}, Swaps = {self.swaps}", True, Color.WHITE)
            self.__window.blit(text_surface, dest=(20, self.WINDOW_HEIGHT - 50))
            


            text_surface_controls = font.render("Up/Down - Increase/decrease values, Left/Right - Cycle algorithms, R - New values, Space - Run algorithm", True, Color.WHITE)
            self.__window.blit(text_surface_controls, dest=((self.WINDOW_WIDTH - text_surface_controls.get_width()) // 2, 50))

            self.DrawBars()
            clock.tick(self.MAX_FPS)
            pygame.display.update()
        pygame.quit()

class Color():
    GREEN = (27, 207, 33)
    BLUE = (17, 84, 217)
    WHITE = (255, 255, 255)
    PURPLE = (213, 20, 219)
    BLACK = (0, 0, 0)