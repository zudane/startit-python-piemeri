# Vairāk piemēru - http://thepythongamebook.com/


#------- pygame draw functions --------
# pygame.draw.rect(Surface, color, Rect, width=0): return Rect
pygame.draw.rect(window, (0,255,0), (50,50,100,25)) # rect: (x1, y1, width, height)
# pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
pygame.draw.circle(window, (0,200,0), (200,50), 35)
# pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
pygame.draw.polygon(window, (0,180,0), ((250,100),(300,0),(350,50)))
# pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
pygame.draw.arc(window, (0,150,0),(400,10,150,100), 0, 3.14) # radiant instead of grad

for point in range(0,641,64): # range(start, stop, step)
    pygame.draw.line(window, (255,0,255), (0,0), (480, point), 1)
