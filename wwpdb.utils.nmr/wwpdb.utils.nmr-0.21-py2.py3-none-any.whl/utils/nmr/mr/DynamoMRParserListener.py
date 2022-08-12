##
# File: DynamoMRParserListener.py
# Date: 17-Jun-2022
#
# Updates:
# Generated from DynamoMRParser.g4 by ANTLR 4.10.1
""" ParserLister class for DYNAMO/PALES/TALOS MR files.
    @author: Masashi Yokochi
"""
import sys
import itertools

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from wwpdb.utils.nmr.mr.DynamoMRParser import DynamoMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (checkCoordinates,
                                                       isLongRangeRestraint,
                                                       getTypeOfDihedralRestraint,
                                                       translateToStdResName,
                                                       translateToStdAtomName,
                                                       isCyclicPolymer,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR,
                                                       KNOWN_ANGLE_ATOM_NAMES,
                                                       KNOWN_ANGLE_SEQ_OFFSET)
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
    from nmr.mr.DynamoMRParser import DynamoMRParser
    from nmr.mr.ParserListenerUtil import (checkCoordinates,
                                           isLongRangeRestraint,
                                           getTypeOfDihedralRestraint,
                                           translateToStdResName,
                                           translateToStdAtomName,
                                           isCyclicPolymer,
                                           REPRESENTATIVE_MODEL_ID,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR,
                                           KNOWN_ANGLE_ATOM_NAMES,
                                           KNOWN_ANGLE_SEQ_OFFSET)
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


TALOS_PREDICTION_CLASSES = ('Strong', 'Good', 'Generous', 'Warn', 'Bad', 'Dyn', 'None')
TALOS_PREDICTION_MIN_CLASSES = ('Strong', 'Good')


# This class defines a complete listener for a parse tree produced by DynamoMRParser.
class DynamoMRParserListener(ParseTreeListener):

    # __verbose = None
    # __lfh = None
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

    # CIF reader
    __cR = None
    __hasCoord = False

    # data item name for model ID in 'atom_site' category
    __modelNumName = None

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    # __authAsymId = None
    # __authSeqId = None
    # __authAtomId = None
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

    __first_resid = 1
    __cur_sequence = ''
    __open_sequence = False
    __has_sequence = False
    __has_seq_align_err = False

    # collection of atom selection
    atomSelectionSet = []

    # collection of auxiliary atom selection
    auxAtomSelectionSet = []

    # collection of number selection
    numberSelection = []

    warningMessage = ''

    reasonsForReParsing = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 mrAtomNameMapping=None,
                 cR=None, cC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        # self.__verbose = verbose
        # self.__lfh = log

        self.__representativeModelId = representativeModelId
        self.__mrAtomNameMapping = None if mrAtomNameMapping is None or len(mrAtomNameMapping) == 0 else mrAtomNameMapping

        self.__cR = cR
        self.__hasCoord = cR is not None

        if self.__hasCoord:
            ret = checkCoordinates(verbose, log, representativeModelId, cR, cC)
            self.__modelNumName = ret['model_num_name']
            # self.__authAsymId = ret['auth_asym_id']
            # self.__authSeqId = ret['auth_seq_id']
            # self.__authAtomId = ret['auth_atom_id']
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

        self.distRestraints = 0      # DYNAMO: Distance restraints
        self.dihedRestraints = 0     # DYNAMO/TALOS: Torsion angle restraints
        self.rdcRestraints = 0       # DYNAMO/PALES: Residual dipolar coupling restraints
        self.jcoupRestraints = 0     # DYNAMO: Scalar coupling constant restraints

    def setDebugMode(self, debug):
        self.__debug = debug

    # Enter a parse tree produced by DynamoMRParser#dynamo_mr.
    def enterDynamo_mr(self, ctx: DynamoMRParser.Dynamo_mrContext):  # pylint: disable=unused-argument
        self.__chainNumberDict = {}
        self.__polySeqRst = []

    # Exit a parse tree produced by DynamoMRParser#dynamo_mr.
    def exitDynamo_mr(self, ctx: DynamoMRParser.Dynamo_mrContext):  # pylint: disable=unused-argument
        if self.__hasPolySeq and self.__polySeqRst is not None:
            sortPolySeqRst(self.__polySeqRst)

            file_type = 'nm-res-dyn'

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

        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]
            self.warningMessage = '\n'.join(set(self.warningMessage.split('\n')))

    # Enter a parse tree produced by DynamoMRParser#sequence.
    def enterSequence(self, ctx: DynamoMRParser.SequenceContext):
        if self.__has_sequence and not self.__open_sequence:
            self.__first_resid = 1
            self.__cur_sequence = ''

        if ctx.First_resid():
            self.__first_resid = int(str(ctx.Integer_DA()))

        if ctx.Sequence():
            i = 0
            while ctx.One_letter_code(i):
                self.__cur_sequence += str(ctx.One_letter_code(i))
                i += 1

        self.__open_sequence = True

    # Exit a parse tree produced by DynamoMRParser#sequence.
    def exitSequence(self, ctx: DynamoMRParser.SequenceContext):  # pylint: disable=unused-argument
        pass

    def closeSequqnce(self):
        self.__has_seq_align_err = False

        if not self.__open_sequence:
            return

        self.__has_sequence = len(self.__cur_sequence) > 0

        self.__open_sequence = False

    # Enter a parse tree produced by DynamoMRParser#distance_restraints.
    def enterDistance_restraints(self, ctx: DynamoMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#distance_restraints.
    def exitDistance_restraints(self, ctx: DynamoMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: DynamoMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: DynamoMRParser.Distance_restraintContext):

        try:

            index = int(str(ctx.Integer(0)))
            group = int(str(ctx.Integer(1)))

            seqId1 = int(str(ctx.Integer(2)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(3)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()

            target_value = None
            lower_limit = None
            upper_limit = None

            if None in self.numberSelection:
                return

            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]
            weight = self.numberSelection[3]
            scale = self.numberSelection[4]

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            if scale < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' must not be a negative value.\n"
                return
            if scale == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' should be a positive value.\n"

            dstFunc = self.validateDistanceRange(index, group, weight, scale, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1, index, group)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2, index, group)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, True, index, group)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, True, index, group)

            if len(self.atomSelectionSet) < 2:
                return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} (index={index}, group={group}) "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        except ValueError:
            self.distRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by DynamoMRParser#distance_restraints_sw_segid.
    def enterDistance_restraints_sw_segid(self, ctx: DynamoMRParser.Distance_restraints_sw_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#distance_restraints_sw_segid.
    def exitDistance_restraints_sw_segid(self, ctx: DynamoMRParser.Distance_restraints_sw_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#distance_restraint_sw_segid.
    def enterDistance_restraint_sw_segid(self, ctx: DynamoMRParser.Distance_restraint_sw_segidContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#distance_restraint_sw_segid.
    def exitDistance_restraint_sw_segid(self, ctx: DynamoMRParser.Distance_restraint_sw_segidContext):

        try:

            index = int(str(ctx.Integer(0)))
            group = int(str(ctx.Integer(1)))

            chainId1 = str(ctx.Simple_name(0))
            seqId1 = int(str(ctx.Integer(2)))
            compId1 = str(ctx.Simple_name(1)).upper()
            atomId1 = str(ctx.Simple_name(2)).upper()
            chainId2 = str(ctx.Simple_name(3))
            seqId2 = int(str(ctx.Integer(3)))
            compId2 = str(ctx.Simple_name(4)).upper()
            atomId2 = str(ctx.Simple_name(5)).upper()

            target_value = None
            lower_limit = None
            upper_limit = None

            if None in self.numberSelection:
                return

            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]
            weight = self.numberSelection[3]
            scale = self.numberSelection[4]

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            if scale < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' must not be a negative value.\n"
                return
            if scale == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' should be a positive value.\n"

            dstFunc = self.validateDistanceRange(index, group, weight, scale, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index, group)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index, group)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, True, index, group)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, True, index, group)

            if len(self.atomSelectionSet) < 2:
                return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} (index={index}, group={group}) "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        except ValueError:
            self.distRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by DynamoMRParser#distance_restraints_ew_segid.
    def enterDistance_restraints_ew_segid(self, ctx: DynamoMRParser.Distance_restraints_ew_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#distance_restraints_ew_segid.
    def exitDistance_restraints_ew_segid(self, ctx: DynamoMRParser.Distance_restraints_ew_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#distance_restraint_ew_segid.
    def enterDistance_restraint_ew_segid(self, ctx: DynamoMRParser.Distance_restraint_ew_segidContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#distance_restraint_ew_segid.
    def exitDistance_restraint_ew_segid(self, ctx: DynamoMRParser.Distance_restraint_ew_segidContext):

        try:

            index = int(str(ctx.Integer(0)))
            group = int(str(ctx.Integer(1)))

            seqId1 = int(str(ctx.Integer(2)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            chainId1 = str(ctx.Simple_name(2))
            chainId2 = str(ctx.Simple_name(5))
            seqId2 = int(str(ctx.Integer(3)))
            compId2 = str(ctx.Simple_name(3)).upper()
            atomId2 = str(ctx.Simple_name(4)).upper()
            chainId2 = str(ctx.Simple_name(5))

            target_value = None
            lower_limit = None
            upper_limit = None

            if None in self.numberSelection:
                return

            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]
            weight = self.numberSelection[3]
            scale = self.numberSelection[4]

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            if scale < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' must not be a negative value.\n"
                return
            if scale == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' should be a positive value.\n"

            dstFunc = self.validateDistanceRange(index, group, weight, scale, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index, group)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index, group)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, True, index, group)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, True, index, group)

            if len(self.atomSelectionSet) < 2:
                return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} (index={index}, group={group}) "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        except ValueError:
            self.distRestraints -= 1
        finally:
            self.numberSelection.clear()

    def validateDistanceRange(self, index, group, weight, scale, target_value, lower_limit, upper_limit, omit_dist_limit_outlier):
        """ Validate distance value range.
        """

        validRange = True
        dstFunc = {'weight': weight, 'scale': scale}

        if target_value is not None:
            if DIST_ERROR_MIN < target_value < DIST_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                if target_value <= DIST_ERROR_MIN and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The target value='{target_value:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    target_value = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The target value='{target_value:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if DIST_ERROR_MIN <= lower_limit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                if lower_limit <= DIST_ERROR_MIN and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The lower limit value='{lower_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    lower_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The lower limit value='{lower_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if DIST_ERROR_MIN < upper_limit <= DIST_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                if upper_limit > DIST_ERROR_MAX and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The upper limit value='{upper_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    upper_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The upper limit value='{upper_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the target value '{target_value:.3f}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The upper limit value='{upper_limit:.3f}' must be greater than the target value '{target_value:.3f}'.\n"

        else:

            if lower_limit is not None and upper_limit is not None:
                if lower_limit > upper_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the upper limit value '{upper_limit:.3f}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if DIST_RANGE_MIN <= target_value <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The target value='{target_value:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if DIST_RANGE_MIN <= lower_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if DIST_RANGE_MIN <= upper_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        return dstFunc

    def getRealChainSeqId(self, ps, seqId, compId, isPolySeq=True):
        compId = translateToStdResName(compId)
        if self.__reasons is not None and 'label_seq_scheme' in self.__reasons and self.__reasons['label_seq_scheme']:
            seqKey = (ps['chain_id' if isPolySeq else 'auth_chain_id'], seqId)
            if seqKey in self.__labelToAuthSeq:
                _chainId, _seqId = self.__labelToAuthSeq[seqKey]
                if _seqId in ps['auth_seq_id']:
                    return _chainId, _seqId
        if seqId in ps['auth_seq_id']:
            idx = ps['auth_seq_id'].index(seqId)
            if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                return ps['auth_chain_id'], seqId
        if seqId in ps['seq_id']:
            idx = ps['seq_id'].index(seqId)
            if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                return ps['auth_chain_id'], ps['auth_seq_id'][idx]
        return ps['chain_id' if isPolySeq else 'auth_chain_id'], seqId

    def assignCoordPolymerSequence(self, refChainId, seqId, compId, atomId, index=None, group=None):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = []

        if self.__has_sequence and self.__reasons is None:
            # """
            # if seqId < self.__first_resid:
            #     self.warningMessage += f"[Sequence mismatch] {self.__getCurrentRestraint()}"\
            #         f"The residue number '{seqId}' must be grater than or equal to the internally defined first residue number {self.__first_resid}.\n"
            #     return chainAssign
            # if seqId - self.__first_resid >= len(self.__cur_sequence):
            #     self.warningMessage += f"[Sequence mismatch] {self.__getCurrentRestraint()}"\
            #         f"The residue number '{seqId}' must be less than {len(self.__cur_sequence)}, total number of the internally defined sequence.\n"
            #     return chainAssign
            # """
            if self.__first_resid <= seqId < self.__first_resid + len(self.__cur_sequence):
                oneLetterCode = self.__cur_sequence[seqId - self.__first_resid].upper()

                _compId = next(k for k, v in monDict3.items() if v == oneLetterCode)

                if _compId != translateToStdResName(compId) and _compId != 'X':
                    self.warningMessage += f"[Sequence mismatch] {self.__getCurrentRestraint()}"\
                        f"Sequence alignment error between the sequence ({seqId}:{_compId}) "\
                        f"and data ({seqId}:{compId}). "\
                        "Please verify the consistency between the internally defined sequence and restraints and re-upload the restraint file(s).\n"
                    self.__has_seq_align_err = True
                    return chainAssign

        _seqId = seqId

        fixedChainId = None
        fixedSeqId = None

        if self.__mrAtomNameMapping is not None and compId not in monDict3:
            seqId, compId, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, compId, atomId)

        if self.__reasons is not None:
            if 'chain_id_remap' in self.__reasons and seqId in self.__reasons['chain_id_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.__reasons['chain_id_remap'], seqId)
                refChainId = fixedChainId
            elif 'seq_id_remap' in self.__reasons:
                fixedChainId, fixedSeqId = retrieveRemappedSeqId(self.__reasons['seq_id_remap'], refChainId, seqId)
                refChainId = fixedChainId
            if fixedSeqId is not None:
                _seqId = fixedSeqId

        updatePolySeqRst(self.__polySeqRst, self.__polySeq[0]['chain_id'] if refChainId is None else refChainId, _seqId, translateToStdResName(compId))

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
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint(n=index,g=group)}"\
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
                                self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint(n=index,g=group)}"\
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
                if refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                    if chainId != self.__chainNumberDict[refChainId]:
                        continue
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    chainAssign.append((chainId, _seqId, cifCompId))
                    if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                        self.__chainNumberDict[refChainId] = chainId
                    """ defer to sequence alignment error
                    if cifCompId != translateToStdResName(compId):
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint(n=index,g=group)}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                    """

        if len(chainAssign) == 0:
            if seqId == 1 and atomId in ('H', 'HN'):
                return self.assignCoordPolymerSequence(refChainId, seqId, compId, 'H1')
            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint(n=index,g=group)}"\
                f"{_seqId}:{compId}:{atomId} is not present in the coordinates.\n"

        return chainAssign

    def selectCoordAtoms(self, chainAssign, seqId, compId, atomId, allowAmbig=True, index=None, group=None):
        """ Select atoms of the coordinates.
        """

        atomSelection = []

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
                self.warningMessage += f"[Invalid atom nomenclature] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"{seqId}:{compId}:{atomId} is invalid atom nomenclature.\n"
                continue
            if lenAtomId > 1 and not allowAmbig:
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"Ambiguous atom selection '{seqId}:{compId}:{atomId}' is not allowed as a angle restraint.\n"
                continue

            for cifAtomId in _atomId:
                atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})

                self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, index, group)

        if len(atomSelection) > 0:
            self.atomSelectionSet.append(atomSelection)

    def selectAuxCoordAtoms(self, chainAssign, seqId, compId, atomId, allowAmbig=True, index=None, group=None):
        """ Select auxiliary atoms of the coordinates.
        """

        atomSelection = []

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
                self.warningMessage += f"[Invalid atom nomenclature] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"{seqId}:{compId}:{atomId} is invalid atom nomenclature.\n"
                continue
            if lenAtomId > 1 and not allowAmbig:
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"Ambiguous atom selection '{seqId}:{compId}:{atomId}' is not allowed as a angle restraint.\n"
                continue

            for cifAtomId in _atomId:
                atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})

                self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, index, group)

        if len(atomSelection) > 0:
            self.auxAtomSelectionSet.append(atomSelection)

    def testCoordAtomIdConsistency(self, chainId, seqId, compId, atomId, seqKey, coordAtomSite, index=None, group=None):
        if not self.__hasCoord:
            return

        found = False

        if coordAtomSite is not None:
            if atomId in coordAtomSite['atom_id']:
                found = True
            elif 'alt_atom_id' in coordAtomSite and atomId in coordAtomSite['alt_atom_id']:
                found = True
                # self.__authAtomId = 'auth_atom_id'
            elif self.__preferAuthSeq:
                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
                if _coordAtomSite is not None:
                    if atomId in _coordAtomSite['atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        # self.__authSeqId = 'label_seq_id'
                        seqKey = _seqKey
                    elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        # self.__authSeqId = 'label_seq_id'
                        # self.__authAtomId = 'auth_atom_id'
                        seqKey = _seqKey

        elif self.__preferAuthSeq:
            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
            if _coordAtomSite is not None:
                if atomId in _coordAtomSite['atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    # self.__authSeqId = 'label_seq_id'
                    seqKey = _seqKey
                elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    # self.__authSeqId = 'label_seq_id'
                    # self.__authAtomId = 'auth_atom_id'
                    seqKey = _seqKey

        if found:
            return

        if chainId in self.__chainNumberDict.values():

            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
            if _coordAtomSite is not None:
                if atomId in _coordAtomSite['atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    # self.__authSeqId = 'label_seq_id'
                    seqKey = _seqKey
                elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    # self.__authSeqId = 'label_seq_id'
                    # self.__authAtomId = 'auth_atom_id'
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
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint(n=index,g=group)}"\
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

    # Enter a parse tree produced by DynamoMRParser#torsion_angle_restraints.
    def enterTorsion_angle_restraints(self, ctx: DynamoMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#torsion_angle_restraints.
    def exitTorsion_angle_restraints(self, ctx: DynamoMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#torsion_angle_restraint.
    def enterTorsion_angle_restraint(self, ctx: DynamoMRParser.Torsion_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#torsion_angle_restraint.
    def exitTorsion_angle_restraint(self, ctx: DynamoMRParser.Torsion_angle_restraintContext):

        try:

            index = int(str(ctx.Integer(0)))

            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(4)).upper()
            atomId3 = str(ctx.Simple_name(5)).upper()
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(6)).upper()
            atomId4 = str(ctx.Simple_name(7)).upper()

            if None in self.numberSelection:
                return

            target_value = None
            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]

            dstFunc = self.validateAngleRange(index, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(None, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(None, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Torsion angle'):
                return

            compId = self.atomSelectionSet[0][0]['comp_id']
            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4])
                if angleName is None:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        except ValueError:
            self.dihedRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by DynamoMRParser#torsion_angle_restraints_sw_segid.
    def enterTorsion_angle_restraints_sw_segid(self, ctx: DynamoMRParser.Torsion_angle_restraints_sw_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#torsion_angle_restraints_sw_segid.
    def exitTorsion_angle_restraints_sw_segid(self, ctx: DynamoMRParser.Torsion_angle_restraints_sw_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#torsion_angle_restraint_sw_segid.
    def enterTorsion_angle_restraint_sw_segid(self, ctx: DynamoMRParser.Torsion_angle_restraint_sw_segidContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#torsion_angle_restraint_sw_segid.
    def exitTorsion_angle_restraint_sw_segid(self, ctx: DynamoMRParser.Torsion_angle_restraint_sw_segidContext):

        try:

            index = int(str(ctx.Integer(0)))

            chainId1 = str(ctx.Simple_name(0))
            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(1)).upper()
            atomId1 = str(ctx.Simple_name(2)).upper()
            chainId2 = str(ctx.Simple_name(3))
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(4)).upper()
            atomId2 = str(ctx.Simple_name(5)).upper()
            chainId3 = str(ctx.Simple_name(6))
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(7)).upper()
            atomId3 = str(ctx.Simple_name(8)).upper()
            chainId4 = str(ctx.Simple_name(9))
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(10)).upper()
            atomId4 = str(ctx.Simple_name(11)).upper()

            if None in self.numberSelection:
                return

            target_value = None
            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]

            dstFunc = self.validateAngleRange(None, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(chainId3, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(chainId4, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Torsion angle'):
                return

            compId = self.atomSelectionSet[0][0]['comp_id']
            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4])
                if angleName is None:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        except ValueError:
            self.dihedRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by DynamoMRParser#torsion_angle_restraints_ew_segid.
    def enterTorsion_angle_restraints_ew_segid(self, ctx: DynamoMRParser.Torsion_angle_restraints_ew_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#torsion_angle_restraints_ew_segid.
    def exitTorsion_angle_restraints_ew_segid(self, ctx: DynamoMRParser.Torsion_angle_restraints_ew_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#torsion_angle_restraint_ew_segid.
    def enterTorsion_angle_restraint_ew_segid(self, ctx: DynamoMRParser.Torsion_angle_restraint_ew_segidContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#torsion_angle_restraint_ew_segid.
    def exitTorsion_angle_restraint_ew_segid(self, ctx: DynamoMRParser.Torsion_angle_restraint_ew_segidContext):

        try:

            index = int(str(ctx.Integer(0)))

            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            chainId1 = str(ctx.Simple_name(2))
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(3)).upper()
            atomId2 = str(ctx.Simple_name(4)).upper()
            chainId2 = str(ctx.Simple_name(5))
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(6)).upper()
            atomId3 = str(ctx.Simple_name(7)).upper()
            chainId3 = str(ctx.Simple_name(8))
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(9)).upper()
            atomId4 = str(ctx.Simple_name(10)).upper()
            chainId4 = str(ctx.Simple_name(11))

            if None in self.numberSelection:
                return

            target_value = None
            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]

            dstFunc = self.validateAngleRange(None, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(chainId3, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(chainId4, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Torsion angle'):
                return

            compId = self.atomSelectionSet[0][0]['comp_id']
            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4])
                if angleName is None:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        except ValueError:
            self.dihedRestraints -= 1
        finally:
            self.numberSelection.clear()

    def validateAngleRange(self, index, weight, target_value, lower_limit, upper_limit):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if ANGLE_ERROR_MIN < target_value < ANGLE_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The target value='{target_value}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if ANGLE_ERROR_MIN <= lower_limit < ANGLE_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if ANGLE_ERROR_MIN < upper_limit <= ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if not validRange:
            return None

        if target_value is not None:
            if ANGLE_RANGE_MIN <= target_value <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The target value='{target_value}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if ANGLE_RANGE_MIN <= lower_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if ANGLE_RANGE_MIN <= upper_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by DynamoMRParser#rdc_restraints.
    def enterRdc_restraints(self, ctx: DynamoMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#rdc_restraints.
    def exitRdc_restraints(self, ctx: DynamoMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: DynamoMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: DynamoMRParser.Rdc_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]
            error = abs(self.numberSelection[1])
            weight = self.numberSelection[2]

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validateRdcRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            diffSeqId = seqId1 - seqId2

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2)

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

            if self.__has_seq_align_err and seq_id_1 - seq_id_2 != diffSeqId:
                return

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

    # Enter a parse tree produced by DynamoMRParser#rdc_restraints_sw_segid.
    def enterRdc_restraints_sw_segid(self, ctx: DynamoMRParser.Rdc_restraints_sw_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#rdc_restraints_sw_segid.
    def exitRdc_restraints_sw_segid(self, ctx: DynamoMRParser.Rdc_restraints_sw_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#rdc_restraint_sw_segid.
    def enterRdc_restraint_sw_segid(self, ctx: DynamoMRParser.Rdc_restraint_sw_segidContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#rdc_restraint_sw_segid.
    def exitRdc_restraint_sw_segid(self, ctx: DynamoMRParser.Rdc_restraint_sw_segidContext):

        try:

            chainId1 = str(ctx.Simple_name(0))
            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(1)).upper()
            atomId1 = str(ctx.Simple_name(2)).upper()
            chainId2 = str(ctx.Simple_name(3))
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(4)).upper()
            atomId2 = str(ctx.Simple_name(5)).upper()

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]
            error = abs(self.numberSelection[1])
            weight = self.numberSelection[2]

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validateRdcRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            diffSeqId = seqId1 - seqId2

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2)

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

            if self.__has_seq_align_err and seq_id_1 - seq_id_2 != diffSeqId:
                return

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

            else:

                if self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

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

    # Enter a parse tree produced by DynamoMRParser#rdc_restraints_ew_segid.
    def enterRdc_restraints_ew_segid(self, ctx: DynamoMRParser.Rdc_restraints_ew_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#rdc_restraints_ew_segid.
    def exitRdc_restraints_ew_segid(self, ctx: DynamoMRParser.Rdc_restraints_ew_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#rdc_restraint_ew_segid.
    def enterRdc_restraint_ew_segid(self, ctx: DynamoMRParser.Rdc_restraint_ew_segidContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#rdc_restraint_ew_segid.
    def exitRdc_restraint_ew_segid(self, ctx: DynamoMRParser.Rdc_restraint_ew_segidContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            chainId1 = str(ctx.Simple_name(2))
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(3)).upper()
            atomId2 = str(ctx.Simple_name(4)).upper()
            chainId2 = str(ctx.Simple_name(5))

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]
            error = abs(self.numberSelection[1])
            weight = self.numberSelection[2]

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validateRdcRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            diffSeqId = seqId1 - seqId2

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2)

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

            if self.__has_seq_align_err and seq_id_1 - seq_id_2 != diffSeqId:
                return

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

            else:

                if self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

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

    # Enter a parse tree produced by DynamoMRParser#pales_meta_outputs.
    def enterPales_meta_outputs(self, ctx: DynamoMRParser.Pales_meta_outputsContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by DynamoMRParser#pales_meta_outputs.
    def exitPales_meta_outputs(self, ctx: DynamoMRParser.Pales_meta_outputsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#pales_rdc_outputs.
    def enterPales_rdc_outputs(self, ctx: DynamoMRParser.Pales_rdc_outputsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#pales_rdc_outputs.
    def exitPales_rdc_outputs(self, ctx: DynamoMRParser.Pales_rdc_outputsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#pales_rdc_output.
    def enterPales_rdc_output(self, ctx: DynamoMRParser.Pales_rdc_outputContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#pales_rdc_output.
    def exitPales_rdc_output(self, ctx: DynamoMRParser.Pales_rdc_outputContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()

            if None in self.numberSelection:
                return

            # di
            target = self.numberSelection[1]  # d_obs
            # d (calc)
            # d_diff
            error = abs(self.numberSelection[4])
            weight = self.numberSelection[5]

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validateRdcRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            diffSeqId = seqId1 - seqId2

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2)

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

            if self.__has_seq_align_err and seq_id_1 - seq_id_2 != diffSeqId:
                return

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

    def validateRdcRange(self, weight, target_value, lower_limit, upper_limit):
        """ Validate RDC value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

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

    # Enter a parse tree produced by DynamoMRParser#coupling_restraints.
    def enterCoupling_restraints(self, ctx: DynamoMRParser.Coupling_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'jcoup'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#coupling_restraints.
    def exitCoupling_restraints(self, ctx: DynamoMRParser.Coupling_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#coupling_restraint.
    def enterCoupling_restraint(self, ctx: DynamoMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#coupling_restraint.
    def exitCoupling_restraint(self, ctx: DynamoMRParser.Coupling_restraintContext):

        try:

            index = int(str(ctx.Integer(0)))

            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(4)).upper()
            atomId3 = str(ctx.Simple_name(5)).upper()
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(6)).upper()
            atomId4 = str(ctx.Simple_name(7)).upper()

            if None in self.numberSelection:
                return

            A = self.numberSelection[0]
            B = self.numberSelection[1]
            C = self.numberSelection[2]
            phase = self.numberSelection[3]
            target_value = self.numberSelection[4]
            lower_limit = upper_limit = None
            # fource_const = self.numberSelection[5]

            dstFunc = self.validateCoupRange(index, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(None, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(None, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Scalar coupling'):
                return

            compId = self.atomSelectionSet[0][0]['comp_id']
            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4])
                if angleName is None:
                    continue
                if self.__debug:
                    if angleName == 'PHI':
                        self.auxAtomSelectionSet.clear()
                        self.selectAuxCoordAtoms(chainAssign2, seqId2, compId2, 'H', False)
                        self.selectAuxCoordAtoms(chainAssign3, seqId3, compId3, 'HA', False)
                        if len(self.auxAtomSelectionSet) == 2:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                                  f"A={A} B={B} C={C} phase={phase} "
                                  f"atom1={self.auxAtomSelectionSet[0][0]} atom2={self.auxAtomSelectionSet[1][0]} {dstFunc}")
                            continue
                    else:
                        print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                              f"A={A} B={B} C={C} phase={phase} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        except ValueError:
            self.jcoupRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by DynamoMRParser#coupling_restraints_sw_segid.
    def enterCoupling_restraints_sw_segid(self, ctx: DynamoMRParser.Coupling_restraints_sw_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'jcoup'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#coupling_restraints_sw_segid.
    def exitCoupling_restraints_sw_segid(self, ctx: DynamoMRParser.Coupling_restraints_sw_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#coupling_restraint_sw_segid.
    def enterCoupling_restraint_sw_segid(self, ctx: DynamoMRParser.Coupling_restraint_sw_segidContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#coupling_restraint_sw_segid.
    def exitCoupling_restraint_sw_segid(self, ctx: DynamoMRParser.Coupling_restraint_sw_segidContext):

        try:

            index = int(str(ctx.Integer(0)))

            chainId1 = str(ctx.Simple_name(0))
            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(1)).upper()
            atomId1 = str(ctx.Simple_name(2)).upper()
            chainId2 = str(ctx.Simple_name(3))
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(4)).upper()
            atomId2 = str(ctx.Simple_name(5)).upper()
            chainId3 = str(ctx.Simple_name(6))
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(7)).upper()
            atomId3 = str(ctx.Simple_name(8)).upper()
            chainId4 = str(ctx.Simple_name(9))
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(10)).upper()
            atomId4 = str(ctx.Simple_name(11)).upper()

            if None in self.numberSelection:
                return

            A = self.numberSelection[0]
            B = self.numberSelection[1]
            C = self.numberSelection[2]
            phase = self.numberSelection[3]
            target_value = self.numberSelection[4]
            lower_limit = upper_limit = None
            # fource_const = self.numberSelection[5]

            dstFunc = self.validateCoupRange(index, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(chainId3, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(chainId4, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Scalar coupling'):
                return

            compId = self.atomSelectionSet[0][0]['comp_id']
            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4])
                if angleName is None:
                    continue
                if self.__debug:
                    if angleName == 'PHI':
                        self.auxAtomSelectionSet.clear()
                        self.selectAuxCoordAtoms(chainAssign2, seqId2, compId2, 'H', False)
                        self.selectAuxCoordAtoms(chainAssign3, seqId3, compId3, 'HA', False)
                        if len(self.auxAtomSelectionSet) == 2:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                                  f"A={A} B={B} C={C} phase={phase} "
                                  f"atom1={self.auxAtomSelectionSet[0][0]} atom2={self.auxAtomSelectionSet[1][0]} {dstFunc}")
                            continue
                    else:
                        print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                              f"A={A} B={B} C={C} phase={phase} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        except ValueError:
            self.jcoupRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by DynamoMRParser#coupling_restraints_ew_segid.
    def enterCoupling_restraints_ew_segid(self, ctx: DynamoMRParser.Coupling_restraints_ew_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'jcoup'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#coupling_restraints_ew_segid.
    def exitCoupling_restraints_ew_segid(self, ctx: DynamoMRParser.Coupling_restraints_ew_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#coupling_restraint_ew_segid.
    def enterCoupling_restraint_ew_segid(self, ctx: DynamoMRParser.Coupling_restraint_ew_segidContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#coupling_restraint_ew_segid.
    def exitCoupling_restraint_ew_segid(self, ctx: DynamoMRParser.Coupling_restraint_ew_segidContext):

        try:

            index = int(str(ctx.Integer(0)))

            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            chainId1 = str(ctx.Simple_name(2))
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(3)).upper()
            atomId2 = str(ctx.Simple_name(4)).upper()
            chainId2 = str(ctx.Simple_name(5))
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(6)).upper()
            atomId3 = str(ctx.Simple_name(7)).upper()
            chainId3 = str(ctx.Simple_name(8))
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(9)).upper()
            atomId4 = str(ctx.Simple_name(10)).upper()
            chainId4 = str(ctx.Simple_name(11))

            if None in self.numberSelection:
                return

            A = self.numberSelection[0]
            B = self.numberSelection[1]
            C = self.numberSelection[2]
            phase = self.numberSelection[3]
            target_value = self.numberSelection[4]
            lower_limit = upper_limit = None
            # fource_const = self.numberSelection[5]

            dstFunc = self.validateCoupRange(index, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(chainId3, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(chainId4, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Scalar coupling'):
                return

            compId = self.atomSelectionSet[0][0]['comp_id']
            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4])
                if angleName is None:
                    continue
                if self.__debug:
                    if angleName == 'PHI':
                        self.auxAtomSelectionSet.clear()
                        self.selectAuxCoordAtoms(chainAssign2, seqId2, compId2, 'H', False)
                        self.selectAuxCoordAtoms(chainAssign3, seqId3, compId3, 'HA', False)
                        if len(self.auxAtomSelectionSet) == 2:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                                  f"A={A} B={B} C={C} phase={phase} "
                                  f"atom1={self.auxAtomSelectionSet[0][0]} atom2={self.auxAtomSelectionSet[1][0]} {dstFunc}")
                            continue
                    else:
                        print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                              f"A={A} B={B} C={C} phase={phase} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        except ValueError:
            self.jcoupRestraints -= 1
        finally:
            self.numberSelection.clear()

    def validateCoupRange(self, index, weight, target_value, lower_limit, upper_limit):
        """ Validate scalar J-coupling value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The target value='{target_value}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if RDC_ERROR_MIN <= lower_limit < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit <= RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The upper limit value='{upper_limit:.6f}' must be greater than the target value '{target_value}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if RDC_RANGE_MIN <= target_value <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The target value='{target_value}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if RDC_RANGE_MIN <= lower_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN <= upper_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by DynamoMRParser#talos_restraints.
    def enterTalos_restraints(self, ctx: DynamoMRParser.Talos_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#talos_restraints.
    def exitTalos_restraints(self, ctx: DynamoMRParser.Talos_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#talos_restraint.
    def enterTalos_restraint(self, ctx: DynamoMRParser.Talos_restraintContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#talos_restraint.
    def exitTalos_restraint(self, ctx: DynamoMRParser.Talos_restraintContext):

        try:

            seqId = int(str(ctx.Integer(0)))
            compId = str(ctx.Simple_name(0)).upper()

            if compId not in monDict3.values() and compId not in monDict3:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found unknown residue name {compId!r}.\n"
                return

            if len(compId) >= 3:
                pass
            else:
                compId = next(k for k, v in monDict3.items() if v == compId and len(k) == 3)

            if None in self.numberSelection:
                return

            # phi
            phi_target_value = self.numberSelection[0]
            psi_target_value = self.numberSelection[1]

            delta_phi_value = self.numberSelection[2]
            delta_psi_value = self.numberSelection[3]

            # dist = self.numberSelection[4]
            # s2 = self.numberSelection[5]

            # count = int(str(ctx.Integer(1)))
            # cs_count = int(str(ctx.Integer(2)))

            _class = str(ctx.Simple_name(1))

            if _class not in TALOS_PREDICTION_CLASSES:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The class name {_class!r} should be one of {TALOS_PREDICTION_CLASSES}.\n"
                return

            if _class not in TALOS_PREDICTION_MIN_CLASSES:  # ignore suspicious predictions
                return

            if not self.__hasPolySeq:
                return

            for angleName in ('PHI', 'PSI'):
                atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
                seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

                if angleName == 'PHI':
                    target_value = phi_target_value
                    lower_limit = phi_target_value - delta_phi_value
                    upper_limit = phi_target_value + delta_phi_value
                else:
                    target_value = psi_target_value
                    lower_limit = psi_target_value - delta_psi_value
                    upper_limit = psi_target_value + delta_psi_value

                dstFunc = self.validateAngleRange(None, 1.0, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                atomId = next(name for name, offset in zip(atomNames, seqOffset) if offset == 0)

                chainAssign = self.assignCoordPolymerSequence(None, seqId, compId, atomId)

                if len(chainAssign) == 0:
                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                        f"{seqId}:{compId} is not present in the coordinates.\n"
                    return

                for chainId, cifSeqId, cifCompId in chainAssign:
                    ps = next(ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId)

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

                    if len(self.atomSelectionSet) < 4:
                        return

                    if not self.areUniqueCoordAtoms('a Torsion angle (TALOS)'):
                        return

                    for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                        self.atomSelectionSet[1],
                                                                        self.atomSelectionSet[2],
                                                                        self.atomSelectionSet[3]):
                        if isLongRangeRestraint([atom1, atom2, atom3, atom4]):
                            continue
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} className={_class} "
                                  f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        except ValueError:
            self.dihedRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by DynamoMRParser#talos_restraints_wo_s2.
    def enterTalos_restraints_wo_s2(self, ctx: DynamoMRParser.Talos_restraints_wo_s2Context):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

        self.closeSequqnce()

    # Exit a parse tree produced by DynamoMRParser#talos_restraints_wo_s2.
    def exitTalos_restraints_wo_s2(self, ctx: DynamoMRParser.Talos_restraints_wo_s2Context):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by DynamoMRParser#talos_restraint_wo_s2.
    def enterTalos_restraint_wo_s2(self, ctx: DynamoMRParser.Talos_restraint_wo_s2Context):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by DynamoMRParser#talos_restraint_wo_s2.
    def exitTalos_restraint_wo_s2(self, ctx: DynamoMRParser.Talos_restraint_wo_s2Context):

        try:

            seqId = int(str(ctx.Integer(0)))
            compId = str(ctx.Simple_name(0)).upper()

            if compId not in monDict3.values() and compId not in monDict3:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found unknown residue name {compId!r}.\n"
                return

            if len(compId) >= 3:
                pass
            else:
                compId = next(k for k, v in monDict3.items() if v == compId and len(k) == 3)

            if None in self.numberSelection:
                return

            # phi
            phi_target_value = self.numberSelection[0]
            psi_target_value = self.numberSelection[1]

            delta_phi_value = self.numberSelection[2]
            delta_psi_value = self.numberSelection[3]

            # dist = self.numberSelection[4]

            # count = int(str(ctx.Integer(1)))

            _class = str(ctx.Simple_name(1))

            if _class not in TALOS_PREDICTION_CLASSES:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The class name {_class!r} should be one of {TALOS_PREDICTION_CLASSES}.\n"
                return

            if _class not in TALOS_PREDICTION_MIN_CLASSES:  # ignore suspicious predictions
                return

            if not self.__hasPolySeq:
                return

            for angleName in ('PHI', 'PSI'):
                atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
                seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

                if angleName == 'PHI':
                    target_value = phi_target_value
                    lower_limit = phi_target_value - delta_phi_value
                    upper_limit = phi_target_value + delta_phi_value
                else:
                    target_value = psi_target_value
                    lower_limit = psi_target_value - delta_psi_value
                    upper_limit = psi_target_value + delta_psi_value

                dstFunc = self.validateAngleRange(None, 1.0, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                atomId = next(name for name, offset in zip(atomNames, seqOffset) if offset == 0)

                chainAssign = self.assignCoordPolymerSequence(None, seqId, compId, atomId)

                if len(chainAssign) == 0:
                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                        f"{seqId}:{compId} is not present in the coordinates.\n"
                    return

                for chainId, cifSeqId, cifCompId in chainAssign:
                    ps = next(ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId)

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

                    if len(self.atomSelectionSet) < 4:
                        return

                    if not self.areUniqueCoordAtoms('a Torsion angle (TALOS)'):
                        return

                    for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                        self.atomSelectionSet[1],
                                                                        self.atomSelectionSet[2],
                                                                        self.atomSelectionSet[3]):
                        if isLongRangeRestraint([atom1, atom2, atom3, atom4]):
                            continue
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} className={_class} "
                                  f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        except ValueError:
            self.dihedRestraints -= 1
        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by DynamoMRParser#number.
    def enterNumber(self, ctx: DynamoMRParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by DynamoMRParser#number.
    def exitNumber(self, ctx: DynamoMRParser.NumberContext):
        if ctx.Float():
            self.numberSelection.append(float(str(ctx.Float())))

        elif ctx.Integer():
            self.numberSelection.append(float(str(ctx.Integer())))

        else:
            self.numberSelection.append(None)

    def __getCurrentRestraint(self, n=None, g=None):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints (index={n}, group={g})] "
        if self.__cur_subtype == 'dihed':
            if n is not None:
                return f"[Check the {self.dihedRestraints}th row of torsion angle restraints (index={n})] "
            return f"[Check the {self.dihedRestraints}th row of torsion angle restraints] "
        if self.__cur_subtype == 'rdc':
            return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
        if self.__cur_subtype == 'jcoup':
            return f"[Check the {self.jcoupRestraints}th row of scalar coupling constant restraints (index={n})] "
        return ''

    def getContentSubtype(self):
        """ Return content subtype of DYNAMO/PALES/TALOS MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'jcoup_restraint': self.jcoupRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of DYNAMO/PALES/TALOS MR file.
        """
        return self.__polySeqRst

    def getSequenceAlignment(self):
        """ Return sequence alignment between coordinates and DYNAMO/PALES/TALOS MR.
        """
        return self.__seqAlign

    def getChainAssignment(self):
        """ Return chain assignment between coordinates and DYNAMO/PALES/TALOS MR.
        """
        return self.__chainAssign

    def getReasonsForReparsing(self):
        """ Return reasons for re-parsing DYNAMO/PALES/TALOS MR file.
        """
        return self.reasonsForReParsing


# del DynamoMRParser
