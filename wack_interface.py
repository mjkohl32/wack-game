
import random
from graphics import *


class Button:
    """
    Makes a clickable button in a graphics window.
    """
    def __init__(self, location, width, height, fillColor, text, textColor, textSize):
        """
        Creates a button with all the parameters.
        Note: text style is automatically bolded.
        Note: size of text does not get automatically fitted into button width and height.
        :param location: Point(x, y) for upperleft corner of button
        :param width: width of button
        :param height: height of button
        :param fillColor: color of button
        :param text: text on button
        :param textColor: color of text
        :param textSize: size of text
        """
        self.upperleft = location
        self.width = width
        self.height = height
        self.lowerright = Point(location.getX() + width, location.getY() + height)
        self.rect = Rectangle(self.upperleft, self.lowerright)
        self.rect.setFill(fillColor)
        self.text = Text(Point((self.lowerright.getX() + self.upperleft.getX()) // 2,
                               (self.lowerright.getY() + self.upperleft.getY()) // 2), text)
        self.text.setStyle('bold')
        self.text.setTextColor(textColor)
        self.text.setSize(textSize)

    def draw(self, window):
        """
        Draws the button.
        :param window: graphics window
        """
        self.rect.draw(window)
        self.text.draw(window)

    def undraw(self):
        """
        Removes the button from the graphics window it is currently in.
        """
        self.rect.undraw()
        self.text.undraw()

    def wasClicked(self, click):
        """
        Takes in a point from a cursor click and returns whether
        the cursor clicked the button or not.
        :param click: Point(x, y) from cursor click
        :return: True or False
        """
        return self.upperleft.getX() <= click.getX() <= self.lowerright.getX() \
               and self.upperleft.getY() <= click.getY() <= self.lowerright.getY()


class Politician:
    """
    Creates an image of a politician head.
    """
    def __init__(self, point, politician_pic):
        """
        Creates an image from a file and puts it at a point.
        :param point: Point(x, y) where head is drawn
        :param politician_pic: filename of image of head
        """
        self.head = Image(point, politician_pic)
        self.center = point

    def draw(self, window):
        """
        Draws the head.
        :param window: graphics window
        """
        self.head.draw(window)

    def undraw(self):
        """
        Removes the button from the graphics window it is currently in.
        """
        self.head.undraw()

    def wasClicked(self, point):
        """
        Takes in a point from a cursor click and returns whether the
        cursor clicked an 80x80 rectangle containing the head or not.
        :param point: Point(x, y) from cursor click
        :return: True or False
        """
        return (self.center.getX() - 40 <= point.getX() <= self.center.getX() + 40) \
               and (self.center.getY() - 40 <= point.getY() <= self.center.getY() + 40)


class InitialInterface:
    """
    Sets up an intro screen, with buttons to pick a politician.
    """
    def __init__(self):
        """
        Creates buttons for each politician and displays text asking
        the player to first choose simulation or to play themselves,
        then to choose a politician.
        """
        self.win = GraphWin('Wack-A-Politician', 400, 400)
        self.win.setBackground('blue')

        self.intro_text = Text(Point(200, 50), 'Welcome to Wack-A-Politician!')
        self.intro_text.setSize(25)
        self.intro_text.setStyle('bold')
        self.intro_text.draw(self.win)
        self.intro_text2 = Text(Point(200, 100), 'First, choose the manner of playing:')
        self.intro_text2.setSize(15)
        self.intro_text3 = Text(Point(200, 100), 'Second, choose a politician to wack:')
        self.intro_text3.setSize(15)
        self.intro_text2.draw(self.win)

        self.sim = Button(Point(150, 150), 100, 50, 'purple', 'Simulation', 'limegreen', 15)
        self.sim.draw(self.win)
        self.playing = Button(Point(150, 220), 100, 50, 'purple', 'Play Myself', 'limegreen', 15)
        self.playing.draw(self.win)

        self.trump = Button(Point(90, 150), 100, 50, 'orangered', 'Trump', 'black', 15)
        self.carson = Button(Point(90, 220), 100, 50, 'rosybrown', 'Ben Carson', 'black', 15)
        self.hillary = Button(Point(90, 290), 100, 50, 'deepskyblue', 'Hillary', 'black', 15)
        self.bernie = Button(Point(210, 150), 100, 50, 'mediumseagreen', 'Bernie', 'black', 15)
        self.obama = Button(Point(210, 220), 100, 50, 'deeppink', 'Obama', 'black', 15)
        self.pence = Button(Point(210, 290), 100, 50, 'khaki', 'Mike Pence', 'black', 15)

        self.quit = Button(Point(0, 0), 60, 20, 'limegreen', 'QUIT GAME', 'yellow', 10)
        self.quit.draw(self.win)

    def select_manner(self):
        """
        Waits for user to either choose to watch a simulation
        or play the game themselves. Also has a blue/red
        alternating background.
        :return: a string, either 'sim' or 'play'
        """
        start_time = time.time()
        manner = ''
        keep_running = True
        while keep_running:
            new_time = time.time()
            if int(new_time - start_time) % 4 == 0:
                self.win.setBackground('blue')
            elif int(new_time - start_time) % 2 == 0:
                self.win.setBackground('red')
            else:
                click = self.win.checkMouse()
                if click is not None:
                    if self.sim.wasClicked(click):
                        self.sim.undraw()
                        self.playing.undraw()
                        manner = 'sim'
                        keep_running = False
                    elif self.playing.wasClicked(click):
                        self.sim.undraw()
                        self.playing.undraw()
                        manner = 'play'
                        keep_running = False
                    elif self.quit.wasClicked(click):
                        keep_running = False
                        self.win.close()
                    else:
                        pass
        self.trump.draw(self.win)
        self.carson.draw(self.win)
        self.hillary.draw(self.win)
        self.bernie.draw(self.win)
        self.obama.draw(self.win)
        self.pence.draw(self.win)
        return manner

    def select_politician(self):
        """
        Waits for the user to select a politician, while alternating
        red and blue background.
        :return: name of politician,
                 color of politician's screen,
                 pronoun of politician
                 filename of politician head
        """
        start_time = time.time()
        self.win.setBackground('blue')
        keep_running = True
        while keep_running:
            new_time = time.time()
            if int(new_time - start_time) % 4 == 0:
                self.win.setBackground('blue')
            elif int(new_time - start_time) % 2 == 0:
                self.win.setBackground('red')
            else:
                click = self.win.checkMouse()
                if click is not None:
                    if self.trump.wasClicked(click):
                        return 'Donald Trump', 'indianred', 'him', 'trump.gif'
                    elif self.carson.wasClicked(click):
                        return 'Ben Carson', 'indianred', 'him', 'carson.gif'
                    elif self.hillary.wasClicked(click):
                        return 'Hillary Clinton', 'royalblue', 'her', 'hillary.gif'
                    elif self.bernie.wasClicked(click):
                        return 'Bernie Sanders', 'royalblue', 'him', 'bernie.gif'
                    elif self.obama.wasClicked(click):
                        return 'Barack Obama', 'royalblue', 'him', 'obama.gif'
                    elif self.pence.wasClicked(click):
                        return 'Mike Pence', 'indianred', 'him', 'pence.gif'
                    elif self.quit.wasClicked(click):
                        keep_running = False
                        self.win.close()
                    else:
                        pass

    def close(self):
        self.win.close()


class GameInterface:
    """
    Plays the actual game in a window. The parameter determines
    the color of the background and the head that pops up.
    Includes a quit button that can be clicked at any time
    during the game.
    """
    def __init__(self, politician):
        """
        Creates window, quit button, start button, next level button,
        politician head, and initial score.
        :param politician: list of attributes: politician name,
                politician background color, politician pronoun,
                politician head filename
        """
        self.win = GraphWin('Play Wack-A-Politician', 800, 800)
        self.win.setBackground(politician[1])
        self.instructions = Text(Point(400, 70), 'Use your mouse to WACK ' + politician[0] +
                                 ' on the head!\n\nHit ' + politician[2] + ' as many times as possible '
                                 'to rack up points.')
        self.instructions.setSize(20)
        self.instructions.setTextColor('whitesmoke')
        self.instructions.draw(self.win)
        self.quit = Button(Point(0, 0), 60, 20, 'limegreen', 'QUIT GAME', 'yellow', 10)
        self.quit.text.setStyle('bold')
        self.quit.draw(self.win)

        self.start_button = Button(Point(350, 400), 100, 50, 'lawngreen', 'Start!', 'saddlebrown', 15)
        self.start_button.draw(self.win)

        self.hole1 = Circle(Point(175, 300), 25)
        self.hole2 = Circle(Point(325, 300), 25)
        self.hole3 = Circle(Point(475, 300), 25)
        self.hole4 = Circle(Point(625, 300), 25)
        self.hole5 = Circle(Point(175, 450), 25)
        self.hole6 = Circle(Point(325, 450), 25)
        self.hole7 = Circle(Point(475, 450), 25)
        self.hole8 = Circle(Point(625, 450), 25)
        self.hole9 = Circle(Point(175, 600), 25)
        self.hole10 = Circle(Point(325, 600), 25)
        self.hole11 = Circle(Point(475, 600), 25)
        self.hole12 = Circle(Point(625, 600), 25)
        self.hole1.setFill('dimgrey')
        self.hole2.setFill('dimgrey')
        self.hole3.setFill('dimgrey')
        self.hole4.setFill('dimgrey')
        self.hole5.setFill('dimgrey')
        self.hole6.setFill('dimgrey')
        self.hole7.setFill('dimgrey')
        self.hole8.setFill('dimgrey')
        self.hole9.setFill('dimgrey')
        self.hole10.setFill('dimgrey')
        self.hole11.setFill('dimgrey')
        self.hole12.setFill('dimgrey')

        self.next_level_button = Button(Point(350, 400), 100, 50, 'lawngreen', 'Next Level', 'saddlebrown', 15)
        self.image = politician[3]
        self.face = Politician(Point(400, 400), self.image)

        self.score_display = Text(Point(400, 175), 'Current level: ' + str(0)
                                  + '\nCurrent score: ' + str(0))
        self.x = 0
        self.y = 0

    def start(self):
        """
        Starts the game, or quits the game.
        """
        click = self.win.getMouse()
        if self.start_button.wasClicked(click):
            self.start_button.undraw()
        elif self.quit.wasClicked(click):
            self.close()
        else:
            self.start()

    def draw_holes(self):
        self.hole1.draw(self.win)
        self.hole2.draw(self.win)
        self.hole3.draw(self.win)
        self.hole4.draw(self.win)
        self.hole5.draw(self.win)
        self.hole6.draw(self.win)
        self.hole7.draw(self.win)
        self.hole8.draw(self.win)
        self.hole9.draw(self.win)
        self.hole10.draw(self.win)
        self.hole11.draw(self.win)
        self.hole12.draw(self.win)

    def undraw_holes(self):
        self.hole1.undraw()
        self.hole2.undraw()
        self.hole3.undraw()
        self.hole4.undraw()
        self.hole5.undraw()
        self.hole6.undraw()
        self.hole7.undraw()
        self.hole8.undraw()
        self.hole9.undraw()
        self.hole10.undraw()
        self.hole11.undraw()
        self.hole12.undraw()

    def new_spot(self):
        """
        Finds the next spot for the head, making sure it is not
        in the same row or column, let alone the same space, as
        the head before. No return value, reassigns self.x and self.y
        """
        x, y = random.choice([175, 325, 475, 625]), random.choice([300, 450, 600])
        if x == self.x or y == self.y:
            self.new_spot()
        else:
            self.x, self.y = x, y

    def head_pop(self, level):
        """
        Draws a politician head in a new spot, then waits for either
        time to run out or the head to get clicked (or quit button to
        get clicked). Time runs out faster for higher levels.
        :param level: current level of game.
        :return: count for that level
        """
        count = 0
        start_time = time.time()
        self.new_spot()
        self.face = Politician(Point(self.x, self.y), self.image)
        self.face.draw(self.win)
        keep_running = True
        while keep_running:
            new_time = time.time()
            if new_time - start_time >= (11 - level) / 5:
                keep_running = False
            else:
                click = self.win.checkMouse()
                if click is not None:
                    if self.face.wasClicked(click):
                        count += 1
                        keep_running = False
                    elif self.quit.wasClicked(click):
                        self.close()
        self.face.undraw()
        return count

    def update(self, new_level, new_score):
        """
        Updates the current level and score of the player on the screen.
        :param new_level: new level
        :param new_score: new total score
        :return: none
        """
        if self.score_display:
            self.score_display.undraw()
        self.score_display = Text(Point(400, 175), 'Current level: ' + str(new_level)
                                  + '\nCurrent score: ' + str(new_score))
        self.score_display.setSize(18)
        self.score_display.setStyle('bold')
        self.score_display.draw(self.win)

    def play(self):
        """
        Plays the game, up to 10 levels. Ends the game if the player does
        not hit the head enough times in a given level.
        :return: score: total score through the game
                 level: last level the player was on
        """
        score = 0
        level = 1
        self.update(level, score)
        while level < 11:
            count = 0
            self.draw_holes()
            for i in range(8):
                count += self.head_pop(level)
                self.update(level, score + count)
            score += count
            if count < 4:
                break
            self.undraw_holes()
            self.next_level_button.draw(self.win)
            click = self.win.getMouse()
            if self.next_level_button.wasClicked(click):
                level += 1
                self.update(level, score)
                self.next_level_button.undraw()
            elif self.quit.wasClicked(click):
                break
            else:
                level += 1
                self.update(level, score)
                self.next_level_button.undraw()
        self.win.close()
        if level == 11:
            level = 10
        return score, level

    def close(self):
        self.win.close()


class SimulationInterface:
    """
    Simulates the game in a new window. The parameter determines
    the color of the background and the head that pops up.
    """
    def __init__(self, politician):
        """
        Creates window, quit button, start button, next level button,
        politician head, and initial score.
        :param politician: list of attributes: politician name,
                politician background color, politician pronoun,
                politician head filename
        """
        self.win = GraphWin('Play Wack-A-Politician', 800, 800)
        self.win.setBackground(politician[1])
        self.instructions = Text(Point(400, 70), 'Watch this bot WACK ' + politician[0] +
                                 ' on the head!\n\nHit ' + politician[2] + ' as many times as possible, bot!')
        self.instructions.setSize(20)
        self.instructions.setTextColor('whitesmoke')
        self.instructions.draw(self.win)
        self.quit = Button(Point(0, 0), 60, 20, 'limegreen', 'QUIT GAME', 'yellow', 10)
        self.quit.text.setStyle('bold')
        self.quit.draw(self.win)

        self.start_button = Button(Point(350, 400), 100, 50, 'lawngreen', 'Start!', 'saddlebrown', 15)
        self.start_button.draw(self.win)

        self.hole1 = Circle(Point(175, 300), 25)
        self.hole2 = Circle(Point(325, 300), 25)
        self.hole3 = Circle(Point(475, 300), 25)
        self.hole4 = Circle(Point(625, 300), 25)
        self.hole5 = Circle(Point(175, 450), 25)
        self.hole6 = Circle(Point(325, 450), 25)
        self.hole7 = Circle(Point(475, 450), 25)
        self.hole8 = Circle(Point(625, 450), 25)
        self.hole9 = Circle(Point(175, 600), 25)
        self.hole10 = Circle(Point(325, 600), 25)
        self.hole11 = Circle(Point(475, 600), 25)
        self.hole12 = Circle(Point(625, 600), 25)
        self.hole1.setFill('dimgrey')
        self.hole2.setFill('dimgrey')
        self.hole3.setFill('dimgrey')
        self.hole4.setFill('dimgrey')
        self.hole5.setFill('dimgrey')
        self.hole6.setFill('dimgrey')
        self.hole7.setFill('dimgrey')
        self.hole8.setFill('dimgrey')
        self.hole9.setFill('dimgrey')
        self.hole10.setFill('dimgrey')
        self.hole11.setFill('dimgrey')
        self.hole12.setFill('dimgrey')

        self.next_level_button = Button(Point(350, 400), 100, 50, 'lawngreen', 'Next Level', 'saddlebrown', 15)
        self.image = politician[3]
        self.face = Politician(Point(400, 400), self.image)

        self.score_display = Text(Point(400, 175), 'Current level: ' + str(0)
                                  + '\nCurrent score: ' + str(0))
        self.x = 0
        self.y = 0

        self.botx = 400
        self.boty = 400

        self.bot = Circle(Point(self.botx, self.boty), 7)
        self.bot.setFill('purple')

    def start(self):
        """
        Starts the simulation, or quits the simulation.
        """
        click = self.win.getMouse()
        if self.start_button.wasClicked(click):
            self.start_button.undraw()
            self.quit.undraw()
        elif self.quit.wasClicked(click):
            self.close()
        else:
            self.start()

    def draw_holes(self):
        self.hole1.draw(self.win)
        self.hole2.draw(self.win)
        self.hole3.draw(self.win)
        self.hole4.draw(self.win)
        self.hole5.draw(self.win)
        self.hole6.draw(self.win)
        self.hole7.draw(self.win)
        self.hole8.draw(self.win)
        self.hole9.draw(self.win)
        self.hole10.draw(self.win)
        self.hole11.draw(self.win)
        self.hole12.draw(self.win)

    def undraw_holes(self):
        self.hole1.undraw()
        self.hole2.undraw()
        self.hole3.undraw()
        self.hole4.undraw()
        self.hole5.undraw()
        self.hole6.undraw()
        self.hole7.undraw()
        self.hole8.undraw()
        self.hole9.undraw()
        self.hole10.undraw()
        self.hole11.undraw()
        self.hole12.undraw()

    def new_spot(self):
        """
        Finds the next spot for the head, making sure it is not
        in the same row or column, let alone the same space, as
        the head before. No return value, reassigns self.x and self.y
        """
        x, y = random.choice([175, 325, 475, 625]), random.choice([300, 450, 600])
        if x == self.x or y == self.y:
            self.new_spot()
        else:
            self.x, self.y = x, y

    def move_bot(self, x, y):
        """
        Gets the bot to go towards the next spot once the head pops up.
        """
        changeX = x - self.botx
        changeY = y - self.boty
        dist = (changeX**2 + changeY**2) **(1/2)
        if dist < 250:
            scalar = 10
        elif dist < 350:
            scalar = 12
        else:
            scalar = 15
        self.bot = Circle(Point(self.botx, self.boty), 7)
        self.bot.setFill('yellow')
        self.bot.draw(self.win)
        while self.botx != x and self.boty != y:
            self.bot.undraw()
            self.botx += changeX/scalar
            self.boty += changeY/scalar
            self.bot = Circle(Point(self.botx, self.boty), 7)
            self.bot.setFill('yellow')
            self.bot.draw(self.win)
        self.bot.undraw()

    def head_pop(self):
        """
        Draws a politician head in a new spot, then waits for
        bot to reach it.
        :return: count for that level
        """
        count = 0
        self.new_spot()
        self.face = Politician(Point(self.x, self.y), self.image)
        self.face.draw(self.win)
        self.move_bot(self.x, self.y)
        count += 1
        self.face.undraw()
        return count

    def update(self, new_level, new_score):
        """
        Updates the current level and score of the bot on the screen.
        :param new_level: new level
        :param new_score: new total score
        :return: none
        """
        if self.score_display:
            self.score_display.undraw()
        self.score_display = Text(Point(400, 175), 'Current level: ' + str(new_level)
                                  + '\nCurrent score: ' + str(new_score))
        self.score_display.setSize(18)
        self.score_display.setStyle('bold')
        self.score_display.draw(self.win)

    def play(self):
        """
        Plays the game, up to 10 levels.
        :return: score: total score at end of simulation
                 level: last level the bot was on
        """
        score = 0
        level = 1
        self.update(level, score)
        while level < 11:
            self.draw_holes()
            count = 0
            for i in range(8):
                count += self.head_pop()
                self.update(level, score + count)
            score += count
            self.undraw_holes()
            self.next_level_button.draw(self.win)
            time.sleep(0.4)
            self.next_level_button.undraw()
            level += 1
            self.update(level, score)
        self.win.close()
        return score, level - 1

    def close(self):
        self.win.close()


class FinalInterface:
    """
    Creates a final screen, with final score and
    option to quit or play again.
    """
    def __init__(self, manner, score, politician):
        """
        Creates a window with the politician's background color
        :param score:
        :param politician:
        """
        self.win = GraphWin('Wack-A-Politician', 400, 400)
        self.win.setBackground(politician[1])

        self.quit = Button(Point(150, 250), 100, 40, 'limegreen', 'QUIT GAME', 'yellow', 15)
        self.quit.text.setStyle('bold')
        self.quit.draw(self.win)
        self.play = Button(Point(140, 300), 120, 40, 'limegreen', 'PLAY AGAIN!', 'yellow', 15)
        self.play.text.setStyle('bold')
        self.play.draw(self.win)

        if manner == 'play':
            if score[1] < 4 or score[0] <= 20:
                self.score = Text(Point(200, 100), 'You ended on level ' + str(score[1])
                                  + '.\nYikes! Looks like wacking is not your thing.\nYou only hit '
                                  + politician[0] + ' ' + str(score[0])
                                  + ' times!\nLame! You can do better than that.')
                self.score.setSize(20)
                self.score.draw(self.win)
            else:
                self.score = Text(Point(200, 100), 'You ended on level ' + str(score[1])
                                  + '.\nLooks like wacking is your calling!\nWow! You hit '
                                  + politician[0] + ' '+ str(score[0]) + ' times!')
                self.score.setSize(20)
                self.score.draw(self.win)
        else:
            self.score = Text(Point(200, 100), 'The bot ended on level ' + str(score[1])
                              + '.\nLooks like wacking is its calling!\nWow! It hit '
                              + politician[0] + ' ' + str(score[0]) + ' times!\nCan YOU do that?')
            self.score.setSize(20)
            self.score.draw(self.win)

    def close(self):
        """
        Waits for user to choose to quit or play again.
        :return: True or False
        """
        click = self.win.getMouse()
        if self.quit.wasClicked(click):
            self.win.close()
            return False
        if self.play.wasClicked(click):
            self.win.close()
            return True
        else:
            self.close()


