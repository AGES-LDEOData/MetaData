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
    sleep(180)

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_air.py
#===============================================================================
def main():
	info('Pump after air analysis')
	sleep(3)
	open('D')
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
