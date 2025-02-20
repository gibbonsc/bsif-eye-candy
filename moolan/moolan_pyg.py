import pygame
from random import randint
from time import sleep

# global variables
crash=win=quitting=playing=False
disp_w = 128; disp_h = 64
y_vel=x_vel=0.0
banner='INSERT COIN'

pygame.init()
screen = pygame.display.set_mode((disp_w,disp_h))
pygame.display.set_caption("m")
pygame.font.init()
tf = pygame.font.SysFont('courier', 8)

def render_pf(grid,typeface,target_pos,sprite_pos,sprite_id,jets,msg1,msg2,msg3):
    craft_vertices = [[-6, 5], [-4, 3], [-3,-5], [ 3,-5], [ 4, 3],
                      [ 6, 5], [ 4, 5], [ 2, 2], [-2, 2], [-4, 5]]
    crash_vertices = [[-6, 0], [-3,-5], [-2, 1], [ 1,-6], [ 0, 1],
                      [ 4,-3], [ 2, 2], [ 6, 3], [ 0, 4], [-4, 2]]
    white = (255,255,255)
    black = (0,0,0)
    grid.fill(black)
    # HUD
    sp=typeface.render(msg1,0,white)
    grid.blit(sp,(disp_w-32,8))
    sp=typeface.render(msg2,0,white)
    grid.blit(sp,(disp_w-32,16))
    sp=typeface.render(msg3,0,white)
    grid.blit(sp,(24,24))
    # spacecraft
    if sprite_id==0:
        svg=crash_vertices
    else:
        svg=craft_vertices
    sprite=list(map(lambda p:[p[0]+sprite_pos[0], p[1]+sprite_pos[1]], svg))
    pygame.draw.polygon(grid, white, sprite, 1)
    # add jet line if thrusting
    if jets[0]:
        pygame.draw.line(grid, white, (cx,cy+5), (cx,cy+8))
    if jets[1]:
        pygame.draw.line(grid, white, (cx-9,cy), (cx-6,cy))
    if jets[2]:
        pygame.draw.line(grid, white, (cx+6,cy), (cx+9,cy))
    # place landing target
    pygame.draw.rect(screen, white, (target_pos[0]-6,target_pos[1]-1,13,2))
    pygame.display.update()

def attract(frame_delay):
    global playing, quitting, crash, y_vel, x_vel, cx, cy, tx, ty, banner
    while not playing and not quitting:
        if crash:
            craft_id=0
        else:
            craft_id=1
        render_pf(screen,tf,(tx,ty),(cx,cy),craft_id,[False,False,False],'V:%2d'%(-y_vel),'H:%2d'%(x_vel),banner)
        sleep(frame_delay)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quitting=True
            elif event.type==pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        quitting=True
                    case pygame.K_SPACE:
                        playing=True
                    case pygame.K_s:
                        playing=True

def play(frame_delay):
    global playing, quitting, crash, win, tx, ty, cx, cy, y_vel, x_vel, banner
    while playing:
        sleep(frame_delay)
        sprite_thrust = [False,False,False]
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                playing=False; quitting=True
            elif event.type==pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        playing=False; quitting=True
                    case pygame.K_DOWN:
                        y_vel -= 1.0 + 0.388326
                        sprite_thrust[0]=True
                    case pygame.K_LEFT:
                        x_vel += 1.0
                        sprite_thrust[1]=True
                    case pygame.K_RIGHT:
                        x_vel -= 1.0
                        sprite_thrust[2]=True
                    case pygame.K_s:
                         playing=False
        # prepare to draw canvas
        y_vel += 0.388326  # e/7
        cy += y_vel
        cx += x_vel
        if cy > disp_h-8:
            if y_vel >= 2.0:
                crash=True; playing=False
            elif tx-5 <= cx <= tx+5:
                win=True; playing=False
            else:
                crash=True; playing=False
        craft_id = 1
        if win:
            banner='WIN'
        elif crash:
            banner='CRASH'
            craft_id = 0
        else:
            banner=''
        render_pf(screen,tf,(tx,ty),(cx,cy),craft_id,sprite_thrust,'V:%2d'%(-y_vel),'H:%2d'%(x_vel),banner)
        sprite_thrust=[False,False,False]

# initial attract craft and target coords
cx=tx=64; cy=5; ty=disp_h-1; y_vel = x_vel = 0.0

# main program loop
playing=False
while not quitting:
    attract(1.0/3.0)
    if not quitting:
        cx = randint(0, disp_w-15); cy=4
        tx = randint(int(disp_w/2)-56,int(disp_w/2)+57); ty=disp_h-2
        y_vel=x_vel=0.0
        crash=win=False
        play(1.0/3.0)

# clean up
pygame.quit()
