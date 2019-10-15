#===============================================================================
# EXTRACTION SCRIPT helix_manual_furnace.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 60
'''
def main():
    info('Helix Manual Furnace Script')
    # For using the manual furnace controller
    close('16')
    close('18')
    open('17')
    gosub('CryoWaitFreeze')
    sleep(5)
    open('9')
    open('50')
    sleep(5)
    open('10')
    open('13')
    open('59')
    open('55')
    open('56')
    open('57')
    sleep(30)
    open('52')
    open('51')
    sleep(60)
    close('51')
    close('52')
    sleep(5)
    info('Heat furnace')
    sleep(600)
    # close furnace
    close('55')
    close('57')
    sleep(5)
    open('52')
    open('51')
    if not analysis_type=='blank':
        info('Drop sample')
    sleep(1200)
    # inlet furnace and wait for first stage cleanup
    close('50')
    open('55')
    sleep(120)
    # open bare cryostat and freeze
    close('18')
    close('15')
    sleep(5)
    open('17')
    open('16')
    gosub('CryoWaitFreeze')
    sleep(120)
    # open charcoal cryostat and focus
    close('13')
    sleep(5)
    open('15')
    open('14')
    gosub('CryoWaitFreeze')
    sleep(900)
    # isolate charcoal, pump remainder, warm to release
    close('15')
    close('14')
    sleep(10)
    open('50')
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
# POST EQUILIBRATION SCRIPT helix_furnace.py
#===============================================================================
def main():
	info('Pump line after furnace input')
	open('50')
	open('57')
	open('9')
	sleep(10)
	gosub('CryoWaitPump')
	sleep(60)
	close('16')
	open('15')
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
