def main():
	info('Pump line')
	# open turbo pump
	open('4')
	sleep(10)
	gosub('CryoWaitPump')
	sleep(60)
	open('8')
	sleep(60)
	set_cryo('freeze')
	sleep(5)
	close('8')
	sleep(30)
	close('10')
