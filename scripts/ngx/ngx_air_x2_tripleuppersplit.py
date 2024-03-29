#===============================================================================
# EXTRACTION SCRIPT ngx_air_x2_tripleuppersplit.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('NGX Air Script')
    p_test = get_pressure('Hub','IG1')
    info('the value of p_test is ={}'.format(p_test))
    if p_test > 1e-7:
        cancel()
    if p_test == 0:
        cancel()
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
    sleep(120)
    close('G')
    sleep(5)
    if not analysis_type=='blank':
        open('H')
    sleep(60)
    close('H')
    sleep(5)
    open('G')
    sleep(cleanup)
    close('A')
    sleep(5)
    open('D')
    sleep(30)
    close('D')
    sleep(5)
    open('A')
    sleep(30)
    close('A')
    sleep(5)
    open('D')
    sleep(30)
    close('D')
    sleep(5)
    open('A')
    sleep(30)
    close('A')
    sleep(5)

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
