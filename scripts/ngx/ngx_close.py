#===============================================================================
# EXTRACTION SCRIPT ngx_close.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('NGX close then pause')
    close('D')
    sleep(cleanup)

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_air.py
#===============================================================================
def main():
	info('Pump after air analysis')
	cryofocus = False
	sleep(3)
	open('D')
	if cryofocus:
		open('A')
		open('C')
		gosub('CryoWaitPump')
		sleep(120)
		close('C')
		set_cryo('freeze')
	close('G')
	open('A')
	# gosub('jan:PumpMicrobone')
	# gosub('jan:PumpMinibone')
	#

#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='Z')
