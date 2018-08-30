#===============================================================================
# EXTRACTION SCRIPT ngx_manual_crusher.py
#===============================================================================
"""
eqtime: 30
"""
def main():
    info('NGX manual crusher analysis')
    close('C')
    gosub('CryoWaitFreeze')
    open('I')
    open('J')
    open('D')
    open('A')
    sleep(20)
    p_test = get_pressure('Hub','IG1')
    info('the value of p_test is ={}'.format(p_test))
    if p_test > 1e-7:
        cancel()
    if p_test == 0:
        cancel()
    if analysis_type=='blank':
        close('J')
        info('is blank. do not crush')
        sleep(duration)
    else:
        close('J')
        info('Crush!')
        sleep(duration)
    close('A')
    close('D')
    open('J')
    sleep(cleanup)
    open('C')
    gosub('CryoWaitFreeze')
    sleep(240)
    close('A')
    sleep(5)
    open('D')
    gosub('CryoWaitRelease')
    p_test = get_pressure('Hub','IG1')
    info('the value of p_test is ={}'.format(p_test))
    if p_test > 1e-7:
        cancel()
    if p_test == 0:
        cancel()
    sleep(300)

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
