import pygame
import sys
from pygame.rect import Rect
from interface.gamestate import ButtonNumber
from interface.gamestate import GameState
from interface.uielement import UIElement
from solve import *
import time


BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
LIGHTCOLORS=[(255,204,204),(255,229,204),(255,255,204),(229,255,204),(204,255,204),(204,255,229),(204,255,255),(204,229,255),(204,204,255),(229,204,255),(255,204,255),(255,204,229), #muito claro
             (255,102,102),(255,178,102),(255,255,102),(178,255,102),(102,255,102),(102,255,178),(102,255,255),(102,178,255),(102,102,255),(178,102,255),(255,102,255),(255,102,178), #medio claro
             (204,  0,  0),(204,102,  0),(204,204,  0),(102,204,  0),( 0 ,204, 0 ),( 0 ,204,102),( 0 ,204,204),( 0 ,102,204),( 0 , 0 ,204),(102, 0 ,204),(204, 0 ,204),(204, 0 ,102)] #pouco claro
DARKCOLORS=[(255,153,153),(255,204,153),(255,255,153),(204,255,153),(153,255,153),(153,255,204),(153,255,255),(153,204,255),(153,153,255),(204,153,255),(255,153,255),(255,153,204),  #pouco escuro
             (255, 0,  0),(255,128,  0),(255,255,  0),(128,255,  0),(0 , 255,  0),(0, 255, 128),( 0, 255,255),( 0, 128,255),( 0,  0, 255),(127, 0, 255),(255, 0, 255),(255, 0, 127),  #medio escuro
             (102, 0 , 0),(102, 51, 0 ),(102,102, 0 ),( 51,102, 0 ),( 0 ,102, 0 ),( 0 ,102, 51),( 0 ,102,102),( 0 , 51,102),( 0 , 0 ,102),( 51, 0 ,102),(102, 0 ,102),(102, 0 , 51)]  #muito escuro

BMS=[ ButtonNumber.BM1, ButtonNumber.BM2, ButtonNumber.BM3, ButtonNumber.BM4, ButtonNumber.BM5, ButtonNumber.BM6, ButtonNumber.BM7, ButtonNumber.BM8,ButtonNumber.BM9,ButtonNumber.BM10,ButtonNumber.BM11,ButtonNumber.BM12,ButtonNumber.BM13,ButtonNumber.BM14,ButtonNumber.BM15,ButtonNumber.BM16,ButtonNumber.BM17,ButtonNumber.BM18,ButtonNumber.BM19,ButtonNumber.BM20,ButtonNumber.BM21,ButtonNumber.BM22,ButtonNumber.BM23,ButtonNumber.BM24,ButtonNumber.BM25,ButtonNumber.BM26,ButtonNumber.BM27,ButtonNumber.BM28,ButtonNumber.BM29,ButtonNumber.BM30,ButtonNumber.BM31,ButtonNumber.BM32,ButtonNumber.BM33,ButtonNumber.BM34,ButtonNumber.BM35]
BPS=[ ButtonNumber.BP1, ButtonNumber.BP2, ButtonNumber.BP3, ButtonNumber.BP4, ButtonNumber.BP5, ButtonNumber.BP6, ButtonNumber.BP7, ButtonNumber.BP8,ButtonNumber.BP9,ButtonNumber.BP10,ButtonNumber.BP11,ButtonNumber.BP12,ButtonNumber.BP13,ButtonNumber.BP14,ButtonNumber.BP15,ButtonNumber.BP16,ButtonNumber.BP17,ButtonNumber.BP18,ButtonNumber.BP19,ButtonNumber.BP20,ButtonNumber.BP21,ButtonNumber.BP22,ButtonNumber.BP23,ButtonNumber.BP24,ButtonNumber.BP25,ButtonNumber.BP26,ButtonNumber.BP27,ButtonNumber.BP28,ButtonNumber.BP29,ButtonNumber.BP30,ButtonNumber.BP31,ButtonNumber.BP32,ButtonNumber.BP33,ButtonNumber.BP34,ButtonNumber.BP35]
class Interface:
    def __init__(self, initial_node):
            self.initial_node=initial_node
            self.currNode=initial_node
            self.n= len(initial_node.state.aquarium)
            self.screen = pygame.display.set_mode((800, 900))

    def updateNode(self,node):
        self.currNode=node


    def main_menu(self):
        human_mode = UIElement(
            center_position=(400, 250),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="1. Human Mode",
            action=GameState.HUMAN_MODE,
        )
        pc_mode = UIElement(
            center_position=(400, 325),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="2. PC Mode",
            action=GameState.PC_MODE,
        )
        quit_btn = UIElement(
            center_position=(400,400),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="3. Exit",
            action=GameState.QUIT,
        )

        title = UIElement(
            center_position=(400, 125),
            font_size=50,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="MAIN MENU",
        )
        
        buttons = [human_mode, pc_mode,quit_btn]
        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)

            pygame.draw.line(self.screen,BLUE,(0,75),(pygame.Surface.get_width(self.screen),75))
            pygame.draw.line(self.screen,BLUE,(0,175),(pygame.Surface.get_width(self.screen),175))

            pygame.display.flip()

    def human_mode(self):
        fill = UIElement(
            center_position=(160, 800),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Fill",
            action=GameState.FILL,
        )
        unfill = UIElement(
            center_position=(320, 800),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Unfill",
            action=GameState.UNFILL,
        )
        hint = UIElement(
            center_position=(480,800),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Hint",
            action=GameState.HINT,
        )

        quit_btn = UIElement(
            center_position=(640, 800),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Exit",
            action=GameState.QUIT,
        )

        title = UIElement(
            center_position=(400, 50),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="AQUARIUM",
        )
        buttons = [quit_btn,fill, unfill, hint]

        while True:
                      
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)


            pygame.draw.line(self.screen,BLUE,(0,20),(pygame.Surface.get_width(self.screen),20))
            pygame.draw.line(self.screen,BLUE,(0,80),(pygame.Surface.get_width(self.screen),80))
            self.displayAquarium()

            pygame.display.flip()


    def displayAquarium(self):
        n=550/self.n
        start_width=125
        start_height=125
        x=0
        y=0
        for line in self.currNode.state.aquarium:
            for cells in line:
                if(cells<0):
                    pygame.draw.rect(self.screen,LIGHTCOLORS[abs(cells)-1], ((start_width+x,start_height+y),(n,n)))
                    cell=UIElement(
                        center_position=((start_width+x+(n/2),start_height+y+(n/2))),
                        font_size=20,
                        bg_rgb=LIGHTCOLORS[abs(cells)-1],
                        text_rgb=BLACK,
                        text=str(cells),
                    )
                    cell.draw(self.screen)
                else:
                    pygame.draw.rect(self.screen,DARKCOLORS[abs(cells)-1], ((start_width+x,start_height+y),(n,n)))
                    cell=UIElement(
                        center_position=((start_width+x+(n/2),start_height+y+(n/2))),
                        font_size=20,
                        bg_rgb=DARKCOLORS[abs(cells)-1],
                        text_rgb=BLACK,
                        text=str(cells),
                    )
                    cell.draw(self.screen)
                
                x+=n
            x=0
            y+=n

        for i in range(self.n-1):
            pygame.draw.line(self.screen,WHITE,(start_width,start_height+(i+1)*n),(675,start_height+(i+1)*n),3)
            pygame.draw.line(self.screen,WHITE,(start_width+(i+1)*n,start_height),(start_width+(i+1)*n,675),3)
        
        #displayRowCap
        for i in range(self.n):
            rowCap=UIElement(
                center_position=(75,start_height-(n/2)+(i+1)*n),
                font_size=20,
                bg_rgb=WHITE,
                text_rgb=BLUE,
                text=str(self.currNode.state.rowCap[i]),
            )
            rowCap.draw(self.screen)

        #displayColCap()
        for i in range(self.n):
            colCap=UIElement(
                center_position=(start_width-(n/2)+(i+1)*n,725),
                font_size=20,
                bg_rgb=WHITE,
                text_rgb=BLUE,
                text=str(self.currNode.state.colCap[i]),
            )
            colCap.draw(self.screen)
        

    def pc_mode(self):
        #menu algorithm
        its = UIElement(
            center_position=(400,250),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="1. Iterative Deepening Search",
            action=GameState.ITS,
        )
        bfs = UIElement(
            center_position=(400, 325),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="2. Breadth First Search",
            action=GameState.BFS,
        )
        dfs = UIElement(
            center_position=(400, 400),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="3. Depth First Search",
            action=GameState.DFS,
        )
        ucs = UIElement(
            center_position=(400,475),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="4. Uniform Cost Search",
            action=GameState.UCS,
        )
   
        greedy = UIElement(
            center_position=(400, 550),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="5. Greedy Search",
            action=GameState.GREEDY,
        )
        a_star = UIElement(
            center_position=(400, 625),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="6. A Star",
            action=GameState.ASTAR,
        )
        return_menu = UIElement(
            center_position=(400,700),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="7. Return",
            action=GameState.RETURN,
        )
        quit_btn = UIElement(
            center_position=(400,775),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="8. Exit",
            action=GameState.QUIT,
        )
        title = UIElement(
            center_position=(400, 125),
            font_size=50,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="ALGORITHM MENU",
        )
        
        buttons = [bfs,dfs,ucs,its,greedy,a_star,return_menu,quit_btn]
        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)

            pygame.draw.line(self.screen,BLUE,(0,75),(pygame.Surface.get_width(self.screen),75))
            pygame.draw.line(self.screen,BLUE,(0,175),(pygame.Surface.get_width(self.screen),175))

            pygame.display.flip()

    def loading_screen(self, algorithm):
        title = UIElement(
            center_position=(400, 400),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="LOADING...",
        )
        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
           
            #pygame.draw.rect(self.screen)


            pygame.draw.line(self.screen,BLUE,(0,300),(pygame.Surface.get_width(self.screen),300))
            pygame.draw.line(self.screen,BLUE,(0,500),(pygame.Surface.get_width(self.screen),500))

            pygame.display.flip()

            if algorithm=="human_mode":
                self.result = aStar(self.initial_node, True)
                self.nAquariums = max([abs(x) for x in set(sum(self.initial_node.state.aquarium,[]))]) #Number of aquariums
                self.aquariumsFilled = numAquariumsFilled(self.nAquariums,self.result)
                return
            if algorithm == "bfs": 
                [node, time]=bfs(self.initial_node)
                break
            elif algorithm == "dfs": 
                [node, time]=dfs(self.initial_node)
                break
            elif algorithm == "ucs":
                [node, time]=ucs(self.initial_node)
                break
            elif algorithm == "its": 
                [node, time]=its(self.initial_node)
                break
            elif algorithm == "greedy": 
                [node, time]=greedy(self.initial_node)
                break
            elif algorithm == "aStar": 
                [node, time]=aStar(self.initial_node)
                break
        self.play_algorithm(node,time)

    def play_algorithm(self,node, time):
        self.updateNode(node)

        time_btn=UIElement(
            center_position=(400, 800),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Time: %6fs" % time,
        )
        quit_btn = UIElement(
            center_position=(400, 850),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Exit",
            action=GameState.QUIT,
        )

        title = UIElement(
            center_position=(400, 50),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="AQUARIUM",
        )
        buttons = [quit_btn]

        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
            time_btn.draw(self.screen)
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)


            pygame.draw.line(self.screen,BLUE,(0,20),(pygame.Surface.get_width(self.screen),20))
            pygame.draw.line(self.screen,BLUE,(0,80),(pygame.Surface.get_width(self.screen),80))
            self.displayAquarium()

            pygame.display.flip()

    def fill(self):
        buttons=[]
        title = UIElement(
            center_position=(400, 50),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="AQUARIUM",
        )
        if self.nAquariums>10:
            n=800/11
        else:
            n=800/(self.nAquariums+1)
        x=0
        for i in range(self.nAquariums):
            if i<10:
                if self.nAquariums>10:
                    btn = UIElement(
                        center_position=((x+1)*n, 775),
                        font_size=20,
                        bg_rgb=WHITE,
                        text_rgb=BLUE,
                        text=str(i+1),
                        action=BPS[i],
                    )
                else:
                    btn = UIElement(
                        center_position=((x+1)*n, 800),
                        font_size=20,
                        bg_rgb=WHITE,
                        text_rgb=BLUE,
                        text=str(i+1),
                        action=BPS[i],
                    )
                x+=1
            elif (i>=10 and i<20):
                if i==10:
                    x=0
                btn = UIElement(
                    center_position=((x+1)*n, 800),
                    font_size=20,
                    bg_rgb=WHITE,
                    text_rgb=BLUE,
                    text=str(i+1),
                    action=BPS[i],
                )
                x+=1
            elif (i>=20 and i<30):
                if i==20:
                    x=0
                btn = UIElement(
                    center_position=((x+1)*n, 825),
                    font_size=20,
                    bg_rgb=WHITE,
                    text_rgb=BLUE,
                    text=str(i+1),
                    action=BPS[i],
                )
                x+=1
            elif (i>=30 and i<35):
                if i==30:
                    x=0
                btn = UIElement(
                    center_position=((x+1)*n, 850),
                    font_size=20,
                    bg_rgb=WHITE,
                    text_rgb=BLUE,
                    text=str(i+1),
                    action=BPS[i],
                )
                x+=1
            buttons.append(btn)
        
        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)


            pygame.draw.line(self.screen,BLUE,(0,20),(pygame.Surface.get_width(self.screen),20))
            pygame.draw.line(self.screen,BLUE,(0,80),(pygame.Surface.get_width(self.screen),80))
            self.displayAquarium()

            pygame.display.flip()

    def fillAquarium(self,option):
        newNode=FillHuman(self.currNode, option).apply()
        if newNode!=-1:
            self.updateNode(newNode)
        else:
            self.displayAquarium()
            pygame.draw.rect(self.screen,WHITE, ((0,750),(800,150)))
            UIElement(
                center_position=(400, 800),
                font_size=30,
                bg_rgb=WHITE,
                text_rgb=BLUE,
                text="Invalid Aquarium!",
            ).draw(self.screen)
            pygame.display.flip()
            time.sleep(0.5)
            self.human_mode()

            
    def unfillAquarium(self,option):
        newNode=UnfillHuman(self.currNode, option).apply()
        if newNode!=-1:
            self.updateNode(newNode)
        else:
            self.displayAquarium()
            pygame.draw.rect(self.screen,WHITE, ((0,750),(800,150)))
            UIElement(
                center_position=(400, 800),
                font_size=30,
                bg_rgb=WHITE,
                text_rgb=BLUE,
                text="Invalid Aquarium!",
            ).draw(self.screen)
            pygame.display.flip()
            time.sleep(0.5)
            self.human_mode()



    def unfill(self):
        buttons=[]
        title = UIElement(
            center_position=(400, 50),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="AQUARIUM",
        )
        if self.nAquariums>10:
            n=800/11
        else:
            n=800/(self.nAquariums+1)
        x=0
        for i in range(self.nAquariums):
            if i<10:
                if self.nAquariums>10:
                    btn = UIElement(
                        center_position=((x+1)*n, 775),
                        font_size=20,
                        bg_rgb=WHITE,
                        text_rgb=BLUE,
                        text=str(i+1),
                        action=BMS[i],
                    )
                else:
                    btn = UIElement(
                        center_position=((x+1)*n, 800),
                        font_size=20,
                        bg_rgb=WHITE,
                        text_rgb=BLUE,
                        text=str(i+1),
                        action=BMS[i],
                    )
                x+=1
            elif (i>=10 and i<20):
                if i==10:
                    x=0
                btn = UIElement(
                    center_position=((x+1)*n, 800),
                    font_size=20,
                    bg_rgb=WHITE,
                    text_rgb=BLUE,
                    text=str(i+1),
                    action=BMS[i],
                )
                x+=1
            elif (i>=20 and i<30):
                if i==20:
                    x=0
                btn = UIElement(
                    center_position=((x+1)*n, 825),
                    font_size=20,
                    bg_rgb=WHITE,
                    text_rgb=BLUE,
                    text=str(i+1),
                    action=BMS[i],
                )
                x+=1
            elif (i>=30 and i<35):
                if i==30:
                    x=0
                btn = UIElement(
                    center_position=((x+1)*n, 850),
                    font_size=20,
                    bg_rgb=WHITE,
                    text_rgb=BLUE,
                    text=str(i+1),
                    action=BMS[i],
                )
                x+=1
            buttons.append(btn)
        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)


            pygame.draw.line(self.screen,BLUE,(0,20),(pygame.Surface.get_width(self.screen),20))
            pygame.draw.line(self.screen,BLUE,(0,80),(pygame.Surface.get_width(self.screen),80))
            self.displayAquarium()

            pygame.display.flip()

    def hint(self):
        number=getHint(self.aquariumsFilled, self.currNode)
        title = UIElement(
            center_position=(400, 50),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="AQUARIUM",
        )
        hint = UIElement(
            center_position=(250,800),
            font_size=22,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Hint:",
        )
        hint_btn = UIElement(
            center_position=(300,800),
            font_size=22,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text=str(number),
        )
        ret= UIElement(
            center_position=(500,800),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Return",
            action=GameState.HUMAN_MODE,
        )
        buttons=[ret]
        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
            hint.draw(self.screen)
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)
            hint_btn.draw(self.screen)

            pygame.draw.line(self.screen,BLUE,(0,20),(pygame.Surface.get_width(self.screen),20))
            pygame.draw.line(self.screen,BLUE,(0,80),(pygame.Surface.get_width(self.screen),80))
            self.displayAquarium()

            pygame.display.flip()
        
    def game_over(self):
        congrats= UIElement(
            center_position=(400,800),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="CONGRATULATIONS! YOU HAVE SOLVED THE PUZZLE",
        )
        quit_btn = UIElement(
            center_position=(400, 850),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="Exit",
            action=GameState.QUIT,
        )

        title = UIElement(
            center_position=(400, 50),
            font_size=30,
            bg_rgb=WHITE,
            text_rgb=BLUE,
            text="AQUARIUM",
        )
        buttons = [quit_btn]

        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(WHITE)

            title.draw(self.screen)
            congrats.draw(self.screen)
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)


            pygame.draw.line(self.screen,BLUE,(0,20),(pygame.Surface.get_width(self.screen),20))
            pygame.draw.line(self.screen,BLUE,(0,80),(pygame.Surface.get_width(self.screen),80))
            self.displayAquarium()

            pygame.display.flip()

    def main(self):
        pygame.init()

        game_state = GameState.TITLE
        flag=False #to update a node after ending a game
        human_mode=False
        while True:
            if isObjective(self.currNode):
                if human_mode:
                    self.game_over()
                pygame.quit()
                return

            if game_state == GameState.TITLE:
                self.updateNode(self.initial_node)
                flag=True
                human_mode=False
                game_state = self.main_menu()

            if game_state == GameState.HUMAN_MODE:
                if(flag):
                    self.loading_screen("human_mode")
                human_mode=True
                game_state = self.human_mode()
                flag=False

            if game_state == GameState.PC_MODE:
                game_state = self.pc_mode()

            if game_state == GameState.QUIT:
                pygame.quit()
                return
            
            if game_state == GameState.FILL:
                game_state = self.fill()

            if game_state == GameState.UNFILL:
                game_state = self.unfill()
            
            if game_state == GameState.HINT:
                game_state = self.hint()
            
            if game_state == GameState.BFS:
                game_state = self.loading_screen("bfs")

            if game_state == GameState.DFS:
                game_state = self.loading_screen("dfs")
            
            if game_state == GameState.UCS:
                game_state = self.loading_screen("ucs")
            
            if game_state == GameState.ITS:
                game_state = self.loading_screen("its")

            if game_state == GameState.GREEDY:
                game_state = self.loading_screen("greedy")
            
            if game_state == GameState.ASTAR:
                game_state = self.loading_screen("aStar")

            if game_state == GameState.RETURN:
                game_state = self.main_menu()

            #UNFILL
            if game_state==ButtonNumber.BM1:
                self.unfillAquarium(-1)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM2:
                self.unfillAquarium(-2)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM3:
                self.unfillAquarium(-3)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM4:
                self.unfillAquarium(-4)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM5:
                self.unfillAquarium(-5)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM6:
                self.unfillAquarium(-6)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM7:
                self.unfillAquarium(-7)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM8:
                self.unfillAquarium(-8)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM9:
                self.unfillAquarium(-9)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM10:
                self.unfillAquarium(-10)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM11:
                self.unfillAquarium(-11)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM12:
                self.unfillAquarium(-12)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM13:
                self.unfillAquarium(-13)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM14:
                self.unfillAquarium(-14)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM15:
                self.unfillAquarium(-15)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM16:
                self.unfillAquarium(-16)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM17:
                self.unfillAquarium(-17)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM18:
                self.unfillAquarium(-18)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM19:
                self.unfillAquarium(-1)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM20:
                self.unfillAquarium(-20)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM21:
                self.unfillAquarium(-21)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM22:
                self.unfillAquarium(-22)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM23:
                self.unfillAquarium(-23)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM24:
                self.unfillAquarium(-24)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM25:
                self.unfillAquarium(-25)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM26:
                self.unfillAquarium(-26)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM27:
                self.unfillAquarium(-27)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM28:
                self.unfillAquarium(-28)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM29:
                self.unfillAquarium(-29)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM30:
                self.unfillAquarium(-30)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM31:
                self.unfillAquarium(-31)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM32:
                self.unfillAquarium(-32)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BM33:
                self.unfillAquarium(-33)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM34:
                self.unfillAquarium(-34)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BM35:
                self.unfillAquarium(-35)
                game_state=GameState.HUMAN_MODE
         
            #FILL
            if game_state==ButtonNumber.BP1:
                self.fillAquarium(1)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP2:
                self.fillAquarium(2)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP3:
                self.fillAquarium(3)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP4:
                self.fillAquarium(4)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP5:
                self.fillAquarium(5)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP6:
                self.fillAquarium(6)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP7:
                self.fillAquarium(7)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP8:
                self.fillAquarium(8)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP9:
                self.fillAquarium(9)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP10:
                self.fillAquarium(10)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP11:
                self.fillAquarium(11)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP12:
                self.fillAquarium(12)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP13:
                self.fillAquarium(13)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP14:
                self.fillAquarium(14)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP15:
                self.fillAquarium(15)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP16:
                self.fillAquarium(16)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP17:
                self.fillAquarium(17)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP18:
                self.fillAquarium(18)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP19:
                self.fillAquarium(1)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP20:
                self.fillAquarium(20)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP21:
                self.fillAquarium(21)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP22:
                self.fillAquarium(22)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP23:
                self.fillAquarium(23)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP24:
                self.fillAquarium(24)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP25:
                self.fillAquarium(25)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP26:
                self.fillAquarium(26)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP27:
                self.fillAquarium(27)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP28:
                self.fillAquarium(28)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP29:
                self.fillAquarium(29)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP30:
                self.fillAquarium(30)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP31:
                self.fillAquarium(31)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP32:
                self.fillAquarium(32)
                game_state=GameState.HUMAN_MODE
            
            if game_state==ButtonNumber.BP33:
                self.fillAquarium(33)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP34:
                self.fillAquarium(34)
                game_state=GameState.HUMAN_MODE

            if game_state==ButtonNumber.BP35:
                self.fillAquarium(35)
                game_state=GameState.HUMAN_MODE

      