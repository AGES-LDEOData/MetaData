#===============================================================================
# EXTRACTION SCRIPT ngx_air_x1_uppersplit.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('NGX Air Script')
    open('D')
    open('A')
    close('H')
    sleep(5)
    open('G')
    sleep(120)
    close('G')
    sleep(5)
    if not analysis_type=='blank':
        open('H')
    sleep(60)
    close('H')
    close('D')
    sleep(5)
    open('G')
    sleep(180)
    close('A')

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_air.py
#===============================================================================
def main():
	info('Pump after air analysis')
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
