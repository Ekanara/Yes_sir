import pygame as pg

_ = False
mini_map = [
    #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, _, _, _, _, _, _, _, 1, 1, _, 1,],
    [1, _, _, 1, _, 1, _, _, _, _, _, 1,],
    [1, _, _, _, _, _, _, 1, _, 1, _, 1,],
    [1, _, _, _, _, _, _, _, _, 1, _, 1,],
    [1, _, _, 1, _, _, _, 1, _, _, _, 1,],
    [1, _, _, _, _, 1, _, _, _, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    #[1, _, _, _, _, _, _, _, _, 1, 1, 1,],
    #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
]
# Dùng ctrl H để thay đổi dữ liệu dễ (nếu dùng vscode, ko chắc pycharm lmao)
class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(surface = self.game.screen, 
                      color = 'darkgray', 
                      rect = (pos[0] * 100, pos[1] * 100, 100, 100), 
                      width = 1)
        for pos in self.world_map]