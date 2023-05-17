#!Measurement
'''
baseline:
  after: true
  before: false
  counts: 10
  detector: AX
  mass: 37.5
default_fits: nominal
equilibration:
  eqtime: 5
  inlet: B
  inlet_delay: 3
  outlet: Z
  use_extraction_eqtime: true
multicollect:
  counts: 75
  detector: AX
  isotope: Ar38
peakcenter:
  config_name: default
  after: true
  before: false
  detector: H4
  isotope: Ar40
peakhop:
  hops_name: hop
  use_peak_hop: true

'''
#this is commit three
#equilibration
#EQ_TIME= 5.0



ACTIVE_DETECTORS=('H4','H2','AX','L2','L4')

def main():
    #this is a comment
    '''
        this is a multiline
        comment aka docstring
    '''
    #display information with info(msg)
    info('unknown measurement script')

    #set the spectrometer parameters
    #provide a value
    # set_source_parameters(YSymmetry=10)

    #or leave blank and values are loaded from a config file (setupfiles/spectrometer/config.cfg)
    # set_source_optics()

    #set the cdd operating voltage
    # set_cdd_operating_voltage(100)

    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)

    #open a plot panel for this detectors
    activate_detectors(*ACTIVE_DETECTORS)

    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector)


    #position mass spectrometer
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    #gas is staged behind inlet

    #post equilibration script triggered after eqtime elapsed
    #equilibrate is non blocking
    #so use either a sniff of sleep as a placeholder until eq finished
    if mx.equilibration.use_extraction_eqtime:
        e = ex.eqtime
    else:
        e = mx.equilibration.eqtime
    set_integration_time(1)
    equilibrate(eqtime=e*1.1, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet,
                delay=mx.equilibration.inlet_delay)

    #equilibrate returns immediately after the inlet opens
    set_time_zero()

    sniff(e)
    #set default regression
    set_fits()
    set_baseline_fits()

    #multicollect on active detectors
    set_integration_time(10)
    multicollect(ncounts=mx.multicollect.counts, integration_time=10)

    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector, integration_time=10)

    set_integration_time(1)
    if mx.peakcenter.after:
        activate_detectors(*ACTIVE_DETECTORS, peak_center=True)
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope, integration_time=1, config_name=mx.peakcenter.config_name)
    info('finished measure script')

    sleep(20)

#========================EOF==============================================================
    #peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)
    #baselines(counts=50,mass=0.5, detector='CDD')s

#isolate sniffer volume
    # close('S')
#     sleep(1)
#
#     #open to mass spec
#     open('R')
#
#     set_time_zero()
#     #display pressure wave
#     sniff(5)
#
#     #define sniff/split threshold
#     sniff_threshold=100
#
#     #test condition
#     #if get_intensity('H1')>sniff_threshold:
#     if True:
#         gosub('splits:jan_split', klass='ExtractionLinePyScript')
#
