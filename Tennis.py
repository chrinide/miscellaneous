
import pygame
import sys
import os
import time

from pygame.locals import *
from random import randint

os.chdir("C:/Users/new/Projects/Tennis")
while True:
	#setup options (let player skip all this with "quick start")
	quick = False
	qs = input("Quick Start? (Y/N): ")
	if qs == "Y" or qs == "y":
		quick = True
	multiplayer = True
	cpu_skill = 1
	mpl = int(input("1 or 2 players?: "))
	if mpl == 1:
		multiplayer = False
		if quick is False:
			cpu_skill = float(input("Set AI error (suggested = 1): "))
	if quick is False:
		ball_speed = int(input("Set speed (suggested = 20): "))
		fps = int(input("Frames per second (suggested = 30): "))
		first_to = int(input("Points to win: "))
		sound_choice = input("Play sounds? Y/N (suggested = N): ")
	else:
		ball_speed = 20
		fps = 30
		first_to = 5
		sound_choice = "N"
		print("First to score 5 points wins!")

	#Define Player and Ball classes
	class Player(pygame.sprite.Sprite):
		def __init__(self, start_x, width, height):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.transform.scale(
				pygame.image.load(bat_img),(width, height))
			self.rect = self.image.get_rect()
			self.rect.x = start_x
			self.rect.y = 200 - height/2
			self.height = height
			self.width = width
			self.sound = pygame.mixer.Sound(bat_sound)
			
		def move(self, dir, speed):
				self.rect.y = self.rect.y + (speed*dir)
				
		def reset_player(self):
			self.rect.y = 200 - self.height/2
		

			
		
		
	class Ball(pygame.sprite.Sprite):
		def __init__(self, start_x, start_y, speed_x, speed_y, start_dir_x):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.transform.scale(
				pygame.image.load(ball_img),(10, 10))
			self.rect = self.image.get_rect()
			self.rect.x = start_x
			self.rect.y = start_y
			self.dir_x = start_dir_x
			self.dir_y = 0
			self.speed_x = speed_x
			self.speed_y = speed_y
			self.sound = pygame.mixer.Sound(wall_bounce)
			self.point_scored = pygame.mixer.Sound(point_scored)
			
			
		def move_x(self, dir_x, speed_x):
			self.rect.x = self.rect.x + (speed_x * dir_x)
			
		def move_y(self, speed_y):
			self.rect.y = self.rect.y + (speed_y)
		
		def move(self, dir_x, speed_x, speed_y):
			self.move_x(dir_x, speed_x)
			self.move_y(speed_y)

	if multiplayer is True:		
		#options
		screen_x = 600
		screen_y = 400
		game_name = "Tennis!"
		bat_img = "imgs/bat.png"
		ball_img = "imgs/ball.png"
		bat_sound = "imgs/bat_hit.ogg"
		wall_bounce = "imgs/wall_bounce.ogg"
		point_scored = "imgs/point_sound.ogg"

		#initialise mixer
		pygame.mixer.pre_init(44100, -16, 8, 2048)
		pygame.mixer.init()

		#initialise pygame
		pygame.init()
		myfont = pygame.font.SysFont("monospace", 32, bold = True)
		myfont2 = pygame.font.SysFont("monospace", 24, bold = True)
		window = pygame.display.set_mode((screen_x, screen_y))
		pygame.display.set_caption(game_name)
		screen = pygame.display.get_surface()

		#initialise vars

		bat_speed = 10
		score1 = 0
		score2 = 0
		pt_scored1 = False
		pt_scored2 = False
		game_over = False

		clock = pygame.time.Clock()
		player1 = Player(10,20,40)
		player1_plain = pygame.sprite.RenderPlain(player1)

		player2 = Player(570,20,40)
		player2_plain = pygame.sprite.RenderPlain(player2)

		ball = Ball(295, 195, ball_speed,0, -1)
		ball_plain = pygame.sprite.RenderPlain(ball)



		finished = False

		while not finished:
			#blank
			screen.fill((0,60,0))
			#events
			for event in pygame.event.get():
				if event.type == QUIT:
					finished = True
					
			#keys
			key_state = pygame.key.get_pressed()
			if key_state[K_w] and player1.rect.y > -(player1.height/2):
				player1.move(-1,bat_speed)
			if key_state[K_s] and player1.rect.y < 400-(player1.height/2):
				player1.move(1,bat_speed)
			if key_state[K_UP] and player2.rect.y > -(player2.height/2):
				player2.move(-1,bat_speed)
			if key_state[K_DOWN] and player2.rect.y < 400-(player2.height/2):
				player2.move(1,bat_speed)
			
			#check if hit sides
			
			if ball.rect.y < 0 or ball.rect.y >390:
				ball.speed_y = ball.speed_y * -1
				if sound_choice == "Y" or sound_choice == "y":
					ball.sound.play()
			
			#check if goal!
			
			if ball.rect.x < 0:
				pt_scored2 = True
				score2 += 1
				if sound_choice == "Y" or sound_choice == "y":
					ball.point_scored.play()
			if ball.rect.x >600:
				pt_scored1 = True
				score1 += 1
				if sound_choice == "Y" or sound_choice == "y":
					ball.point_scored.play()
				
			#check if game over?
			
			if score1 == first_to or score2 == first_to:
				game_over = True
				
				
			
			#check_bat_and_ball
			if ball.rect.colliderect(player1.rect):
				ball.dir_x = ball.dir_x * -1
				#get distance from centre of bat (-9 or +49 if right on edge; -15 if exactly in middle)
				contact = (player1.rect.y - ball.rect.y)-15
				ball.speed_y = -int((contact+30)/6)
				
				if sound_choice == "Y" or sound_choice == "y":
					player1.sound.play()

				print(ball.speed_y)


				#change ball.speed_y accordingly
				
			
			if ball.rect.colliderect(player2.rect):
				ball.dir_x = ball.dir_x * -1
				#get distance from centre of bat (-9 or +49 if right on edge; -15 if exactly in middle)
				contact = (player2.rect.y - ball.rect.y)-15
				ball.speed_y = -int((contact+30)/6)
				
				if sound_choice == "Y" or sound_choice == "y":
					player2.sound.play()

				print(ball.speed_y)

				
				#change ball.speed_y accordingly
			
			#move ball
			ball.move(ball.dir_x, ball.speed_x, ball.speed_y)
			
			#render
			
			#score at bottom
			score_msg = str(score1)+"   -   "+str(score2)
			score_label = myfont.render(score_msg, 1, (255,255,255))
			screen.blit(score_label, (220, 360))
			
			
			player1_plain.draw(screen)
			player2_plain.draw(screen)
			ball_plain.draw(screen)
			
			#update
			pygame.display.update()
			
			if pt_scored1 and score1 != first_to:
				ball = Ball(295, 195, ball_speed,0, -1)
				ball_plain = pygame.sprite.RenderPlain(ball)
				msg = "Player 1 scores!"
				label = myfont.render(msg, 1, (255,255,255))
				screen.blit(label, (170, 160))
				pygame.display.update()
				time.sleep(2)
				player1.reset_player()
				player2.reset_player()
				pt_scored1 = False
				
			if pt_scored2 and score2 != first_to:
				ball = Ball(295, 195, ball_speed,0, +1)
				ball_plain = pygame.sprite.RenderPlain(ball)
				msg = "Player 2 scores!"
				label = myfont.render(msg, 1, (255,255,255))
				screen.blit(label, (170, 160))
				pygame.display.update()
				time.sleep(2)
				player1.reset_player()
				player2.reset_player()
				pt_scored2 = False
				
			if game_over:
				if score1 > score2:
					go_label = myfont.render("Player 1 wins!", 1, (255,255,255))
					screen.blit(go_label, (170, 160))
					pygame.display.update()
					time.sleep(3)
					finished = True
				if score2 > score1:
					go_label = myfont.render("Player 2 wins!", 1, (255,255,255))
					screen.blit(go_label, (170, 160))
					pygame.display.update()
					time.sleep(3)
					finished = True
				
			#set speed
			clock.tick(fps)
			
	if multiplayer is False:

		#options
		screen_x = 600
		screen_y = 400
		game_name = "Tennis!"
		bat_img = "imgs/bat.png"
		ball_img = "imgs/ball.png"
		bat_sound = "imgs/bat_hit.ogg"
		wall_bounce = "imgs/wall_bounce.ogg"
		point_scored = "imgs/point_sound.ogg"

		#initialise mixer
		pygame.mixer.pre_init(44100, -16, 8, 2048)
		pygame.mixer.init()

		#initialise pygame
		pygame.init()
		myfont = pygame.font.SysFont("monospace", 32, bold = True)
		myfont2 = pygame.font.SysFont("monospace", 24, bold = True)
		window = pygame.display.set_mode((screen_x, screen_y))
		pygame.display.set_caption(game_name)
		screen = pygame.display.get_surface()

		#initialise vars

		bat_speed = 10
		score1 = 0
		score2 = 0
		pt_scored1 = False
		pt_scored2 = False
		game_over = False

		clock = pygame.time.Clock()
		player1 = Player(10,20,40)
		player1_plain = pygame.sprite.RenderPlain(player1)

		comp = Player(570,20,40)
		comp_plain = pygame.sprite.RenderPlain(comp)

		ball = Ball(295, 195, ball_speed,0, -1)
		ball_plain = pygame.sprite.RenderPlain(ball)



		finished = False

		while not finished:
			#blank
			screen.fill((0,60,0))
			#events
			for event in pygame.event.get():
				if event.type == QUIT:
					finished = True
					
			#keys (COMMENT OUT PLAYER 2 INPUT!!!)
			key_state = pygame.key.get_pressed()
			if key_state[K_w] and player1.rect.y > -(player1.height/2):
				player1.move(-1,bat_speed)
			if key_state[K_s] and player1.rect.y < 400-(player1.height/2):
				player1.move(1,bat_speed)
			#if key_state[K_UP] and comp.rect.y > -(comp.height/2):
			#	comp.move(-1,bat_speed)
			#if key_state[K_DOWN] and comp.rect.y < 400-(comp.height/2):
			#	comp.move(1,bat_speed)
			
			#check if hit sides
			
			if ball.rect.y < 0 or ball.rect.y >390:
				ball.speed_y = ball.speed_y * -1
				if sound_choice == "Y" or sound_choice == "y":
					ball.sound.play()
			
			#check if goal!
			
			if ball.rect.x < 0:
				pt_scored2 = True
				score2 += 1
				if sound_choice == "Y" or sound_choice == "y":
					ball.point_scored.play()
			if ball.rect.x >600:
				pt_scored1 = True
				score1 += 1
				if sound_choice == "Y" or sound_choice == "y":
					ball.point_scored.play()
				
			#check if game over?
			
			if score1 == first_to or score2 == first_to:
				game_over = True
				
				
			
			#check_bat_and_ball
			if ball.rect.colliderect(player1.rect):
				ball.dir_x = ball.dir_x * -1
				#get distance from centre of bat (-9 or +49 if right on edge; -15 if exactly in middle)
				contact = (player1.rect.y - ball.rect.y)-15
				ball.speed_y = -int((contact+30)/6)
				
				if sound_choice == "Y" or sound_choice == "y":
					player1.sound.play()

				print(ball.speed_y)


				#change ball.speed_y accordingly
				
			
			if ball.rect.colliderect(comp.rect):
				ball.dir_x = ball.dir_x * -1
				#get distance from centre of bat (-9 or +49 if right on edge; -15 if exactly in middle)
				contact = (comp.rect.y - ball.rect.y)-15
				ball.speed_y = -int((contact+30)/6)
				
				if sound_choice == "Y" or sound_choice == "y":
					comp.sound.play()

				print(ball.speed_y)

				
				#change ball.speed_y accordingly
			
			#move ball
			ball.move(ball.dir_x, ball.speed_x, ball.speed_y)
			
			#move cpu player
			#if ball is moving towards player1, move cpu towards centre
			
			if ball.dir_x < 0:
				if comp.rect.y < 200 - comp.height/2:
					comp.move(1, bat_speed)
				elif comp.rect.y > 200 - comp.height/2:
					comp.move(-1, bat_speed)
					
			#if ball is moving back towards cpu, estimate trajectory from ball x and y speeds
			#first, make an estimate (add a random error as well)
			#then, check cpu's current position
			#adjust as required
			if ball.dir_x > 0:
				t = (600 - ball.rect.x)/ball_speed
				estimate = ball.rect.y + (ball.dir_y * t) + randint(int(-comp.height*cpu_skill), int(cpu_skill * comp.height))
				if comp.rect.y < estimate - comp.height/2:
					comp.move(1,bat_speed)
				elif comp.rect.y > estimate - comp.height/2:
					comp.move(-1,bat_speed)
				
				
			
			#render
			
			#score at bottom
			score_msg = str(score1)+"   -   "+str(score2)
			score_label = myfont.render(score_msg, 1, (255,255,255))
			screen.blit(score_label, (220, 360))
			
			
			player1_plain.draw(screen)
			comp_plain.draw(screen)
			ball_plain.draw(screen)
			
			#update
			pygame.display.update()
			
			if pt_scored1 and score1 != first_to:
				ball = Ball(295, 195, ball_speed,0, -1)
				ball_plain = pygame.sprite.RenderPlain(ball)
				msg = "Player 1 scores!"
				label = myfont.render(msg, 1, (255,255,255))
				screen.blit(label, (170, 160))
				pygame.display.update()
				time.sleep(2)
				player1.reset_player()
				comp.reset_player()
				pt_scored1 = False
				
			if pt_scored2 and score2 != first_to:
				ball = Ball(295, 195, ball_speed,0, +1)
				ball_plain = pygame.sprite.RenderPlain(ball)
				msg = "Player 2 scores!"
				label = myfont.render(msg, 1, (255,255,255))
				screen.blit(label, (170, 160))
				pygame.display.update()
				time.sleep(2)
				player1.reset_player()
				comp.reset_player()
				pt_scored2 = False
				
			if game_over:
				if score1 > score2:
					go_label = myfont.render("Player 1 wins!", 1, (255,255,255))
					screen.blit(go_label, (170, 160))
					pygame.display.update()
					time.sleep(3)
					finished = True
				if score2 > score1:
					go_label = myfont.render("Player 2 wins!", 1, (255,255,255))
					screen.blit(go_label, (170, 160))
					pygame.display.update()
					time.sleep(3)
					finished = True
				
			#set speed
			clock.tick(fps)
			