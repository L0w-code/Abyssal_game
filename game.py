import pygame
import pytmx
import pyscroll

from player import Player


class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jeu-exploration")

        tmx_data = pytmx.util_pygame.load_pygame(r'C:/Users/doria/Documents/travail/prepa2-S2/jeu-tipe/carte.tmx')

        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)
        self.walls = []
        self.tre = []
        self.tre_name = []
        self.layers = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "tre":
                self.tre_name.append(obj.name)
                self.tre.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=25)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def text_counter(self, count, myfont):
        text = "vous avez " + str(count) + " trésors"
        textsurface = myfont.render(text, False, (0, 0, 0))
        self.screen.blit(textsurface, (350, 5))

    def victory(self, count):
        if count == 20:
            self.screen.blit(pygame.image.load("win.png"), (0, 0))

    def update(self, count):
        self.group.update()

        for sprite in self.group.sprites():
            if self.player.rect.collidelist(self.tre) > -1:
                index = self.player.rect.collidelist(self.tre)
                self.tre.pop(index)
                name = self.tre_name[index]
                #print(name)
                #self.remove_tre(name)

                count = count + 1

            elif sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

        return count

    def run(self):

        tmx_data = pytmx.util_pygame.load_pygame(r'C:/Users/doria/Documents/travail/prepa2-S2/jeu-tipe/carte.tmx')
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        clock = pygame.time.Clock()
        running = True

        count = 19
        while running:

            self.player.save_location()
            self.handle_input()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)

            count = self.update(count)
            self.text_counter(count, myfont)
            self.victory(count)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        running = False

            clock.tick(60)

        pygame.QUIT()

"""
    def remove_tre(self, name):
        tmx_data = pytmx.util_pygame.load_pygame(r'C:/Users/doria/Documents/travail/prepa2-S2/jeu-tipe/carte.tmx')

        tmx_data.layers.get_layer_by_name(name)
        tmx_data.layers.remove(name)

        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        self.player = Player(self.old_position[0], self.old_position[1])
        self.walls = []
        self.tre = []
        self.tre_name = []
        self.layers = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "tre":
                self.tre_name.append(obj.name)
                self.tre.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
"""