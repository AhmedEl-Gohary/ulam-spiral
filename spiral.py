import pygame, sys	

pygame.init()

WIDTH = 1600
HEIGHT = 1200
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 100, 80)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ulam Spiral')

step_size = 1
steps = 0
switch_counter = 0
num = 1
horizontal = True
increment = True
x = WIDTH // 2 + 200
y = HEIGHT // 2


# Precomputing prime numbers from 1 to n
n = 14000
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, n + 1):
	if is_prime[i] and i * i <= n:
		for j in range(i * i, n + 1, i):
			is_prime[j] = False

while True:
	# checking for user input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if is_prime[num]:
		pygame.draw.circle(screen, WHITE, (x, y), 5, 0)

	if  steps == step_size:
		steps = 0
		horizontal = not horizontal
		switch_counter += 1

	if switch_counter == 2:
		step_size += 1
		switch_counter = 0

	inc = 10 if step_size % 2 == 1 else -10

	if horizontal:
		x += inc
	else:
		y -= inc

	steps += 1
	if num < n: 
		num += 1

	pygame.display.update()





