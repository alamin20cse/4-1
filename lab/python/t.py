import matplotlib.pyplot as plt
import pygame
from OpenGL.GL import *

def test_matplotlib():
    print("Running matplotlib test...")
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Matplotlib Test")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()
    print("Matplotlib test complete.\n")

def test_opengl():
    print("Running OpenGL test...")
    pygame.init()
    display = (640, 480)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    
    glClearColor(0.0, 0.3, 0.5, 1.0)  # blueish background
    glClear(GL_COLOR_BUFFER_BIT)
    pygame.display.flip()
    
    print("OpenGL window will close in 2 seconds...")
    pygame.time.wait(2000)
    pygame.quit()
    print("OpenGL test complete.\n")

if __name__ == "__main__":
    test_matplotlib()
    test_opengl()
