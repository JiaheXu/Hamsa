# TODO: Lower the amount of duplicated code in this module

from os.path import expandvars
import yaml
from hamsa import firmware
import configparser

hamsa_config = expandvars('$HOME/robothand/hamsa/hamsa.config')
config = configparser.ConfigParser()
config.read(hamsa_config)

robo_hand = firmware.Hand()

##########################################
# Curling functions
##########################################

# Actuating

def curl_pinky(position, time):
    finger_data = config['pinky curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    robo_hand.curl(position, time, *params)

def curl_ring(position, time):
    finger_data = config['ring curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    robo_hand.curl(position, time, *params)

def curl_middle(position, time):
    finger_data = config['middle curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    robo_hand.curl(position, time, *params)

def curl_index(position, time):
    finger_data = config['index curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    robo_hand.curl(position, time, *params)

def curl_thumb(position, time):
    finger_data = config['thumb curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    robo_hand.curl(position, time, *params)

def curl_wrist(position, time):
    finger_data = config['wrist']
    params = [finger_data.getint('forwards'), finger_data.getint('backwards'), finger_data.getint('id')]
    robo_hand.curl(position, time, *params)

# Position querying

def curl_pinky_pos():
    finger_data = config['pinky curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    return robo_hand.curl_position(*params)

def curl_ring_pos():
    finger_data = config['ring curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    return robo_hand.curl_position(*params)

def curl_middle_pos():
    finger_data = config['middle curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    return robo_hand.curl_position(*params)

def curl_index_pos():
    finger_data = config['index curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    return robo_hand.curl_position(*params)

def curl_thumb_pos():
    finger_data = config['thumb curl']
    params = [finger_data.getint('in'), finger_data.getint('out'), finger_data.getint('id')]
    return robo_hand.curl_position(*params)

def curl_wrist_pos():
    finger_data = config['wrist curl']
    params = [finger_data.getint('forwards'), finger_data.getint('backwards'), finger_data.getint('id')]
    return robo_hand.curl_position(*params)

##########################################
# Wiggling functions
##########################################

def wiggle_pinky(position, time):
    finger_data = config['pinky wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    robo_hand.wiggle(position, time, *params)

def wiggle_ring(position, time):
    finger_data = config['ring wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    robo_hand.wiggle(position, time, *params)

def wiggle_middle(position, time):
    finger_data = config['middle wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    robo_hand.wiggle(position, time, *params)

def wiggle_index(position, time):
    finger_data = config['index wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    robo_hand.wiggle(position, time, *params)

def wiggle_thumb(position, time):
    finger_data = config['thumb wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    robo_hand.wiggle(position, time, *params)

# Position querying

def wiggle_pinky_pos():
    finger_data = config['pinky wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    return robo_hand.wiggle_position(*params)

def wiggle_ring_pos():
    finger_data = config['ring wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    return robo_hand.wiggle_position(*params)

def wiggle_middle_pos():
    finger_data = config['middle wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    return robo_hand.wiggle_position(*params)

def wiggle_index_pos():
    finger_data = config['index wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    return robo_hand.wiggle_position(*params)

def wiggle_thumb_pos():
    finger_data = config['thumb wiggle']
    params = [finger_data.getint('left'), finger_data.getint('right'), finger_data.getint('id')]
    return robo_hand.wiggle_position(*params)
