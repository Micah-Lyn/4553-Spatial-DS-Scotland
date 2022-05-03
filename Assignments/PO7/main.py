# # from quadTree import Rect
# from operator import pos
# # from turtle import width
# import pygame
# import random
# from pygame import *
# # from quadTree import * 


# import quadTree

# from quadTree import QuadTree
# from quadTree import Rect



# quadTree.init()


# #initalize pygame
# pygame.init()



# #name screen
# pygame.display.set_caption('PO7')


# # screen_width,screen_height = 500,500 

# # window = pygame.display.set_mode((screen_width, screen_height))



# #create random points

# # creating a bool value which checks
# # if game is running
# running = True


# #array to store points to go in quadtree
# pointsForTree = []
# #returns a float so cast to int
# #number of points to load quad tree with
# toPoints = int((quadTree.screen_width // 100) * (quadTree.screen_height//100)*2.5)

# # creating the points and storing it in array to load in quad tree
# for point in range(toPoints):    
#     circleX = random.randint(0,500)
#     circleY = random.randint(0,500)
#     radius = random.randint(8,10)

#     #create random color
#     r = random.randint(0,255)
#     b = random.randint(0,255)
#     g = random.randint(0,255)
#     colorCode = (r,g,b)

#     pointsForTree.append([circleX, circleY])

#     # circleCreated = pygame.draw.circle(quadTree.window,colorCode,(circleX,circleY),radius)
   
#     #append the x,y coordinates for circle to be used in query
    
#     # pygame.display.update()


# # print(pointsForTree)
# # print(len(pointsForTree))

# results = []


# # bbox = Rect((quadTree.screen_width//2), (quadTree.screen_height//2), quadTree.screen_width, quadTree.screen_height)
# # print(bbox)
# # quadT = QuadTree(bbox,quadTree.window) 
# # bbox.draw()
# # pygame.display.flip()



# #LOAD POINT TO QUADTREE

# # bbox = Rect(screen_width/2, screen_height/2, screen_width, screen_height, window)
# # print(screen_width//2, screen_height//2, screen_width, screen_height)
# # print(Rect(screen_width//2, screen_height//2, screen_width, screen_height))

# # Game loop
# # keep game running till running is true

# v = [2,0]

# done = False

# pos_list = []

# bbox = Rect((quadTree.screen_width//2), (quadTree.screen_height//2), quadTree.screen_width, quadTree.screen_height)

# while not done:

#     # creating the points and storing it in array to load in quad tree
    
#     # Check for event if user has pushed
#     # any event in queue
#     for event in pygame.event.get():
#         # if event is of type quit then set
#         # running bool to false
#         if event.type == pygame.QUIT:
#             done = True
#         if event.type == pygame.K_ESCAPE:
#             done = True
    


        
      
        
#         # dist = 1
#         # if key[pygame.K_LEFT]:
#         #    bbox.move_ip(-1, 0)
#         # if key[pygame.K_RIGHT]:
#         #    bbox.move_ip(1, 0)
#         # if key[pygame.K_UP]:
#         #    bbox.move_ip(0, -1)
#         # if key[pygame.K_DOWN]:
#         #    bbox.move_ip(0, 1)
    

#     quadTree.window.fill((255,255,255))
#     for x, y in pos_list:
#         bbox.draw(x,y)
#     bbox.handle_keys()
   

 

#     #iterate through points
#     for x,y in pointsForTree:

#         #if points collides with the rectangle, color them 
#         bbox.contactPoint(x,y,radius)
 
        
          
#     pygame.display.update() 
    





#     # pygame.display.update()
#     # clock.tick(90)
#     # pygame.time.delay(60)
#     pygame.display.flip()
# pygame.quit()



# from quadTree import Rect
# from turtle import width
# import pygame
import random
from pygame import *
from quadTree import * 


import quadTree

# from quadTree import QuadTree
# from quadTree import Rect

quadTree.init()


#initalize pygame
pygame.init()



#name screen
pygame.display.set_caption('PO7')


#create random points

# creating a bool value which checks

#array to store points to go in quadtree
pointsForTree = []

#returns a float so cast to int
#number of points to load quad tree with
toPoints = int((quadTree.screen_width // 100) * (quadTree.screen_height//100)*2.5)

# creating the points and storing it in array to load in quad tree
for point in range(toPoints):    
    circleX = random.randint(0,500)
    circleY = random.randint(0,500)

    #append the x,y coordinates for circle to be used in query
    pointsForTree.append([circleX, circleY])



#LOAD POINT TO QUADTREE

# Game loop
# keep game running till running is true


done = False

bbox = Rect((quadTree.screen_width//2), (quadTree.screen_height//2), 0, 0)

two_points = False
clicks_2 = 0

points1bbox = [quadTree.screen_width//2, quadTree.screen_height//2]
points2bbox = [quadTree.screen_width, quadTree.screen_height]

while not done:

    # creating the points and storing it in array to load in quad tree
    
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.K_ESCAPE:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                
                clicks_2 += 1

                if clicks_2 != 0:
                    if clicks_2 % 2 == 0:
                        two_points = True

                        #converts the x,y position of mouse cursor to list
                        points2bbox = list(pygame.mouse.get_pos())
                       

                        bbox = Rect(( ((points1bbox[0] + points2bbox[0]) // 2)), 
                        ((points1bbox[1] + points2bbox[1]) // 2),
                         (points2bbox[0] - points1bbox[0]), (points2bbox[1] - points1bbox[1]))

                    else:
                        two_points = False
                        points1bbox = list(pygame.mouse.get_pos())

       

    quadTree.window.fill((255,255,255))


    if two_points:
        dxdy = bbox.handle_keys(bbox)


        points1bbox[0] += dxdy[0]
        points2bbox[0] += dxdy[0]
        points1bbox[1] += dxdy[1]
        points2bbox[1] += dxdy[1]

        bbox.draw(points1bbox, points2bbox)
        # bbox.clamp_ip(quadTree.window.get_rect())


    #iterate through points
    for x,y in pointsForTree:

        #if points collides with the rectangle, color them 
        radius = random.randint(8,10)
       
        bbox.contactPoint(x, y, radius)
          
    pygame.display.update() 
    

    pygame.display.flip()
pygame.quit()











