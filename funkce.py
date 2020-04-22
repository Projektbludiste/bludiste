def main():
    # vytvoření mřížky
    def grid_setup(x, y, w):
        for i in range(1, int(slozitost) + 1):  # generuje bludiště 20x20
            x = 20  # zadani x souradnic na zacatek
            y = y + x  # začátek nové řady
            for j in range(1, int(slozitost) + 1):
                # pygame kod
                pygame.draw.line(screen, black, [x, y], [x + w, y])  # vrsek bunky
                pygame.draw.line(screen, black, [x + w, y], [x + w, y + w])  # pravá strana
                pygame.draw.line(screen, black, [x + w, y + w], [x, y + w])  # spodek buňky
                pygame.draw.line(screen, black, [x, y + w], [x, y])  # levá strana buňky
                grid.append((x, y))
                x = x + 20

    # pohyby
    def nahoru(x, y):
        pygame.draw.rect(screen, white, (x + 1, y - w + 1, 19, 39), 0)  # draw a rectangle twice the width of the cell
        pygame.display.update()  # to animate the wall being removed

    def dolu(x, y):
        pygame.draw.rect(screen, white, (x + 1, y + 1, 19, 39), 0)
        pygame.display.update()

    def doleva(x, y):
        pygame.draw.rect(screen, white, (x - w + 1, y + 1, 39, 19), 0)
        pygame.display.update()

    def doprava(x, y):
        pygame.draw.rect(screen, white, (x + 1, y + 1, 39, 19), 0)
        pygame.display.update()

    def bunka_setup(x, y):
        pygame.draw.rect(screen, green, (x + 1, y + 1, 18, 18), 0)
        pygame.display.update()

    def backtracking(x, y):
        pygame.draw.rect(screen, white, (x + 1, y + 1, 18, 18), 0)
        time.sleep(0.05)
        pygame.display.update()

    def reseni(x, y):
        # pygame.draw.rect(screen, yellow, (x + 8, y + 8, 5, 5), 0,) # ukáže řešení
        screen.blit(robot, (x, y))
        time.sleep(0.1)
        pygame.display.update()

    # vykreslení bludiště
    def vykresleni(x, y):
        bunka_setup(x, y)  # počátek bludiště
        stack.append((x, y))
        visited.append((x, y))
        while len(stack) > 0:
            time.sleep(.01)
            bunka = []
            if (x + w, y) not in visited and (x + w, y) in grid:
                bunka.append("doprava")
            if (x - w, y) not in visited and (x - w, y) in grid:
                bunka.append("doleva")
            if (x, y + w) not in visited and (x, y + w) in grid:
                bunka.append("dolu")
            if (x, y - w) not in visited and (x, y - w) in grid:
                bunka.append("nahoru")
            if len(bunka) > 0:
                vybrany_smer = random.choice(bunka)
                if vybrany_smer == "doprava":
                    doprava(x, y)
                    solution[(x + w, y)] = x, y
                    x = x + w
                    visited.append((x, y))
                    stack.append((x, y))
                elif vybrany_smer == "doleva":
                    doleva(x, y)
                    solution[(x - w, y)] = x, y
                    x = x - w
                    visited.append((x, y))
                    stack.append((x, y))
                elif vybrany_smer == "nahoru":
                    nahoru(x, y)
                    solution[(x, y - w)] = x, y
                    y = y - w
                    visited.append((x, y))
                    stack.append((x, y))
                elif vybrany_smer == "dolu":
                    dolu(x, y)
                    solution[(x, y + w)] = x, y
                    y = y + w
                    visited.append((x, y))
                    stack.append((x, y))
            else:
                x, y = stack.pop()
                bunka_setup(x, y)
                backtracking(x, y)  # změna barvy na backtracking

    def cesta_zpet(x, y):
        reseni(x, y)
        while (x, y) != (20, 20):  # dokud nejsou na počáteční pozici
            x, y = solution[x, y]
            reseni(x, y)
        time.sleep(.1)


    x, y = 20, 20  # starting position of grid
    grid_setup(20, 20, 20)  # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
    vykresleni(x, y)  # call build the maze  function
    cesta_zpet((20 * slozitost), (20 * slozitost) + 20)  # call the plot solution function
if __name__ == "__main__":
    main()