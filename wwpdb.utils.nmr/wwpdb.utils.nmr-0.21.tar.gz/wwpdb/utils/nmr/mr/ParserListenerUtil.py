##
# File: ParserListenerUtil.py
# Date: 18-Feb-2022
#
# Updates:
""" Utilities for MR/PT parser listener.
    @author: Masashi Yokochi
"""
import sys
import re
import copy
import collections
import itertools

import numpy as np

try:
    from wwpdb.utils.nmr.AlignUtil import (monDict3,
                                           MAJOR_ASYM_ID_SET,
                                           LEN_MAJOR_ASYM_ID_SET)
except ImportError:
    from nmr.AlignUtil import (monDict3,
                               MAJOR_ASYM_ID_SET,
                               LEN_MAJOR_ASYM_ID_SET)


MAX_ERROR_REPORT = 1
MAX_ERR_LINENUM_REPORT = 20


REPRESENTATIVE_MODEL_ID = 1


DIST_RESTRAINT_RANGE = {'min_inclusive': 0.0, 'max_inclusive': 101.0}
DIST_RESTRAINT_ERROR = {'min_exclusive': 0.0, 'max_exclusive': 150.0}


ANGLE_RESTRAINT_RANGE = {'min_inclusive': -330.0, 'max_inclusive': 330.0}
ANGLE_RESTRAINT_ERROR = {'min_exclusive': -360.0, 'max_exclusive': 360.0}


RDC_RESTRAINT_RANGE = {'min_inclusive': -100.0, 'max_inclusive': 100.0}
RDC_RESTRAINT_ERROR = {'min_exclusive': -200.0, 'max_exclusive': 200.0}


CS_RESTRAINT_RANGE = {'min_inclusive': -300.0, 'max_inclusive': 300.0}
CS_RESTRAINT_ERROR = {'min_exclusive': -999.0, 'max_exclusive': 999.0}


CSA_RESTRAINT_RANGE = {'min_inclusive': -300.0, 'max_inclusive': 300.0}
CSA_RESTRAINT_ERROR = {'min_exclusive': -999.0, 'max_exclusive': 999.0}


PCS_RESTRAINT_RANGE = {'min_inclusive': -20.0, 'max_inclusive': 20.0}
PCS_RESTRAINT_ERROR = {'min_exclusive': -40.0, 'max_exclusive': 40.0}


CCR_RESTRAINT_RANGE = {'min_inclusive': -10.0, 'max_inclusive': 10.0}
CCR_RESTRAINT_ERROR = {'min_exclusive': -20.0, 'max_exclusive': 20.0}


PRE_RESTRAINT_RANGE = {'min_inclusive': 0.0, 'max_inclusive': 20.0}
PRE_RESTRAINT_ERROR = {'min_exclusive': 0.0, 'max_exclusive': 40.0}


T1T2_RESTRAINT_RANGE = {'min_inclusive': 1.0, 'max_inclusive': 20.0}
T1T2_RESTRAINT_ERROR = {'min_exclusive': 0.0, 'max_exclusive': 100.0}


CS_UNCERTAINTY_RANGE = {'min_inclusive': 0.0, 'max_inclusive': 3.0}

DIST_UNCERTAINTY_RANGE = {'min_inclusive': 0.0, 'max_inclusive': 5.0}

ANGLE_UNCERTAINTY_RANGE = {'min_inclusive': 0.0, 'max_inclusive': 90.0}

RDC_UNCERTAINTY_RANGE = {'min_inclusive': 0.0, 'max_inclusive': 5.0}

WEIGHT_RANGE = {'min_inclusive': 0.0, 'max_inclusive': 100.0}

SCALE_RANGE = {'min_inclusive': 0.0, 'max_inclusive': 100.0}


# @see: https://x3dna.org/highlights/torsion-angles-of-nucleic-acid-structures for nucleic acids
KNOWN_ANGLE_ATOM_NAMES = {'PHI': ['C', 'N', 'CA', 'C'],  # i-1, i, i, i
                          'PSI': ['N', 'CA', 'C', 'N'],  # i, i, i, i+1
                          'OMEGA': ['CA', 'C', 'N', 'CA'],  # i, i, i+1, i+1; modified CYANA definition [O C N (H or CD for Proline residue)]
                          'CHI1': ['N', 'CA', 'CB', re.compile(r'^[COS]G1?$')],
                          'CHI2': ['CA', 'CB', re.compile(r'^CG1?$'), re.compile(r'^[CNOS]D1?$')],
                          'CHI3': ['CB', 'CG', re.compile(r'^[CS]D$'), re.compile(r'^[CNO]E1?$')],
                          'CHI4': ['CG', 'CD', re.compile(r'^[CN]E$'), re.compile(r'^[CN]Z$')],
                          'CHI5': ['CD', 'NE', 'CZ', 'NH1'],
                          'CHI21': ['CA', 'CB', re.compile(r'^[CO]G1$'), re.compile(r'^CD1|HG11?$')],  # ILE: (CG1, CD1), THR: (OG1, HG1), VAL: (CD1, HG11)
                          'CHI22': ['CA', 'CB', 'CG2', 'HG21'],  # ILE or THR or VAL
                          'CHI31': ['CB', re.compile(r'^CG1?$'), 'CD1', 'HD11'],  # ILE: CG1, LEU: CG
                          'CHI32': ['CB', 'CG', re.compile(r'^[CO]D2$'), re.compile(r'^HD21?$')],  # ASP: (OD2, HD2), LEU: (CD2, HD21)
                          'CHI42': ['CG', 'CD', 'OE2', 'HE2'],  # GLU
                          'ALPHA': ["O3'", 'P', "O5'", "C5'"],  # i-1, i, i, i
                          'BETA': ['P', "O5'", "C5'", "C4'"],
                          'GAMMA': ["O5'", "C5'", "C4'", "C3'"],
                          'DELTA': ["C5'", "C4'", "C3'", "O3'"],
                          'EPSILON': ["C4'", "C3'", "O3'", 'P'],  # i, i, i, i+1
                          'ZETA': ["C3'", "O3'", 'P', "O5'"],  # i, i, i+1, i+1
                          # aka. CHIN (nucleic CHI angle)
                          'CHI': {'Y': ["O4'", "C1'", 'N1', 'C2'],  # for pyrimidines (i.e. C, T, U) N1/3
                                  'R': ["O4'", "C1'", 'N9', 'C4']  # for purines (i.e. G, A) N1/3/7/9
                                  },
                          'ETA': ["C4'", 'P', "C4'", 'P'],  # i-1, i, i, i+1
                          'THETA': ['P', "C4'", 'P', "C4'"],  # i, i, i+1, i+1
                          "ETA'": ["C1'", 'P', "C1'", 'P'],  # i-1, i, i, i+1
                          "THETA'": ['P', "C1'", 'P', "C1'"],  # i, i, i+1, i+1
                          'NU0': ["C4'", "O4'", "C1'", "C2'"],
                          'NU1': ["O4'", "C1'", "C2'", "C3'"],
                          'NU2': ["C1'", "C2'", "C3'", "C4'"],
                          'NU3': ["C2'", "C3'", "C4'", "O4'"],
                          'NU4': ["C3'", "C4'", "O4'", "C1'"],
                          'TAU0': ["C4'", "O4'", "C1'", "C2'"],  # identical to NU0
                          'TAU1': ["O4'", "C1'", "C2'", "C3'"],  # identical to NU1
                          'TAU2': ["C1'", "C2'", "C3'", "C4'"],  # identical to NU2
                          'TAU3': ["C2'", "C3'", "C4'", "O4'"],  # identical to NU3
                          'TAU4': ["C3'", "C4'", "O4'", "C1'"],  # identical to NU4
                          'PPA': ["C1'", "C2'", "C3'", "C4'", "O4'"]  # phase angle of pseudorotation made up from five NU[0-4] dihedral angles
                          }

# @see: http://dx.doi.org/10.1107/S0907444909001905
KNOWN_ANGLE_CARBO_ATOM_NAMES = {'PHI': [re.compile(r'^H1|O5$'), 'C1', 'O1', re.compile(r'^C[46]$')],
                                'PSI': ['C1', 'O1', re.compile(r'^C[46]$'), re.compile(r'^H4|C[35]$')],
                                'OMEGA': ['O1', 'C6', 'C5', re.compile('^H5|C4|O5$')]}

KNOWN_ANGLE_NAMES = KNOWN_ANGLE_ATOM_NAMES.keys()

KNOWN_ANGLE_SEQ_OFFSET = {'PHI': [-1, 0, 0, 0],  # i-1, i, i, i
                          'PSI': [0, 0, 0, 1],  # i, i, i, i+1
                          'OMEGA': [0, 0, 1, 1],  # i, i, i+1, i+1; modified CYANA definition [O C N (H or CD for Proline residue)]
                          'CHI1': [0] * 4,
                          'CHI2': [0] * 4,
                          'CHI3': [0] * 4,
                          'CHI4': [0] * 4,
                          'CHI5': [0] * 4,
                          'CHI21': [0] * 4,  # ILE: (CG1, CD1), THR: (OG1, HG1), VAL: (CD1, HG11)
                          'CHI22': [0] * 4,  # ILE or THR or VAL
                          'CHI31': [0] * 4,  # ILE: CG1, LEU: CG
                          'CHI32': [0] * 4,  # ASP: (OD2, HD2), LEU: (CD2, HD21)
                          'CHI42': [0] * 4,  # GLU
                          'ALPHA': [-1, 0, 0, 0],  # i-1, i, i, i
                          'BETA': [0] * 4,
                          'GAMMA': [0] * 4,
                          'DELTA': [0] * 4,
                          'EPSILON': [0, 0, 0, 1],  # i, i, i, i+1
                          'ZETA': [0, 0, 1, 1],  # i, i, i+1, i+1
                          # aka. CHIN (nucleic CHI angle)
                          'CHI': {'Y': [0] * 4,  # for pyrimidines (i.e. C, T, U) N1/3
                                  'R': [0] * 4  # for purines (i.e. G, A) N1/3/7/9
                                  },
                          'ETA': [-1, 0, 0, 1],  # i-1, i, i, i+1
                          'THETA': [0, 0, 1, 1],  # i, i, i+1, i+1
                          "ETA'": [-1, 0, 0, 1],  # i-1, i, i, i+1
                          "THETA'": [0, 0, 1, 1],  # i, i, i+1, i+1
                          'NU0': [0] * 4,
                          'NU1': [0] * 4,
                          'NU2': [0] * 4,
                          'NU3': [0] * 4,
                          'NU4': [0] * 4,
                          'TAU0': [0] * 4,  # identical to NU0
                          'TAU1': [0] * 4,  # identical to NU1
                          'TAU2': [0] * 4,  # identical to NU2
                          'TAU3': [0] * 4,  # identical to NU3
                          'TAU4': [0] * 4,  # identical to NU4
                          'PPA': [0] * 5  # phase angle of pseudorotation made up from five NU[0-4] dihedral angles
                          }

KNOWN_ANGLE_CARBO_SEQ_OFFSET = {'PHI': [0, 0, 0, -1],  # i, i, i, i-n; for n > 0
                                'PSI': [0, 0, -1, -1],  # i, i, i-n, i-n; for n > 0
                                'OMEGA': [0, -1, -1, -1]  # i, i-n, i-n, i-n; for n > 0
                                }

XPLOR_RDC_PRINCIPAL_AXIS_NAMES = ('OO', 'X', 'Y', 'Z')

XPLOR_ORIGIN_AXIS_COLS = [0, 1, 2, 3]

LEGACY_PDB_RECORDS = ['HEADER', 'OBSLTE', 'TITLE ', 'SPLIT ', 'CAVEAT', 'COMPND', 'SOURCE', 'KEYWDS', 'EXPDAT',
                      'NUMMDL', 'MDLTYP', 'AUTHOR', 'REVDAT', 'SPRSDE', 'JRNL', 'REMARK',
                      'DBREF', 'DBREF1', 'DBREF2', 'SEQADV', 'SEQRES', 'MODRES',
                      'HET ', 'HETNAM', 'HETSYN', 'FORMUL',
                      'HELIX ', 'SHEET ',
                      'SSBOND', 'LINK ', 'CISPEP',
                      'SITE ',
                      'CRYST1', 'ORIGX1', 'ORIGX2', 'ORIGX3', 'SCALE1', 'SCALE2', 'SCALE3',
                      'MTRIX1', 'MTRIX2', 'MTRIX3',
                      'MODEL ', 'ATOM ', 'ANISOU', 'TER ', 'HETATM', 'ENDMDL',
                      'CONECT',
                      'MASTER'
                      ]

CYANA_MR_FILE_EXTS = (None, 'upl', 'lol', 'aco', 'rdc', 'pcs', 'upv', 'lov', 'cco')


def toNpArray(atom):
    """ Return Numpy array of a given Cartesian coordinate in {'x': float, 'y': float, 'z': float} format.
    """

    return np.asarray([atom['x'], atom['y'], atom['z']], dtype=float)


def toRegEx(string):
    """ Return regular expression for a given string including XPLOR-NIH wildcard format.
    """

    if '*' in string:  # any string
        return string.replace('*', '.*')
    if '%' in string:  # a single character
        return string.replace('%', '.')
    if '#' in string:  # any number
        return string.replace('#', '[+-]?[0-9\\.]*')
    if '+' in string:  # any digit
        return string.replace('+', '[0-9]*')
    return string


def toNefEx(string):
    """ Return NEF regular expression for a given string including XPLOR-NIH wildcard format.
    """

    if '*' in string:  # any string
        return re.sub(r'\*\*', '*', string)
    if '%' in string:  # a single character
        return re.sub(r'\*\*', '*', string.replace('%', '*'))
    if '#' in string:  # any number
        return re.sub(r'\*\*', '*', string.replace('#', '*'))
    if '+' in string:  # any digit
        return re.sub(r'\%\%', '%', string.replace('+', '%'))
    return string


def stripOnce(string, char):
    """ Return stripped string with given chars on the both sides removed.
    """

    if len(string) < 3 or not string.startswith(char) or not string.endswith(char):
        return string

    return string[1:len(string) - 1]


def translateToStdAtomName(atomId, refCompId=None, refAtomIdList=None, ccU=None):
    """ Translate software specific atom nomenclature for standard residues to the CCD one.
    """

    atomId = atomId.upper()

    if refAtomIdList is not None:
        if atomId in refAtomIdList:
            return atomId

    elif refCompId is not None and ccU is not None:
        refCompId = translateToStdResName(refCompId)
        if ccU.updateChemCompDict(refCompId):
            refAtomIdList = [cca[ccU.ccaAtomId] for cca in ccU.lastAtomList]
            if atomId in refAtomIdList:
                return atomId
            # DNA/RNA OH 5/3 prime terminus
            if atomId.startswith("H1'"):
                if atomId == "H1''" and "H1'A" in refAtomIdList:  # 4DG
                    return "H1'A"
            elif atomId.startswith("H2'"):
                if atomId == "H2'" and "H2'1" in refAtomIdList:  # DCZ, THM
                    return "H2'1"
                if atomId == "H2''" and "H2'2" in refAtomIdList:  # DCZ, THM
                    return "H2'2"
            elif atomId.startswith("H4'"):
                if atomId == "H4''" and "H4'A" in refAtomIdList:  # 4DG
                    return "H4'A"
            elif atomId.startswith("H5'"):
                if atomId == "H5'" and "H5'1" in refAtomIdList:  # DCZ, THM
                    return "H5'1"
                if atomId == "H5''" and "H5'2" in refAtomIdList:  # DCZ, THM
                    return "H5'2"
                if atomId == "H5''" and "H5'A" in refAtomIdList:  # 4DG, 23G
                    return "H5'A"
            elif atomId.startswith('M'):  # methyl group
                if 'H' + atomId[1:] + '1' in refAtomIdList:
                    return 'H' + atomId[1:]
                candidates = ccU.getRepresentativeMethylProtons(refCompId)
                if len(candidates) == 1:
                    atomId = candidates[0]
                    return atomId[:-1] if atomId.endswith('1') else atomId
            elif (atomId[0] + 'N' + atomId[1:] in refAtomIdList) or (atomId[0] + 'N' + atomId[1:] + '1' in refAtomIdList):  # 5CM
                return atomId[0] + 'N' + atomId[1:]
            elif atomId[0].endswith('2') and (atomId[0:-1] + 'A') in refAtomIdList:
                return atomId[0:-1] + 'A'
            elif atomId[0].endswith('3') and (atomId[0:-1] + 'B') in refAtomIdList:
                return atomId[0:-1] + 'B'
            elif atomId.startswith('1H'):
                if atomId[1:] + '1' in refAtomIdList:
                    return atomId[1:] + '1'
            elif atomId.startswith('2H'):
                if atomId[1:] + '2' in refAtomIdList:
                    return atomId[1:] + '2'
            elif atomId == "HX'":  # derived from 2mko AMBER RDC restraints
                if "H4'" in refAtomIdList:
                    return "H4'"

            # ambiguous atom generated by 'makeDIST_RST'
            if atomId[0] == 'Q':
                if atomId.startswith('QP'):
                    if 'H' + atomId[2:] + '2' in refAtomIdList:
                        return 'H' + atomId[2:] + '%'
                else:
                    if 'H' + atomId[1:] + '2' in refAtomIdList:
                        return 'H' + atomId[1:] + '%'

            elif atomId[-1] in ('-', '+'):
                if atomId[:-1] + '2' in refAtomIdList:
                    return atomId[:-1] + '%'

            elif atomId[0] == 'M':
                if atomId[-1] in ('X', 'Y'):
                    if 'H' + atomId[1:-1] + '1' in refAtomIdList or 'H' + atomId[1:-1] + '11' in refAtomIdList:
                        return 'H' + atomId[1:-1] + '%'
                elif 'H' + atomId[1:] + '1' in refAtomIdList or 'H' + atomId[1:] + '11' in refAtomIdList:
                    return 'H' + atomId[1:] + '%'

            elif atomId + '2' in refAtomIdList:
                return atomId + '%'

    # GROMACS atom nomenclature
    if refCompId is not None:
        if refCompId == 'ILE':
            if atomId in ('HD1', 'HD2', 'HD3'):
                return 'HD1' + atomId[-1]
            if atomId == 'CD':
                return 'CD1'
        if len(refCompId) == 3 and refCompId in monDict3:
            if atomId == 'O1':
                return 'O'
            if atomId == 'O2':
                return 'OXT'

    if atomId.endswith("O'1"):
        atomId = atomId[:len(atomId) - 3] + "O1'"
    elif atomId.endswith("O'2"):
        atomId = atomId[:len(atomId) - 3] + "O2'"
    elif atomId.endswith("O'3"):
        atomId = atomId[:len(atomId) - 3] + "O3'"
    elif atomId.endswith("O'4"):
        atomId = atomId[:len(atomId) - 3] + "O4'"
    elif atomId.endswith("O'5"):
        atomId = atomId[:len(atomId) - 3] + "O5'"
    elif atomId.endswith("O'6"):
        atomId = atomId[:len(atomId) - 3] + "O6'"
    elif atomId.endswith("'1") and not atomId.endswith("''1"):
        atomId = atomId.rstrip('1')
    elif atomId.endswith("'2") and not atomId.endswith("''2"):
        atomId = atomId.rstrip('2') + "'"
    elif atomId == 'O1P':
        atomId = 'OP1'
    elif atomId == 'O2P':
        atomId = 'OP2'
    elif atomId == 'O3P':
        atomId = 'OP3'
    elif atomId == 'H3T':
        atomId = "HO3'"
    elif atomId == 'H5T':
        atomId = 'HOP2'
    elif atomId.endswith("''"):
        if atomId[0] in ('C', 'O') and atomId[1].isdigit():
            atomId = atomId[:len(atomId) - 1]
    elif atomId.endswith('"'):
        atomId = atomId[:len(atomId) - 1] + "''"

    if refAtomIdList is not None and atomId not in refAtomIdList:
        if not atomId.endswith("'") and (atomId + "'") in refAtomIdList:
            return atomId + "'"
        if atomId.endswith("'''") and atomId[:-1] in refAtomIdList:
            return atomId[:-1]
        if atomId == "H2''1" and "H2'" in refAtomIdList:
            return "H2'"
        if atomId in ("H2''2", "H2''"):
            if "HO2'" in refAtomIdList:
                return "HO2'"
            if "H2''" in refAtomIdList:
                return "H2''"
        if atomId.endswith("''") and atomId[:-1] in refAtomIdList:
            return atomId[:-1]
        if atomId[0] == 'H' and len(atomId) == 3 and atomId[1].isdigit() and atomId[2] in ('1', '2'):
            n = atomId[1]
            if atomId.endswith('1') and ('HN' + n) in refAtomIdList:
                return 'HN' + n
            if atomId.endswith('2') and ('HN' + n + 'A') in refAtomIdList:
                return 'HN' + n + 'A'

    return atomId


def translateToStdResName(compId):
    """ Translate software specific residue name for standard residues to the CCD one.
    """

    if len(compId) > 3:
        compId3 = compId[:3]

        if compId3 in monDict3:
            return compId3

    if compId.endswith('5') or compId.endswith('3'):
        _compId = compId[:-1]

        if _compId in monDict3:
            return _compId

    if compId.startswith('R') and compId[1] in ('A', 'C', 'G', 'U'):
        _compId = compId[1:]

        if _compId in monDict3:
            return _compId
        """ do not use
        if _compId.endswith('5') or _compId.endswith('3'):
            _compId = _compId[:-1]

            if _compId in monDict3:
                return _compId
        """
    if compId in ('HIE', 'HIP', 'HID'):
        return 'HIS'

    if len(compId) == 3:
        if compId == 'ADE' or compId.startswith('DA'):
            return 'DA'
        if compId == 'CYT' or compId.startswith('DC'):
            return 'DC'
        if compId == 'GUA' or compId.startswith('DG'):
            return 'DG'
        if compId == 'THY' or compId.startswith('DT'):
            return 'DT'

    if compId == 'RADE':
        return 'A'
    if compId == 'RCYT':
        return 'C'
    if compId == 'RGUA':
        return 'G'
    if compId == 'URA':
        return 'U'

    return compId


def checkCoordinates(verbose=True, log=sys.stdout,
                     representativeModelId=REPRESENTATIVE_MODEL_ID,
                     cR=None, prevCoordCheck=None,
                     testTag=True):
    """ Examine the coordinates for MR/PT parser listener.
    """

    changed = False

    polySeq = None if prevCoordCheck is None or 'polymer_sequence' not in prevCoordCheck else prevCoordCheck['polymer_sequence']
    altPolySeq = None if prevCoordCheck is None or 'alt_polymer_sequence' not in prevCoordCheck else prevCoordCheck['alt_polymer_sequence']
    nonPoly = None if prevCoordCheck is None or 'non_polymer' not in prevCoordCheck else prevCoordCheck['non_polymer']

    if polySeq is None:
        changed = True

        polySeqAuthMonIdName = 'auth_mon_id' if cR.hasItem('pdbx_poly_seq_scheme', 'auth_mon_id') else 'mon_id'
        nonPolyAuthMonIdName = 'auth_mon_id' if cR.hasItem('pdbx_nonpoly_scheme', 'auth_mon_id') else 'mon_id'

        # loop categories
        _lpCategories = {'poly_seq': 'pdbx_poly_seq_scheme',
                         'non_poly': 'pdbx_nonpoly_scheme',
                         'coordinate': 'atom_site'
                         }

        # key items of loop
        _keyItems = {'poly_seq': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                  {'name': 'seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                  {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'},
                                  {'name': 'pdb_strand_id', 'type': 'str', 'alt_name': 'auth_chain_id'},
                                  {'name': 'pdb_seq_num', 'type': 'int', 'alt_name': 'auth_seq_id'},
                                  {'name': polySeqAuthMonIdName, 'type': 'str', 'alt_name': 'auth_comp_id', 'default': '.'}
                                  ],
                     'non_poly': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                  {'name': 'pdb_seq_num', 'type': 'int', 'alt_name': 'seq_id'},
                                  {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'},
                                  {'name': 'pdb_strand_id', 'type': 'str', 'alt_name': 'auth_chain_id'},
                                  {'name': 'auth_seq_num', 'type': 'int', 'alt_name': 'auth_seq_id'},
                                  {'name': nonPolyAuthMonIdName, 'type': 'str', 'alt_name': 'auth_comp_id', 'default': '.'}
                                  ],
                     'coordinate': [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'auth_chain_id'},
                                    {'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                    {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'auth_seq_id'},
                                    {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'seq_id'},
                                    {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'auth_comp_id'},
                                    {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'}
                                    ]
                     }

        contentSubtype = 'poly_seq'

        lpCategory = _lpCategories[contentSubtype]
        keyItems = _keyItems[contentSubtype]

        try:

            try:
                polySeq = cR.getPolymerSequence(lpCategory, keyItems,
                                                withStructConf=False,
                                                withRmsd=False)
            except KeyError:  # pdbx_PDB_ins_code throws KeyError
                polySeq = []

            if len(polySeq) == 0:
                contentSubtype = 'coordinate'

                lpCategory = _lpCategories[contentSubtype]
                keyItems = _keyItems[contentSubtype]

                try:
                    polySeq = cR.getPolymerSequence(lpCategory, keyItems,
                                                    withStructConf=False,
                                                    withRmsd=False)
                except KeyError:
                    polySeq = []

            if len(polySeq) > 1:
                ps = copy.copy(polySeq[0])
                ps['auth_seq_id'] = ps['seq_id']
                altPolySeq = [ps]
                lastSeqId = ps['auth_seq_id'][-1]

                for chainId in range(1, len(polySeq)):
                    ps = copy.copy(polySeq[chainId])
                    if ps['seq_id'][0] <= lastSeqId:
                        offset = lastSeqId + 1 - ps['seq_id'][0]
                    else:
                        offset = 0
                    ps['auth_seq_id'] = [s + offset for s in ps['seq_id']]
                    altPolySeq.append(ps)
                    lastSeqId = ps['auth_seq_id'][-1]

        except Exception as e:
            if verbose:
                log.write(f"+ParserListenerUtil.checkCoordinates() ++ Error  - {str(e)}\n")

        contentSubtype = 'non_poly'

        lpCategory = _lpCategories[contentSubtype]
        keyItems = _keyItems[contentSubtype]

        nonPoly = None

        if cR.hasCategory(lpCategory):

            try:
                nonPoly = cR.getPolymerSequence(lpCategory, keyItems,
                                                withStructConf=False,
                                                withRmsd=False)
            except KeyError:
                nonPoly = None

    if not testTag:
        if not changed:
            return prevCoordCheck

        return {'polymer_sequence': polySeq,
                'alt_polymer_sequence': altPolySeq,
                'non_polymer': nonPoly}

    modelNumName = None if prevCoordCheck is None or 'model_num_name' not in prevCoordCheck else prevCoordCheck['model_num_name']
    authAsymId = None if prevCoordCheck is None or 'auth_asym_id' not in prevCoordCheck else prevCoordCheck['auth_asym_id']
    authSeqId = None if prevCoordCheck is None or 'auth_seq_id' not in prevCoordCheck else prevCoordCheck['auth_seq_id']
    authAtomId = None if prevCoordCheck is None or 'auth_atom_id' not in prevCoordCheck else prevCoordCheck['auth_atom_id']

    coordAtomSite = None if prevCoordCheck is None or 'coord_atom_site' not in prevCoordCheck else prevCoordCheck['coord_atom_site']
    coordUnobsRes = None if prevCoordCheck is None or 'coord_unobs_res' not in prevCoordCheck else prevCoordCheck['coord_unobs_res']
    labelToAuthSeq = None if prevCoordCheck is None or 'label_to_auth_seq' not in prevCoordCheck else prevCoordCheck['label_to_auth_seq']
    authToLabelSeq = None if prevCoordCheck is None or 'auth_to_label_seq' not in prevCoordCheck else prevCoordCheck['auth_to_label_seq']

    try:

        if modelNumName is None:
            modelNumName = 'pdbx_PDB_model_num' if cR.hasItem('atom_site', 'pdbx_PDB_model_num') else 'ndb_model'
        if authAsymId is None:
            authAsymId = 'pdbx_auth_asym_id' if cR.hasItem('atom_site', 'pdbx_auth_asym_id') else 'auth_asym_id'
        if authSeqId is None:
            authSeqId = 'pdbx_auth_seq_id' if cR.hasItem('atom_site', 'pdbx_auth_seq_id') else 'auth_seq_id'
        if authAtomId is None:
            authAtomId = 'pdbx_auth_atom_name' if cR.hasItem('atom_site', 'pdbx_auth_atom_name') else 'auth_atom_id'
        altAuthAtomId = None if authAtomId == 'auth_atom_id' else 'auth_atom_id'

        if coordAtomSite is None or labelToAuthSeq is None or authToLabelSeq is None:
            changed = True

            if len(polySeq) > LEN_MAJOR_ASYM_ID_SET:

                if altAuthAtomId is not None:
                    coord = cR.getDictListWithFilter('atom_site',
                                                     [{'name': authAsymId, 'type': 'str', 'alt_name': 'chain_id'},
                                                      {'name': 'label_asym_id', 'type': 'str', 'alt_name': 'alt_chain_id'},
                                                      {'name': authSeqId, 'type': 'int', 'alt_name': 'seq_id'},
                                                      {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'alt_seq_id'},
                                                      {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                      {'name': authAtomId, 'type': 'str', 'alt_name': 'atom_id'},
                                                      {'name': altAuthAtomId, 'type': 'str', 'alt_name': 'alt_atom_id'},
                                                      {'name': 'type_symbol', 'type': 'str'}
                                                      ],
                                                     [{'name': modelNumName, 'type': 'int',
                                                       'value': representativeModelId},
                                                      {'name': 'label_alt_id', 'type': 'enum', 'enum': ('A')},
                                                      {'name': authAsymId, 'type': 'enum', 'enum': MAJOR_ASYM_ID_SET}
                                                      ])
                else:
                    coord = cR.getDictListWithFilter('atom_site',
                                                     [{'name': authAsymId, 'type': 'str', 'alt_name': 'chain_id'},
                                                      {'name': 'label_asym_id', 'type': 'str', 'alt_name': 'alt_chain_id'},
                                                      {'name': authSeqId, 'type': 'int', 'alt_name': 'seq_id'},
                                                      {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'alt_seq_id'},
                                                      {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                      {'name': authAtomId, 'type': 'str', 'alt_name': 'atom_id'},
                                                      {'name': 'type_symbol', 'type': 'str'}
                                                      ],
                                                     [{'name': modelNumName, 'type': 'int',
                                                       'value': representativeModelId},
                                                      {'name': 'label_alt_id', 'type': 'enum', 'enum': ('A')},
                                                      {'name': authAsymId, 'type': 'enum', 'enum': MAJOR_ASYM_ID_SET}
                                                      ])

            else:

                if altAuthAtomId is not None:
                    coord = cR.getDictListWithFilter('atom_site',
                                                     [{'name': authAsymId, 'type': 'str', 'alt_name': 'chain_id'},
                                                      {'name': 'label_asym_id', 'type': 'str', 'alt_name': 'alt_chain_id'},
                                                      {'name': authSeqId, 'type': 'int', 'alt_name': 'seq_id'},
                                                      {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'alt_seq_id'},
                                                      {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                      {'name': authAtomId, 'type': 'str', 'alt_name': 'atom_id'},
                                                      {'name': altAuthAtomId, 'type': 'str', 'alt_name': 'alt_atom_id'},
                                                      {'name': 'type_symbol', 'type': 'str'}
                                                      ],
                                                     [{'name': modelNumName, 'type': 'int',
                                                       'value': representativeModelId},
                                                      {'name': 'label_alt_id', 'type': 'enum', 'enum': ('A')}
                                                      ])
                else:
                    coord = cR.getDictListWithFilter('atom_site',
                                                     [{'name': authAsymId, 'type': 'str', 'alt_name': 'chain_id'},
                                                      {'name': 'label_asym_id', 'type': 'str', 'alt_name': 'alt_chain_id'},
                                                      {'name': authSeqId, 'type': 'int', 'alt_name': 'seq_id'},
                                                      {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'alt_seq_id'},
                                                      {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                      {'name': authAtomId, 'type': 'str', 'alt_name': 'atom_id'},
                                                      {'name': 'type_symbol', 'type': 'str'}
                                                      ],
                                                     [{'name': modelNumName, 'type': 'int',
                                                       'value': representativeModelId},
                                                      {'name': 'label_alt_id', 'type': 'enum', 'enum': ('A')}
                                                      ])

            authToLabelChain = {ps['auth_chain_id']: ps['chain_id'] for ps in polySeq}

            coordAtomSite = {}
            labelToAuthSeq = {}
            chainIds = set(c['chain_id'] for c in coord)
            for chainId in chainIds:
                seqIds = set(c['seq_id'] for c in coord if c['chain_id'] == chainId)
                for seqId in seqIds:
                    seqKey = (chainId, seqId)
                    compId = next(c['comp_id'] for c in coord
                                  if c['chain_id'] == chainId and c['seq_id'] is not None and c['seq_id'] == seqId)
                    atomIds = [c['atom_id'] for c in coord
                               if c['chain_id'] == chainId and c['seq_id'] is not None and c['seq_id'] == seqId]
                    typeSymbols = [c['type_symbol'] for c in coord
                                   if c['chain_id'] == chainId and c['seq_id'] is not None and c['seq_id'] == seqId]
                    coordAtomSite[seqKey] = {'comp_id': compId, 'atom_id': atomIds, 'type_symbol': typeSymbols}
                    if altAuthAtomId is not None:
                        altAtomIds = [c['alt_atom_id'] for c in coord
                                      if c['chain_id'] == chainId and c['seq_id'] is not None and c['seq_id'] == seqId]
                        coordAtomSite[seqKey]['alt_atom_id'] = altAtomIds
                    altSeqId = next((c['alt_seq_id'] for c in coord if c['chain_id'] == chainId and c['seq_id'] == seqId), None)
                    if altSeqId is not None and altSeqId.isdigit():
                        labelToAuthSeq[(authToLabelChain[chainId], int(altSeqId))] = seqKey
            authToLabelSeq = {v: k for k, v in labelToAuthSeq.items()}

        if coordUnobsRes is None:
            coordUnobsRes = {}

            if cR.hasCategory('pdbx_unobs_or_zero_occ_residues'):

                unobs = cR.getDictListWithFilter('pdbx_unobs_or_zero_occ_residues',
                                                 [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                  {'name': 'auth_seq_id', 'type': 'str', 'alt_name': 'seq_id'},
                                                  {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'}
                                                  ],
                                                 [{'name': 'PDB_model_num', 'type': 'int', 'value': representativeModelId}
                                                  ])

                if len(unobs) > 0:
                    chainIds = set(u['chain_id'] for u in unobs)
                    for chainId in chainIds:
                        seqIds = set(int(u['seq_id']) for u in unobs if u['chain_id'] == chainId and u['seq_id'] is not None)
                        for seqId in seqIds:
                            seqKey = (chainId, seqId)
                            compId = next(u['comp_id'] for u in unobs
                                          if u['chain_id'] == chainId and u['seq_id'] is not None and int(u['seq_id']) == seqId)
                            coordUnobsRes[seqKey] = {'comp_id': compId}

                    if any(seqKey for seqKey in coordUnobsRes.keys() if seqKey not in authToLabelSeq):

                        if cR.hasItem('pdbx_unobs_or_zero_occ_residues', 'label_asym_id') and cR.hasItem('pdbx_unobs_or_zero_occ_residues', 'label_seq_id'):

                            unobs = cR.getDictListWithFilter('pdbx_unobs_or_zero_occ_residues',
                                                             [{'name': 'auth_asym_id', 'type': 'str'},
                                                              {'name': 'auth_seq_id', 'type': 'str'},
                                                              {'name': 'label_asym_id', 'type': 'str'},
                                                              {'name': 'label_seq_id', 'type': 'str'}
                                                              ],
                                                             [{'name': 'PDB_model_num', 'type': 'int', 'value': representativeModelId}
                                                              ])

                            if len(unobs) > 0:
                                for u in unobs:
                                    if u['auth_asym_id'] is not None and u['auth_seq_id'] is not None and u['label_asym_id'] is not None and u['label_seq_id'] is not None:
                                        authSeqKey = (u['auth_asym_id'], int(u['auth_seq_id']))
                                        labelSeqKey = (u['label_asym_id'], int(u['label_seq_id']))

                                        if authSeqKey not in authToLabelSeq:
                                            authToLabelSeq[authSeqKey] = labelSeqKey
                                        if labelSeqKey not in labelToAuthSeq:
                                            labelToAuthSeq[labelSeqKey] = authSeqKey

    except Exception as e:
        if verbose:
            log.write(f"+ParserListenerUtil.checkCoordinates() ++ Error  - {str(e)}\n")

    if not changed:
        return prevCoordCheck

    return {'model_num_name': modelNumName,
            'auth_asym_id': authAsymId,
            'auth_seq_id': authSeqId,
            'auth_atom_id': authAtomId,
            'alt_auth_atom_id': altAuthAtomId,
            'polymer_sequence': polySeq,
            'alt_polymer_sequence': altPolySeq,
            'non_polymer': nonPoly,
            'coord_atom_site': coordAtomSite,
            'coord_unobs_res': coordUnobsRes,
            'label_to_auth_seq': labelToAuthSeq,
            'auth_to_label_seq': authToLabelSeq}


def isLongRangeRestraint(atoms):
    """ Return whether restraint is neither an intra residue nor sequential residues.
    """

    chainIds = [a['chain_id'] for a in atoms]

    if len(collections.Counter(chainIds).most_common()) > 1:
        return True

    seqIds = [a['seq_id'] for a in atoms]

    commonSeqId = collections.Counter(seqIds).most_common()

    if len(commonSeqId) == 1:
        return False

    for s1, s2 in itertools.combinations(commonSeqId, 2):
        if abs(s1[0] - s2[0]) > 1:
            return True

    return False


def isAsymmetricRangeRestraint(atoms, chainIdSet, symmetric):
    """ Return whether restraint is asymmetric.
    """

    lenAtoms = len(atoms)

    if len(set((frozenset(atom.items()) for atom in atoms))) != lenAtoms:  # reject identical atom
        return True

    lenChainIdSet = len(chainIdSet)

    chainIds = [a['chain_id'] for a in atoms]
    indices = [chainIdSet.index(c) for c in chainIds]

    for pos, index in enumerate(indices):
        if pos == lenAtoms - 1:
            break
        if index + 1 < lenChainIdSet:
            nextIndex = index + 1
        elif symmetric == 'circular':
            nextIndex = 0
        else:
            return True
        if indices[pos + 1] != nextIndex:
            return True

    seqIds = [a['seq_id'] for a in atoms]

    commonSeqId = collections.Counter(seqIds).most_common()

    if len(commonSeqId) == 1:
        return False

    for s1, s2 in itertools.combinations(commonSeqId, 2):
        if abs(s1[0] - s2[0]) > 1:
            return True

    return False


def getTypeOfDihedralRestraint(polypeptide, polynucleotide, carbohydrates, atoms):
    """ Return type of dihedral angle restraint.
    """

    chainIds = [a['chain_id'] for a in atoms]
    seqIds = [a['seq_id'] for a in atoms]
    atomIds = [a['atom_id'] for a in atoms]

    if len(collections.Counter(chainIds).most_common()) > 1:
        return None

    commonSeqId = collections.Counter(seqIds).most_common()

    lenCommonSeqId = len(commonSeqId)

    if polypeptide:

        if lenCommonSeqId == 2:

            phiPsiCommonAtomIds = ['N', 'CA', 'C']

            # PHI or PSI
            if commonSeqId[0][1] == 3 and commonSeqId[1][1] == 1:

                # PHI
                prevSeqId = commonSeqId[1][0]

                if commonSeqId[0][0] == prevSeqId + 1:

                    j = 0
                    if seqIds[j] == prevSeqId and atomIds[j] == 'C':
                        atomIds.pop(j)
                        if atomIds == phiPsiCommonAtomIds:
                            return 'PHI'

                # PSI
                nextSeqId = commonSeqId[1][0]

                if commonSeqId[0][0] == nextSeqId - 1:

                    j = 3
                    if seqIds[j] == nextSeqId and atomIds[j] == 'N':
                        atomIds.pop(j)
                        if atomIds == phiPsiCommonAtomIds:
                            return 'PSI'

            # OMEGA
            if atomIds[0] == 'CA' and atomIds[1] == 'N' and atomIds[2] == 'C' and atomIds[3] == 'CA'\
               and seqIds[0] == seqIds[1] and seqIds[1] - 1 == seqIds[2] and seqIds[2] == seqIds[3]:
                return 'OMEGA'

            if atomIds[0] == 'CA' and atomIds[1] == 'C' and atomIds[2] == 'N' and atomIds[3] == 'CA'\
               and seqIds[0] == seqIds[1] and seqIds[1] + 1 == seqIds[2] and seqIds[2] == seqIds[3]:
                return 'OMEGA'

            # OMEGA - modified CYANA definition
            if atomIds[0] == 'O' and atomIds[1] == 'C' and atomIds[2] == 'N'\
               and (atomIds[3] == 'H' or atomIds[3] == 'CD')\
               and seqIds[0] == seqIds[1] and seqIds[1] + 1 == seqIds[2] and seqIds[2] == seqIds[3]:
                return 'OMEGA'

        elif lenCommonSeqId == 1:

            testDataType = ['CHI1', 'CHI2', 'CHI3', 'CHI4', 'CHI5',
                            'CHI21', 'CHI22', 'CHI31', 'CHI32', 'CHI42']

            for dataType in testDataType:

                found = True

                for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES[dataType]):

                    if isinstance(angAtomId, str):
                        if atomId != angAtomId:
                            found = False
                            break

                    else:
                        if not angAtomId.match(atomId):
                            found = False
                            break

                if found:
                    return dataType

        testDataType = ['PHI', 'PSI', 'OMEGA',
                        'CHI1', 'CHI2', 'CHI3', 'CHI4', 'CHI5',
                        'CHI21', 'CHI22', 'CHI31', 'CHI32', 'CHI42']

        for dataType in testDataType:

            found = True

            for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES[dataType]):

                if isinstance(angAtomId, str):
                    if atomId != angAtomId:
                        found = False
                        break

                else:
                    if not angAtomId.match(atomId):
                        found = False
                        break

            if found:
                return None

    elif polynucleotide:

        if lenCommonSeqId == 3:

            # ETA or ETA'
            _seqIds = [s - o for s, o in zip(seqIds, KNOWN_ANGLE_SEQ_OFFSET['ETA'])]
            _commonSeqId = collections.Counter(_seqIds).most_common()

            if len(_commonSeqId) == 1:

                testDataType = ['ETA', "ETA'"]

                for dataType in testDataType:

                    found = True

                    for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES[dataType]):

                        if atomId != angAtomId:
                            found = False
                            break

                    if found:
                        return dataType

        elif lenCommonSeqId == 2:

            # ALPHA or EPSILON or ZETA or THETA or or THETA'
            testDataType = ['ALPHA', 'EPSILON', 'ZETA', 'THETA', "THETA'"]

            for dataType in testDataType:
                _seqIds = [s - o for s, o in zip(seqIds, KNOWN_ANGLE_SEQ_OFFSET[dataType])]
                _commonSeqId = collections.Counter(_seqIds).most_common()

                if len(_commonSeqId) == 1:

                    found = True

                    for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES[dataType]):

                        if atomId != angAtomId:
                            found = False
                            break

                    if found:
                        return dataType

        elif lenCommonSeqId == 1:

            if 'N1' in atomIds:

                found = True

                for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES['CHI']['Y']):

                    if atomId != angAtomId:
                        found = False
                        break

                if found:
                    return 'CHI'

            elif 'N9' in atomIds:

                found = True

                for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES['CHI']['R']):

                    if atomId != angAtomId:
                        found = False
                        break

                if found:
                    return 'CHI'

            else:

                # BETA or GAMMA or DELTA or NU0 or NU1 or NU2 or NU4
                testDataType = ['BETA', 'GAMMA', 'DELTA', 'NU0', 'NU1', 'NU2', 'NU3', 'NU4']

                for dataType in testDataType:

                    found = True

                    for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES[dataType]):

                        if atomId != angAtomId:
                            found = False
                            break

                    if found:
                        return dataType

        testDataType = ['ETA', "ETA'",
                        'ALPHA', 'EPSILON', 'ZETA', 'THETA', "THETA'",
                        'BETA', 'GAMMA', 'DELTA', 'NU0', 'NU1', 'NU2', 'NU3', 'NU4']

        for dataType in testDataType:

            found = True

            for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES[dataType]):

                if isinstance(angAtomId, str):
                    if atomId != angAtomId:
                        found = False
                        break

                else:
                    if not angAtomId.match(atomId):
                        found = False
                        break

            if found:
                return None

        if 'N1' in atomIds:

            found = True

            for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES['CHI']['Y']):

                if atomId != angAtomId:
                    found = False
                    break

            if found:
                return None

        elif 'N9' in atomIds:

            found = True

            for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_ATOM_NAMES['CHI']['R']):

                if atomId != angAtomId:
                    found = False
                    break

            if found:
                return None

    elif carbohydrates:

        if lenCommonSeqId == 2:

            # PHI or PSI or OMEGA
            testDataType = ['PHI', 'PSI', 'OMEGA']

            for dataType in testDataType:
                seqId1 = seqIds[0]
                seqId4 = seqIds[3]

                if seqId1 > seqId4:
                    m = seqId1 - seqId4
                    _seqIds = [s - o * m for s, o in zip(seqIds, KNOWN_ANGLE_CARBO_SEQ_OFFSET[dataType])]
                    _commonSeqId = collections.Counter(_seqIds).most_common()

                    if len(_commonSeqId) == 1:

                        found = True

                        for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_CARBO_ATOM_NAMES[dataType]):

                            if isinstance(angAtomId, str):
                                if atomId != angAtomId:
                                    found = False
                                    break

                            else:
                                if not angAtomId.match(atomId):
                                    found = False
                                    break

                        if found:
                            return dataType

        testDataType = ['PHI', 'PSI', 'OMEGA']

        for dataType in testDataType:

            found = True

            for atomId, angAtomId in zip(atomIds, KNOWN_ANGLE_CARBO_ATOM_NAMES[dataType]):

                if isinstance(angAtomId, str):
                    if atomId != angAtomId:
                        found = False
                        break

                else:
                    if not angAtomId.match(atomId):
                        found = False
                        break

            if found:
                return None

    return '.' if lenCommonSeqId == 1 else None


def startsWithPdbRecord(line):
    """ Return whether a given line string starts with legacy PDB records.
    """

    if any(line.startswith(pdb_record) for pdb_record in LEGACY_PDB_RECORDS):
        return True

    return any(line[:-1] == pdb_record[:-1] for pdb_record in LEGACY_PDB_RECORDS if pdb_record.endswith(' '))


def isCyclicPolymer(cR, polySeq, authAsymId, representativeModelId=1, modelNumName='PDB_model_num'):
    """ Return whether a given chain is cyclic polymer based on coordinate annotation.
    """

    if cR is None or polySeq is None:
        return False

    ps = next((ps for ps in polySeq if ps['auth_chain_id'] == authAsymId), None)

    if ps is None:
        return False

    labelAsymId = ps['chain_id']
    begAuthSeqId = ps['auth_seq_id'][0]
    endAuthSeqId = ps['auth_seq_id'][-1]
    begLabelSeqId = ps['seq_id'][0]
    endLabelSeqId = ps['seq_id'][-1]

    try:

        if cR.hasItem('struct_conn', 'pdbx_leaving_atom_flag'):
            struct_conn = cR.getDictListWithFilter('struct_conn',
                                                   [{'name': 'conn_type_id', 'type': 'str'}
                                                    ],
                                                   [{'name': 'pdbx_leaving_atom_flag', 'type': 'str', 'value': 'both'},
                                                    {'name': 'ptnr1_label_asym_id', 'type': 'str', 'value': labelAsymId},
                                                    {'name': 'ptnr2_label_asym_id', 'type': 'str', 'value': labelAsymId},
                                                    {'name': 'ptnr1_label_seq_id', 'type': 'int', 'value': begLabelSeqId},
                                                    {'name': 'ptnr2_label_seq_id', 'type': 'int', 'value': endLabelSeqId},
                                                    ])
        else:
            struct_conn = cR.getDictListWithFilter('struct_conn',
                                                   [{'name': 'conn_type_id', 'type': 'str'}
                                                    ],
                                                   [{'name': 'ptnr1_label_asym_id', 'type': 'str', 'value': labelAsymId},
                                                    {'name': 'ptnr2_label_asym_id', 'type': 'str', 'value': labelAsymId},
                                                    {'name': 'ptnr1_label_seq_id', 'type': 'int', 'value': begLabelSeqId},
                                                    {'name': 'ptnr2_label_seq_id', 'type': 'int', 'value': endLabelSeqId},
                                                    ])

    except Exception:
        return False

    if len(struct_conn) == 0:

        try:

            close_contact = cR.getDictListWithFilter('pdbx_validate_close_contact',
                                                     [{'name': 'dist', 'type': 'float'}
                                                      ],
                                                     [{'name': modelNumName, 'type': 'int', 'value': representativeModelId},
                                                      {'name': 'auth_asym_id_1', 'type': 'str', 'value': authAsymId},
                                                      {'name': 'auth_seq_id_1', 'type': 'int', 'value': begAuthSeqId},
                                                      {'name': 'auth_atom_id_1', 'type': 'str', 'value': 'N'},
                                                      {'name': 'auth_asym_id_2', 'type': 'str', 'value': authAsymId},
                                                      {'name': 'auth_seq_id_2', 'type': 'int', 'value': endAuthSeqId},
                                                      {'name': 'auth_atom_id_2', 'type': 'str', 'value': 'C'}
                                                      ])

        except Exception:
            return False

        if len(close_contact) == 0:

            bond = getCoordBondLength(cR, labelAsymId, begLabelSeqId, 'N', labelAsymId, endLabelSeqId, 'C', modelNumName)

            if bond is None:
                return False

            distance = next((b['distance'] for b in bond if b['model_id'] == representativeModelId), None)

            if distance is None:
                return False

            return 1.2 < distance < 1.4

        return 1.2 < close_contact[0]['dist'] < 1.4

    return struct_conn[0]['conn_type_id'] == 'covale'


def getCoordBondLength(cR, labelAsymId1, labelSeqId1, labelAtomId1, labelAsymId2, labelSeqId2, labelAtomId2, modelNumName='PDB_model_num'):
    """ Return the bond length of given two CIF atoms.
        @return: the bond length
    """

    try:

        atom_site_1 = cR.getDictListWithFilter('atom_site',
                                               [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                {'name': modelNumName, 'type': 'int', 'alt_name': 'model_id'}
                                                ],
                                               [{'name': 'label_asym_id', 'type': 'str', 'value': labelAsymId1},
                                                {'name': 'label_seq_id', 'type': 'int', 'value': labelSeqId1},
                                                {'name': 'label_atom_id', 'type': 'str', 'value': labelAtomId1},
                                                {'name': 'label_alt_id', 'type': 'enum', 'enum': ('A')}
                                                ])

        atom_site_2 = cR.getDictListWithFilter('atom_site',
                                               [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                {'name': modelNumName, 'type': 'int', 'alt_name': 'model_id'}
                                                ],
                                               [{'name': 'label_asym_id', 'type': 'str', 'value': labelAsymId2},
                                                {'name': 'label_seq_id', 'type': 'int', 'value': labelSeqId2},
                                                {'name': 'label_atom_id', 'type': 'str', 'value': labelAtomId2},
                                                {'name': 'label_alt_id', 'type': 'enum', 'enum': ('A')}
                                                ])

    except Exception:
        return None

    model_ids = set(a['model_id'] for a in atom_site_1) | set(a['model_id'] for a in atom_site_2)

    bond = []

    for model_id in model_ids:
        a_1 = next((a for a in atom_site_1 if a['model_id'] == model_id), None)
        a_2 = next((a for a in atom_site_2 if a['model_id'] == model_id), None)

        if a_1 is None or a_2 is None:
            continue

        bond.append({'model_id': model_id, 'distance': float(f"{np.linalg.norm(toNpArray(a_1) - toNpArray(a_2)):.3f}")})

    if len(bond) > 0:
        return bond

    return None
