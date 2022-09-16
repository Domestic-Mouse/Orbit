from cmath import pi
import math
import pygame
from pygame.locals import *
import time

#intialises pygame 

pygame.init


def dis(xpos1,xpos2,ypos1,ypos2):
  return math.sqrt(((xpos1-xpos2)**2)+(ypos1-ypos2)**2)

def Force(body1mass,body2mass,distance):
  gravconst = 6.68*10**-11
  Force = gravconst*((body1mass*body2mass)/(distance**2))
  return Force


#acts as a fucntion for the main part of the pprogram after everything has been imported and intialised
def core(): 
  #Creates key variables
  window = pygame.display.set_mode([1250,750])
  totalFX = 0
  totalFY = 0
  AU = 150000000 # distance from moon to Earth in KM
  scale = (300/AU)
  running = True
  Orbit_moon = (3600*24)
  clock = pygame.time.Clock()
  Pause = False
  # initalises the class for the bodies
  class body(): 
    def __init__(self,mass,radius,xposition,yposition,colour,xvelocity,yvelocity):
      self.mass = mass
      self.rad = radius
      self.xpos = xposition #coordinates of the planet
      self.ypos = yposition
      self.colour = colour
      self.xvel = xvelocity # determines the x and y velocity of the planet
      self.yvel = yvelocity

  #defines 2 bodies
  planet1 = body(5.9*10**24,6371,625,370,((0,0,255)),0,0)
  planet2 = body(7.3*10**22,1737,925,375,((255,255,255)),1,1)
  # has the secondary planet circle the main body + draws the bodies
  pygame.display.set_caption("Orbit Simulation")
  
  while running:
    #updates window after every change
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(window,((200,200,200)),[1000,100,100,50])
    if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[1000,100,100,50])

    clock.tick(60)
    pygame.display.update()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False
      #pausing
      if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause/unpause
        if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
          Pause = not Pause
    
    while Pause:
      for event in pygame.event.get():
        #unpausing    
        if event.type == pygame.QUIT:
          Pause = False
          running = False
          break
        if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause/unpause
          if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
            Pause = not Pause
      
    #resets frame
    window.fill((0,0,0))

    
    #bulk of calculations
    distance = dis(planet1.xpos,planet2.xpos,planet1.ypos,planet2.ypos)
    force = Force(planet1.mass,planet2.mass,distance)
    angle = math.atan2(planet1.ypos-planet2.ypos,planet1.xpos-planet2.xpos)
    #Angle(planet1.ypos,planet2.ypos,distance)
    forceX = math.cos(angle) * force
    forceY = math.sin(angle) * force
    totalFX += forceX
    totalFY += forceY

    planet2.xvel += totalFX/planet2.mass*Orbit_moon
    planet2.yvel += totalFY/planet2.mass*Orbit_moon
    planet2.xpos += (planet2.xvel * Orbit_moon)
    planet2.ypos += (planet2.yvel * Orbit_moon)

    

    #draws bodies based on qualities and a line connecting bodies (temp)
    pygame.draw.line(window,((255,255,255)),(planet1.xpos,planet1.ypos),(planet2.xpos,planet2.ypos))
    pygame.draw.circle(window,((planet1.colour)),(planet1.xpos,planet1.ypos),30,0)
    pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    time.sleep(0.038)
core()
