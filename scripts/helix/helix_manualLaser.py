#===============================================================================
# EXTRACTION SCRIPT helix_manualLaser.py
#===============================================================================
def main():

	info('Helix Manual Laser Script')

	gosub('CryoWaitFreeze')
	sleep(5)
	# pump line
	open('4')
	sleep(30)
	# Isolate laser chamber
	close('2')
	# 15 minute wait time for working with the laser
	sleep(900)
	# close turbopump
	close('4')
	sleep(5)
	# inlet
	open('2')
	sleep(120)

	close('11')
	sleep(5)
	open('8')
	gosub('CryoWaitFreeze')
	sleep(300)

	open('4')
	sleep(60)

	p_test = get_pressure('Maxi2','P2')
	info('the value of p_test is ={}'.format(p_test))
	if p_test > 1e-7:
		cancel()
	if p_test == 0:
		cancel()

	close('8')
	sleep(10)

	gosub('CryoWaitRelease')

	sleep(300)

#===============================================================================
# POST EQUILIBRATION SCRIPT helix_post.py
#===============================================================================
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

#===============================================================================
# POST MEASUREMENT SCRIPT helix_pump_ms.py
#===============================================================================
def main():
	info('Pump mass spec after analysis')
	open(name='1')
