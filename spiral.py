import pygame, sys, random, math	

pygame.init()

# Initializing screen settings
WIDTH = 2000
HEIGHT = 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ulam Spiral')
over_screen = pygame.image.load('images/mainmenu.jpg').convert_alpha()
over_rect = over_screen.get_rect(center = (WIDTH // 2, HEIGHT // 2))
font = pygame.font.Font('font/CrimsonText-Bold.ttf', 60)

# Initializing Labels
prime_label = font.render('Prime', True, 'gray')
prime_rect = prime_label.get_rect(center = (480, 1100))
random_label = font.render('Random', True, 'gray')
random_rect = random_label.get_rect(center = (1500, 1100))


# Varibales for prime spiral
x_prime = 480
y_prime = HEIGHT // 2 - 100
step_size = 1
steps = 0
switch_counter = 0
num = 1
horizontal = True
increment = True

# Variables for random spiral
x_random = 1500
y_random = HEIGHT // 2 - 100
step_size_random = 1
steps_random = 0
switch_counter_random = 0
num_random = 1
horizontal_random = True
increment_random = True

# Global variables
start = False
switched = False
n = 12000

# Button class with clicking detection
class Button:
	def __init__(self, text, x_pos, y_pos):
		self.text = text
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.draw()

	def draw(self):
		button_text = font.render(self.text, True, 'black')
		button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (520, 100))
		pygame.draw.rect(screen, 'gray', button_rect, 0, 5)
		screen.blit(button_text, (self.x_pos + 20, self.y_pos + 5))

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		left_click = pygame.mouse.get_pressed()[0]
		button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (520, 100))
		if left_click and button_rect.collidepoint(mouse_pos):
			return True
		return False

# Precomputing prime numbers
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, n + 1):
	if is_prime[i] and i * i <= n:
		for j in range(i * i, n + 1, i):
			is_prime[j] = False

# Precomputing random numbers
is_rand = [False] * (n + 1)
for i in range(n):
	if random.random() < 1 / math.log(n):
		is_rand[i] = True

# Displaying menu screen and buttons
screen.blit(over_screen, over_rect)
button = Button('Prime vs.  Random', 760, 700)

while True:
	# checking for user input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if button.check_click():
		start = True

	if start:
		if not switched: 
			screen.fill('black')
			switched = True

		screen.blit(prime_label, prime_rect)
		screen.blit(random_label, random_rect)
		
		# Prime spiral
		if is_prime[num]:
			pygame.draw.circle(screen, 'white', (x_prime, y_prime), 4, 0)

		if steps == step_size:
			steps = 0
			horizontal = not horizontal
			switch_counter += 1

		if switch_counter == 2:
			step_size += 1
			switch_counter = 0

		inc = 8 if step_size % 2 == 1 else -8

		if horizontal:
			x_prime += inc
		else:
			y_prime -= inc

		steps += 1
		if num < n: 
			num += 1

		# Random spiral
		if is_rand[num_random]:
			pygame.draw.circle(screen, 'white', (x_random, y_random), 4, 0)

		if  steps_random == step_size_random:
			steps_random = 0
			horizontal_random = not horizontal_random
			switch_counter_random += 1

		if switch_counter_random == 2:
			step_size_random += 1
			switch_counter_random = 0

		inc_random = 8 if step_size_random % 2 == 1 else -8

		if horizontal:
			x_random += inc_random
		else:
			y_random -= inc_random

		steps_random += 1
		if num_random < n: 
			num_random += 1

	pygame.display.update()





