##
# File: CyanaMRParserListener.py
# Date: 27-Jan-2022
#
# Updates:
# Generated from CyanaMRParser.g4 by ANTLR 4.10.1
""" ParserLister class for CYANA MR files.
    @author: Masashi Yokochi
"""
import sys
import itertools
import numpy

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from wwpdb.utils.nmr.mr.CyanaMRParser import CyanaMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (toNpArray,
                                                       checkCoordinates,
                                                       translateToStdResName,
                                                       translateToStdAtomName,
                                                       isLongRangeRestraint,
                                                       isCyclicPolymer,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR,
                                                       PCS_RESTRAINT_RANGE,
                                                       PCS_RESTRAINT_ERROR,
                                                       KNOWN_ANGLE_NAMES,
                                                       KNOWN_ANGLE_ATOM_NAMES,
                                                       KNOWN_ANGLE_SEQ_OFFSET,
                                                       KNOWN_ANGLE_CARBO_ATOM_NAMES,
                                                       KNOWN_ANGLE_CARBO_SEQ_OFFSET,
                                                       CYANA_MR_FILE_EXTS)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                             ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from wwpdb.utils.nmr.AlignUtil import (monDict3,
                                           updatePolySeqRst,
                                           sortPolySeqRst,
                                           alignPolymerSequence,
                                           assignPolymerSequence,
                                           trimSequenceAlignment,
                                           retrieveAtomIdentFromMRMap,
                                           retrieveRemappedSeqId,
                                           splitPolySeqRstForMultimers,
                                           retrieveRemappedChainId)
except ImportError:
    from nmr.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from nmr.mr.CyanaMRParser import CyanaMRParser
    from nmr.mr.ParserListenerUtil import (toNpArray,
                                           checkCoordinates,
                                           translateToStdResName,
                                           translateToStdAtomName,
                                           isLongRangeRestraint,
                                           isCyclicPolymer,
                                           REPRESENTATIVE_MODEL_ID,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR,
                                           PCS_RESTRAINT_RANGE,
                                           PCS_RESTRAINT_ERROR,
                                           KNOWN_ANGLE_NAMES,
                                           KNOWN_ANGLE_ATOM_NAMES,
                                           KNOWN_ANGLE_SEQ_OFFSET,
                                           KNOWN_ANGLE_CARBO_ATOM_NAMES,
                                           KNOWN_ANGLE_CARBO_SEQ_OFFSET,
                                           CYANA_MR_FILE_EXTS)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                 ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from nmr.AlignUtil import (monDict3,
                               updatePolySeqRst,
                               sortPolySeqRst,
                               alignPolymerSequence,
                               assignPolymerSequence,
                               trimSequenceAlignment,
                               retrieveAtomIdentFromMRMap,
                               retrieveRemappedSeqId,
                               splitPolySeqRstForMultimers,
                               retrieveRemappedChainId)


DIST_RANGE_MIN = DIST_RESTRAINT_RANGE['min_inclusive']
DIST_RANGE_MAX = DIST_RESTRAINT_RANGE['max_inclusive']

DIST_ERROR_MIN = DIST_RESTRAINT_ERROR['min_exclusive']
DIST_ERROR_MAX = DIST_RESTRAINT_ERROR['max_exclusive']


ANGLE_RANGE_MIN = ANGLE_RESTRAINT_RANGE['min_inclusive']
ANGLE_RANGE_MAX = ANGLE_RESTRAINT_RANGE['max_inclusive']

ANGLE_ERROR_MIN = ANGLE_RESTRAINT_ERROR['min_exclusive']
ANGLE_ERROR_MAX = ANGLE_RESTRAINT_ERROR['max_exclusive']


RDC_RANGE_MIN = RDC_RESTRAINT_RANGE['min_inclusive']
RDC_RANGE_MAX = RDC_RESTRAINT_RANGE['max_inclusive']

RDC_ERROR_MIN = RDC_RESTRAINT_ERROR['min_exclusive']
RDC_ERROR_MAX = RDC_RESTRAINT_ERROR['max_exclusive']


PCS_RANGE_MIN = PCS_RESTRAINT_RANGE['min_inclusive']
PCS_RANGE_MAX = PCS_RESTRAINT_RANGE['max_inclusive']

PCS_ERROR_MIN = PCS_RESTRAINT_ERROR['min_exclusive']
PCS_ERROR_MAX = PCS_RESTRAINT_ERROR['max_exclusive']


# This class defines a complete listener for a parse tree produced by CyanaMRParser.
class CyanaMRParserListener(ParseTreeListener):

    __verbose = None
    __lfh = None
    __debug = False
    __remediate = False
    __omitDistLimitOutlier = True

    # atom name mapping of public MR file between the archive coordinates and submitted ones
    __mrAtomNameMapping = None

    # CCD accessing utility
    __ccU = None

    # BMRB chemical shift statistics
    __csStat = None

    # NEFTranslator
    __nefT = None

    # Pairwise align
    __pA = None

    # reasons for re-parsing request from the previous trial
    __reasons = None

    __upl_or_lol = None  # must be one of (None, 'upl_only', 'upl_w_lol', 'lol_only', 'lol_w_upl')

    __file_ext = None  # must be one of (None, 'upl', 'lol', 'aco', 'rdc', 'pcs', 'upv', 'lov', 'cco')

    # CIF reader
    __cR = None
    __hasCoord = False

    # data item name for model ID in 'atom_site' category
    __modelNumName = None

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    __authAsymId = None
    __authSeqId = None
    __authAtomId = None
    # __altAuthAtomId = None

    # coordinates information generated by ParserListenerUtil.checkCoordinates()
    __polySeq = None
    __altPolySeq = None
    __nonPoly = None
    __coordAtomSite = None
    __coordUnobsRes = None
    __labelToAuthSeq = None
    __authToLabelSeq = None

    __representativeModelId = REPRESENTATIVE_MODEL_ID
    __hasPolySeq = False
    __hasNonPoly = False
    __preferAuthSeq = True

    # chain number dictionary
    __chainNumberDict = None

    # polymer sequence of MR file
    __polySeqRst = None

    __seqAlign = None
    __chainAssign = None

    # current restraint subtype
    __cur_subtype = ''
    __cur_subtype_altered = False
    __cur_rdc_orientation = 0

    # column_order of distance restraints with chain
    __col_order_of_dist_w_chain = None

    # RDC parameter dictionary
    rdcParameterDict = None

    # PCS parameter dictionary
    pcsParameterDict = None

    # collection of atom selection
    atomSelectionSet = []

    # collection of number selection
    numberSelection = []

    # collection of auxiliary atom selection
    auxAtomSelectionSet = ''

    # current residue name for atom name mapping
    __cur_resname_for_mapping = ''

    # unambigous atom name mapping
    unambigAtomNameMapping = {}

    # ambigous atom name mapping
    ambigAtomNameMapping = {}

    # collection of general atom name extended with ambig code
    genAtomNameSelection = []

    warningMessage = ''

    reasonsForReParsing = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 mrAtomNameMapping=None,
                 cR=None, cC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None, upl_or_lol=None, file_ext=None):
        self.__verbose = verbose
        self.__lfh = log

        self.__representativeModelId = representativeModelId
        self.__mrAtomNameMapping = None if mrAtomNameMapping is None or len(mrAtomNameMapping) == 0 else mrAtomNameMapping

        self.__cR = cR
        self.__hasCoord = cR is not None

        if self.__hasCoord:
            ret = checkCoordinates(verbose, log, representativeModelId, cR, cC)
            self.__modelNumName = ret['model_num_name']
            self.__authAsymId = ret['auth_asym_id']
            self.__authSeqId = ret['auth_seq_id']
            self.__authAtomId = ret['auth_atom_id']
            # self.__altAuthAtomId = ret['alt_auth_atom_id']
            self.__polySeq = ret['polymer_sequence']
            self.__altPolySeq = ret['alt_polymer_sequence']
            self.__nonPoly = ret['non_polymer']
            self.__coordAtomSite = ret['coord_atom_site']
            self.__coordUnobsRes = ret['coord_unobs_res']
            self.__labelToAuthSeq = ret['label_to_auth_seq']
            self.__authToLabelSeq = ret['auth_to_label_seq']

        self.__hasPolySeq = self.__polySeq is not None and len(self.__polySeq) > 0
        self.__hasNonPoly = self.__nonPoly is not None and len(self.__nonPoly) > 0

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT

        # Pairwise align
        if self.__hasPolySeq:
            self.__pA = PairwiseAlign()
            self.__pA.setVerbose(verbose)

        # reasons for re-parsing request from the previous trial
        self.__reasons = reasons

        self.__upl_or_lol = upl_or_lol

        if upl_or_lol not in (None, 'upl_only', 'upl_w_lol', 'lol_only', 'lol_w_upl'):
            msg = f"The argument 'upl_or_lol' must be one of {(None, 'upl_only', 'upl_w_lol', 'lol_only', 'lol_w_upl')}"
            log.write(f"'+CyanaMRParserListener.__init__() ++ ValueError  -  {msg}\n")
            raise ValueError(f"'+CyanaMRParserListener.__init__() ++ ValueError  -  {msg}")

        self.__file_ext = file_ext

        if file_ext not in CYANA_MR_FILE_EXTS:
            msg = f"The argument 'file_ext' must be one of {CYANA_MR_FILE_EXTS}"
            log.write(f"'+CyanaMRParserListener.__init__() ++ ValueError  -  {msg}\n")
            raise ValueError(f"'+CyanaMRParserListener.__init__() ++ ValueError  -  {msg}")

        if upl_or_lol is None and file_ext is not None:

            if file_ext == 'upl':
                self.__upl_or_lol = 'upl_w_lol'

            if file_ext == 'lol':
                self.__upl_or_lol = 'lol_w_upl'

        self.__max_dist_value = None

        self.__dihed_lb_greater_than_ub = False
        self.__dihed_ub_always_positive = True

        self.distRestraints = 0      # CYANA: Distance restraint file (.upl or .lol)
        self.dihedRestraints = 0     # CYANA: Torsion angle restraint file (.aco)
        self.rdcRestraints = 0       # CYANA: Residual dipolar coupling restraint file (.rdc)
        self.pcsRestraints = 0       # CYANA: Pseudocontact shift restraint file (.pcs)
        self.noepkRestraints = 0     # CYANA: NOESY volume restraint file (.upv or .lov)
        self.jcoupRestraints = 0     # CYANA: Scalar coupling constant restraint file (.cco)
        self.geoRestraints = 0       # CYANA: Coordinate geometry restraints
        self.hbondRestraints = 0     # CYANA: Hydrogen bond geometry restraints

    def setDebugMode(self, debug):
        self.__debug = debug

    def setRemediateMode(self, remediate):
        self.__remediate = remediate

    # Enter a parse tree produced by CyanaMRParser#cyana_mr.
    def enterCyana_mr(self, ctx: CyanaMRParser.Cyana_mrContext):  # pylint: disable=unused-argument
        self.__chainNumberDict = {}
        self.__polySeqRst = []

    # Exit a parse tree produced by CyanaMRParser#cyana_mr.
    def exitCyana_mr(self, ctx: CyanaMRParser.Cyana_mrContext):  # pylint: disable=unused-argument
        if self.__hasPolySeq and self.__polySeqRst is not None:
            sortPolySeqRst(self.__polySeqRst)

            file_type = 'nm-res-cya'

            self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst,
                                                      resolvedMultimer=(self.__reasons is not None))
            self.__chainAssign, message = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__polySeq, self.__polySeqRst, self.__seqAlign)

            if len(message) > 0:
                self.warningMessage += message

            if self.__chainAssign is not None:

                if len(self.__polySeq) == len(self.__polySeqRst):

                    chain_mapping = {}

                    for chain_assign in self.__chainAssign:
                        ref_chain_id = chain_assign['ref_chain_id']
                        test_chain_id = chain_assign['test_chain_id']

                        if ref_chain_id != test_chain_id:
                            chain_mapping[test_chain_id] = ref_chain_id

                    if len(chain_mapping) == len(self.__polySeq):

                        for ps in self.__polySeqRst:
                            if ps['chain_id'] in chain_mapping:
                                ps['chain_id'] = chain_mapping[ps['chain_id']]

                        self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst,
                                                                  resolvedMultimer=(self.__reasons is not None))
                        self.__chainAssign, _ = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__polySeq, self.__polySeqRst, self.__seqAlign)

                trimSequenceAlignment(self.__seqAlign, self.__chainAssign)

                if 'Atom not found' in self.warningMessage and self.__reasons is None:

                    seqIdRemap = []

                    for chain_assign in self.__chainAssign:
                        ref_chain_id = chain_assign['ref_chain_id']
                        test_chain_id = chain_assign['test_chain_id']

                        seq_align = next(sa for sa in self.__seqAlign
                                         if sa['ref_chain_id'] == ref_chain_id
                                         and sa['test_chain_id'] == test_chain_id)

                        poly_seq_rst = next(ps for ps in self.__polySeqRst
                                            if ps['chain_id'] == test_chain_id)

                        seq_id_mapping = {}
                        for ref_seq_id, mid_code, test_seq_id in zip(seq_align['ref_seq_id'], seq_align['mid_code'], seq_align['test_seq_id']):
                            if mid_code == '|':
                                seq_id_mapping[test_seq_id] = ref_seq_id

                        if isCyclicPolymer(self.__cR, self.__polySeq, ref_chain_id, self.__representativeModelId, self.__modelNumName):

                            poly_seq_model = next(ps for ps in self.__polySeq
                                                  if ps['chain_id'] == ref_chain_id)

                            for seq_id, comp_id in zip(poly_seq_rst['seq_id'], poly_seq_rst['comp_id']):
                                if seq_id not in seq_id_mapping:
                                    _seq_id = next((_seq_id for _seq_id, _comp_id in zip(poly_seq_model['seq_id'], poly_seq_model['comp_id'])
                                                    if _seq_id not in seq_id_mapping.values() and _comp_id == comp_id), None)
                                    if _seq_id is not None:
                                        offset = seq_id - _seq_id
                                        break

                            for seq_id in poly_seq_rst['seq_id']:
                                if seq_id not in seq_id_mapping:
                                    seq_id_mapping[seq_id] = seq_id - offset

                        if any(k for k, v in seq_id_mapping.items() if k != v):
                            seqIdRemap.append({'chain_id': test_chain_id, 'seq_id_dict': seq_id_mapping})

                    if len(seqIdRemap) > 0:
                        if self.reasonsForReParsing is None:
                            self.reasonsForReParsing = {}
                        if 'seq_id_remap' not in self.reasonsForReParsing:
                            self.reasonsForReParsing['seq_id_remap'] = seqIdRemap

                    if any(ps for ps in self.__polySeq if 'identical_chain_id' in ps):
                        polySeqRst, chainIdMapping = splitPolySeqRstForMultimers(self.__pA, self.__polySeq, self.__polySeqRst, self.__chainAssign)

                        if polySeqRst is not None:
                            self.__polySeqRst = polySeqRst
                            if self.reasonsForReParsing is None:
                                self.reasonsForReParsing = {}
                            if 'chain_id_remap' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['chain_id_remap'] = chainIdMapping

            if 'Atom not found' in self.warningMessage:
                if len(self.unambigAtomNameMapping) > 0:
                    if self.reasonsForReParsing is None:
                        self.reasonsForReParsing = {}
                    if 'unambig_atom_id_remap' not in self.reasonsForReParsing:
                        self.reasonsForReParsing['unambig_atom_id_remap'] = self.unambigAtomNameMapping
                if len(self.ambigAtomNameMapping) > 0:
                    if self.reasonsForReParsing is None:
                        self.reasonsForReParsing = {}
                    if 'ambig_atom_id_remap' not in self.reasonsForReParsing:
                        self.reasonsForReParsing['ambig_atom_id_remap'] = self.ambigAtomNameMapping

        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]
            self.warningMessage = '\n'.join(set(self.warningMessage.split('\n')))

        if self.__remediate:
            if self.__dihed_lb_greater_than_ub and self.__dihed_ub_always_positive:
                if self.reasonsForReParsing is None:
                    self.reasonsForReParsing = {}
                if 'dihed_unusual_order' not in self.reasonsForReParsing:
                    self.reasonsForReParsing['dihed_unusual_order'] = True

    # Enter a parse tree produced by CyanaMRParser#distance_restraints.
    def enterDistance_restraints(self, ctx: CyanaMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist' if self.__file_ext is None or self.__file_ext != 'cco' else 'jcoup'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#distance_restraints.
    def exitDistance_restraints(self, ctx: CyanaMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: CyanaMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        if self.__cur_subtype == 'dist':
            self.distRestraints += 1
        elif self.__cur_subtype == 'jcoup':
            self.jcoupRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: CyanaMRParser.Distance_restraintContext):

        try:

            if None in self.genAtomNameSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                elif self.__cur_subtype == 'jcoup':
                    self.jcoupRestraints -= 1
                return

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = self.genAtomNameSelection[0]
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(1)).upper()
            atomId2 = self.genAtomNameSelection[1]

            if len(compId1) == 1 and len(compId2) == 1 and compId1.isalpha() and compId2.isalpha():
                atom_like = self.__csStat.getAtomLikeNameSet(True, True, 1)
                if atomId1 in atom_like and atomId2 in atom_like:
                    self.exitDistance_wo_comp_restraint(ctx)
                    return

            target_value = None
            lower_limit = None
            upper_limit = None

            if None in self.numberSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                elif self.__cur_subtype == 'jcoup':
                    self.jcoupRestraints -= 1
                return

            if self.__cur_subtype == 'dist':

                value = self.numberSelection[0]
                weight = 1.0

                delta = None
                has_square = False

                if len(self.numberSelection) > 2:
                    value2 = self.numberSelection[1]
                    weight = self.numberSelection[2]

                    has_square = True

                elif len(self.numberSelection) > 1:
                    value2 = self.numberSelection[1]

                    if value2 <= 1.0 or value2 < value:
                        delta = abs(value2)
                    else:
                        has_square = True

                if weight < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' must not be a negative value.\n"
                    return
                if weight == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' should be a positive value.\n"

                if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX and not self.__cur_subtype_altered:
                    if self.__max_dist_value is None:
                        self.__max_dist_value = value
                    if value > self.__max_dist_value:
                        self.__max_dist_value = value

                if has_square:
                    if value2 > DIST_RANGE_MAX:  # lol_only
                        lower_limit = value

                    elif 1.8 <= value <= DIST_ERROR_MAX and DIST_RANGE_MIN <= value2 <= DIST_RANGE_MAX:
                        upper_limit = value2
                        lower_limit = value
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                    else:  # upl_only
                        if value2 > 1.8:
                            upper_limit = value2
                            lower_limit = 1.8  # default value of PDBStat
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                        else:
                            upper_limit = value2

                elif delta is not None:
                    target_value = value
                    lower_limit = value - delta
                    upper_limit = value + delta

                elif self.__upl_or_lol is None or self.__upl_or_lol == 'upl_only':
                    if value > 1.8:
                        upper_limit = value
                        lower_limit = 1.8  # default value of PDBStat
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                    else:
                        lower_limit = value

                elif self.__upl_or_lol == 'upl_w_lol':
                    upper_limit = value

                elif self.__upl_or_lol == 'lol_only':
                    lower_limit = value
                    upper_limit = 5.5  # default value of PDBStat
                    target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                else:  # 'lol_w_upl'
                    lower_limit = value

                if not self.__hasPolySeq:  # can't decide whether NOE or RDC wo the coordinates
                    return

                chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                if len(self.atomSelectionSet[0]) == 1 and len(self.atomSelectionSet[1]) == 1:

                    isRdc = True

                    chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
                    seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
                    comp_id_1 = self.atomSelectionSet[0][0]['comp_id']
                    atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

                    chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
                    seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
                    comp_id_2 = self.atomSelectionSet[1][0]['comp_id']
                    atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

                    if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                        isRdc = False

                    if chain_id_1 != chain_id_2:
                        isRdc = False

                    if abs(seq_id_1 - seq_id_2) > 1:
                        isRdc = False

                    if abs(seq_id_1 - seq_id_2) == 1:

                        if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                                ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                                 or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                            pass

                        else:
                            isRdc = False

                    elif atom_id_1 == atom_id_2:
                        isRdc = False

                    elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                        if not any(b for b in self.__ccU.lastBonds
                                   if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                                       or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                            if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                                isRdc = False

                    if not isRdc:
                        self.__cur_subtype_altered = False

                    else:

                        isRdc = False

                        if self.__cur_subtype_altered and atom_id_1 + atom_id_2 == self.auxAtomSelectionSet:
                            isRdc = True

                        elif value < 1.0 or value > 6.0:
                            self.auxAtomSelectionSet = atom_id_1 + atom_id_2
                            self.__cur_subtype_altered = True
                            self.__cur_rdc_orientation += 1
                            isRdc = True

                        if isRdc:
                            self.__cur_subtype = 'rdc'
                            self.rdcRestraints += 1
                            self.distRestraints -= 1

                            target_value = value
                            lower_limit = upper_limit = None

                            if len(self.numberSelection) > 2:
                                error = abs(self.numberSelection[1])
                                lower_limit = target_value - error
                                upper_limit = target_value + error

                            dstFunc = self.validateRdcRange(weight, self.__cur_rdc_orientation, target_value, lower_limit, upper_limit)

                            if dstFunc is None:
                                return

                            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                                  self.atomSelectionSet[1]):
                                if isLongRangeRestraint([atom1, atom2]):
                                    continue
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                                          f"atom1={atom1} atom2={atom2} {dstFunc}")

                            self.__cur_subtype = 'dist'

                            return

                dstFunc = self.validateDistanceRange(weight, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

                if dstFunc is None:
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

            else:  # cco

                target = self.numberSelection[0]
                error = None

                weight = 1.0
                if len(self.numberSelection) > 2:
                    error = abs(self.numberSelection[1])
                    weight = self.numberSelection[2]

                elif len(self.numberSelection) > 1:
                    error = abs(self.numberSelection[1])

                if weight < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' must not be a negative value.\n"
                    return
                if weight == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' should be a positive value.\n"

                target_value = target
                lower_limit = target - error if error is not None else None
                upper_limit = target + error if error is not None else None

                dstFunc = self.validateRdcRange(weight, None, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                if not self.__hasPolySeq:
                    return

                chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                if not self.areUniqueCoordAtoms('a Scalar coupling'):
                    return

                chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
                seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
                comp_id_1 = self.atomSelectionSet[0][0]['comp_id']
                atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

                chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
                seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
                comp_id_2 = self.atomSelectionSet[1][0]['comp_id']
                atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

                if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Non-magnetic susceptible spin appears in scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                if chain_id_1 != chain_id_2:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Found inter-chain scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                if abs(seq_id_1 - seq_id_2) > 1:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Found inter-residue scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                if abs(seq_id_1 - seq_id_2) == 1:

                    if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                            ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                             or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                        pass

                    else:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            "Found inter-residue scalar coupling constant; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

                elif atom_id_1 == atom_id_2:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found zero scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if isLongRangeRestraint([atom1, atom2]):
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.jcoupRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

        except ValueError:
            if self.__cur_subtype == 'dist':
                self.distRestraints -= 1
            elif self.__cur_subtype == 'jcoup':
                self.jcoupRestraints -= 1
        finally:
            self.numberSelection.clear()
            self.genAtomNameSelection.clear()

    # Exit a parse tree produced by CyanaMRParser#distance_restraint.
    def exitDistance_wo_comp_restraint(self, ctx: CyanaMRParser.Distance_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            chainId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(1)))
            chainId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()

            target_value = None
            lower_limit = None
            upper_limit = None

            if None in self.numberSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                elif self.__cur_subtype == 'jcoup':
                    self.jcoupRestraints -= 1
                return

            if self.__cur_subtype == 'dist':

                value = self.numberSelection[0]
                weight = 1.0

                delta = None
                has_square = False

                if len(self.numberSelection) > 2:
                    value2 = self.numberSelection[1]
                    weight = self.numberSelection[2]

                    has_square = True

                elif len(self.numberSelection) > 1:
                    value2 = self.numberSelection[1]

                    if value2 <= 1.0 or value2 < value:
                        delta = abs(value2)
                    else:
                        has_square = True

                if weight < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' must not be a negative value.\n"
                    return
                if weight == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' should be a positive value.\n"

                if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX and not self.__cur_subtype_altered:
                    if self.__max_dist_value is None:
                        self.__max_dist_value = value
                    if value > self.__max_dist_value:
                        self.__max_dist_value = value

                if has_square:
                    if value2 > DIST_RANGE_MAX:  # lol_only
                        lower_limit = value

                    elif 1.8 <= value <= DIST_ERROR_MAX and DIST_RANGE_MIN <= value2 <= DIST_RANGE_MAX:
                        upper_limit = value2
                        lower_limit = value
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                    else:  # upl_only
                        if value2 > 1.8:
                            upper_limit = value2
                            lower_limit = 1.8  # default value of PDBStat
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                        else:
                            upper_limit = value2

                elif delta is not None:
                    target_value = value
                    lower_limit = value - delta
                    upper_limit = value + delta

                elif self.__upl_or_lol is None or self.__upl_or_lol == 'upl_only':
                    if value > 1.8:
                        upper_limit = value
                        lower_limit = 1.8  # default value of PDBStat
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                    else:
                        lower_limit = value

                elif self.__upl_or_lol == 'upl_w_lol':
                    upper_limit = value

                elif self.__upl_or_lol == 'lol_only':
                    lower_limit = value
                    upper_limit = 5.5  # default value of PDBStat
                    target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                else:  # 'lol_w_upl'
                    lower_limit = value

                if not self.__hasPolySeq:  # can't decide whether NOE or RDC wo the coordinates
                    return

                chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(chainId1, seqId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(chainId2, seqId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, None, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, None, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                if len(self.atomSelectionSet[0]) == 1 and len(self.atomSelectionSet[1]) == 1:

                    isRdc = True

                    chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
                    seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
                    comp_id_1 = self.atomSelectionSet[0][0]['comp_id']
                    atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

                    chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
                    seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
                    comp_id_2 = self.atomSelectionSet[1][0]['comp_id']
                    atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

                    if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                        isRdc = False

                    if chain_id_1 != chain_id_2:
                        isRdc = False

                    if abs(seq_id_1 - seq_id_2) > 1:
                        isRdc = False

                    if abs(seq_id_1 - seq_id_2) == 1:

                        if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                                ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                                 or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                            pass

                        else:
                            isRdc = False

                    elif atom_id_1 == atom_id_2:
                        isRdc = False

                    elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                        if not any(b for b in self.__ccU.lastBonds
                                   if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                                       or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                            if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                                isRdc = False

                    if not isRdc:
                        self.__cur_subtype_altered = False

                    else:

                        isRdc = False

                        if self.__cur_subtype_altered and atom_id_1 + atom_id_2 == self.auxAtomSelectionSet:
                            isRdc = True

                        elif value < 1.0 or value > 6.0:
                            self.auxAtomSelectionSet = atom_id_1 + atom_id_2
                            self.__cur_subtype_altered = True
                            self.__cur_rdc_orientation += 1
                            isRdc = True

                        if isRdc:
                            self.__cur_subtype = 'rdc'
                            self.rdcRestraints += 1
                            self.distRestraints -= 1

                            target_value = value
                            lower_limit = upper_limit = None

                            if len(self.numberSelection) > 2:
                                error = abs(self.numberSelection[1])
                                lower_limit = target_value - error
                                upper_limit = target_value + error

                            dstFunc = self.validateRdcRange(weight, self.__cur_rdc_orientation, target_value, lower_limit, upper_limit)

                            if dstFunc is None:
                                return

                            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                                  self.atomSelectionSet[1]):
                                if isLongRangeRestraint([atom1, atom2]):
                                    continue
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                                          f"atom1={atom1} atom2={atom2} {dstFunc}")

                            self.__cur_subtype = 'dist'

                            return

                dstFunc = self.validateDistanceRange(weight, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

                if dstFunc is None:
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

            else:  # cco

                target = self.numberSelection[0]
                error = None

                weight = 1.0
                if len(self.numberSelection) > 2:
                    error = abs(self.numberSelection[1])
                    weight = self.numberSelection[2]

                elif len(self.numberSelection) > 1:
                    error = abs(self.numberSelection[1])

                if weight < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' must not be a negative value.\n"
                    return
                if weight == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' should be a positive value.\n"

                target_value = target
                lower_limit = target - error if error is not None else None
                upper_limit = target + error if error is not None else None

                dstFunc = self.validateRdcRange(weight, None, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                if not self.__hasPolySeq:
                    return

                chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(chainId1, seqId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(chainId2, seqId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, None, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, None, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                if not self.areUniqueCoordAtoms('a Scalar coupling'):
                    return

                chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
                seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
                comp_id_1 = self.atomSelectionSet[0][0]['comp_id']
                atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

                chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
                seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
                comp_id_2 = self.atomSelectionSet[1][0]['comp_id']
                atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

                if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Non-magnetic susceptible spin appears in scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                if chain_id_1 != chain_id_2:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Found inter-chain scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                if abs(seq_id_1 - seq_id_2) > 1:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Found inter-residue scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                if abs(seq_id_1 - seq_id_2) == 1:

                    if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                            ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                             or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                        pass

                    else:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            "Found inter-residue scalar coupling constant; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

                elif atom_id_1 == atom_id_2:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found zero scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if isLongRangeRestraint([atom1, atom2]):
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.jcoupRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

        except ValueError:
            if self.__cur_subtype == 'dist':
                self.distRestraints -= 1
            elif self.__cur_subtype == 'jcoup':
                self.jcoupRestraints -= 1
        finally:
            self.numberSelection.clear()

    def validateDistanceRange(self, weight, target_value, lower_limit, upper_limit, omit_dist_limit_outlier):
        """ Validate distance value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if DIST_ERROR_MIN < target_value < DIST_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                if target_value <= DIST_ERROR_MIN and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The target value='{target_value:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    target_value = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The target value='{target_value:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if DIST_ERROR_MIN <= lower_limit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                if lower_limit <= DIST_ERROR_MIN and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    lower_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if DIST_ERROR_MIN < upper_limit <= DIST_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                if upper_limit > DIST_ERROR_MAX and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    upper_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the target value '{target_value:.3f}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.3f}' must be greater than the target value '{target_value:.3f}'.\n"

        else:

            if lower_limit is not None and upper_limit is not None:
                if lower_limit > upper_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the upper limit value '{upper_limit:.3f}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if DIST_RANGE_MIN <= target_value <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if DIST_RANGE_MIN <= lower_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if DIST_RANGE_MIN <= upper_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        return dstFunc

    def validatePeakVolumeRange(self, weight, target_value, lower_limit, upper_limit):
        """ Validate NOESY peak volume value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            dstFunc['target_value'] = f"{target_value}"

        if lower_limit is not None:
            dstFunc['lower_limit'] = f"{lower_limit}"

        if upper_limit is not None:
            dstFunc['upper_limit'] = f"{upper_limit}"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit}' must be greater than the target value '{target_value}'.\n"

        if not validRange:
            return None

        return dstFunc

    def getRealChainSeqId(self, ps, seqId, compId=None, isPolySeq=True):
        if compId is not None:
            compId = translateToStdResName(compId)
        if self.__reasons is not None and 'label_seq_scheme' in self.__reasons and self.__reasons['label_seq_scheme']:
            seqKey = (ps['chain_id' if isPolySeq else 'auth_chain_id'], seqId)
            if seqKey in self.__labelToAuthSeq:
                _chainId, _seqId = self.__labelToAuthSeq[seqKey]
                if _seqId in ps['auth_seq_id']:
                    return _chainId, _seqId
        if seqId in ps['auth_seq_id']:
            if compId is None:
                return ps['auth_chain_id'], seqId
            idx = ps['auth_seq_id'].index(seqId)
            if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                return ps['auth_chain_id'], seqId
        if seqId in ps['seq_id']:
            idx = ps['seq_id'].index(seqId)
            if compId is None:
                return ps['auth_chain_id'], ps['auth_seq_id'][idx]
            if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                return ps['auth_chain_id'], ps['auth_seq_id'][idx]
        return ps['chain_id' if isPolySeq else 'auth_chain_id'], seqId

    def assignCoordPolymerSequence(self, seqId, compId, atomId):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = []
        _seqId = seqId

        fixedChainId = None
        fixedSeqId = None

        if self.__mrAtomNameMapping is not None and compId not in monDict3:
            seqId, compId, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, compId, atomId)

        if self.__reasons is not None:
            if 'ambig_atom_id_remap' in self.__reasons and compId in self.__reasons['ambig_atom_id_remap']\
               and atomId in self.__reasons['ambig_atom_id_remap'][compId]:
                return self.atomIdListToChainAssign(self.__reasons['ambig_atom_id_remap'][compId][atomId])
            if 'unambig_atom_id_remap' in self.__reasons and compId in self.__reasons['unambig_atom_id_remap']\
               and atomId in self.__reasons['unambig_atom_id_remap'][compId]:
                atomId = self.__reasons['unambig_atom_id_remap'][compId][atomId][0]  # select representative one
            if 'chain_id_remap' in self.__reasons and seqId in self.__reasons['chain_id_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.__reasons['chain_id_remap'], seqId)
            elif 'seq_id_remap' in self.__reasons:
                fixedChainId, fixedSeqId = retrieveRemappedSeqId(self.__reasons['seq_id_remap'], None, seqId)
            if fixedSeqId is not None:
                _seqId = fixedSeqId

        if len(self.ambigAtomNameMapping) > 0:
            if compId in self.ambigAtomNameMapping\
               and atomId in self.ambigAtomNameMapping[compId]:
                return self.atomIdListToChainAssign(self.ambigAtomNameMapping[compId][atomId])
        if len(self.unambigAtomNameMapping) > 0:
            if compId in self.unambigAtomNameMapping\
               and atomId in self.unambigAtomNameMapping[compId]:
                atomId = self.unambigAtomNameMapping[compId][atomId][0]  # select representative one

        updatePolySeqRst(self.__polySeqRst, self.__polySeq[0]['chain_id'] if fixedChainId is None else fixedChainId, _seqId, translateToStdResName(compId))

        for ps in self.__polySeq:
            chainId, seqId = self.getRealChainSeqId(ps, _seqId, compId)
            if self.__reasons is not None:
                if fixedChainId is not None:
                    if fixedChainId != chainId:
                        continue
                    seqId = fixedSeqId
                elif fixedSeqId is not None:
                    seqId = fixedSeqId
            if seqId in ps['auth_seq_id']:
                idx = ps['auth_seq_id'].index(seqId)
                cifCompId = ps['comp_id'][idx]
                origCompId = ps['auth_comp_id'][idx]
                if compId in (cifCompId, origCompId):
                    if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.append((chainId, seqId, cifCompId))
                elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.append((chainId, seqId, cifCompId))
                    """ defer to sequence alignment error
                    if cifCompId != translateToStdResName(compId):
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                    """

        if self.__hasNonPoly:
            for np in self.__nonPoly:
                chainId, seqId = self.getRealChainSeqId(np, _seqId, compId, False)
                if self.__reasons is not None:
                    if fixedChainId is not None:
                        if fixedChainId != chainId:
                            continue
                        seqId = fixedSeqId
                    elif fixedSeqId is not None:
                        seqId = fixedSeqId
                if seqId in np['auth_seq_id']:
                    idx = np['auth_seq_id'].index(seqId)
                    cifCompId = np['comp_id'][idx]
                    origCompId = np['auth_comp_id'][idx]
                    if compId in (cifCompId, origCompId):
                        if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((chainId, seqId, cifCompId))
                    elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.append((chainId, seqId, cifCompId))

        if len(chainAssign) == 0:
            for ps in self.__polySeq:
                chainId = ps['chain_id']
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        origCompId = ps['auth_comp_id'][ps['seq_id'].index(seqId)]
                        if compId in (cifCompId, origCompId):
                            if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                                if self.reasonsForReParsing is None:
                                    self.reasonsForReParsing = {}
                                if 'label_seq_scheme' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['label_seq_scheme'] = True
                        elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                            """ defer to sequence alignment error
                            if cifCompId != translateToStdResName(compId):
                                self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                                    f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                            """

            if self.__hasNonPoly:
                for np in self.__nonPoly:
                    chainId = np['auth_chain_id']
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            cifCompId = np['comp_id'][np['seq_id'].index(seqId)]
                            origCompId = np['auth_comp_id'][np['seq_id'].index(seqId)]
                            if compId in (cifCompId, origCompId):
                                if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                    chainAssign.append((np['auth_chain_id'], _seqId, cifCompId))
                                    if self.reasonsForReParsing is None:
                                        self.reasonsForReParsing = {}
                                    if 'label_seq_scheme' not in self.reasonsForReParsing:
                                        self.reasonsForReParsing['label_seq_scheme'] = True
                            elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((np['auth_chain_id'], _seqId, cifCompId))

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    chainAssign.append((chainId, _seqId, cifCompId))
                    """ defer to sequence alignment error
                    if cifCompId != translateToStdResName(compId):
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                    """

        if len(chainAssign) == 0:
            if seqId == 1 and atomId in ('H', 'HN'):
                return self.assignCoordPolymerSequence(seqId, compId, 'H1')
            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                f"{_seqId}:{compId}:{atomId} is not present in the coordinates.\n"

        return chainAssign

    def assignCoordPolymerSequenceWithChainId(self, refChainId, seqId, compId, atomId):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = []
        _seqId = seqId

        fixedChainId = None
        fixedSeqId = None

        if self.__mrAtomNameMapping is not None and compId not in monDict3:
            seqId, compId, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, compId, atomId)

        if self.__reasons is not None:
            if 'ambig_atom_id_remap' in self.__reasons and compId in self.__reasons['ambig_atom_id_remap']\
               and atomId in self.__reasons['ambig_atom_id_remap'][compId]:
                return self.atomIdListToChainAssign(self.__reasons['ambig_atom_id_remap'][compId][atomId])
            if 'unambig_atom_id_remap' in self.__reasons and compId in self.__reasons['unambig_atom_id_remap']\
               and atomId in self.__reasons['unambig_atom_id_remap'][compId]:
                atomId = self.__reasons['unambig_atom_id_remap'][compId][atomId][0]  # select representative one
            if 'chain_id_remap' in self.__reasons and seqId in self.__reasons['chain_id_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.__reasons['chain_id_remap'], seqId)
                refChainId = fixedChainId
            elif 'seq_id_remap' in self.__reasons:
                _, fixedSeqId = retrieveRemappedSeqId(self.__reasons['seq_id_remap'], str(refChainId), seqId)
            if fixedSeqId is not None:
                _seqId = fixedSeqId

        if len(self.ambigAtomNameMapping) > 0:
            if compId in self.ambigAtomNameMapping and atomId in self.ambigAtomNameMapping[compId]:
                return self.atomIdListToChainAssign(self.ambigAtomNameMapping[compId][atomId])
        if len(self.unambigAtomNameMapping) > 0:
            if compId in self.unambigAtomNameMapping and atomId in self.unambigAtomNameMapping[compId]:
                atomId = self.unambigAtomNameMapping[compId][atomId][0]  # select representative one

        updatePolySeqRst(self.__polySeqRst, str(refChainId), _seqId, translateToStdResName(compId))

        for ps in self.__polySeq:
            chainId, seqId = self.getRealChainSeqId(ps, _seqId, compId)
            if fixedChainId is None and refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                if chainId != self.__chainNumberDict[refChainId]:
                    continue
            if self.__reasons is not None:
                if fixedChainId is not None:
                    if fixedChainId != chainId:
                        continue
                    seqId = fixedSeqId
                elif fixedSeqId is not None:
                    seqId = fixedSeqId
            if seqId in ps['auth_seq_id']:
                idx = ps['auth_seq_id'].index(seqId)
                cifCompId = ps['comp_id'][idx]
                origCompId = ps['auth_comp_id'][idx]
                if compId in (cifCompId, origCompId):
                    if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.append((chainId, seqId, cifCompId))
                        if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                            self.__chainNumberDict[refChainId] = chainId
                elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.append((chainId, seqId, cifCompId))
                    if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                        self.__chainNumberDict[refChainId] = chainId
                    """ defer to sequence alignment error
                    if cifCompId != translateToStdResName(compId):
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                    """

        if self.__hasNonPoly:
            for np in self.__nonPoly:
                chainId, seqId = self.getRealChainSeqId(np, _seqId, compId, False)
                if fixedChainId is None and refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                    if chainId != self.__chainNumberDict[refChainId]:
                        continue
                if self.__reasons is not None:
                    if fixedChainId is not None:
                        if fixedChainId != chainId:
                            continue
                        seqId = fixedSeqId
                    elif fixedSeqId is not None:
                        seqId = fixedSeqId
                if seqId in np['auth_seq_id']:
                    idx = np['auth_seq_id'].index(seqId)
                    cifCompId = np['comp_id'][idx]
                    origCompId = np['auth_comp_id'][idx]
                    if compId in (cifCompId, origCompId):
                        if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((chainId, seqId, cifCompId))
                            if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                                self.__chainNumberDict[refChainId] = chainId
                    elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.append((chainId, seqId, cifCompId))
                        if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                            self.__chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0:
            for ps in self.__polySeq:
                chainId = ps['chain_id']
                if refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                    if chainId != self.__chainNumberDict[refChainId]:
                        continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        origCompId = ps['auth_comp_id'][ps['seq_id'].index(seqId)]
                        if compId in (cifCompId, origCompId):
                            if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                                if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                                    self.__chainNumberDict[refChainId] = chainId
                                if self.reasonsForReParsing is None:
                                    self.reasonsForReParsing = {}
                                if 'label_seq_scheme' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['label_seq_scheme'] = True
                        elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                            if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                                self.__chainNumberDict[refChainId] = chainId
                            """ defer to sequence alignment error
                            if cifCompId != translateToStdResName(compId):
                                self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                                    f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                            """

            if self.__hasNonPoly:
                for np in self.__nonPoly:
                    chainId = np['auth_chain_id']
                    if refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                        if chainId != self.__chainNumberDict[refChainId]:
                            continue
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            cifCompId = np['comp_id'][np['seq_id'].index(seqId)]
                            origCompId = np['auth_comp_id'][np['seq_id'].index(seqId)]
                            if compId in (cifCompId, origCompId):
                                if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                    chainAssign.append((np['auth_chain_id'], _seqId, cifCompId))
                                    if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                                        self.__chainNumberDict[refChainId] = chainId
                                    if self.reasonsForReParsing is None:
                                        self.reasonsForReParsing = {}
                                    if 'label_seq_scheme' not in self.reasonsForReParsing:
                                        self.reasonsForReParsing['label_seq_scheme'] = True
                            elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((np['auth_chain_id'], _seqId, cifCompId))
                                if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                                    self.__chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if fixedChainId is None and refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                    if chainId != self.__chainNumberDict[refChainId]:
                        continue
                if self.__reasons is not None:
                    if fixedChainId is not None:
                        if fixedChainId != chainId:
                            continue
                        _seqId = fixedSeqId
                    elif fixedSeqId is not None:
                        _seqId = fixedSeqId
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    chainAssign.append((chainId, _seqId, cifCompId))
                    if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                        self.__chainNumberDict[refChainId] = chainId
                    """ defer to sequence alignment error
                    if cifCompId != translateToStdResName(compId):
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                    """

        if len(chainAssign) == 0:
            if seqId == 1 and atomId in ('H', 'HN'):
                return self.assignCoordPolymerSequenceWithChainId(refChainId, seqId, compId, 'H1')
            if compId == 'AMB' and (('-' in atomId and ':' in atomId) or '.' in atomId):
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                    f"{_seqId}:{compId}:{atomId} is not present in the coordinates. "\
                    "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the CYANA restraint file.\n"
            else:
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                    f"{_seqId}:{compId}:{atomId} is not present in the coordinates.\n"

        return chainAssign

    def assignCoordPolymerSequenceWithoutCompId(self, seqId, atomId=None):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = []
        _seqId = seqId

        fixedChainId = None
        fixedSeqId = None

        for ps in self.__polySeq:
            chainId, seqId = self.getRealChainSeqId(ps, _seqId, None)
            if self.__reasons is not None:
                if 'chain_id_remap' in self.__reasons and seqId in self.__reasons['chain_id_remap']:
                    fixedChainId, fixedSeqId = retrieveRemappedChainId(self.__reasons['chain_id_remap'], seqId)
                    if fixedChainId != chainId:
                        continue
                elif 'seq_id_remap' in self.__reasons:
                    _, fixedSeqId = retrieveRemappedSeqId(self.__reasons['seq_id_remap'], chainId, seqId)
                if fixedSeqId is not None:
                    seqId = _seqId = fixedSeqId
            if seqId in ps['auth_seq_id']:
                idx = ps['auth_seq_id'].index(seqId)
                cifCompId = ps['comp_id'][idx]
                updatePolySeqRst(self.__polySeqRst, chainId, _seqId, cifCompId)
                if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.append((chainId, seqId, cifCompId))

        if self.__hasNonPoly:
            for np in self.__nonPoly:
                chainId, seqId = self.getRealChainSeqId(np, _seqId, None, False)
                if self.__reasons is not None:
                    if 'chain_id_remap' in self.__reasons and seqId in self.__reasons['chain_id_remap']:
                        fixedChainId, fixedSeqId = retrieveRemappedChainId(self.__reasons['chain_id_remap'], seqId)
                        if fixedChainId != chainId:
                            continue
                    elif 'seq_id_remap' in self.__reasons:
                        _, fixedSeqId = retrieveRemappedSeqId(self.__reasons['seq_id_remap'], chainId, seqId)
                    if fixedSeqId is not None:
                        seqId = _seqId = fixedSeqId
                if seqId in np['auth_seq_id']:
                    idx = np['auth_seq_id'].index(seqId)
                    cifCompId = np['comp_id'][idx]
                    updatePolySeqRst(self.__polySeqRst, chainId, _seqId, cifCompId)
                    if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.append((chainId, seqId, cifCompId))

        if len(chainAssign) == 0:
            for ps in self.__polySeq:
                chainId = ps['chain_id']
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        updatePolySeqRst(self.__polySeqRst, chainId, _seqId, cifCompId)
                        if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                            if self.reasonsForReParsing is None:
                                self.reasonsForReParsing = {}
                            if 'label_seq_scheme' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['label_seq_scheme'] = True

            if self.__hasNonPoly:
                for np in self.__nonPoly:
                    chainId = np['auth_chain_id']
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            cifCompId = np['comp_id'][np['seq_id'].index(seqId)]
                            updatePolySeqRst(self.__polySeqRst, chainId, _seqId, cifCompId)
                            if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((np['auth_chain_id'], _seqId, cifCompId))
                                if self.reasonsForReParsing is None:
                                    self.reasonsForReParsing = {}
                                if 'label_seq_scheme' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['label_seq_scheme'] = True

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    updatePolySeqRst(self.__polySeqRst, chainId, _seqId, cifCompId)
                    chainAssign.append((chainId, _seqId, cifCompId))

        if len(chainAssign) == 0:
            if seqId == 1 and atomId is not None and atomId in ('H', 'HN'):
                return self.assignCoordPolymerSequenceWithoutCompId(seqId, 'H1')
            if (('-' in atomId and ':' in atomId) or '.' in atomId):
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                    f"{_seqId}:{atomId} is not present in the coordinates. "\
                    "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the CYANA restraint file.\n"
            else:
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                    f"{_seqId}:{atomId} is not present in the coordinates.\n"

        return chainAssign

    def assignCoordPolymerSequenceWithChainIdWithoutCompId(self, fixedChainId, seqId, atomId):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = []
        _seqId = seqId

        fixedSeqId = None

        for ps in self.__polySeq:
            chainId, seqId = self.getRealChainSeqId(ps, _seqId, None)
            if chainId != fixedChainId:
                continue
            if self.__reasons is not None:
                if 'chain_id_remap' in self.__reasons and seqId in self.__reasons['chain_id_remap']:
                    fixedChainId, fixedSeqId = retrieveRemappedChainId(self.__reasons['chain_id_remap'], seqId)
                    if fixedChainId != chainId:
                        continue
                elif 'seq_id_remap' in self.__reasons:
                    _, fixedSeqId = retrieveRemappedSeqId(self.__reasons['seq_id_remap'], chainId, seqId)
                if fixedSeqId is not None:
                    seqId = _seqId = fixedSeqId
            if seqId in ps['auth_seq_id']:
                idx = ps['auth_seq_id'].index(seqId)
                cifCompId = ps['comp_id'][idx]
                updatePolySeqRst(self.__polySeqRst, fixedChainId, _seqId, cifCompId)
                if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.append((chainId, seqId, cifCompId))

        if self.__hasNonPoly:
            for np in self.__nonPoly:
                chainId, seqId = self.getRealChainSeqId(np, _seqId, None, False)
                if chainId != fixedChainId:
                    continue
                if self.__reasons is not None:
                    if 'chain_id_remap' in self.__reasons and seqId in self.__reasons['chain_id_remap']:
                        fixedChainId, fixedSeqId = retrieveRemappedChainId(self.__reasons['chain_id_remap'], seqId)
                        if fixedChainId != chainId:
                            continue
                    elif 'seq_id_remap' in self.__reasons:
                        _, fixedSeqId = retrieveRemappedSeqId(self.__reasons['seq_id_remap'], chainId, seqId)
                    if fixedSeqId is not None:
                        seqId = _seqId = fixedSeqId
                if seqId in np['auth_seq_id']:
                    idx = np['auth_seq_id'].index(seqId)
                    cifCompId = np['comp_id'][idx]
                    updatePolySeqRst(self.__polySeqRst, fixedChainId, _seqId, cifCompId)
                    if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.append((chainId, seqId, cifCompId))

        if len(chainAssign) == 0:
            for ps in self.__polySeq:
                chainId = ps['chain_id']
                if chainId != fixedChainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        updatePolySeqRst(self.__polySeqRst, fixedChainId, _seqId, cifCompId)
                        if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                            if self.reasonsForReParsing is None:
                                self.reasonsForReParsing = {}
                            if 'label_seq_scheme' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['label_seq_scheme'] = True

            if self.__hasNonPoly:
                for np in self.__nonPoly:
                    chainId = np['auth_chain_id']
                    if chainId != fixedChainId:
                        continue
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            cifCompId = np['comp_id'][np['seq_id'].index(seqId)]
                            updatePolySeqRst(self.__polySeqRst, fixedChainId, _seqId, cifCompId)
                            if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((np['auth_chain_id'], _seqId, cifCompId))
                                if self.reasonsForReParsing is None:
                                    self.reasonsForReParsing = {}
                                if 'label_seq_scheme' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['label_seq_scheme'] = True

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if chainId != fixedChainId:
                    continue
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    updatePolySeqRst(self.__polySeqRst, fixedChainId, _seqId, cifCompId)
                    chainAssign.append((chainId, _seqId, cifCompId))

        if len(chainAssign) == 0:
            if seqId == 1 and atomId in ('H', 'HN'):
                return self.assignCoordPolymerSequenceWithChainIdWithoutCompId(fixedChainId, seqId, 'H1')
            if (('-' in atomId and ':' in atomId) or '.' in atomId):
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                    f"{fixedChainId}:{_seqId}:{atomId} is not present in the coordinates. "\
                    "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the CYANA restraint file.\n"
            else:
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                    f"{fixedChainId}:{_seqId}:{atomId} is not present in the coordinates.\n"

        return chainAssign

    def selectCoordAtoms(self, chainAssign, seqId, compId, atomId, allowAmbig=True, enableWarning=True):
        """ Select atoms of the coordinates.
        """

        atomSelection = []

        if compId is not None:
            if self.__reasons is not None:
                if 'ambig_atom_id_remap' in self.__reasons and compId in self.__reasons['ambig_atom_id_remap']\
                   and atomId in self.__reasons['ambig_atom_id_remap'][compId]:
                    atomSelection = self.atomIdListToAtomSelection(self.__reasons['ambig_atom_id_remap'][compId][atomId])
                    for atom in atomSelection:
                        chainId = atom['chain_id']
                        cifSeqId = atom['seq_id']
                        cifCompId = atom['comp_id']
                        cifAtomId = atom['atom_id']
                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)
                        self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, enableWarning)
                    if len(atomSelection) > 0:
                        self.atomSelectionSet.append(atomSelection)
                    return
                if 'unambig_atom_id_remap' in self.__reasons and compId in self.__reasons['unambig_atom_id_remap']\
                   and atomId in self.__reasons['unambig_atom_id_remap'][compId]:
                    atomIds = self.__reasons['unambig_atom_id_remap'][compId][atomId]
                    for chainId, cifSeqId, cifCompId in chainAssign:
                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)
                        for cifAtomId in atomIds:
                            self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, enableWarning)
                        atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})
                    if len(atomSelection) > 0:
                        self.atomSelectionSet.append(atomSelection)
                    return

            if len(self.ambigAtomNameMapping) > 0:
                if compId in self.ambigAtomNameMapping and atomId in self.ambigAtomNameMapping[compId]:
                    atomSelection = self.atomIdListToAtomSelection(self.ambigAtomNameMapping[compId][atomId])
                    for atom in atomSelection:
                        chainId = atom['chain_id']
                        cifSeqId = atom['seq_id']
                        cifCompId = atom['comp_id']
                        cifAtomId = atom['atom_id']
                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)
                        self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, enableWarning)
                    if len(atomSelection) > 0:
                        self.atomSelectionSet.append(atomSelection)
                    return
            if len(self.unambigAtomNameMapping) > 0:
                if compId in self.unambigAtomNameMapping and atomId in self.unambigAtomNameMapping[compId]:
                    atomIds = self.unambigAtomNameMapping[compId][atomId]
                    for chainId, cifSeqId, cifCompId in chainAssign:
                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)
                        for cifAtomId in atomIds:
                            self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, enableWarning)
                        atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})
                    if len(atomSelection) > 0:
                        self.atomSelectionSet.append(atomSelection)
                    return

            if self.__mrAtomNameMapping is not None and compId not in monDict3:
                seqId, compId, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, compId, atomId)

        for chainId, cifSeqId, cifCompId in chainAssign:
            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)

            _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomId, leave_unmatched=True)
            if details is not None and len(atomId) > 1:
                _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomId[:-1], leave_unmatched=True)

            if details is not None:
                _atomId_ = translateToStdAtomName(atomId, cifCompId, ccU=self.__ccU)
                if _atomId_ != atomId:
                    _atomId = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, _atomId_)[0]
            # _atomId = self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]
            lenAtomId = len(_atomId)
            if lenAtomId == 0:
                if enableWarning:
                    self.warningMessage += f"[Invalid atom nomenclature] {self.__getCurrentRestraint()}"\
                        f"{seqId}:{compId}:{atomId} is invalid atom nomenclature.\n"
                continue
            if lenAtomId > 1 and not allowAmbig:
                if enableWarning:
                    self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint()}"\
                        f"Ambiguous atom selection '{seqId}:{compId}:{atomId}' is not allowed as a angle restraint.\n"
                continue

            for cifAtomId in _atomId:
                atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})

                self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, enableWarning)

        if len(atomSelection) > 0:
            self.atomSelectionSet.append(atomSelection)

    def testCoordAtomIdConsistency(self, chainId, seqId, compId, atomId, seqKey, coordAtomSite, enableWarning=True):
        if not self.__hasCoord:
            return

        found = False

        if coordAtomSite is not None:
            if atomId in coordAtomSite['atom_id']:
                found = True
            elif 'alt_atom_id' in coordAtomSite and atomId in coordAtomSite['alt_atom_id']:
                found = True
                self.__authAtomId = 'auth_atom_id'
            elif self.__preferAuthSeq:
                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
                if _coordAtomSite is not None:
                    if atomId in _coordAtomSite['atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        seqKey = _seqKey
                    elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        self.__authAtomId = 'auth_atom_id'
                        seqKey = _seqKey

        elif self.__preferAuthSeq:
            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
            if _coordAtomSite is not None:
                if atomId in _coordAtomSite['atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    self.__authSeqId = 'label_seq_id'
                    seqKey = _seqKey
                elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    self.__authSeqId = 'label_seq_id'
                    self.__authAtomId = 'auth_atom_id'
                    seqKey = _seqKey

        if found:
            return

        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
        if _coordAtomSite is not None:
            if atomId in _coordAtomSite['atom_id']:
                found = True
                self.__preferAuthSeq = False
                self.__authSeqId = 'label_seq_id'
                seqKey = _seqKey
            elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                found = True
                self.__preferAuthSeq = False
                self.__authSeqId = 'label_seq_id'
                self.__authAtomId = 'auth_atom_id'
                seqKey = _seqKey

        if found:
            return

        if self.__ccU.updateChemCompDict(compId):
            cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
            if cca is not None and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                if seqId == 1 and atomId in ('H', 'HN'):
                    self.testCoordAtomIdConsistency(chainId, seqId, compId, 'H1', seqKey, coordAtomSite)
                    return
                if atomId[0] == 'H':
                    ccb = next((ccb for ccb in self.__ccU.lastBonds
                                if atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                    if ccb is not None:
                        bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == atomId else ccb[self.__ccU.ccbAtomId1]
                        if bondedTo[0] in ('N', 'O', 'S'):
                            return
                if enableWarning:
                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                        f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinates.\n"

    def getCoordAtomSiteOf(self, chainId, seqId, cifCheck=True, asis=True):
        seqKey = (chainId, seqId)
        coordAtomSite = None
        if cifCheck:
            preferAuthSeq = self.__preferAuthSeq if asis else not self.__preferAuthSeq
            if preferAuthSeq:
                if seqKey in self.__coordAtomSite:
                    coordAtomSite = self.__coordAtomSite[seqKey]
            else:
                if seqKey in self.__labelToAuthSeq:
                    seqKey = self.__labelToAuthSeq[seqKey]
                    if seqKey in self.__coordAtomSite:
                        coordAtomSite = self.__coordAtomSite[seqKey]
        return seqKey, coordAtomSite

    # Enter a parse tree produced by CyanaMRParser#torsion_angle_restraints.
    def enterTorsion_angle_restraints(self, ctx: CyanaMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#torsion_angle_restraints.
    def exitTorsion_angle_restraints(self, ctx: CyanaMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#torsion_angle_restraint.
    def enterTorsion_angle_restraint(self, ctx: CyanaMRParser.Torsion_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#torsion_angle_restraint.
    def exitTorsion_angle_restraint(self, ctx: CyanaMRParser.Torsion_angle_restraintContext):  # pylint: disable=unused-argument

        try:

            compId = str(ctx.Simple_name(0)).upper()
            if self.__cur_subtype_altered:  # invoked from exitCco_restraint()
                seqId = int(str(ctx.Integer()))
                chainId = str(ctx.Simple_name(1)).upper()
                angleName = str(ctx.Simple_name(2)).upper()
            else:
                seqId = int(str(ctx.Integer(0)))
                angleName = str(ctx.Simple_name(1)).upper()

            if None in self.numberSelection:
                self.dihedRestraints -= 1
                return

            target_value = None
            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]

            if self.__remediate and self.__reasons is not None and 'dihed_unusual_order' in self.__reasons:
                target_value, deviation = lower_limit, upper_limit
                lower_limit = target_value - deviation
                upper_limit = target_value + deviation

            weight = 1.0
            if len(self.numberSelection) > 2:
                weight = self.numberSelection[2]

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"
            """
            if lower_limit > upper_limit:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The angle's lower limit '{lower_limit}' must be less than or equal to the upper limit '{upper_limit}'.\n"
                if self.__remediate:
                    self.__dihed_lb_greater_than_ub = True
                return
            """
            if self.__remediate and upper_limit < 0.0:
                self.__dihed_ub_always_positive = False

            # target_value = (upper_limit + lower_limit) / 2.0

            dstFunc = self.validateAngleRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            # support AMBER's dihedral angle naming convention for nucleic acids
            # http://ambermd.org/tutorials/advanced/tutorial4/
            if angleName in ('EPSILN', 'EPSLN'):
                angleName = 'EPSILON'

            # nucleic CHI angle
            if angleName == 'CHIN':
                angleName = 'CHI'

            if angleName not in KNOWN_ANGLE_NAMES:
                lenAngleName = len(angleName)
                try:
                    # For the case 'EPSIL' could be standard name 'EPSILON'
                    angleName = next(name for name in KNOWN_ANGLE_NAMES if len(name) >= lenAngleName and name[:lenAngleName] == angleName)
                except StopIteration:
                    self.warningMessage += f"[Insufficient angle selection] {self.__getCurrentRestraint()}"\
                        f"The angle identifier {str(ctx.Simple_name(1))!r} is unknown for the residue {compId!r}, "\
                        "of which CYANA residue library should be uploaded.\n"
                    return

            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            if carbohydrate and angleName in KNOWN_ANGLE_CARBO_ATOM_NAMES:
                atomNames = KNOWN_ANGLE_CARBO_ATOM_NAMES[angleName]
                seqOffset = KNOWN_ANGLE_CARBO_SEQ_OFFSET[angleName]
            else:
                atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
                seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

            if angleName != 'PPA':

                if isinstance(atomNames, list):
                    atomId = next(name for name, offset in zip(atomNames, seqOffset) if offset == 0)
                else:  # nucleic CHI angle
                    atomId = next(name for name, offset in zip(atomNames['Y'], seqOffset['Y']) if offset == 0)

                if self.__cur_subtype_altered:  # invoked from exitCco_restraint()
                    chainAssign = self.assignCoordPolymerSequenceWithChainId(chainId, seqId, compId, atomId)
                else:
                    chainAssign = self.assignCoordPolymerSequence(seqId, compId, atomId)

                if len(chainAssign) == 0:
                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                        f"{seqId}:{compId} is not present in the coordinates.\n"
                    return

                for chainId, cifSeqId, cifCompId in chainAssign:
                    ps = next(ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId)

                    peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(cifCompId)

                    if peptide and angleName in ('PHI', 'PSI', 'OMEGA',
                                                 'CHI1', 'CHI2', 'CHI3', 'CHI4', 'CHI5',
                                                 'CHI21', 'CHI22', 'CHI31', 'CHI32', 'CHI42'):
                        pass
                    elif nucleotide and angleName in ('ALPHA', 'BETA', 'GAMMA', 'DELTA', 'EPSILON', 'ZETA',
                                                      'CHI', 'ETA', 'THETA', "ETA'", "THETA'",
                                                      'NU0', 'NU1', 'NU2', 'NU3', 'NU4',
                                                      'TAU0', 'TAU1', 'TAU2', 'TAU3', 'TAU4'):
                        pass
                    elif carbohydrate and angleName in ('PHI', 'PSI', 'OMEGA'):
                        pass
                    else:
                        self.warningMessage += f"[Insufficient angle selection] {self.__getCurrentRestraint()}"\
                            f"The angle identifier {str(ctx.Simple_name(1))!r} is unknown for the residue {compId!r}, "\
                            "of which CYANA residue library should be uploaded.\n"
                        return

                    atomNames = None
                    seqOffset = None

                    if carbohydrate:
                        atomNames = KNOWN_ANGLE_CARBO_ATOM_NAMES[angleName]
                        seqOffset = KNOWN_ANGLE_CARBO_SEQ_OFFSET[angleName]
                    elif nucleotide and angleName == 'CHI':
                        if self.__ccU.updateChemCompDict(cifCompId):
                            try:
                                next(cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == 'N9')
                                atomNames = KNOWN_ANGLE_ATOM_NAMES['CHI']['R']
                                seqOffset = KNOWN_ANGLE_SEQ_OFFSET['CHI']['R']
                            except StopIteration:
                                atomNames = KNOWN_ANGLE_ATOM_NAMES['CHI']['Y']
                                seqOffset = KNOWN_ANGLE_SEQ_OFFSET['CHI']['Y']
                    else:
                        atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
                        seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

                    atomSelection = []

                    for atomId, offset in zip(atomNames, seqOffset):

                        atomSelection.clear()

                        _cifSeqId = cifSeqId + offset
                        _cifCompId = cifCompId if offset == 0 else (ps['comp_id'][ps['auth_seq_id'].index(_cifSeqId)] if _cifSeqId in ps['auth_seq_id'] else None)

                        if _cifCompId is None:
                            self.warningMessage += f"[Sequence mismatch warning] {self.__getCurrentRestraint()}"\
                                f"The residue number '{seqId+offset}' is not present in polymer sequence of chain {chainId} of the coordinates. "\
                                "Please update the sequence in the Macromolecules page.\n"
                            _cifCompId = '.'
                            cifAtomId = atomId

                        else:
                            self.__ccU.updateChemCompDict(_cifCompId)

                            if isinstance(atomId, str):
                                cifAtomId = next((cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
                            else:
                                cifAtomId = next((cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if atomId.match(cca[self.__ccU.ccaAtomId])), None)

                            if cifAtomId is None:
                                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                    f"{seqId+offset}:{compId}:{atomId} is not present in the coordinates.\n"
                                return

                        atomSelection.append({'chain_id': chainId, 'seq_id': _cifSeqId, 'comp_id': _cifCompId, 'atom_id': cifAtomId})

                        if len(atomSelection) > 0:
                            self.atomSelectionSet.append(atomSelection)

                    if len(self.atomSelectionSet) < 4:
                        return

                    if not self.areUniqueCoordAtoms('a Torsion angle'):
                        return

                    for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                        self.atomSelectionSet[1],
                                                                        self.atomSelectionSet[2],
                                                                        self.atomSelectionSet[3]):
                        if isLongRangeRestraint([atom1, atom2, atom3, atom4]):
                            continue
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} "
                                  f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

            # phase angle of pseudorotation
            else:

                atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
                seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

                atomId = next(name for name, offset in zip(atomNames, seqOffset) if offset == 0)

                chainAssign = self.assignCoordPolymerSequence(seqId, compId, atomId)

                if len(chainAssign) == 0:
                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                        f"{seqId}:{compId} is not present in the coordinates.\n"
                    return

                for chainId, cifSeqId, cifCompId in chainAssign:
                    ps = next(ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId)

                    peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(cifCompId)

                    atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
                    seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

                    if nucleotide:
                        pass
                    else:
                        self.warningMessage += f"[Insufficient angle selection] {self.__getCurrentRestraint()}"\
                            f"The angle identifier {str(ctx.Simple_name(1))!r} did not match with residue {compId!r}.\n"
                        return

                    atomSelection = []

                    for atomId, offset in zip(atomNames, seqOffset):

                        atomSelection.clear()

                        _cifSeqId = cifSeqId + offset
                        _cifCompId = cifCompId if offset == 0 else (ps['comp_id'][ps['auth_seq_id'].index(_cifSeqId)] if _cifSeqId in ps['auth_seq_id'] else None)

                        if _cifCompId is None:
                            self.warningMessage += f"[Sequence mismatch warning] {self.__getCurrentRestraint()}"\
                                f"The residue number '{seqId+offset}' is not present in polymer sequence of chain {chainId} of the coordinates. "\
                                "Please update the sequence in the Macromolecules page.\n"
                            _cifCompId = '.'
                            cifAtomId = atomId

                        else:
                            self.__ccU.updateChemCompDict(_cifCompId)

                            cifAtomId = next((cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)

                            if cifAtomId is None:
                                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                    f"{seqId+offset}:{compId}:{atomId} is not present in the coordinates.\n"
                                return

                        atomSelection.append({'chain_id': chainId, 'seq_id': _cifSeqId, 'comp_id': _cifCompId, 'atom_id': cifAtomId})

                        if len(atomSelection) > 0:
                            self.atomSelectionSet.append(atomSelection)

                    if len(self.atomSelectionSet) < 5:
                        return

                    if not self.areUniqueCoordAtoms('a Torsion angle'):
                        return

                    for atom1, atom2, atom3, atom4, atom5 in itertools.product(self.atomSelectionSet[0],
                                                                               self.atomSelectionSet[1],
                                                                               self.atomSelectionSet[2],
                                                                               self.atomSelectionSet[3],
                                                                               self.atomSelectionSet[4]):
                        if isLongRangeRestraint([atom1, atom2, atom3, atom4, atom5]):
                            continue
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} "
                                  f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} atom5={atom5} {dstFunc}")

        except ValueError:
            self.dihedRestraints -= 1
        finally:
            self.numberSelection.clear()

    def validateAngleRange(self, weight, target_value, lower_limit, upper_limit):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if ANGLE_ERROR_MIN < target_value < ANGLE_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if ANGLE_ERROR_MIN <= lower_limit < ANGLE_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if ANGLE_ERROR_MIN < upper_limit <= ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if not validRange:
            return None

        if target_value is not None:
            if ANGLE_RANGE_MIN <= target_value <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if ANGLE_RANGE_MIN <= lower_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if ANGLE_RANGE_MIN <= upper_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by CyanaMRParser#rdc_restraints.
    def enterRdc_restraints(self, ctx: CyanaMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

        self.__cur_subtype_altered = False

        self.rdcParameterDict = {}

    # Exit a parse tree produced by CyanaMRParser#rdc_restraints.
    def exitRdc_restraints(self, ctx: CyanaMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#rdc_parameter.
    def enterRdc_parameter(self, ctx: CyanaMRParser.Rdc_parameterContext):  # pylint: disable=unused-argument
        orientation = self.__cur_rdc_orientation = int(str(ctx.Integer(0)))
        magnitude = float(str(ctx.Float(0)))
        rhombicity = float(str(ctx.Float(1)))
        orientationCenterSeqId = int(str(ctx.Integer(1)))

        self.rdcParameterDict[orientation] = {'magnitude': magnitude,
                                              'rhombicity': rhombicity,
                                              'orientation_center_seq_id': orientationCenterSeqId}

        if self.__debug:
            print(f"subtype={self.__cur_subtype} orientation={orientation} "
                  f"parameters={self.rdcParameterDict[orientation]}")

    # Exit a parse tree produced by CyanaMRParser#rdc_parameter.
    def exitRdc_parameter(self, ctx: CyanaMRParser.Rdc_parameterContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: CyanaMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: CyanaMRParser.Rdc_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()

            if None in self.numberSelection:
                self.rdcRestraints -= 1
                return

            target = self.numberSelection[0]
            error = abs(self.numberSelection[1])
            weight = self.numberSelection[2]
            orientation = int(str(ctx.Integer(2)))

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            if orientation not in self.rdcParameterDict:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The orientation '{orientation}' must be defined before you start to describe RDC restraints.\n"
                return

            if seqId1 == self.rdcParameterDict[orientation]['orientation_center_seq_id']:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The residue number '{seqId1}' must not be the same as the center of orientation.\n"
                return

            if seqId2 == self.rdcParameterDict[orientation]['orientation_center_seq_id']:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The residue number '{seqId2}' must not be the same as the center of orientation.\n"
                return

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validateRdcRange(weight, orientation, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

            if len(self.atomSelectionSet) < 2:
                return

            if not self.areUniqueCoordAtoms('an RDC'):
                return

            chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
            seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
            comp_id_1 = self.atomSelectionSet[0][0]['comp_id']
            atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

            chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
            seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
            comp_id_2 = self.atomSelectionSet[1][0]['comp_id']
            atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

            if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Non-magnetic susceptible spin appears in RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if chain_id_1 != chain_id_2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found inter-chain RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if abs(seq_id_1 - seq_id_2) > 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found inter-residue RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if abs(seq_id_1 - seq_id_2) == 1:

                if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                        ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                         or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                    pass

                else:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found inter-residue RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif atom_id_1 == atom_id_2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Found zero RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                if not any(b for b in self.__ccU.lastBonds
                           if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                               or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                    if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            "Found an RDC vector over multiple covalent bonds; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if isLongRangeRestraint([atom1, atom2]):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        except ValueError:
            self.rdcRestraints -= 1
        finally:
            self.numberSelection.clear()

    def validateRdcRange(self, weight, orientation, target_value, lower_limit, upper_limit):
        """ Validate RDC value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if orientation is not None:
            dstFunc['orientation'] = orientation

        if target_value is not None:
            if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if RDC_ERROR_MIN <= lower_limit < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit <= RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.6f}' must be greater than the target value '{target_value}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if RDC_RANGE_MIN <= target_value <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if RDC_RANGE_MIN <= lower_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN <= upper_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        return dstFunc

    def areUniqueCoordAtoms(self, subtype_name):
        """ Check whether atom selection sets are uniquely assigned.
        """

        for _atomSelectionSet in self.atomSelectionSet:

            if len(_atomSelectionSet) < 2:
                continue

            for (atom1, atom2) in itertools.combinations(_atomSelectionSet, 2):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if atom1['seq_id'] != atom2['seq_id']:
                    continue
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint()}"\
                    f"Ambiguous atom selection '{atom1['chain_id']}:{atom1['seq_id']}:{atom1['comp_id']}:{atom1['atom_id']} or "\
                    f"{atom2['atom_id']}' is not allowed as {subtype_name} restraint.\n"
                return False

        return True

    # Enter a parse tree produced by CyanaMRParser#pcs_restraints.
    def enterPcs_restraints(self, ctx: CyanaMRParser.Pcs_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'pcs'

        self.__cur_subtype_altered = False

        self.pcsParameterDict = {}

    # Exit a parse tree produced by CyanaMRParser#pcs_restraints.
    def exitPcs_restraints(self, ctx: CyanaMRParser.Pcs_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#pcs_parameter.
    def enterPcs_parameter(self, ctx: CyanaMRParser.Pcs_parameterContext):
        orientation = int(str(ctx.Integer(0)))
        magnitude = float(str(ctx.Float(0)))
        rhombicity = float(str(ctx.Float(1)))
        orientationCenterSeqId = int(str(ctx.Integer(1)))

        self.pcsParameterDict[orientation] = {'magnitude': magnitude,
                                              'rhombicity': rhombicity,
                                              'orientation_center_seq_id': orientationCenterSeqId}

        if self.__debug:
            print(f"subtype={self.__cur_subtype} orientation={orientation} "
                  f"parameters={self.pcsParameterDict[orientation]}")

    # Exit a parse tree produced by CyanaMRParser#pcs_parameter.
    def exitPcs_parameter(self, ctx: CyanaMRParser.Pcs_parameterContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#pcs_restraint.
    def enterPcs_restraint(self, ctx: CyanaMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        self.pcsRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#pcs_restraint.
    def exitPcs_restraint(self, ctx: CyanaMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument

        try:

            seqId = int(str(ctx.Integer(0)))
            compId = str(ctx.Simple_name(0)).upper()
            atomId = str(ctx.Simple_name(1)).upper()

            if None in self.numberSelection:
                self.pcsRestraints -= 1
                return

            target = self.numberSelection[0]
            error = abs(self.numberSelection[1])
            weight = self.numberSelection[2]
            orientation = int(str(ctx.Integer(1)))

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            if orientation not in self.pcsParameterDict:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The orientation '{orientation}' must be defined before you start to describe PCS restraints.\n"
                return

            if seqId == self.pcsParameterDict[orientation]['orientation_center_seq_id']:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The residue number '{seqId}' must not be the same as the center of orientation.\n"
                return

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validatePcsRange(weight, orientation, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign = self.assignCoordPolymerSequence(seqId, compId, atomId)

            if len(chainAssign) == 0:
                return

            self.selectCoordAtoms(chainAssign, seqId, compId, atomId)

            if len(self.atomSelectionSet) < 1:
                return

            for atom in self.atomSelectionSet[0]:
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.pcsRestraints} "
                          f"atom={atom} {dstFunc}")

        except ValueError:
            self.pcsRestraints -= 1
        finally:
            self.numberSelection.clear()

    def validatePcsRange(self, weight, orientation, target_value, lower_limit, upper_limit):
        """ Validate PCS value range.
        """

        validRange = True
        dstFunc = {'weight': weight, 'orientation': orientation}

        if target_value is not None:
            if PCS_ERROR_MIN < target_value < PCS_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {PCS_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if PCS_ERROR_MIN <= lower_limit < PCS_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.6f}' must be within range {PCS_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if PCS_ERROR_MIN < upper_limit <= PCS_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.6f}' must be within range {PCS_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.6f}' must be greater than the target value '{target_value}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if PCS_RANGE_MIN <= target_value <= PCS_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {PCS_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if PCS_RANGE_MIN <= lower_limit <= PCS_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.6f}' should be within range {PCS_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if PCS_RANGE_MIN <= upper_limit <= PCS_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.6f}' should be within range {PCS_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by CyanaMRParser#fixres_distance_restraints.
    def enterFixres_distance_restraints(self, ctx: CyanaMRParser.Fixres_distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist' if self.__file_ext is None or self.__file_ext not in ('upv', 'lov') else 'noepk'
        if self.__reasons is not None and 'noepk_fixres' in self.__reasons:
            self.__cur_subtype = 'noepk'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#fixres_distance_restraints.
    def exitFixres_distance_restraints(self, ctx: CyanaMRParser.Fixres_distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#fixres_distance_restraint.
    def enterFixres_distance_restraint(self, ctx: CyanaMRParser.Fixres_distance_restraintContext):  # pylint: disable=unused-argument
        if self.__cur_subtype == 'dist':
            self.distRestraints += 1
        else:
            self.noepkRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#fixres_distance_restraint.
    def exitFixres_distance_restraint(self, ctx: CyanaMRParser.Fixres_distance_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()

            int_col = 1
            str_col = 1

            omit_dist_limit_outlier = self.__reasons is not None and self.__omitDistLimitOutlier

            if None in self.numberSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                else:
                    self.noepkRestraints -= 1
                return

            for num_col, value in enumerate(self.numberSelection):
                atomId1 = str(ctx.Simple_name(str_col)).upper()
                seqId2 = int(str(ctx.Integer(int_col)))
                compId2 = str(ctx.Simple_name(str_col + 1)).upper()
                atomId2 = str(ctx.Simple_name(str_col + 2)).upper()

                target_value = None
                lower_limit = None
                upper_limit = None

                if self.__cur_subtype == 'dist':

                    if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX:
                        if self.__max_dist_value is None:
                            self.__max_dist_value = value
                        if value > self.__max_dist_value:
                            self.__max_dist_value = value

                    if self.__upl_or_lol is None or self.__upl_or_lol == 'upl_only':
                        if value > 1.8:
                            upper_limit = value
                            lower_limit = 1.8  # default value of PDBStat
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                        else:
                            lower_limit = value

                    elif self.__upl_or_lol == 'upl_w_lol':
                        upper_limit = value

                    elif self.__upl_or_lol == 'lol_only':
                        lower_limit = value
                        upper_limit = 5.5  # default value of PDBStat
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                    else:  # 'lol_w_upl'
                        lower_limit = value

                    dstFunc = self.validateDistanceRange(1.0, target_value, lower_limit, upper_limit, omit_dist_limit_outlier)

                    if dstFunc is None and abs(value) > DIST_ERROR_MAX * 10.0:
                        if self.reasonsForReParsing is None:
                            self.reasonsForReParsing = {}
                        self.reasonsForReParsing['noepk_fixres'] = True

                else:  # 'noepk'

                    target_value = value

                    dstFunc = self.validatePeakVolumeRange(1.0, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                if not self.__hasPolySeq:
                    return

                chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

                if num_col > 0:
                    self.distRestraints += 1

                int_col += 1
                str_col += 3

        except ValueError:
            if self.__cur_subtype == 'dist':
                self.distRestraints -= 1
            else:
                self.noepkRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CyanaMRParser#fixresw_distance_restraints.
    def enterFixresw_distance_restraints(self, ctx: CyanaMRParser.Fixresw_distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist' if self.__file_ext is None or self.__file_ext not in ('upv', 'lov') else 'noepk'
        if self.__reasons is not None and 'noepk_fixresw' in self.__reasons:
            self.__cur_subtype = 'noepk'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#fixresw_distance_restraints.
    def exitFixresw_distance_restraints(self, ctx: CyanaMRParser.Fixresw_distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#fixresw_distance_restraint.
    def enterFixresw_distance_restraint(self, ctx: CyanaMRParser.Fixresw_distance_restraintContext):  # pylint: disable=unused-argument
        if self.__cur_subtype == 'dist':
            self.distRestraints += 1
        else:
            self.noepkRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#fixresw_distance_restraint.
    def exitFixresw_distance_restraint(self, ctx: CyanaMRParser.Fixresw_distance_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()

            int_col = 1
            str_col = 1

            omit_dist_limit_outlier = self.__reasons is not None and self.__omitDistLimitOutlier

            if None in self.numberSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                else:
                    self.noepkRestraints -= 1
                return

            for num_col in range(0, len(self.numberSelection), 2):
                atomId1 = str(ctx.Simple_name(str_col)).upper()
                seqId2 = int(str(ctx.Integer(int_col)))
                compId2 = str(ctx.Simple_name(str_col + 1)).upper()
                atomId2 = str(ctx.Simple_name(str_col + 2)).upper()

                value = self.numberSelection[num_col]
                value2 = self.numberSelection[num_col + 1]

                delta = None
                has_square = False

                if value2 <= 1.0 or value2 < value:
                    delta = abs(value2)
                else:
                    weight = 1.0
                    has_square = True

                if weight < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' must not be a negative value.\n"
                    return
                if weight == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' should be a positive value.\n"

                target_value = None
                lower_limit = None
                upper_limit = None

                if self.__cur_subtype == 'dist':

                    if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX:
                        if self.__max_dist_value is None:
                            self.__max_dist_value = value
                        if value > self.__max_dist_value:
                            self.__max_dist_value = value

                    if has_square:
                        if value2 > DIST_RANGE_MAX:  # lol_only
                            lower_limit = value

                        elif 1.8 <= value <= DIST_ERROR_MAX and DIST_RANGE_MIN <= value2 <= DIST_RANGE_MAX:
                            upper_limit = value2
                            lower_limit = value
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                        else:  # upl_only
                            if value2 > 1.8:
                                upper_limit = value2
                                lower_limit = 1.8  # default value of PDBStat
                                target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                            else:
                                upper_limit = value2

                    elif delta is not None:
                        target_value = value
                        lower_limit = value - delta
                        upper_limit = value + delta

                    elif self.__upl_or_lol is None or self.__upl_or_lol == 'upl_only':
                        if value > 1.8:
                            upper_limit = value
                            lower_limit = 1.8  # default value of PDBStat
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                        else:
                            lower_limit = value

                    elif self.__upl_or_lol == 'upl_w_lol':
                        upper_limit = value

                    elif self.__upl_or_lol == 'lol_only':
                        lower_limit = value
                        upper_limit = 5.5  # default value of PDBStat
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                    else:  # 'lol_w_upl'
                        lower_limit = value

                    dstFunc = self.validateDistanceRange(weight, target_value, lower_limit, upper_limit, omit_dist_limit_outlier)

                    if dstFunc is None and (abs(value) > DIST_ERROR_MAX * 10.0 or abs(value2) > DIST_ERROR_MAX * 10.0):
                        if self.reasonsForReParsing is None:
                            self.reasonsForReParsing = {}
                        self.reasonsForReParsing['noepk_fixresw'] = True

                else:  # 'noepk'

                    if has_square:
                        lower_limit = value
                        upper_limit = value2
                    else:
                        target_value = value

                    dstFunc = self.validatePeakVolumeRange(weight, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                if not self.__hasPolySeq:
                    return

                chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

                if num_col > 0:
                    self.distRestraints += 1

                int_col += 1
                str_col += 3

        except ValueError:
            if self.__cur_subtype == 'dist':
                self.distRestraints -= 1
            else:
                self.noepkRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CyanaMRParser#fixresw2_distance_restraints.
    def enterFixresw2_distance_restraints(self, ctx: CyanaMRParser.Fixresw2_distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist' if self.__file_ext is None or self.__file_ext not in ('upv', 'lov') else 'noepk'
        if self.__reasons is not None and 'noepk_fixresw2' in self.__reasons:
            self.__cur_subtype = 'noepk'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#fixresw2_distance_restraints.
    def exitFixresw2_distance_restraints(self, ctx: CyanaMRParser.Fixresw2_distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#fixresw2_distance_restraint.
    def enterFixresw2_distance_restraint(self, ctx: CyanaMRParser.Fixresw2_distance_restraintContext):  # pylint: disable=unused-argument
        if self.__cur_subtype == 'dist':
            self.distRestraints += 1
        else:
            self.noepkRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#fixresw2_distance_restraint.
    def exitFixresw2_distance_restraint(self, ctx: CyanaMRParser.Fixresw2_distance_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()

            int_col = 1
            str_col = 1

            omit_dist_limit_outlier = self.__reasons is not None and self.__omitDistLimitOutlier

            if None in self.numberSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                else:
                    self.noepkRestraints -= 1
                return

            for num_col in range(0, len(self.numberSelection), 3):
                atomId1 = str(ctx.Simple_name(str_col)).upper()
                seqId2 = int(str(ctx.Integer(int_col)))
                compId2 = str(ctx.Simple_name(str_col + 1)).upper()
                atomId2 = str(ctx.Simple_name(str_col + 2)).upper()

                value = self.numberSelection[num_col]
                value2 = self.numberSelection[num_col + 1]
                weight = self.numberSelection[num_col + 2]

                if weight < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' must not be a negative value.\n"
                    return
                if weight == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' should be a positive value.\n"

                target_value = None
                lower_limit = None
                upper_limit = None

                if self.__cur_subtype == 'dist':

                    if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX:
                        if self.__max_dist_value is None:
                            self.__max_dist_value = value
                        if value > self.__max_dist_value:
                            self.__max_dist_value = value

                    if value2 > DIST_RANGE_MAX:  # lol_only
                        lower_limit = value

                    elif 1.8 <= value <= DIST_ERROR_MAX and DIST_RANGE_MIN <= value2 <= DIST_RANGE_MAX:
                        upper_limit = value2
                        lower_limit = value
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                    else:  # upl_only
                        if value2 > 1.8:
                            upper_limit = value2
                            lower_limit = 1.8  # default value of PDBStat
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                        else:
                            upper_limit = value2

                    dstFunc = self.validateDistanceRange(weight, target_value, lower_limit, upper_limit, omit_dist_limit_outlier)

                    if dstFunc is None and (abs(value) > DIST_ERROR_MAX * 10.0 or abs(value2) > DIST_ERROR_MAX * 10.0):
                        if self.reasonsForReParsing is None:
                            self.reasonsForReParsing = {}
                        self.reasonsForReParsing['noepk_fixresw2'] = True

                else:  # 'noepk'

                    lower_limit = value
                    upper_limit = value2

                    dstFunc = self.validatePeakVolumeRange(weight, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                if not self.__hasPolySeq:
                    return

                chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

                if num_col > 0:
                    self.distRestraints += 1

                int_col += 1
                str_col += 3

        except ValueError:
            if self.__cur_subtype == 'dist':
                self.distRestraints -= 1
            else:
                self.noepkRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CyanaMRParser#fixatm_distance_restraints.
    def enterFixatm_distance_restraints(self, ctx: CyanaMRParser.Fixatm_distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist' if self.__file_ext is None or self.__file_ext not in ('upv', 'lov') else 'noepk'
        if self.__reasons is not None and 'noepk_fixatm' in self.__reasons:
            self.__cur_subtype = 'noepk'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#fixatm_distance_restraints.
    def exitFixatm_distance_restraints(self, ctx: CyanaMRParser.Fixatm_distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#fixatm_distance_restraint.
    def enterFixatm_distance_restraint(self, ctx: CyanaMRParser.Fixatm_distance_restraintContext):  # pylint: disable=unused-argument
        if self.__cur_subtype == 'dist':
            self.distRestraints += 1
        else:
            self.noepkRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#fixatm_distance_restraint.
    def exitFixatm_distance_restraint(self, ctx: CyanaMRParser.Fixatm_distance_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()

            int_col = 1
            str_col = 2

            omit_dist_limit_outlier = self.__reasons is not None and self.__omitDistLimitOutlier

            if None in self.numberSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                else:
                    self.noepkRestraints -= 1
                return

            for num_col, value in enumerate(self.numberSelection):
                seqId2 = int(str(ctx.Integer(int_col)))
                compId2 = str(ctx.Simple_name(str_col)).upper()
                atomId2 = str(ctx.Simple_name(str_col + 1)).upper()

                target_value = None
                lower_limit = None
                upper_limit = None

                if self.__cur_subtype == 'dist':

                    if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX:
                        if self.__max_dist_value is None:
                            self.__max_dist_value = value
                        if value > self.__max_dist_value:
                            self.__max_dist_value = value

                    if self.__upl_or_lol is None or self.__upl_or_lol == 'upl_only':
                        if value > 1.8:
                            upper_limit = value
                            lower_limit = 1.8  # default value of PDBStat
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                        else:
                            lower_limit = value

                    elif self.__upl_or_lol == 'upl_w_lol':
                        upper_limit = value

                    elif self.__upl_or_lol == 'lol_only':
                        lower_limit = value
                        upper_limit = 5.5  # default value of PDBStat
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                    else:  # 'lol_w_upl'
                        lower_limit = value

                    dstFunc = self.validateDistanceRange(1.0, target_value, lower_limit, upper_limit, omit_dist_limit_outlier)

                    if dstFunc is None and abs(value) > DIST_ERROR_MAX * 10.0:
                        if self.reasonsForReParsing is None:
                            self.reasonsForReParsing = {}
                        self.reasonsForReParsing['noepk_fixatm'] = True

                else:  # 'noepk'

                    target_value = value

                    dstFunc = self.validatePeakVolumeRange(1.0, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                if not self.__hasPolySeq:
                    return

                chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

                if num_col > 0:
                    self.distRestraints += 1

                int_col += 1
                str_col += 2

        except ValueError:
            if self.__cur_subtype == 'dist':
                self.distRestraints -= 1
            else:
                self.noepkRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CyanaMRParser#fixatmw_distance_restraints.
    def enterFixatmw_distance_restraints(self, ctx: CyanaMRParser.Fixatmw_distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist' if self.__file_ext is None or self.__file_ext not in ('upv', 'lov') else 'noepk'
        if self.__reasons is not None and 'noepk_fixatmw' in self.__reasons:
            self.__cur_subtype = 'noepk'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#fixatmw_distance_restraints.
    def exitFixatmw_distance_restraints(self, ctx: CyanaMRParser.Fixatmw_distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#fixatmw_distance_restraint.
    def enterFixatmw_distance_restraint(self, ctx: CyanaMRParser.Fixatmw_distance_restraintContext):  # pylint: disable=unused-argument
        if self.__cur_subtype == 'dist':
            self.distRestraints += 1
        else:
            self.noepkRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#fixatmw_distance_restraint.
    def exitFixatmw_distance_restraint(self, ctx: CyanaMRParser.Fixatmw_distance_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()

            int_col = 1
            str_col = 2

            omit_dist_limit_outlier = self.__reasons is not None and self.__omitDistLimitOutlier

            if None in self.numberSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                else:
                    self.noepkRestraints -= 1
                return

            for num_col in range(0, len(self.numberSelection), 2):
                seqId2 = int(str(ctx.Integer(int_col)))
                compId2 = str(ctx.Simple_name(str_col)).upper()
                atomId2 = str(ctx.Simple_name(str_col + 1)).upper()

                value = self.numberSelection[num_col]
                value2 = self.numberSelection[num_col + 1]

                delta = None
                has_square = False

                if value2 < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{value2}' must not be a negative value.\n"
                    return
                if value2 == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{value2}' should be a positive value.\n"

                if value2 <= 1.0 or value2 < value:
                    delta = abs(value2)
                else:
                    weight = 1.0
                    has_square = True

                target_value = None
                lower_limit = None
                upper_limit = None

                if self.__cur_subtype == 'dist':

                    if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX:
                        if self.__max_dist_value is None:
                            self.__max_dist_value = value
                        if value > self.__max_dist_value:
                            self.__max_dist_value = value

                    if has_square:
                        if value2 > DIST_RANGE_MAX:  # lol_only
                            lower_limit = value

                        elif 1.8 <= value <= DIST_ERROR_MAX and DIST_RANGE_MIN <= value2 <= DIST_RANGE_MAX:
                            upper_limit = value2
                            lower_limit = value
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                        else:  # upl_only
                            if value2 > 1.8:
                                upper_limit = value2
                                lower_limit = 1.8  # default value of PDBStat
                                target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                            else:
                                upper_limit = value2

                    elif delta is not None:
                        target_value = value
                        lower_limit = value - delta
                        upper_limit = value + delta

                    elif self.__upl_or_lol is None or self.__upl_or_lol == 'upl_only':
                        if value > 1.8:
                            upper_limit = value
                            lower_limit = 1.8  # default value of PDBStat
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                        else:
                            lower_limit = value

                    elif self.__upl_or_lol == 'upl_w_lol':
                        upper_limit = value

                    elif self.__upl_or_lol == 'lol_only':
                        lower_limit = value
                        upper_limit = 5.5  # default value of PDBStat
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                    else:  # 'lol_w_upl'
                        lower_limit = value

                    dstFunc = self.validateDistanceRange(weight, target_value, lower_limit, upper_limit, omit_dist_limit_outlier)

                    if dstFunc is None and (abs(value) > DIST_ERROR_MAX * 10.0 or abs(value2) > DIST_ERROR_MAX * 10.0):
                        if self.reasonsForReParsing is None:
                            self.reasonsForReParsing = {}
                        self.reasonsForReParsing['noepk_fixatmw'] = True

                else:  # 'noepk'

                    if has_square:
                        lower_limit = value
                        upper_limit = value2
                    else:
                        target_value = value

                    dstFunc = self.validatePeakVolumeRange(weight, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                if not self.__hasPolySeq:
                    return

                chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

                if num_col > 0:
                    self.distRestraints += 1

                int_col += 1
                str_col += 2

        except ValueError:
            if self.__cur_subtype == 'dist':
                self.distRestraints -= 1
            else:
                self.noepkRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CyanaMRParser#fixatmw2_distance_restraints.
    def enterFixatmw2_distance_restraints(self, ctx: CyanaMRParser.Fixatmw2_distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist' if self.__file_ext is None or self.__file_ext not in ('upv', 'lov') else 'noepk'
        if self.__reasons is not None and 'noepk_fixatmw2' in self.__reasons:
            self.__cur_subtype = 'noepk'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#fixatmw2_distance_restraints.
    def exitFixatmw2_distance_restraints(self, ctx: CyanaMRParser.Fixatmw2_distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#fixatmw2_distance_restraint.
    def enterFixatmw2_distance_restraint(self, ctx: CyanaMRParser.Fixatmw2_distance_restraintContext):  # pylint: disable=unused-argument
        if self.__cur_subtype == 'dist':
            self.distRestraints += 1
        else:
            self.noepkRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#fixatmw2_distance_restraint.
    def exitFixatmw2_distance_restraint(self, ctx: CyanaMRParser.Fixatmw2_distance_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()

            int_col = 1
            str_col = 2

            omit_dist_limit_outlier = self.__reasons is not None and self.__omitDistLimitOutlier

            if None in self.numberSelection:
                if self.__cur_subtype == 'dist':
                    self.distRestraints -= 1
                else:
                    self.noepkRestraints -= 1
                return

            for num_col in range(0, len(self.numberSelection), 3):
                seqId2 = int(str(ctx.Integer(int_col)))
                compId2 = str(ctx.Simple_name(str_col)).upper()
                atomId2 = str(ctx.Simple_name(str_col + 1)).upper()

                value = self.numberSelection[num_col]
                value2 = self.numberSelection[num_col + 1]
                weight = self.numberSelection[num_col + 2]

                if weight < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' must not be a negative value.\n"
                    return
                if weight == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The relative weight value of '{weight}' should be a positive value.\n"

                target_value = None
                lower_limit = None
                upper_limit = None

                if self.__cur_subtype == 'dist':

                    if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX:
                        if self.__max_dist_value is None:
                            self.__max_dist_value = value
                        if value > self.__max_dist_value:
                            self.__max_dist_value = value

                    if value2 > DIST_RANGE_MAX:  # lol_only
                        lower_limit = value

                    elif 1.8 <= value <= DIST_ERROR_MAX and DIST_RANGE_MIN <= value2 <= DIST_RANGE_MAX:
                        upper_limit = value2
                        lower_limit = value
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                    else:  # upl_only
                        if value2 > 1.8:
                            upper_limit = value2
                            lower_limit = 1.8  # default value of PDBStat
                            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                        else:
                            upper_limit = value2

                    dstFunc = self.validateDistanceRange(weight, target_value, lower_limit, upper_limit, omit_dist_limit_outlier)

                    if dstFunc is None and (abs(value) > DIST_ERROR_MAX * 10.0 or abs(value2) > DIST_ERROR_MAX * 10.0):
                        if self.reasonsForReParsing is None:
                            self.reasonsForReParsing = {}
                        self.reasonsForReParsing['noepk_fixatmw2'] = True

                else:  # 'noepk'

                    lower_limit = value
                    upper_limit = value2

                    dstFunc = self.validatePeakVolumeRange(weight, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                if not self.__hasPolySeq:
                    return

                chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
                chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

                if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                    return

                self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
                self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

                if len(self.atomSelectionSet) < 2:
                    return

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

                if num_col > 0:
                    self.distRestraints += 1

                int_col += 1
                str_col += 2

        except ValueError:
            if self.__cur_subtype == 'dist':
                self.distRestraints -= 1
            else:
                self.noepkRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CyanaMRParser#distance_w_chain_restraints.
    def enterDistance_w_chain_restraints(self, ctx: CyanaMRParser.Distance_w_chain_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

        self.__col_order_of_dist_w_chain = {}

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#distance_w_chain_restraints.
    def exitDistance_w_chain_restraints(self, ctx: CyanaMRParser.Distance_w_chain_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#distance_w_chain_restraint.
    def enterDistance_w_chain_restraint(self, ctx: CyanaMRParser.Distance_w_chain_restraintContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#distance_w_chain_restraint.
    def exitDistance_w_chain_restraint(self, ctx: CyanaMRParser.Distance_w_chain_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            seqId2 = int(str(ctx.Integer(1)))
            jVal = [''] * 6
            for j in range(6):
                jVal[j] = str(ctx.Simple_name(j)).upper()

            if len(self.__col_order_of_dist_w_chain) == 0:
                for j in range(3):
                    if len(jVal[j]) > 2 and translateToStdResName(jVal[j]) in monDict3:
                        self.__col_order_of_dist_w_chain['comp_id_1'] = j
                        compId = jVal[j]
                        if self.__ccU.updateChemCompDict(compId):
                            for k in range(3):
                                if k == j:
                                    continue
                                atomId = jVal[k]
                                _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                if details is not None and len(atomId) > 1:
                                    _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId[:-1], leave_unmatched=True)

                                if details is not None:
                                    _atomId_ = translateToStdAtomName(atomId, compId, ccU=self.__ccU)
                                    if _atomId_ != atomId:
                                        _atomId = self.__nefT.get_valid_star_atom_in_xplor(compId, _atomId_)[0]
                                if len(_atomId) > 0:
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId[0]), None)
                                    if cca is not None:
                                        self.__col_order_of_dist_w_chain['atom_id_1'] = k
                                        self.__col_order_of_dist_w_chain['chain_id_1'] = 3 - (j + k)
                                        break
                for j in range(3, 6):
                    if len(jVal[j]) > 2 and translateToStdResName(jVal[j]) in monDict3:
                        self.__col_order_of_dist_w_chain['comp_id_2'] = j
                        compId = jVal[j]
                        if self.__ccU.updateChemCompDict(compId):
                            for k in range(3, 6):
                                if k == j:
                                    continue
                                atomId = jVal[k]
                                _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                if details is not None and len(atomId) > 1:
                                    _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId[:-1], leave_unmatched=True)

                                if details is not None:
                                    _atomId_ = translateToStdAtomName(atomId, compId, ccU=self.__ccU)
                                    if _atomId_ != atomId:
                                        _atomId = self.__nefT.get_valid_star_atom_in_xplor(compId, _atomId_)[0]
                                if len(_atomId) > 0:
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId[0]), None)
                                    if cca is not None:
                                        self.__col_order_of_dist_w_chain['atom_id_2'] = k
                                        self.__col_order_of_dist_w_chain['chain_id_2'] = 12 - (j + k)
                                        break

            if len(self.__col_order_of_dist_w_chain) != 6:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Failed to identify columns for comp_id_1, atom_id_1, chain_id_1, comp_id_2, atom_id_2, chain_id_2.\n"
                self.distRestraints -= 1
                return

            if None in self.numberSelection:
                self.distRestraints -= 1
                return

            target_value = None
            lower_limit = None
            upper_limit = None

            value = self.numberSelection[0]
            weight = 1.0

            delta = None
            has_square = False

            if len(self.numberSelection) > 2:
                value2 = self.numberSelection[1]
                weight = self.numberSelection[2]

                has_square = True

            elif len(self.numberSelection) > 1:
                value2 = self.numberSelection[1]

                if value2 <= 1.0 or value2 < value:
                    delta = abs(value2)
                else:
                    has_square = True

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX and not self.__cur_subtype_altered:
                if self.__max_dist_value is None:
                    self.__max_dist_value = value
                if value > self.__max_dist_value:
                    self.__max_dist_value = value

            if has_square:
                if value2 > DIST_RANGE_MAX:  # lol_only
                    lower_limit = value

                elif 1.8 <= value <= DIST_ERROR_MAX and DIST_RANGE_MIN <= value2 <= DIST_RANGE_MAX:
                    upper_limit = value2
                    lower_limit = value
                    target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

                else:  # upl_only
                    if value2 > 1.8:
                        upper_limit = value2
                        lower_limit = 1.8  # default value of PDBStat
                        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                    else:
                        upper_limit = value2

            elif delta is not None:
                target_value = value
                lower_limit = value - delta
                upper_limit = value + delta

            elif self.__upl_or_lol is None or self.__upl_or_lol == 'upl_only':
                if value > 1.8:
                    upper_limit = value
                    lower_limit = 1.8  # default value of PDBStat
                    target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
                else:
                    lower_limit = value

            elif self.__upl_or_lol == 'upl_w_lol':
                upper_limit = value

            elif self.__upl_or_lol == 'lol_only':
                lower_limit = value
                upper_limit = 5.5  # default value of PDBStat
                target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

            else:  # 'lol_w_upl'
                lower_limit = value

            if not self.__hasPolySeq:  # can't decide whether NOE or RDC wo the coordinates
                return

            chainId1 = jVal[self.__col_order_of_dist_w_chain['chain_id_1']]
            chainId2 = jVal[self.__col_order_of_dist_w_chain['chain_id_2']]
            compId1 = jVal[self.__col_order_of_dist_w_chain['comp_id_1']]
            compId2 = jVal[self.__col_order_of_dist_w_chain['comp_id_2']]
            atomId1 = jVal[self.__col_order_of_dist_w_chain['atom_id_1']]
            atomId2 = jVal[self.__col_order_of_dist_w_chain['atom_id_2']]

            chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

            if len(self.atomSelectionSet) < 2:
                return

            if len(self.atomSelectionSet[0]) == 1 and len(self.atomSelectionSet[1]) == 1:

                isRdc = True

                chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
                seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
                comp_id_1 = self.atomSelectionSet[0][0]['comp_id']
                atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

                chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
                seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
                comp_id_2 = self.atomSelectionSet[1][0]['comp_id']
                atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

                if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                    isRdc = False

                if chain_id_1 != chain_id_2:
                    isRdc = False

                if abs(seq_id_1 - seq_id_2) > 1:
                    isRdc = False

                if abs(seq_id_1 - seq_id_2) == 1:

                    if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                            ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                             or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                        pass

                    else:
                        isRdc = False

                elif atom_id_1 == atom_id_2:
                    isRdc = False

                elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                    if not any(b for b in self.__ccU.lastBonds
                               if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                                   or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                        if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                            isRdc = False

                if not isRdc:
                    self.__cur_subtype_altered = False

                else:

                    isRdc = False

                    if self.__cur_subtype_altered and atom_id_1 + atom_id_2 == self.auxAtomSelectionSet:
                        isRdc = True

                    elif value < 1.0 or value > 6.0:
                        self.auxAtomSelectionSet = atom_id_1 + atom_id_2
                        self.__cur_subtype_altered = True
                        self.__cur_rdc_orientation += 1
                        isRdc = True

                    if isRdc:
                        self.__cur_subtype = 'rdc'
                        self.rdcRestraints += 1
                        self.distRestraints -= 1

                        target_value = value
                        lower_limit = upper_limit = None

                        if len(self.numberSelection) > 2:
                            error = abs(self.numberSelection[1])
                            lower_limit = target_value - error
                            upper_limit = target_value + error

                        dstFunc = self.validateRdcRange(weight, self.__cur_rdc_orientation, target_value, lower_limit, upper_limit)

                        if dstFunc is None:
                            return

                        for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                              self.atomSelectionSet[1]):
                            if isLongRangeRestraint([atom1, atom2]):
                                continue
                            if self.__debug:
                                print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                                      f"atom1={atom1} atom2={atom2} {dstFunc}")

                        self.__cur_subtype = 'dist'

                        return

            dstFunc = self.validateDistanceRange(weight, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

            if dstFunc is None:
                return

            chainAssign1 = self.assignCoordPolymerSequenceWithChainId(chainId1, seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequenceWithChainId(chainId2, seqId2, compId2, atomId2)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

            if len(self.atomSelectionSet) < 2:
                return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        except ValueError:
            self.distRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CyanaMRParser#distance_w_chain2_restraints.
    def enterDistance_w_chain2_restraints(self, ctx: CyanaMRParser.Distance_w_chain2_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

        self.__col_order_of_dist_w_chain = {}

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#distance_w_chain2_restraints.
    def exitDistance_w_chain2_restraints(self, ctx: CyanaMRParser.Distance_w_chain2_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#distance_w_chain2_restraint.
    def enterDistance_w_chain2_restraint(self, ctx: CyanaMRParser.Distance_w_chain2_restraintContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#distance_w_chain2_restraint.
    def exitDistance_w_chain2_restraint(self, ctx: CyanaMRParser.Distance_w_chain2_restraintContext):
        self.exitDistance_w_chain_restraint(ctx)

    # Enter a parse tree produced by CyanaMRParser#distance_w_chain3_restraints.
    def enterDistance_w_chain3_restraints(self, ctx: CyanaMRParser.Distance_w_chain3_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

        self.__col_order_of_dist_w_chain = {}

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#distance_w_chain3_restraints.
    def exitDistance_w_chain3_restraints(self, ctx: CyanaMRParser.Distance_w_chain3_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#distance_w_chain3_restraint.
    def enterDistance_w_chain3_restraint(self, ctx: CyanaMRParser.Distance_w_chain3_restraintContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#distance_w_chain3_restraint.
    def exitDistance_w_chain3_restraint(self, ctx: CyanaMRParser.Distance_w_chain3_restraintContext):
        self.exitDistance_w_chain_restraint(ctx)

    # Enter a parse tree produced by CyanaMRParser#cco_restraints.
    def enterCco_restraints(self, ctx: CyanaMRParser.Cco_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'jcoup'

        self.__cur_subtype_altered = False

    # Exit a parse tree produced by CyanaMRParser#cco_restraints.
    def exitCco_restraints(self, ctx: CyanaMRParser.Cco_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#cco_restraint.
    def enterCco_restraint(self, ctx: CyanaMRParser.Cco_restraintContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#cco_restraint.
    def exitCco_restraint(self, ctx: CyanaMRParser.Cco_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer()))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            atomId2 = str(ctx.Simple_name(2)).upper()

            if None in self.numberSelection:
                self.jcoupRestraints -= 1
                return

            if atomId2 in KNOWN_ANGLE_NAMES:
                self.__cur_subtype_altered = True
                self.__cur_subtype = 'dihed'
                self.dihedRestraints += 1
                self.jcoupRestraints -= 1
                self.exitTorsion_angle_restraint(ctx)
                return

            target = self.numberSelection[0]
            error = None

            weight = 1.0
            if len(self.numberSelection) > 2:
                error = abs(self.numberSelection[1])
                weight = self.numberSelection[2]

            elif len(self.numberSelection) > 1:
                error = abs(self.numberSelection[1])

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            target_value = target
            lower_limit = target - error if error is not None else None
            upper_limit = target + error if error is not None else None

            dstFunc = self.validateRdcRange(weight, None, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(seqId1, compId1, atomId2)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
            self.selectCoordAtoms(chainAssign2, seqId1, compId1, atomId2)

            if len(self.atomSelectionSet) < 2:
                return

            if not self.areUniqueCoordAtoms('a Scalar coupling'):
                return

            chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
            seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
            comp_id_1 = self.atomSelectionSet[0][0]['comp_id']
            atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

            chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
            seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
            comp_id_2 = self.atomSelectionSet[1][0]['comp_id']
            atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

            if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Non-magnetic susceptible spin appears in scalar coupling constant; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if chain_id_1 != chain_id_2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found inter-chain scalar coupling constant; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if abs(seq_id_1 - seq_id_2) > 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found inter-residue scalar coupling constant; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if abs(seq_id_1 - seq_id_2) == 1:

                if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                        ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                         or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                    pass

                else:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found inter-residue scalar coupling constant; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif atom_id_1 == atom_id_2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Found zero scalar coupling constant; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if isLongRangeRestraint([atom1, atom2]):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.jcoupRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        except ValueError:
            self.jcoupRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CyanaMRParser#ssbond_macro.
    def enterSsbond_macro(self, ctx: CyanaMRParser.Ssbond_macroContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'geo'

    # Exit a parse tree produced by CyanaMRParser#ssbond_macro.
    def exitSsbond_macro(self, ctx: CyanaMRParser.Ssbond_macroContext):
        self.geoRestraints += 1

        try:
            seqId1, seqId2 = str(ctx.Ssbond_resids()).split('-')
        except ValueError:
            self.geoRestraints -= 1
            return

        if not self.__hasPolySeq:
            return

        compId = 'CYSS'
        atomId = 'SG'

        chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId, atomId)
        chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId, atomId)

        if len(chainAssign1) == 0 or len(chainAssign2) == 0:
            return

        self.selectCoordAtoms(chainAssign1, seqId1, compId, atomId)
        self.selectCoordAtoms(chainAssign2, seqId2, compId, atomId)

        if len(self.atomSelectionSet) < 2:
            return

        for atom1 in self.atomSelectionSet[0]:
            if atom1['comp_id'] != 'CYS':
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint()}"\
                    f"Failed to select a Cystein residue for disulfide bond between '{seqId1}' and '{seqId2}'.\n"
                self.geoRestraints -= 1
                return

        for atom2 in self.atomSelectionSet[1]:
            if atom2['comp_id'] != 'CYS':
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint()}"\
                    f"Failed to select a Cystein residue for disulfide bond between '{seqId1}' and '{seqId2}'.\n"
                self.geoRestraints -= 1
                return

        chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
        seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
        atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

        chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
        seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
        atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

        try:

            _head =\
                self.__cR.getDictListWithFilter('atom_site',
                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                 ],
                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chain_id_1},
                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seq_id_1},
                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atom_id_1},
                                                 {'name': self.__modelNumName, 'type': 'int',
                                                  'value': self.__representativeModelId},
                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                  'enum': ('A')}
                                                 ])

            _tail =\
                self.__cR.getDictListWithFilter('atom_site',
                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                 ],
                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chain_id_2},
                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seq_id_2},
                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atom_id_2},
                                                 {'name': self.__modelNumName, 'type': 'int',
                                                  'value': self.__representativeModelId},
                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                  'enum': ('A')}
                                                 ])

            if len(_head) == 1 and len(_tail) == 1:
                distance = numpy.linalg.norm(toNpArray(_head[0]) - toNpArray(_tail[0]))
                if distance > 2.4:
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The distance of the disulfide bond linkage ({chain_id_1}:{seq_id_1}:{atom_id_1} - "\
                        f"{chain_id_2}:{seq_id_2}:{atom_id_2}) is too far apart in the coordinates ({distance:.3f}Å).\n"

        except Exception as e:
            if self.__verbose:
                self.__lfh.write(f"+CyanaMRParserListener.exitSsbond_macro() ++ Error  - {str(e)}\n")

        for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                              self.atomSelectionSet[1]):
            if self.__debug:
                print(f"subtype={self.__cur_subtype} (CYANA macro: disulfide bond linkage) id={self.geoRestraints} "
                      f"atom1={atom1} atom2={atom2}")

    # Enter a parse tree produced by CyanaMRParser#hbond_macro.
    def enterHbond_macro(self, ctx: CyanaMRParser.Hbond_macroContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'hbond'

    # Exit a parse tree produced by CyanaMRParser#hbond_macro.
    def exitHbond_macro(self, ctx: CyanaMRParser.Hbond_macroContext):
        self.hbondRestraints += 1

        seqId1 = int(str(ctx.Integer_HB(0)))
        seqId2 = int(str(ctx.Integer_HB(1)))
        atomId1 = str(ctx.Simple_name_HB(0))
        atomId2 = str(ctx.Simple_name_HB(1))

        if not self.__hasPolySeq:
            return

        chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(seqId1, atomId1)
        chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(seqId2, atomId2)

        if len(chainAssign1) == 0 or len(chainAssign2) == 0:
            return

        self.selectCoordAtoms(chainAssign1, seqId1, None, atomId1)
        self.selectCoordAtoms(chainAssign2, seqId2, None, atomId2)

        if len(self.atomSelectionSet) < 2:
            return

        if not self.areUniqueCoordAtoms('a hydrogen bond linkage'):
            return

        chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
        seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
        atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

        chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
        seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
        atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

        try:

            _head =\
                self.__cR.getDictListWithFilter('atom_site',
                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                 ],
                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chain_id_1},
                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seq_id_1},
                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atom_id_1},
                                                 {'name': self.__modelNumName, 'type': 'int',
                                                  'value': self.__representativeModelId},
                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                  'enum': ('A')}
                                                 ])

            _tail =\
                self.__cR.getDictListWithFilter('atom_site',
                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                 ],
                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chain_id_2},
                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seq_id_2},
                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atom_id_2},
                                                 {'name': self.__modelNumName, 'type': 'int',
                                                  'value': self.__representativeModelId},
                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                  'enum': ('A')}
                                                 ])

            if len(_head) == 1 and len(_tail) == 1:
                distance = numpy.linalg.norm(toNpArray(_head[0]) - toNpArray(_tail[0]))
                if distance > (3.4 if atom_id_1[0] != 'H' and atom_id_2[0] != 'H' else 2.4):
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The distance of the hydrogen bond linkage ({chain_id_1}:{seq_id_1}:{atom_id_1} - "\
                        f"{chain_id_2}:{seq_id_2}:{atom_id_2}) is too far apart in the coordinates ({distance:.3f}Å).\n"

        except Exception as e:
            if self.__verbose:
                self.__lfh.write(f"+CyanaMRParserListener.exitHbond_macro() ++ Error  - {str(e)}\n")

        for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                              self.atomSelectionSet[1]):
            if self.__debug:
                print(f"subtype={self.__cur_subtype} (CYANA macro: hydrogen bond linkage) id={self.hbondRestraints} "
                      f"atom1={atom1} atom2={atom2}")

    # Enter a parse tree produced by CyanaMRParser#link_statement.
    def enterLink_statement(self, ctx: CyanaMRParser.Link_statementContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'geo'

    # Exit a parse tree produced by CyanaMRParser#link_statement.
    def exitLink_statement(self, ctx: CyanaMRParser.Link_statementContext):
        self.geoRestraints += 1

        seqId1 = int(str(ctx.Integer(0)))
        seqId2 = int(str(ctx.Integer(1)))
        atomId1 = str(ctx.Simple_name(0))
        atomId2 = str(ctx.Simple_name(1))

        if not self.__hasPolySeq:
            return

        chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(seqId1, atomId1)
        chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(seqId2, atomId2)

        if len(chainAssign1) == 0 or len(chainAssign2) == 0:
            return

        self.selectCoordAtoms(chainAssign1, seqId1, None, atomId1)
        self.selectCoordAtoms(chainAssign2, seqId2, None, atomId2)

        if len(self.atomSelectionSet) < 2:
            return

        if not self.areUniqueCoordAtoms('a covalent bond linkage'):
            return

        chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
        seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
        atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

        chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
        seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
        atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

        try:

            _head =\
                self.__cR.getDictListWithFilter('atom_site',
                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                 ],
                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chain_id_1},
                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seq_id_1},
                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atom_id_1},
                                                 {'name': self.__modelNumName, 'type': 'int',
                                                  'value': self.__representativeModelId},
                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                  'enum': ('A')}
                                                 ])

            _tail =\
                self.__cR.getDictListWithFilter('atom_site',
                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                 ],
                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chain_id_2},
                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seq_id_2},
                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atom_id_2},
                                                 {'name': self.__modelNumName, 'type': 'int',
                                                  'value': self.__representativeModelId},
                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                  'enum': ('A')}
                                                 ])

            if len(_head) == 1 and len(_tail) == 1:
                distance = numpy.linalg.norm(toNpArray(_head[0]) - toNpArray(_tail[0]))
                if distance > (3.4 if atom_id_1[0] != 'H' and atom_id_2[0] != 'H' else 2.4):
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The distance of the covalent bond linkage ({chain_id_1}:{seq_id_1}:{atom_id_1} - "\
                        f"{chain_id_2}:{seq_id_2}:{atom_id_2}) is too far apart in the coordinates ({distance:.3f}Å).\n"

        except Exception as e:
            if self.__verbose:
                self.__lfh.write(f"+CyanaMRParserListener.exitLink_statement() ++ Error  - {str(e)}\n")

        for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                              self.atomSelectionSet[1]):
            if self.__debug:
                print(f"subtype={self.__cur_subtype} (CYANA statement: covalent bond linkage) id={self.geoRestraints} "
                      f"atom1={atom1} atom2={atom2}")

    # Enter a parse tree produced by CyanaMRParser#unambig_atom_name_mapping.
    def enterUnambig_atom_name_mapping(self, ctx: CyanaMRParser.Unambig_atom_name_mappingContext):
        self.__cur_resname_for_mapping = str(ctx.Simple_name()).upper()

    # Exit a parse tree produced by CyanaMRParser#unambig_atom_name_mapping.
    def exitUnambig_atom_name_mapping(self, ctx: CyanaMRParser.Unambig_atom_name_mappingContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#mapping_list.
    def enterMapping_list(self, ctx: CyanaMRParser.Mapping_listContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CyanaMRParser#mapping_list.
    def exitMapping_list(self, ctx: CyanaMRParser.Mapping_listContext):
        atomName = str(ctx.Simple_name_MP(0)).upper()
        iupacName = set()

        i = 1
        while ctx.Simple_name_MP(i):
            iupacName.add(str(ctx.Simple_name_MP(i)).upper())
            i += 1

        if self.__cur_resname_for_mapping not in self.unambigAtomNameMapping:
            self.unambigAtomNameMapping[self.__cur_resname_for_mapping] = {}
        self.unambigAtomNameMapping[self.__cur_resname_for_mapping][atomName] = list(iupacName)

    # Enter a parse tree produced by CyanaMRParser#ambig_atom_name_mapping.
    def enterAmbig_atom_name_mapping(self, ctx: CyanaMRParser.Ambig_atom_name_mappingContext):
        self.__cur_resname_for_mapping = str(ctx.Simple_name()).upper()

    # Exit a parse tree produced by CyanaMRParser#ambig_atom_name_mapping.
    def exitAmbig_atom_name_mapping(self, ctx: CyanaMRParser.Ambig_atom_name_mappingContext):  # pylint: disable=unused-argument
        self.updateAmbigAtomNameMapping()

    # Enter a parse tree produced by CyanaMRParser#ambig_list.
    def enterAmbig_list(self, ctx: CyanaMRParser.Ambig_listContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CyanaMRParser#ambig_list.
    def exitAmbig_list(self, ctx: CyanaMRParser.Ambig_listContext):
        if ctx.Ambig_code_MP():
            ambigCode = str(ctx.Ambig_code_MP())
            i = 0
        else:
            ambigCode = str(ctx.Simple_name_MP(0)).upper()
            i = 1

        mapName = []

        j = 0
        while ctx.Simple_name_MP(i):
            mapName.append({'atom_name': str(ctx.Simple_name_MP(i)).upper(),
                            'seq_id': int(str(ctx.Integer_MP(j)))})
            i += 1
            j += 1

        if self.__cur_resname_for_mapping not in self.ambigAtomNameMapping:
            self.ambigAtomNameMapping[self.__cur_resname_for_mapping] = {}
        self.ambigAtomNameMapping[self.__cur_resname_for_mapping][ambigCode] = mapName

    def updateAmbigAtomNameMapping(self):
        if not self.__hasPolySeq or len(self.ambigAtomNameMapping) == 0:
            return

        unambigResidues = None
        if len(self.unambigAtomNameMapping) > 0:
            unambigResidues = [translateToStdResName(residue) for residue in self.unambigAtomNameMapping.keys()]

        for ambigDict in self.ambigAtomNameMapping.values():
            for ambigList in ambigDict.values():
                for ambig in ambigList:

                    if 'atom_id_list' in ambig:
                        continue

                    atomName = ambig['atom_name']
                    seqId = ambig['seq_id']

                    chainAssign = self.assignCoordPolymerSequenceWithoutCompId(seqId)

                    if len(chainAssign) == 0:
                        continue

                    ambig['atom_id_list'] = []

                    for cifChainId, cifSeqId, cifCompId in chainAssign:

                        has_unambig = False

                        if unambigResidues is not None and cifCompId in unambigResidues:

                            unambigMap = next(v for k, v in self.unambigAtomNameMapping.items()
                                              if translateToStdResName(k) == cifCompId)

                            if atomName in unambigMap:

                                for cifAtomId in unambigMap[atomName]:
                                    ambig['atom_id_list'].append({'chain_id': cifChainId,
                                                                  'seq_id': cifSeqId,
                                                                  'comp_id': cifCompId,
                                                                  'atom_id': cifAtomId})

                                has_unambig = True

                        if has_unambig:
                            continue

                        self.atomSelectionSet.clear()

                        self.selectCoordAtoms(chainAssign, seqId, None, ambig['atom_name'].upper(), enableWarning=False)

                        if len(self.atomSelectionSet[0]) > 0:
                            ambig['atom_id_list'].extend(self.atomSelectionSet[0])
                            continue

                        _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomName, leave_unmatched=True)
                        if details is not None and len(atomName) > 1:
                            _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomName[:-1], leave_unmatched=True)

                        if details is not None:
                            _atomId_ = translateToStdAtomName(atomName, cifCompId, ccU=self.__ccU)
                            if _atomId_ != atomName:
                                _atomId = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, _atomId_)[0]

                        for cifAtomId in _atomId:
                            ambig['atom_id_list'].append({'chain_id': cifChainId,
                                                          'seq_id': cifSeqId,
                                                          'comp_id': cifCompId,
                                                          'atom_id': cifAtomId})

                    ambig['atom_id_list'] = [dict(s) for s in set(frozenset(atom.items()) for atom in ambig['atom_id_list'])]

    def atomIdListToChainAssign(self, atomIdList):  # pylint: disable=no-self-use
        chainAssign = set()
        for item in atomIdList:
            if 'atom_id_list' in item:
                for atom_id in item['atom_id_list']:
                    chainAssign.add((atom_id['chain_id'], atom_id['seq_id'], atom_id['comp_id']))
        return list(chainAssign)

    def atomIdListToAtomSelection(self, atomIdList):  # pylint: disable=no-self-use
        atomSelection = []
        for item in atomIdList:
            if 'atom_id_list' in item:
                for atom_id in item['atom_id_list']:
                    if atom_id not in atomSelection:
                        atomSelection.append(atom_id)
        return atomSelection

    # Enter a parse tree produced by CyanaMRParser#number.
    def enterNumber(self, ctx: CyanaMRParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CyanaMRParser#number.
    def exitNumber(self, ctx: CyanaMRParser.NumberContext):
        if ctx.Float():
            self.numberSelection.append(float(str(ctx.Float())))

        elif ctx.Integer():
            self.numberSelection.append(float(str(ctx.Integer())))

        else:
            self.numberSelection.append(None)

    # Enter a parse tree produced by CyanaMRParser#gen_atom_name.
    def enterGen_atom_name(self, ctx: CyanaMRParser.Gen_atom_nameContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CyanaMRParser#gen_atom_name.
    def exitGen_atom_name(self, ctx: CyanaMRParser.Gen_atom_nameContext):
        if ctx.Simple_name():
            self.genAtomNameSelection.append(str(ctx.Simple_name()))

        elif ctx.Ambig_code():
            self.genAtomNameSelection.append(str(ctx.Ambig_code()))

        else:
            self.genAtomNameSelection.append(None)

    def __getCurrentRestraint(self):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints] "
        if self.__cur_subtype == 'dihed':
            return f"[Check the {self.dihedRestraints}th row of torsion angle restraints] "
        if self.__cur_subtype == 'rdc':
            return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
        if self.__cur_subtype == 'pcs':
            return f"[Check the {self.pcsRestraints}th row of pseudocontact shift restraints] "
        if self.__cur_subtype == 'noepk':
            return f"[Check the {self.noepkRestraints}th row of NOESY volume restraints] "
        if self.__cur_subtype == 'jcoup':
            return f"[Check the {self.jcoupRestraints}th row of scalar coupling constant restraints] "
        if self.__cur_subtype == 'geo':
            return f"[Check the {self.geoRestraints}th row of coordinate geometry restraints] "
        if self.__cur_subtype == 'hbond':
            return f"[Check the {self.geoRestraints}th row of hydrogen bond restraints] "
        return ''

    def getContentSubtype(self):
        """ Return content subtype of CYANA MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'pcs_restraint': self.pcsRestraints,
                          'noepk_restraint': self.noepkRestraints,
                          'jcoup_restraint': self.jcoupRestraints,
                          'geo_restraint': self.geoRestraints,
                          'hbond_restraint': self.hbondRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getEffectiveContentSubtype(self):
        """ Return effective content subtype of CYANA MR file (excluding .upv, lov, and .cco).
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'pcs_restraint': self.pcsRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of CYANA MR file.
        """
        return self.__polySeqRst

    def getSequenceAlignment(self):
        """ Return sequence alignment between coordinates and CYANA MR.
        """
        return self.__seqAlign

    def getChainAssignment(self):
        """ Return chain assignment between coordinates and CYANA MR.
        """
        return self.__chainAssign

    def getReasonsForReparsing(self):
        """ Return reasons for re-parsing CYANA MR file.
        """
        return self.reasonsForReParsing

    def isUplDistanceRestraint(self):
        """ Return whether CYANA MR file contains upper limit distance restraints.
        """
        if self.__max_dist_value is None:
            return None
        return self.__max_dist_value > 3.5

# del CyanaMRParser
