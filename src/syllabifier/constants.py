#!/usr/bin/env python3
import re

# Sets required to check for valid onset and coda clusters
VOICELESS = set(['K', 'KCL', 'P', 'PCL', 'T', 'TCL', 'F', 'HH', 'HV', 'S', 'SH', 'TH', 'CH', 'AX-H', 'Q'])
VOICED = set(['G', 'GCL', 'B', 'BCL', 'D', 'DCL', 'DX' 'DH', 'V', 'Z', 'ZH', 'JH'])

STOPS = set(['K', 'KCL', 'P', 'PCL', 'T', 'TCL', 'G', 'GCL', 'B', 'BCL', 'D', 'DCL', 'DX', 'Q'])
FRICATIVES = set(['F', 'DH', 'HH', 'HV', 'S', 'SH', 'TH', 'V', 'Z', 'ZH'])
AFFRICATES = set(['CH', 'JH'])
NASALS = set(['M', 'N', 'NG'])
APPROXIMANTS = set(['L', 'R', 'W', 'Y'])
CONSONANTS = STOPS.union(FRICATIVES).union(AFFRICATES).union(NASALS).union(APPROXIMANTS)

S_EXTENDED_CODAS = set(['K', 'KCL', 'P', 'PCL', 'T', 'TCL', 'F', 'TH', 'D', 'DCL', 'DX', 'NG'])
Z_EXTENDED_CODAS = set(['G', 'GCL', 'B', 'BCL', 'D', 'DX', 'DH', 'V', 'M', 'N', 'NG', 'L'])

T_EXTENDED_CODAS = set(['K', 'KCL', 'P', 'PCL', 'F', 'S', 'SH', 'TH', 'CH', 'N', 'Q'])
D_EXTENDED_CODAS = set(['G', 'GCL', 'B', 'BCL', 'DH', 'V', 'Z', 'ZH', 'JH', 'M', 'N', 'NG'])

PHONESET = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'AX-H', 'AX', 'AXR', 'B', 'BCL', 
                'CH', 'D', 'DX', 'DH', 'EH', 'ER', 'EY', 'F', 'G', 'GCL',
                'HH', 'HV', 'IH', 'IX', 'IY', 'JH', 'K', 'KCL', 'L', 'M', 'N',
                'NG', 'OW', 'OY', 'P', 'PCL', 'R', 'S', 'SH', 'T', 'TCL',
                'TH', 'UH', 'UW', 'UX' 'V', 'W', 'Y', 'Z', 'ZH', 'Q'])

# Optional stress markers (0,1,2) after the vowel for flexibility
VOWELS_REGEX = re.compile(r'(?:AA|AE|AH|AO|AW|AY|EH|ER|EY|IH|IY|OW|OY|UW|UH|IX|UX|AX|AXR)[012]?')
