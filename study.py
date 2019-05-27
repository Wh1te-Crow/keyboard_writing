import pickle,time
from pynput.keyboard import Listener
arr = []
print("enter 15 times the word:'APOLOGIZE'")
for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
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
	arr.append(TempArr)
	print("you entered {} words".format(i))

print("you have finished typing")
print(arr)

with open('data.pickle','wb') as f:
	pickle.dump(arr,f)



