import pygame

from Classes import VerticalLine, HorizontalLine, Cell, Game
from typing import Dict, Tuple
print("Leave empty for default config")
scale = input("Scale (Default 10): ")
if scale == "":
    scale = 10
else:
    scale = int(scale)
Horizontal = input("Horizontal length (Default 10): ")
if Horizontal == "":
    Horizontal = 10
else:
    Horizontal = int(Horizontal)
Vertical = input("Vertical length (default): ")
if Vertical == "":
    Vertical = 10
else:
    Vertical = int(Vertical)
pygame.init()
screen = pygame.display.set_mode(((6 * Horizontal - 1) * scale, (6 * Vertical - 1) * scale))
pygame.display.set_caption("Conway")
clock = pygame.time.Clock()
VerticalLines = {}
x = 0
for i in range(Horizontal):
    x = (i * 6 - 1) * scale
    VerticalLines[i] = VerticalLine(scale, (6 * Vertical - 1) * scale, x, 0, "White", i, pygame.Surface((scale, (6 * Vertical - 1) * scale)), None)
    VerticalLines[i].surf.fill(VerticalLines[i].color)
    VerticalLines[i].rect = VerticalLines[i].surf.get_rect(topleft=(x, 0))
HorizontalLines = {}
y = 0
for i in range(Vertical):
    y = (i * 6 - 1) * scale
    HorizontalLines[i] = HorizontalLine(scale, (6 * Horizontal - 1) * scale, 0, y, "White", i, pygame.Surface(((6 * Horizontal - 1) * scale, scale)), None)
    HorizontalLines[i].surf.fill(HorizontalLines[i].color)
    HorizontalLines[i].rect = HorizontalLines[i].surf.get_rect(topleft=(0, y))
Cells: Dict[Tuple[int, int], Cell] = {}
for x in range(Horizontal):
    for y in range(Vertical):
        Cells[x, y] = Cell(x * 6 * scale, y * 6 * scale, x, y, "Red", pygame.Surface((5 * scale, 5 * scale)), None, [],[],False, False)
        Cells[x, y].surf.fill(Cells[x, y].color)
        Cells[x, y].rect = Cells[x, y].surf.get_rect(topleft=(x * 6 * scale, y * 6 * scale))
for cell in Cells.values():
    if cell.gridx == 0 and cell.gridy == 0:
        # Top left cell
        cell.adjacent.append(Cells[cell.gridx + 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy + 1])
        cell.near.append(Cells[cell.gridx + 1, cell.gridy + 1])
    elif cell.gridx == 0 and cell.gridy != Vertical - 1:
        # Left column
        cell.adjacent.append(Cells[cell.gridx + 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy + 1])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy - 1])
        cell.near.append(Cells[cell.gridx + 1, cell.gridy + 1])
        cell.near.append(Cells[cell.gridx + 1, cell.gridy - 1])
    elif cell.gridx == 0 and cell.gridy == Vertical - 1:
        # Bottom left cell
        cell.adjacent.append(Cells[cell.gridx + 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy - 1])
        cell.near.append(Cells[cell.gridx + 1, cell.gridy - 1])
    elif cell.gridx != Horizontal - 1 and cell.gridy == 0:
        # Top row
        cell.adjacent.append(Cells[cell.gridx - 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx + 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy + 1])
        cell.near.append(Cells[cell.gridx - 1, cell.gridy + 1])
        cell.near.append(Cells[cell.gridx + 1, cell.gridy + 1])
    elif cell.gridx == Horizontal - 1 and cell.gridy == 0:
        # Top right cell
        cell.adjacent.append(Cells[cell.gridx - 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy + 1])
        cell.near.append(Cells[cell.gridx - 1, cell.gridy + 1])
    elif cell.gridx != Horizontal - 1 and cell.gridy != Vertical - 1:
        # Middle cells
        cell.adjacent.append(Cells[cell.gridx - 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx + 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy - 1])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy + 1])
        cell.near.append(Cells[cell.gridx - 1, cell.gridy + 1])
        cell.near.append(Cells[cell.gridx + 1, cell.gridy + 1])
        cell.near.append(Cells[cell.gridx - 1, cell.gridy - 1])
        cell.near.append(Cells[cell.gridx + 1, cell.gridy - 1])
    else:
        # Bottom right cell
        cell.adjacent.append(Cells[cell.gridx - 1, cell.gridy])
        cell.adjacent.append(Cells[cell.gridx, cell.gridy - 1])
        cell.near.append(Cells[cell.gridx - 1, cell.gridy - 1])
space = Horizontal // 5
Cells[space, Vertical // 5].isAlive = True
Cells[Horizontal - space - 1, Vertical // 5].isAlive = True
Cells[1, Vertical * 3 // 5].isAlive = True
Cells[Horizontal - 2, Vertical * 3 // 5].isAlive = True
for i in range(2, Horizontal - 2):
    Cells[i, Vertical * 7 // 10].isAlive = True
numOfAlive = 0
Game = Game(False, False, True)
Mouse = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            Game.auto = not Game.auto
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            Game.step = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            Game.FFD = not Game.FFD
        if event.type == pygame.MOUSEBUTTONDOWN and not Game.auto:
            Mouse = pygame.mouse.get_pos()
            for Cell in Cells.values():
                if Cell.rect.collidepoint(Mouse) and pygame.mouse.get_pressed()[0]:
                    Cell.isAlive = not Cell.isAlive
                    Cell.willLive = not Cell.willLive

    screen.fill("Black")
    for line in VerticalLines.values():
        screen.blit(line.surf, (line.x, line.y))
    for line in HorizontalLines.values():
        screen.blit(line.surf, (line.x, line.y))

    if not Game.auto:
        Mouse = pygame.mouse.get_pos()
        for Cell in Cells.values():
            if Cell.rect.collidepoint(Mouse) and pygame.mouse.get_pressed()[2]:
                Cell.isAlive = not Cell.isAlive
                Cell.willLive = not Cell.willLive
    for cell in Cells.values():
        if cell.isAlive:
            screen.blit(cell.surf, (cell.x, cell.y))
        if Game.auto or Game.step:
            numOfAlive = 0
            #Live neighbour count
            for adj in cell.adjacent:
                if adj.isAlive:
                    numOfAlive += 1
            for near in cell.near:
                if near.isAlive:
                    numOfAlive += 1
            #Determining the next stage
            if numOfAlive == 3 or (numOfAlive == 2 and cell.isAlive):
                cell.willLive = True
            else:
                cell.willLive = False
        else:
            if cell.isAlive:
                cell.willLive = True
            else:
                cell.willLive = False
    Game.step = False
    for cell in Cells.values():
        if cell.willLive:
            cell.isAlive = True
        else:
            cell.isAlive = False
    pygame.display.update()
    if Game.FFD:
        clock.tick(30)
    else:
        clock.tick(5)