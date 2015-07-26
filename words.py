#!/usr/local/bin/python3
#coding: utf-8
with open('words/super700.txt', encoding='UTF-8') as a:
	super700 = a.read().split('b')

with open('words/scary.txt', encoding='UTF-8') as a:
	scary = a.read().split('b')

with open('words/films.txt', encoding='UTF-8') as a:
	films = a.read().split('b')

with open('words/girls.txt', encoding='UTF-8') as a:
	girls = a.read().split('b')
	
with open('words/mudreci.txt', encoding='UTF-8') as a:
	mudreci = a.read().split('b')

with open('words/life.txt', encoding='UTF-8') as a:
 life =a.read().split('b')

with open('words/sex.txt', encoding='UTF-8') as a:
	sex = a.read().split('b')

with open('words/vselen.txt', encoding='UTF-8') as a:
	vselen = a.read().split('b')

with open('words/psy.txt', encoding='UTF-8') as a:
	psy = a.read().split('b')

with open('words/psy2.txt', encoding='utf-8') as a:
	psy2 = list(filter(None, a.read().split('b')))

with open('words/davidovich.txt', encoding='utf-8') as dvdch:
	davch = dvdch.read().split('b')

with open('words/mudreci2.txt') as mudro2:
	mudreci2=mudro2.read().split('b')

slist = list(filter(None, mudreci+life+girls+sex+films+scary+super700+vselen+psy2 ))

phrases = ['На всяком кладбище, даже очень старом, всегда ощутим острый, трагический аромат разорванной любви — когда смерть отрывает любящих друг от друга.', 'Приятно знать, каков наш мир и где в нем твое место', 'Надо найти место внутри себя, вокруг себя. Место, которое тебе подходит.Похожее на тебя хотя бы отчасти.','Есть нечто особенное в месте твоего рождения. Не все это знают. Это знает лишь тот, кого силой оторвали от места его рождения.','Так же, как кожа выделяет пот, печень— желчь, а поджелудочная железа — инсулин, мозг — этот поразительный орган, состоящий из миллиардов клеток — «выделяет» сознание.']