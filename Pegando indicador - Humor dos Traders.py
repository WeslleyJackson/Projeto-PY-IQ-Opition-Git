# Para pegar de apenas uma paridade #################
par = 'USDCHF-OTC'

API.start_mood_stream(par)

while True:
	x = API.get_traders_mood(par)
	print(int(100 * round(x, 2)))
	
	time.sleep(1)
	
API.stop_mood_stream(par)


# Para pegar de multiplas paridades #################
id = dict([(l, u) for u,l in API.get_all_ACTIVES_OPCODE().items()])

API.start_mood_stream('USDCHF-OTC')
API.start_mood_stream('GBPUSD-OTC')

while True:
	x = API.get_all_traders_mood()
	
	for i in x:
		print(id[i]+': '+str(int(100 * round(x[i], 2))), end=' ')
		
	print('\n')
	
	time.sleep(1)
	
API.stop_mood_stream('USDCHF-OTC')
API.stop_mood_stream('GBPUSD-OTC')