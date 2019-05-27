import pickle,time
from math import sqrt
from pynput.keyboard import Listener

print("enter 1 times the word:'APOLOGIZE'")

for i in [1]:
	default_value, TempArr = "",[]
	temp_dict = dict.fromkeys(['str','startInterval','endInterval','wallinterval','data'],default_value)
	while temp_dict['str'] != 'apologize':
		def push(button):
			temp_dict['data'], temp_dict['startInterval'] = str(button)[1],int((time.time())*1000//1)

		def squeeze(button):
			temp_dict['endInterval'] = int((time.time())*1000//1)
			return False

		with Listener(on_press=push,on_release=squeeze) as listener: listener.join()

		if 'apologize'[len(temp_dict['str'])] == temp_dict['data']:
			if temp_dict['str'] == "":
				temp_dict['str'] += temp_dict['data']
				TempArr.append(temp_dict['endInterval']-temp_dict['startInterval'])
			else:
				temp_dict['str'] += temp_dict['data']
				TempArr.append(temp_dict['startInterval']-temp_dict['wallinterval'])
				TempArr.append(temp_dict['endInterval']-temp_dict['startInterval'])
			temp_dict['wallinterval'] = temp_dict['endInterval']
		print(temp_dict['str'])
	

print("you have finished typing")

with open('data.pickle','rb') as f:
	Data = pickle.load(f)

#search of math expectation

math_expectation = []
for j in range(0,17):
	amount = 0
	for i in range(0,10):
		amount += Data[i][j]
	amount = amount/10
	math_expectation.append(amount)

#dispersion search

dispersion = []

for j in range(0,17):
	amount = 0
	for i in range(0,10):
		amount  += (Data[i][j]-math_expectation[j])*(Data[i][j]-math_expectation[j])
	dispersion.append(amount/10)

#finding the interval of correct indicators

Tmin,Tmax = [],[]

for j in range(0,17):
	(Tmin).append(math_expectation[j] - 2.228 * sqrt(dispersion[j]))
for j in range(0,17):
	(Tmax).append(math_expectation[j] + 2.228 * sqrt(dispersion[j]))

#Hamming measure search

Hamming_measure = []

for i in range(10,15):
	amount = 0
	for j in range(0,17):
		if not(Tmin[j] < Data[i][j] < Tmax[j]):
			amount += 1
	Hamming_measure.append(amount)

#search of math expectation/dispersion and absolute measure hamming

math_expectation_Last,dispersion_Last = 0,0
for i in Hamming_measure:
	math_expectation_Last += i
math_expectation_Last = math_expectation_Last/5

for i in Hamming_measure:
	dispersion_Last += (i - math_expectation_Last)*(i - math_expectation_Last)
dispersion_Last = dispersion_Last/5

absolute_hamming_measure = math_expectation_Last + 2.571*sqrt(dispersion_Last)

real_hamming_measures = 0
for i in range(0,17):
	if not(Tmin[i] < TempArr[i] < Tmax[i]):
		real_hamming_measures += 1

if(real_hamming_measures < absolute_hamming_measure):
	print("It's you")
else:
	print("It isn't you")