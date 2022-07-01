import random
import pygame

pygame.init()

WIDTH = 600    
HEIGHT = 320
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# This is the title at the top of the game
pygame.display.set_caption('Tenzi!')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
background = (252, 3, 232)
white = (255, 255, 255)
black = (0, 0, 0)
teal = (3, 248, 252)
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
roll = False
won = False
selected = [False, False, False, False,
            False, False, False, False, False, False]
round_number = 1
num_rolls = 0 
# select_to_keep = False


class Dice:
    def __init__(self, x_pos, y_pos, num, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        global selected
        self.key = key
        self.active = selected[self.key]
        self.die = ''
        self.selected = selected[key]

    def draw(self):  # draw the die faces 1 through 6
        self.die = pygame.draw.rect(screen, (255, 255, 255), [
                                    self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 5:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 6:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.active:
            pygame.draw.rect(screen, (255, 0, 0), [
                             self.x_pos, self.y_pos, 100, 100], 4, 5)
        if self.selected:
            pygame.draw.rect(screen, (235, 37, 19), [
                             self.x_pos, self.y_pos, 100, 100], 4, 5)

    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if selected[self.key]:
                self.selected = False
                selected[self.key] = False
            else:
                selected[self.key] = True # check to see if the ones are all selected for round one and so forth
                self.selected = True
                check_round_complete()


class Choice:
    def __init__(self, x_pos, Y_pos, text, select, possible, used):
        self.x_pos = x_pos
        self.y_pos = Y_pos
        self.text = text
        self.select = select
        self.possible = possible
        self.used = used
        # self.select_to_keep = select_to_keep

    def draw(self):
        pygame.draw.line(screen, white, (self.x_pos, self.y_pos),
                         (self.x_pos + 255, self.y_pos), 2)
        pygame.draw.line(screen, white, (self.x_pos, self.y_pos + 30),
                         (self.x_pos + 255, self.y_pos + 30), 2)

        if not self.used:
            if self.possible:
                my_text = font.render(self.text, True, teal)
            elif not self.possible:
                my_text = font.render(self.text, True, teal)
            else:
                my_text = font.render(self.text, True, black)
        screen.blit(my_text, (self.x_pos + 5, self.y_pos + 10))


def reset():
    global won
    global numbers
    global selected
    global roll
    global round_number
    global num_rolls
    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    roll = False
    won = False
    selected = [False, False, False, False,
                False, False, False, False, False, False]
    round_number = 1
    num_rolls = 0
    


def check_round_complete():
    global selected
    global round_number
    global won
    round_complete = True
    for number in numbers:
        if number != round_number:  # whatever number the user is trying for in the number level
            round_complete = False
    if round_complete:
        if round_number == 6:
            won = True
        else:
            round_number += 1
            selected = [False, False, False, False,
                False, False, False, False, False, False]


running = True
while running:
    timer.tick(fps)
    screen.fill(background)


    # screen.blit(rolls_text, (15, 15))
    # call the instance of the class
    if not won:

        die1 = Dice(10, 50, numbers[0], 0)
        die2 = Dice(130, 50, numbers[1], 1)
        die3 = Dice(250, 50, numbers[2], 2)
        die4 = Dice(370, 50, numbers[3], 3)
        die5 = Dice(490, 50, numbers[4], 4)
        die6 = Dice(10, 170, numbers[5], 5)
        die7 = Dice(130, 170, numbers[6], 6)
        die8 = Dice(250, 170, numbers[7], 7)
        die9 = Dice(370, 170, numbers[8], 8)
        die10 = Dice(490, 170, numbers[9], 9)
        # ones = Choice(0, 220, 'Ones', True, True, False)
        # twos = Choice(0, 250, 'Twos', True, True, False)
        # threes = Choice(0, 280, 'Threes', True, True, False)
        # fours = Choice(0, 310, 'Fours', True, True, False)
        # fives = Choice(0, 340, 'Fives', True, True, False)
        # sixes = Choice(0, 370, 'Sixes', True, True, False)
        # sum = Choice(0, 400, 'Sum', False, False, False)

        # player_1 = Choice(300, 190, 'Player 1', True, True, False)

        button1 = pygame.draw.rect(screen, (0, 0, 0), [10, 280, 280, 30])

        # button2 = pygame.draw.rect(screen, (0, 0, 0), [310, 160, 280, 30])
        
        num_rolls_text =  font.render(f"Rolls: {num_rolls}", True, white)
        screen.blit(num_rolls_text, (400, 287))

        roll_text = font.render(f"Trying For {round_number}'s", True, white)
        screen.blit(roll_text, (240, 10))
        roll_text = font.render('Click to Roll', True, white)
        screen.blit(roll_text, (85, 287))

        # accept_turn_text = font.render('Accept Turn', True, white)
        # screen.blit(accept_turn_text, (375, 167))
        die1.draw()
        die2.draw()
        die3.draw()
        die4.draw()
        die5.draw()
        die6.draw()
        die7.draw()
        die8.draw()
        die9.draw()
        die10.draw() 
        # ones.draw()
        # twos.draw()
        # threes.draw()
        # fours.draw()
        # fives.draw()
        # sixes.draw()
        # sum.draw()

        # player_1.draw()

        for event in pygame.event.get():  # Event Handling without this condition it will be an infinite loop
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                die1.check_click(event.pos)
                die2.check_click(event.pos)
                die3.check_click(event.pos)
                die4.check_click(event.pos)
                die5.check_click(event.pos)
                die6.check_click(event.pos)
                die7.check_click(event.pos)
                die8.check_click(event.pos)
                die9.check_click(event.pos)
                die10.check_click(event.pos)
                if button1.collidepoint(event.pos):
                    roll = True

        if roll:
            num_rolls += 1
            for number in range(len(numbers)):
                if not selected[number]:
                    numbers[number] = random.randint(1, 6)
            roll = False

    else:
        roll_text = font.render(f'You completed the game in {num_rolls} rolls!!', True, white)
        screen.blit(roll_text, (85, 200))
        button1 = pygame.draw.rect(screen, (0, 0, 0), [10, 160, 280, 30])
        reset_text = font.render('Play Again', True, white)
        screen.blit(reset_text, (85, 167))
        for event in pygame.event.get():  # Event Handling without this condition it will be an infinite loop
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    reset()
    pygame.display.flip()


pygame.quit()
