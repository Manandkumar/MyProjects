capitals_india={

'Andhra Pradesh':'Hyderabad',
'Arunachal Pradesh':'Itanagar',
'Assam':'Dispur',
'Bihar':'Patna',
'Chhattisgarh':'Raipur',
'Goa':'Panaji',
'Gujarat':'Gandhinagar',
'Haryana':'Chandigarh',
'Himachal Pradesh':'Shimla',
'Jammu and Kashmir':'Srinagar,Jammu',
'Jharkhand':'Ranchi',
'Karnataka':'Bengaluru',
'Kerala':'Thiruvananthapuram',
'Madhya Pradesh':'Bhopal',
'Maharashtra':'Mumbai',
'Manipur':'Imphal',
'Meghalaya':'Shillong',
'Mizoram':'Aizawl',
'Nagaland':'Kohima',
'Odisha':'Bhubaneswar',
'Punjab':'Chandigarh',
'Rajasthan':'Jaipur',
'Sikkim':'Gangtok',
'Tamil Nadu':'Chennai',
'Telangana':'Hyderabad',
'Tripura':'Agartala',
'Uttar Pradesh':'Lucknow',
'Uttarakhand':'Dehradun',
'West Bengal':'Kolkata'

}

import random

states= list(capitals_india.keys())

for i in [1,2,3,4,5,6]:
	state =random.choice(states)
	capital=capitals_india[state]
    print"What is the capital of " + state +"?"

import speech_recognition as sr
r=sr.Recognizer()
	with sr.Microphone() as source
    audio =r.adjust_for_ambient_noise()
    audio=r.listen(source)

	capital_guess =r.recognize_google(audio)

	if capital_guess == capital:
		print("Correct! Nice Job..")
	else:
		print("Incorrect!!! The capital of " +state + " is : " + capital +".")
print ("All done")
