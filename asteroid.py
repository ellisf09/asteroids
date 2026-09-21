
import random
import pygame
from constants import *
from circleshape import *
from logger import *
class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
	def update(self, dt):
		self.position+=self.velocity*dt
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			rangle=random.uniform(20, 50)
			currvel=self.velocity
			newastvel1=self.velocity.rotate(rangle)
			newastvel2=self.velocity.rotate(-rangle)
			newrad=self.radius-ASTEROID_MIN_RADIUS
			nas=Asteroid(self.position.x, self.position.y, newrad)
			nas2=Asteroid(self.position.x, self.position.y, newrad)
			nas.velocity=newastvel1*1.2
			nas2.velocity=newastvel2
