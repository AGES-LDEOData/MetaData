#===============================================================================
# EXTRACTION SCRIPT helix_air_pipette.py
#===============================================================================
def main():

	info('Helix MC Air Shot Script')

	gosub('CryoWaitFreeze')
	sleep(5)
	# pump line
	open('4')
	sleep(5)
	open('6')
	sleep(30)
	# pump pipette
	open('10')
	sleep(120)
	close('10')
	sleep(15)
	# fill pipette
	if not analysis_type=='blank':
		open('9')
	sleep(60)
	close('9')
	sleep(15)
	# close turbopump
	close('4')
	sleep(5)
	# inlet pipette
	open('10')
	sleep(120)

	close('11')
	sleep(5)
	open('8')
	gosub('CryoWaitFreeze')
	sleep(600)

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

	sleep(600)

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
