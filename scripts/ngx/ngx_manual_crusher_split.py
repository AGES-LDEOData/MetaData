#===============================================================================
# EXTRACTION SCRIPT ngx_manual_crusher_split.py
#===============================================================================
"""
eqtime: 30
"""
def main():
    info('NGX manual crusher analysis')
    sleep(10)

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_crusher.py
#===============================================================================
def main():
	info('Pump after crusher analysis')
	sleep(3)
	open('D')
	open('A')
	open('C')
	open('I')
	open('J')
	gosub('CryoWaitPump')
	sleep(120)
	close('C')
	set_cryo('freeze')
	# gosub('jan:PumpMicrobone')
	# gosub('jan:PumpMinibone')
	#

#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='Z')
