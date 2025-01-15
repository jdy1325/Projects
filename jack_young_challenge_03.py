# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:56:21 2024

@author: JackD
"""

import random

#Creating Humanoid class
class Humanoid:
	height=0
	weight=0
	hair_color=""
	eye_color=""
	strength=0
	dexterity=0
	constitution=0
	intelligence=0
	wisdom=0
	charisma=0
	sleep_res=0
	magic_res=0

    #For random attribute generation
	def __init__(self):
		self.strength= random.randint(1,18)
		self.dexterity= random.randint(1,18)
		self.constitution= random.randint(1,18)
		self.intelligence= random.randint(1,18)
		self.wisdom= random.randint(1,18)
		self.charisma= random.randint(1,18)

    #Printing character information
	def __str__(self):
		print(f'Height:{self.height}ft')
		print(f'Weight:{self.weight}lbs')
		print(f'Hair color:{self.hair_color}')
		print(f'Eye color:{self.eye_color}')
		print(f'Str:{self.strength}')
		print(f'Dex:{self.dexterity}')
		print(f'Con:{self.constitution}')
		print(f'Int:{self.intelligence}')
		print(f'Wis:{self.wisdom}')
		print(f'Char:{self.charisma}')
		if self.sleep_res>0:
			print(f'Resistance to sleep:{self.sleep_res}%')
		if self.magic_res>0:
			print(f'Resistance to mmagic:{self.magic_res}%')
		return ''
		
#Creating Human subclass
class Humans(Humanoid):

	def addAttribute(self,attr): #Attribute for Humans or being +2
		if attr=="strength":
			self.strength+=2
		elif attr=="dexterity":
			self.dexterity+=2
		elif attr=="constitution":
			self.constitution+=2
		elif attr=="intelligence":
			self.intelligence+=2
		elif attr=="wisdom":
			self.wisdom+=2
		elif attr=="charisma":
			self.charisma+=2
		else:
			pass

#Creating Elves subclass
class Elves(Humanoid):

	def addAttribute(self): #Attributes for Elves
		self.sleep_res=100
		self.dexterity+=2
		self.charisma+=2

#Creating Dwarves subclass
class Dwarves(Humanoid):

	def addAttribute(self): #Attributes for Dwarves
		self.sleep_res=20
		self.strength+=2
		self.constitution+=2
		self.charisma-=2

#Character creation
def characterCreation():
	print('You may choose from the following playable races:\n')
	print('1.Human\n2.Elf\n3.Dwarf\n')
	ch=input('Which race have you chosen for your starting character?')

	if ch=='1':
		hum=Humans() #Humans output

		hair_color=input('Please enter the hair color for your human character:')
		eye_color=input('Please enter the eye color for you human character:')
		height=int(input('Please enter the height of your character from 4ft - 7ft:'))
		weight=int(input('Please enter the weight for you character from 60 - 300lbs:'))

		hum.hair_color=hair_color
		hum.eye_color=eye_color
		hum.height=height
		hum.weight=weight

		print('\n**** Now randomly rolling stat attributes for you character ****')
		print('You character has the following attributes:')

		print(hum)

		attr=input('\nAs a Human, you may add +2 bonus points to a single attribute of your choosing (Enter one of these: strength, dexterity, constitution, intelligence, wisdom, charisma:')
		hum.addAttribute(attr)
		print('\nYou character\'s final attributes are:')
		print(hum)
	
		return hum
    
    
	elif ch=='2':
		el=Elves() #Elves output

		hair_color=input('Please enter the hair color for your elves character:')
		eye_color=input('Please enter the eye color for you elves character:')
		height=int(input('Please enter the height of your character from 4ft - 7ft:'))
		weight=int(input('Please enter the weight for you character from 60 - 300lbs:'))

		el.hair_color=hair_color
		el.eye_color=eye_color
		el.height=height
		el.weight=weight

		print('\n**** Now randomly rolling stat attributes for you character ****')
		print('You character has the following attributes:')

		print(el)

		print('\nAs a Elves, added +2 bonus points to a  attribute  Dexterity and Charisma and added 100% Resistance to Sleep ')
		el.addAttribute()
		print('\nYou character\'s final attributes are:')
		print(el)
        
		return el
    
    
	else:
		dw=Dwarves() #Dwarves output

		hair_color=input('Please enter the hair color for your dwarf character:')
		eye_color=input('Please enter the eye color for you dwarf character:')
		height=int(input('Please enter the height of your character from 4ft - 7ft:'))
		weight=int(input('Please enter the weight for you character from 60 - 300lbs:'))

		dw.hair_color=hair_color
		dw.eye_color=eye_color
		dw.height=height
		dw.weight=weight

		print('\n**** Now randomly rolling stat attributes for you character ****')
		print('You character has the following attributes:')

		print(dw)

		print('\nAs a Dwarf, added +2 bonus points to a  attribute  Strength and Constiution,subtracterd 2 points from Charisma and added 20% Resistance to magic ')
		dw.addAttribute()
		print('\nYour character\'s final attributes are:')
		print(dw)
        
		return dw


print('Welcome to Falls of Eternity. This is a simple RPG simulator written in Python.')
character=characterCreation()