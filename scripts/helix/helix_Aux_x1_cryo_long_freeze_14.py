#===============================================================================
# EXTRACTION SCRIPT helix_Aux_x1_cryo_long_freeze_14.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('Helix MC Aux Tank Standard Script')
    # Aux tank is hooked up at valve 59; set correct control valve numbers!
    close('16')
    close('18')
    gosub('CryoWaitFreeze_14')
    sleep(5)
    open('9')
    open('50')
    sleep(5)
    open('10')
    open('13')
    open('59')
    sleep(30)
    # pump pipette
    open('37')
    sleep(120)
    close('37')
    sleep(15)
    # fill pipette
    if not analysis_type=='blank':
        open('36')
    sleep(60)
    close('36')
    sleep(15)
    # close turbopump
    close('50')
    sleep(5)
    # inlet pipette and wait for first stage cleanup
    open('37')
    sleep(120)
    # open bare cryostat and freeze
    close('15')
    sleep(5)
    open('17')
    open('16')
    gosub('CryoWaitFreeze_14')
    sleep(120)
    # open charcoal cryostat and focus
    close('13')
    sleep(5)
    open('15')
    open('14')
    gosub('CryoWaitFreeze_14')
    sleep(360)
    # isolate charcoal, pump remainder, warm to release
    close('15')
    close('14')
    sleep(10)
    # open 10 and 13 if closed (might depend on getter/quad usage)
    open('10')
    open('13')
    sleep(5)
    # ensure pumping
    open('9')
    gosub('CryoWaitRelease')
    sleep(300)
    # equilibrate into inlet volume, then prepare to inlet
    close('9')
    sleep(5)
    open('14')

#===============================================================================
# POST EQUILIBRATION SCRIPT helix_aux.py
#===============================================================================
def main():
	info('Pump line after aux tank input')
	open('50')
	open('9')
	sleep(10)
	close('3')
	gosub('CryoWaitPump')
	sleep(60)
	open('3')
	close('16')
	open('15')
	close('37')
	sleep(60)
	set_cryo('freeze')
	sleep(5)
	close('14')

#===============================================================================
# POST MEASUREMENT SCRIPT helix_pump_ms.py
#===============================================================================
def main():
	info('Pump mass spec after analysis')
	open(name='1')
