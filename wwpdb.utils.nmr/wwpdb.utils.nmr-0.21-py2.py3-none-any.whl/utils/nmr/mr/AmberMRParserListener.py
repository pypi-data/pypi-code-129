##
# File: AmberMRParserListener.py
# Date: 27-Jan-2022
#
# Updates:
# Generated from AmberMRParser.g4 by ANTLR 4.10.1
""" ParserLister class for AMBER MR files.
    @author: Masashi Yokochi
"""
import sys
import copy
import re
import itertools

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from wwpdb.utils.nmr.mr.AmberMRParser import AmberMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (stripOnce,
                                                       checkCoordinates,
                                                       translateToStdAtomName,
                                                       translateToStdResName,
                                                       isLongRangeRestraint,
                                                       getTypeOfDihedralRestraint,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR,
                                                       CSA_RESTRAINT_RANGE,
                                                       CSA_RESTRAINT_ERROR,
                                                       PCS_RESTRAINT_RANGE,
                                                       PCS_RESTRAINT_ERROR,
                                                       CS_RESTRAINT_RANGE,
                                                       CS_RESTRAINT_ERROR)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                             ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from wwpdb.utils.nmr.AlignUtil import (monDict3,
                                           updatePolySeqRstFromAtomSelectionSet,
                                           sortPolySeqRst,
                                           alignPolymerSequence,
                                           assignPolymerSequence,
                                           trimSequenceAlignment,
                                           retrieveAtomIdentFromMRMap)
except ImportError:
    from nmr.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from nmr.mr.AmberMRParser import AmberMRParser
    from nmr.mr.ParserListenerUtil import (stripOnce,
                                           checkCoordinates,
                                           translateToStdAtomName,
                                           translateToStdResName,
                                           isLongRangeRestraint,
                                           getTypeOfDihedralRestraint,
                                           REPRESENTATIVE_MODEL_ID,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR,
                                           CSA_RESTRAINT_RANGE,
                                           CSA_RESTRAINT_ERROR,
                                           PCS_RESTRAINT_RANGE,
                                           PCS_RESTRAINT_ERROR,
                                           CS_RESTRAINT_RANGE,
                                           CS_RESTRAINT_ERROR)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                 ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from nmr.AlignUtil import (monDict3,
                               updatePolySeqRstFromAtomSelectionSet,
                               sortPolySeqRst,
                               alignPolymerSequence,
                               assignPolymerSequence,
                               trimSequenceAlignment,
                               retrieveAtomIdentFromMRMap)


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


CSA_RANGE_MIN = CSA_RESTRAINT_RANGE['min_inclusive']
CSA_RANGE_MAX = CSA_RESTRAINT_RANGE['max_inclusive']

CSA_ERROR_MIN = CSA_RESTRAINT_ERROR['min_exclusive']
CSA_ERROR_MAX = CSA_RESTRAINT_ERROR['max_exclusive']


PCS_RANGE_MIN = PCS_RESTRAINT_RANGE['min_inclusive']
PCS_RANGE_MAX = PCS_RESTRAINT_RANGE['max_inclusive']

PCS_ERROR_MIN = PCS_RESTRAINT_ERROR['min_exclusive']
PCS_ERROR_MAX = PCS_RESTRAINT_ERROR['max_exclusive']


CS_RANGE_MIN = CS_RESTRAINT_RANGE['min_inclusive']
CS_RANGE_MAX = CS_RESTRAINT_RANGE['max_inclusive']

CS_ERROR_MIN = CS_RESTRAINT_ERROR['min_exclusive']
CS_ERROR_MAX = CS_RESTRAINT_ERROR['max_exclusive']


# maximum column size of IAT
MAX_COL_IAT = 8


# maximum column size of IGRn
MAX_COL_IGR = 200


# maximum column size of RSTWT
MAX_COL_RSTWT = 4


# column sizes of distance restraint
COL_DIST = 2


# column sizes of angle restraint
COL_ANG = 3


# column sizes of torsional angle restraint
COL_DIHED = 4


# column sizes of plane-point angle restraint
COL_PLANE_POINT = 5


# column sizes of plane-plane angle restraint
COL_PLANE_PLANE = 8


# column sizes of generalized distance restraint (2 coordinate vectors)
COL_DIST_COORD2 = 4


# column sizes of generalized distance restraint (3 coordinate vectors)
COL_DIST_COORD3 = 6


# column sizes of generalized distance restraint (4 coordinate vectors)
COL_DIST_COORD4 = 8


# This class defines a complete listener for a parse tree produced by AmberMRParser.
class AmberMRParserListener(ParseTreeListener):

    # __verbose = None
    # __lfh = None
    __debug = False
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

    # AmberPTParserListener.getAtomNumberDict()
    __atomNumberDict = None

    # AMBER atom number dictionary reconstructing from Sander comments
    __sanderAtomNumberDict = None
    __hasComments = False

    # CIF reader
    # __cR = None
    __hasCoord = False

    # data item name for model ID in 'atom_site' category
    # __modelNumName = None

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

    __hasPolySeq = False
    __hasNonPoly = False
    __preferAuthSeq = True

    # polymer sequence of MR file
    __polySeqRst = None

    __seqAlign = None
    __chainAssign = None

    # current restraint subtype
    __cur_subtype = ''

    # last Sander comment
    lastComment = None
    prevComment = None

    lastElemName = None
    lastPlaneSeqId = None

    metalIonMapping = None

    # IAT
    numIatCol = 0
    setIatCol = None
    iat = None

    likeDist = None

    # IGRn
    numIgrCol = None
    setIgrCol = None
    igr = None

    ixpk = -1
    inpk = -1

    iresid = 0

    numAtnamCol = 0
    setAtnamCol = None
    atnam = None

    numGrnamCol = None
    setGrnamCol = None
    grnam = None

    # R1, R2, R3, R4
    lowerLinearLimit = None
    lowerLimit = None
    upperLimit = None
    upperLinearLimit = None

    rstwt = [0.0, 0.0, 0.0, 0.0]  # generalized distance 2/3/4

    # dipolar couplings
    id = None
    jd = None
    dobsl = None
    dobsu = None
    dwt = None
    gigj = None
    dij = None
    ndip = None
    dataset = None
    numDatasets = None
    s11 = None
    s12 = None
    s13 = None
    s22 = None
    s23 = None

    # CSA
    icsa = None
    jcsa = None
    kcsa = None
    cobsl = None
    cobsu = None
    cwt = None
    ncsa = None
    datasetc = None
    sigma11 = None
    sigma12 = None
    sigma13 = None
    sigma22 = None
    sigma23 = None
    field = None

    # PCS
    iprot = None
    obs = None
    wt = None
    tolpro = None
    mltpro = None
    nprot = None
    nmpmc = None
    optphi = None
    opttet = None
    optomg = None
    opta1 = None
    opta2 = None
    optkon = None
    nme = None

    # CS
    shrang = None
    iatr = None
    natr = None
    namr = None
    _str = None
    nring = None
    nter = None
    cter = None

    # NOESY
    ihp = None
    jhp = None
    aexp = None
    arange = None
    awt = None
    emix = None
    npeak = None
    invwt1 = None
    invwt2 = None
    omega = None
    taurot = None
    taumet = None
    id2o = None

    # Amber 10: ambmask
    depth = 0

    hasFuncExprs = False
    funcExprs = None

    inGenDist = False
    inGenDist_funcExprs = None
    inGenDist_weight = None

    inPlane = False
    inPlane_columnSel = -1
    inPlane_funcExprs = None
    inPlane_funcExprs2 = None

    inCom = False
    inCom_funcExprs = None

    # collection of atom selection
    atomSelectionSet = []

    # current residue name for atom name mapping
    __cur_resname_for_mapping = ''

    # unambigous atom name mapping
    unambigAtomNameMapping = {}

    # ambigous atom name mapping
    ambigAtomNameMapping = {}

    warningMessage = ''

    reasonsForReParsing = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 mrAtomNameMapping=None,
                 cR=None, cC=None, ccU=None, csStat=None, nefT=None,
                 atomNumberDict=None, reasons=None):
        # self.__verbose = verbose
        # self.__lfh = log

        self.__mrAtomNameMapping = None if mrAtomNameMapping is None or len(mrAtomNameMapping) == 0 else mrAtomNameMapping

        # self.__cR = cR
        self.__hasCoord = cR is not None

        if self.__hasCoord:
            ret = checkCoordinates(verbose, log, representativeModelId, cR, cC)
            # self.__modelNumName = ret['model_num_name']
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

        if atomNumberDict is not None:
            self.__atomNumberDict = atomNumberDict
        else:
            self.__sanderAtomNumberDict = {}

        self.nmrRestraints = 0       # AMBER: NMR restraints
        self.distRestraints = 0      # AMBER: Distance restraints
        self.angRestraints = 0       # AMBER: Angle restraints
        self.dihedRestraints = 0     # AMBER: Torsional angle restraints
        self.planeRestraints = 0     # AMBER: Plane-point/plane angle restraints
        self.noepkRestraints = 0     # AMBER: NOESY volume restraints
        self.procsRestraints = 0     # AMBER: Chemical shift restraints
        self.pcsRestraints = 0       # AMBER: Psuedocontact shift restraints
        self.rdcRestraints = 0       # AMBER: Direct dipolar coupling restraints
        self.csaRestraints = 0       # AMBER: Residual CSA or pseudo-CSA restraints

        # last Sander comment
        self.lastComment = None

        # IAT
        self.numIatCol = 0
        self.setIatCol = None
        self.iat = None

        self.likeDist = None

        # IGRn
        self.numIgrCol = None
        self.setIgrCol = None
        self.igr = None

        self.ixpk = -1
        self.nxpk = -1

        self.iresid = 0

        self.numAtnamCol = 0
        self.setAtnamCol = None
        self.atnam = None

        self.numGrnamCol = None
        self.setGrnamCol = None
        self.grnam = None

        # R1, R2, R3, R4
        self.lowerLinearLimit = None
        self.lowerLimit = None
        self.upperLimit = None
        self.upperLinearLimit = None

        # dipolar couplings
        self.id = None
        self.jd = None
        self.dobsl = None
        self.dobsu = None
        self.dwt = None
        self.gigj = None
        self.dij = None
        self.ndip = None
        self.dataset = None
        self.numDatasets = None
        self.s11 = None
        self.s12 = None
        self.s13 = None
        self.s22 = None
        self.s23 = None

        # CSA
        self.icsa = None
        self.jcsa = None
        self.kcsa = None
        self.cobsl = None
        self.cobsu = None
        self.cwt = None
        self.ncsa = None
        self.datasetc = None
        self.sigma11 = None
        self.sigma12 = None
        self.sigma13 = None
        self.sigma22 = None
        self.sigma23 = None
        self.field = None

        # PCS
        self.iprot = None
        self.obs = None
        self.wt = None
        self.tolpro = None
        self.mltpro = None
        self.nprot = None
        self.nmpmc = None
        self.optphi = None
        self.opttet = None
        self.optomg = None
        self.opta1 = None
        self.opta2 = None
        self.optkon = None
        self.nme = None

        # CS
        self.shrang = None
        self.iatr = None
        self.natr = None
        self.namr = None
        self._str = None
        self.nring = None
        self.nter = None
        self.cter = None

        # NOESY
        self.ihp = None
        self.jhp = None
        self.aexp = None
        self.arange = None
        self.awt = None
        self.emix = None
        self.npeak = None
        self.invwt1 = None
        self.invwt2 = None
        self.omega = None
        self.taurot = None
        self.taumet = None
        self.id2o = None

        self.dist_sander_pat = re.compile(r'(\d+) (\S+) (\S+) '
                                          r'(\d+) (\S+) (\S+) '
                                          r'([-+]?\d*\.?\d+).*')

        self.ang_sander_pat = re.compile(r'(\d+) (\S+) (\S+): '
                                         r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                         r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                         r'\(\s*(\d+) (\S+) (\S+)\s*\).*')  # r'([-+]?\d*\.?\d+) [-+]?\d*\.?\d+).*')
        self.ang_nang_sander_pat = re.compile(r'N angles for residue (\d+).*')

        self.ang_nang_atoms = [['H', 'N', 'C'],
                               ['H', 'N', 'CA']
                               ]

        self.dihed_sander_pat = re.compile(r'(\d+) (\S+) (\S+): '
                                           r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                           r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                           r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                           r'\(\s*(\d+) (\S+) (\S+)\s*\) '
                                           r'([-+]?\d*\.?\d+) '
                                           r'([-+]?\d*\.?\d+).*')

        self.dihed_chiral_sander_pat = re.compile(r'chirality for residue (\d+) atoms: '
                                                  r'(\S+) (\S+) (\S+) (\S+).*')
        self.dihed_omega_sander_pat = re.compile(r'trans-omega constraint for residue (\d+).*')

        self.dihed_plane_residue_pat = re.compile(r'PLANAR RESTRAINTS FOR RESIDUE (\d+).*')
        self.dihed_plane_sander_pat = re.compile(r'ANGLE (\S+)\s*-\s*(\S+)\s*-\s*(\S+)\s*-\s*(\S+) -> '
                                                 r'([-+]?\d*\.?\d+).*')

        self.dihed_omega_atoms = ['CA', 'N', 'C', 'CA']  # OMEGA dihedral angle defined by CA(i), N(i), C(i-1), CA(i-1)

    def setDebugMode(self, debug):
        self.__debug = debug

    # Enter a parse tree produced by AmberMRParser#amber_mr.
    def enterAmber_mr(self, ctx: AmberMRParser.Amber_mrContext):  # pylint: disable=unused-argument
        self.__polySeqRst = []

    # Exit a parse tree produced by AmberMRParser#amber_mr.
    def exitAmber_mr(self, ctx: AmberMRParser.Amber_mrContext):  # pylint: disable=unused-argument
        if self.__hasPolySeq and self.__polySeqRst is not None:
            sortPolySeqRst(self.__polySeqRst)

            file_type = 'nm-res-amb'

            self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst)
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

                        self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst)
                        self.__chainAssign, _ = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__polySeq, self.__polySeqRst, self.__seqAlign)

                trimSequenceAlignment(self.__seqAlign, self.__chainAssign)

            if 'Missing data' in self.warningMessage:
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

    # Enter a parse tree produced by AmberMRParser#comment.
    def enterComment(self, ctx: AmberMRParser.CommentContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#comment.
    def exitComment(self, ctx: AmberMRParser.CommentContext):
        comment = []
        for col in range(20):
            if ctx.Any_name(col):
                text = str(ctx.Any_name(col))
                if text[0] in ('#', '!'):
                    break
                comment.append(str(ctx.Any_name(col)))
            else:
                break
        self.lastComment = None if len(comment) == 0 else ' '.join(comment)

        if self.lastComment:
            if len(comment) == 1 and self.__hasNonPoly:
                self.lastElemName = ''.join([s for s in self.lastComment.upper() if not s.isdigit()])
                if not any(np for np in self.__nonPoly if self.lastElemName in np['auth_comp_id']):
                    self.lastElemName = None
                if self.lastElemName is not None:
                    if self.metalIonMapping is None:
                        self.metalIonMapping = {}
                    self.metalIonMapping[self.lastElemName] = []

            if self.dihed_plane_residue_pat.match(self.lastComment):
                g = self.dihed_plane_residue_pat.search(self.lastComment).groups()
                self.lastPlaneSeqId = int(g[0])

    # Enter a parse tree produced by AmberMRParser#nmr_restraint.
    def enterNmr_restraint(self, ctx: AmberMRParser.Nmr_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#nmr_restraint.
    def exitNmr_restraint(self, ctx: AmberMRParser.Nmr_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#noesy_volume_restraint.
    def enterNoesy_volume_restraint(self, ctx: AmberMRParser.Noesy_volume_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#noesy_volume_restraint.
    def exitNoesy_volume_restraint(self, ctx: AmberMRParser.Noesy_volume_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#chemical_shift_restraint.
    def enterChemical_shift_restraint(self, ctx: AmberMRParser.Chemical_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#chemical_shift_restraint.
    def exitChemical_shift_restraint(self, ctx: AmberMRParser.Chemical_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#pcs_restraint.
    def enterPcs_restraint(self, ctx: AmberMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#pcs_restraint.
    def exitPcs_restraint(self, ctx: AmberMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#dipolar_coupling_restraint.
    def enterDipolar_coupling_restraint(self, ctx: AmberMRParser.Dipolar_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#dipolar_coupling_restraint.
    def exitDipolar_coupling_restraint(self, ctx: AmberMRParser.Dipolar_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#csa_restraint.
    def enterCsa_restraint(self, ctx: AmberMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#csa_restraint.
    def exitCsa_restraint(self, ctx: AmberMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#restraint_statement.
    def enterRestraint_statement(self, ctx: AmberMRParser.Restraint_statementContext):  # pylint: disable=unused-argument
        self.nmrRestraints += 1

        self.__cur_subtype = ''

        self.numIatCol = 0
        self.setIatCol = None
        self.iat = [0] * 8

        self.likeDist = False

        self.numIgrCol = None
        self.setIgrCol = None
        self.igr = None

        self.ixpk = -1
        self.nxpk = -1

        self.iresid = 0

        self.numAtnamCol = 0
        self.setAtnamCol = None
        self.atnam = [''] * 8

        self.numGrnamCol = None
        self.setGrnamCol = None
        self.grnam = None

        # No need to reset R1/2/3/4 because Amber allows to refer the previous value defined
        # self.lowerLinearLimit = None
        # self.lowerLimit = None
        # self.upperLimit = None
        # self.upperLinearLimit = None

        self.hasFuncExprs = False

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by AmberMRParser#restraint_statement.
    def exitRestraint_statement(self, ctx: AmberMRParser.Restraint_statementContext):  # pylint: disable=unused-argument

        try:

            self.detectRestraintType(self.likeDist)

            if len(self.__cur_subtype) == 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Couldn't specify NMR restraint type because the number of columns in the 'iat' clause did not match.\n"
                return

            # conventional restraint
            if not self.hasFuncExprs:

                if self.setIatCol is not None and len(self.setIatCol) > 0:
                    setIatCol = sorted(self.setIatCol)
                    self.numIatCol = max(setIatCol)
                    if list(range(1, self.numIatCol + 1)) != setIatCol:
                        misIatCol = ','.join([str(col) for col in set(range(1, self.numIatCol + 1)) - set(setIatCol)])
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"Couldn't specify NMR restraint type because of missing 'iat({misIatCol})' clause(s).\n"
                        return

                # cross-check between IAT and IGRn variables
                for col in range(0, self.numIatCol):
                    iat = self.iat[col]

                    varNum = col + 1
                    varName = 'igr' + str(varNum)

                    if iat > 0 and self.igr is not None and varNum in self.igr:
                        if len(self.igr[varNum]) > 0:
                            nonpCols = [col_ for col_, val in enumerate(self.igr[varNum]) if val <= 0]
                            maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                            valArray = ','.join([str(val) for col_, val in enumerate(self.igr[varNum]) if val > 0 and col_ < maxCol])
                            if len(valArray) > 0:
                                self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                                    f"'{varName}={valArray}' has no effect because 'iat({varNum})={iat}'.\n"
                        del self.igr[varNum]

                    elif iat < 0:
                        if self.igr is None or varNum not in self.igr or len(self.igr[varNum]) == 0:
                            hint = ''
                            if self.ixpk != -1:
                                hint += f"ixpk={self.ixpk},"
                            if self.nxpk != -1:
                                hint += f"nxpk={self.nxpk},"
                            for _col in range(0, self.numIatCol):
                                if _col == col:
                                    continue
                                _varNum = _col + 1
                                if self.iat[_col] > 0:
                                    hint += f"iat({_col+1})={self.iat[_col]},"
                                elif self.igr is not None and _varNum in self.igr:
                                    nonpCols = [col_ for col_, val in enumerate(self.igr[_varNum]) if val <= 0]
                                    maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                                    valArray = ','.join([str(val) for col_, val in enumerate(self.igr[_varNum]) if val > 0 and col_ < maxCol])
                                    hint += f"igr({_col+1})={valArray},"
                            if len(hint) > 0:
                                hint = f" The peripheral atom selections are: {hint[:-1]}."
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"'{varName}' is missing despite being set 'iat({varNum})={iat}'.{hint}\n"
                        else:
                            nonpCols = [col_ for col_, val in enumerate(self.igr[varNum]) if val <= 0]
                            maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                            valArray = ','.join([str(val) for col_, val in enumerate(self.igr[varNum]) if val > 0 and col_ < maxCol])
                            if len(valArray) == 0:
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                    f"'{varName}' includes non-positive integers.\n"
                                del self.igr[varNum]
                            else:
                                nonp = [val for col_, val in enumerate(self.igr[varNum]) if val > 0 and col_ < maxCol]
                                if self.iresid == 0:
                                    if len(nonp) != len(set(nonp)):
                                        if self.__hasPolySeq:
                                            self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                                                f"'{varName}={valArray}' includes redundant integers.\n"
                                    elif len(nonp) < 2:
                                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                            f"Surprisingly '{varName}={valArray}' consists of a single integer.\n"
                                else:
                                    mask = [str(val) + '@' + grnam
                                            for col_, (val, grnam) in enumerate(zip(self.igr[varNum], self.grnam[varNum]))
                                            if val > 0 and col_ < maxCol]
                                    varName2 = 'grnam' + str(varNum)
                                    valArray2 = ','.join([val for col_, val in enumerate(self.grnam[varNum]) if len(val) > 0 and col_ < maxCol])
                                    if len(mask) != len(set(mask)):
                                        if self.__hasPolySeq:
                                            self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                                                f"'{varName}={valArray}' and '{varName2}={valArray2}' include redundant atoms.\n"
                                    elif len(nonp) < 2 or len(mask) < 2:
                                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                            f"Surprisingly '{varName}={valArray}' consists of a single integer "\
                                            f"or '{varName2}={valArray2}' consists of a single string.\n"
                                self.igr[varNum] = list(set(nonp))  # trimming non-positive/redundant integer

                self.iat = self.iat[0:self.numIatCol]  # trimming default zero integer

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None or self.iresid == 1:

                    self.__hasComments = True

                    subtype_name = ''
                    if self.__cur_subtype == 'dist':
                        subtype_name = ' as a distance restraint'
                    elif self.__cur_subtype == 'ang':
                        subtype_name = ' as an angle restraint'
                    elif self.__cur_subtype == 'dihed':
                        subtype_name = ' as a dihedral angle restraint'
                    lastComment = str(self.lastComment)
                    hint = '' if lastComment is None else\
                        (" or ambiguous atom name mapping information generated by 'makeDIST_RST' should be attached to the AMBER restraint file "
                         f"for interpretation of Sander comment {lastComment!r}{subtype_name}, "
                         if 'AMB' in lastComment and (('-' in lastComment and ':' in lastComment) or '.' in lastComment)
                         else f" or Sander comment {lastComment!r} couldn't be interpreted{subtype_name}")

                    for col, iat in enumerate(self.iat):

                        atomSelection = []

                        if self.iresid == 0:

                            if iat > 0:
                                if iat in self.__atomNumberDict:
                                    atomSelection.append(self.__atomNumberDict[iat])
                                else:
                                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                        f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file{hint}.\n"
                            elif iat < 0:
                                varNum = col + 1
                                if self.igr is None:
                                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                        f"'igr({varNum})' is not defined in the AMBER parameter/topology file{hint}.\n"
                                elif varNum in self.igr:
                                    for igr in self.igr[varNum]:
                                        if igr in self.__atomNumberDict:
                                            atomSelection.append(self.__atomNumberDict[igr])
                                        else:
                                            self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                                f"'igr({varNum})={igr}' is not defined in the AMBER parameter/topology file{hint}.\n"

                        else:

                            if iat > 0:
                                if col >= len(self.atnam):
                                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                        f"'atnam({col+1})' is missing despite being set iresid=1, iat({col+1})={iat}.\n"
                                else:
                                    atnam = self.atnam[col]
                                    if len(atnam) == 0:
                                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                            f"'atnam({col+1})={atnam}' is empty despite being set iresid=1, iat({col+1})={iat}.\n"
                                    else:
                                        factor = self.getAtomNumberDictFromAmbmaskInfo(iat, self.atnam[col])
                                        if factor is not None:
                                            atomSelection.append(factor)

                            elif iat < 0:
                                varNum = col + 1
                                if self.igr is None:
                                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                        f"'igr({varNum})' is not defined in the AMBER parameter/topology file{hint}.\n"
                                elif varNum in self.igr:
                                    if varNum not in self.grnam:
                                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                            f"'grnam({varNum})' is missing despite being set iresid=1, igr({varNum})={self.igr[varNum]}.\n"
                                    else:
                                        for igr, grnam in zip(self.igr[varNum], self.grnam[varNum]):
                                            if len(grnam) == 0:
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"'grnam({varNum})={self.grnam[varNum]}' is empty "\
                                                    f"despite being set iresid=1, igr({varNum})={self.igr[varNum]}.\n"
                                            else:
                                                factor = self.getAtomNumberDictFromAmbmaskInfo(igr, grnam)
                                                if factor is not None:
                                                    atomSelection.append(factor)

                        self.atomSelectionSet.append(atomSelection)

                    if self.lastComment is not None:
                        if self.__debug:
                            print('# ' + self.lastComment)

                    updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                    if self.__cur_subtype == 'dist':

                        dstFunc = self.validateDistanceRange(1.0)

                        if dstFunc is None:
                            return

                        lenIat = len(self.iat)

                        # simple distance
                        if lenIat == COL_DIST:
                            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                                  self.atomSelectionSet[1]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                          f"atom1={atom1} atom2={atom2} {dstFunc}")

                        # generalized distance
                        else:

                            # generalized distance 2
                            if lenIat == COL_DIST_COORD2:
                                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                                    self.atomSelectionSet[1],
                                                                                    self.atomSelectionSet[2],
                                                                                    self.atomSelectionSet[3]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                              f"weight=[{self.rstwt[0]}, {self.rstwt[1]}] "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"{dstFunc}")

                            # generalized distance 3
                            elif lenIat == COL_DIST_COORD3:
                                for atom1, atom2, atom3, atom4, atom5, atom6 in itertools.product(self.atomSelectionSet[0],
                                                                                                  self.atomSelectionSet[1],
                                                                                                  self.atomSelectionSet[2],
                                                                                                  self.atomSelectionSet[3],
                                                                                                  self.atomSelectionSet[4],
                                                                                                  self.atomSelectionSet[5]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                              f"weight=[{self.rstwt[0]}, {self.rstwt[1]}, {self.rstwt[2]}] "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"|atom5={atom5} atom6={atom6}| "
                                              f"{dstFunc}")

                            # generalized distance 4
                            else:
                                for atom1, atom2, atom3, atom4, atom5, atom6, atom7, atom8 in itertools.product(self.atomSelectionSet[0],
                                                                                                                self.atomSelectionSet[1],
                                                                                                                self.atomSelectionSet[2],
                                                                                                                self.atomSelectionSet[3],
                                                                                                                self.atomSelectionSet[4],
                                                                                                                self.atomSelectionSet[5],
                                                                                                                self.atomSelectionSet[6],
                                                                                                                self.atomSelectionSet[7]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                              f"weight={self.rstwt} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"|atom5={atom5} atom6={atom6}| "
                                              f"|atom7={atom7} atom8={atom8}| "
                                              f"{dstFunc}")

                            self.rstwt = [0.0, 0.0, 0.0, 0.0]

                    # angle
                    elif self.__cur_subtype == 'ang':
                        valid = True
                        for col, iat in enumerate(self.iat):
                            if iat < 0:
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                    f"Ambiguous atom selection 'iat({col+1})={iat}' is not allowed as a angle restraint.\n"
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[0],
                                                                     self.atomSelectionSet[1],
                                                                     self.atomSelectionSet[2]):
                            if isLongRangeRestraint([atom1, atom2, atom3]):
                                continue
                            if self.__debug:
                                print(f"subtype={self.__cur_subtype} id={self.angRestraints} "
                                      f"atom1={atom1} atom2={atom2} atom3={atom3} {dstFunc}")

                    # torsional angle
                    elif self.__cur_subtype == 'dihed':
                        valid = True
                        for col, iat in enumerate(self.iat):
                            if iat < 0:
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                    f"Ambiguous atom selection 'iat({col+1})={iat}' is not allowed as a torsional angle restraint.\n"
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        if len(self.atomSelectionSet[0]) == 0:
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
                                print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} "
                                      f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

                    # plane-(point/plane) angle
                    else:
                        valid = True
                        for col, iat in enumerate(self.iat):
                            if iat < 0:
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                    f"Ambiguous atom selection 'iat({col+1})={iat}' is not allowed as a plane-(point/plane) angle restraint.\n"
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        # plane-point angle
                        if lenIat == COL_PLANE_POINT:
                            for atom1, atom2, atom3, atom4, atom5 in itertools.product(self.atomSelectionSet[0],
                                                                                       self.atomSelectionSet[1],
                                                                                       self.atomSelectionSet[2],
                                                                                       self.atomSelectionSet[3],
                                                                                       self.atomSelectionSet[4]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.planeRestraints} "
                                          f"plane: |atom_1={atom1} atom_2={atom2} atom_3={atom3} atom_4={atom4}| "
                                          f"point: atom={atom5}"
                                          f"{dstFunc}")

                        # plane-plane angle
                        else:
                            for atom1, atom2, atom3, atom4, atom5, atom6, atom7, atom8 in itertools.product(self.atomSelectionSet[0],
                                                                                                            self.atomSelectionSet[1],
                                                                                                            self.atomSelectionSet[2],
                                                                                                            self.atomSelectionSet[3],
                                                                                                            self.atomSelectionSet[4],
                                                                                                            self.atomSelectionSet[5],
                                                                                                            self.atomSelectionSet[6],
                                                                                                            self.atomSelectionSet[7]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.planeRestraints} "
                                          f"plane_1: |atom_1={atom1} atom_2={atom2} atom_3={atom3} atom_4={atom4}| "
                                          f"plane_2: |atom_1={atom5} atom_2={atom6} atom_3={atom7} atom_4={atom8}| "
                                          f"{dstFunc}")

                # try to update AMBER atom number dictionary based on Sander comments
                elif self.__hasPolySeq and self.iresid == 0:

                    self.__hasComments = True

                    if self.__cur_subtype == 'dist' and len(self.iat) == COL_DIST:
                        subtype_name = 'distance restraint'

                        e = self.lastElemName

                        g = None\
                            if self.lastComment is None or not self.dist_sander_pat.match(self.lastComment)\
                            else self.dist_sander_pat.search(self.lastComment).groups()

                        for col, iat in enumerate(self.iat):
                            offset = col * 3

                            if iat > 0:
                                if iat in self.__sanderAtomNumberDict:
                                    pass
                                else:
                                    if g is None and (e is None or col > 0):
                                        self.reportSanderCommentIssue(subtype_name)
                                        return
                                    if g is not None:
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            if 'AMB' in g[offset + 1] and ((':' in g[offset + 2] and '-' in g[offset + 2]) or '.' in g[offset + 2]):
                                                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}. "\
                                                    "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the AMBER restraint file.\n"
                                            else:
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}.\n"
                                    else:
                                        s = None
                                        for np in self.__nonPoly:
                                            for _s, _c in zip(np['auth_seq_id'], np['auth_comp_id']):
                                                if _c != e:
                                                    continue
                                                if _s in self.metalIonMapping[e]:
                                                    continue
                                                s = _s
                                                break
                                            if s is not None:
                                                break
                                        if s is None:
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {e!r}.\n"
                                        else:
                                            factor = {'auth_seq_id': s,
                                                      'auth_comp_id': e,
                                                      'auth_atom_id': e,
                                                      'iat': iat
                                                      }
                                            if self.updateSanderAtomNumberDict(factor):
                                                self.metalIonMapping[e].append(s)
                                            else:
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {e!r}.\n"

                            elif iat < 0:
                                varNum = col + 1
                                if self.igr is None:
                                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                        f"'igr({varNum})' is not defined in the AMBER parameter/topology file{hint}.\n"
                                elif varNum in self.igr:
                                    igr = self.igr[varNum]
                                    if igr[0] not in self.__sanderAtomNumberDict:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'igr': igr
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            if 'AMB' in g[offset + 1] and ((':' in g[offset + 2] and '-' in g[offset + 2]) or '.' in g[offset + 2]):
                                                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'igr({varNum})={igr}' in the coordinates "\
                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}. "\
                                                    "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the AMBER restraint file.\n"
                                            else:
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'igr({varNum})={igr}' in the coordinates "\
                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}.\n"

                    if self.__cur_subtype == 'ang':
                        subtype_name = 'angle restraint'

                        g = None\
                            if self.lastComment is None or not self.ang_sander_pat.match(self.lastComment)\
                            else self.ang_sander_pat.search(self.lastComment).groups()

                        gn = None\
                            if self.lastComment is None or not self.ang_nang_sander_pat.match(self.lastComment)\
                            else self.ang_nang_sander_pat.search(self.lastComment).groups()

                        _gn = None\
                            if self.lastComment is not None or gn is not None or self.prevComment is None\
                            or not self.ang_nang_sander_pat.match(self.prevComment)\
                            else self.ang_nang_sander_pat.search(self.prevComment).groups()

                        if _gn is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        seqId = int(_gn[0])
                                        atomId = self.ang_nang_atoms[1][col]
                                        _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                        if _factor is None:
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {self.prevComment!r}.\n"
                                            continue
                                        factor = {'auth_seq_id': seqId,
                                                  'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                  'auth_atom_id': atomId,
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {self.prevComment!r}.\n"

                            self.prevComment = None

                        elif gn is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        seqId = int(gn[0])
                                        atomId = self.ang_nang_atoms[0][col]
                                        _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                        if _factor is None:
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {self.lastComment!r}.\n"
                                            continue
                                        factor = {'auth_seq_id': seqId,
                                                  'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                  'auth_atom_id': atomId,
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {self.lastComment!r}.\n"

                        else:
                            for col, iat in enumerate(self.iat):
                                offset = col * 3 + 3

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {' '.join(g[offset:offset+3])!r}.\n"

                    if self.__cur_subtype == 'dihed':
                        subtype_name = 'torsional angle restraint'

                        g = None\
                            if self.lastComment is None or not self.dihed_sander_pat.match(self.lastComment)\
                            else self.dihed_sander_pat.search(self.lastComment).groups()

                        gc = None\
                            if self.lastComment is None or not self.dihed_chiral_sander_pat.match(self.lastComment)\
                            else self.dihed_chiral_sander_pat.search(self.lastComment).groups()

                        go = None\
                            if self.lastComment is None or not self.dihed_omega_sander_pat.match(self.lastComment)\
                            else self.dihed_omega_sander_pat.search(self.lastComment).groups()

                        gp = None\
                            if self.lastComment is None or self.lastPlaneSeqId is None or not self.dihed_plane_sander_pat.match(self.lastComment)\
                            else self.dihed_plane_sander_pat.search(self.lastComment).groups()

                        if gp is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        factor = {'auth_seq_id': self.lastPlaneSeqId,
                                                  'auth_atom_id': gp[col],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment 'PLANAR RESTRAINTS FOR RESIDUE {self.lastPlaneSeqId}' and {gp[col]!r}.\n"

                        if go is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        seqId = int(go[0])
                                        if col >= 2:
                                            seqId -= 1
                                        atomId = self.dihed_omega_atoms[col]
                                        _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                        if _factor is None:
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {self.lastComment!r}.\n"
                                            continue
                                        factor = {'auth_seq_id': seqId,
                                                  'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                  'auth_atom_id': atomId,
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {self.lastComment!r}.\n"

                        elif gc is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        seqId = int(gc[0])
                                        atomId = gc[col + 1]
                                        _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                        if _factor is None:
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {self.lastComment!r}.\n"
                                            continue
                                        factor = {'auth_seq_id': seqId,
                                                  'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                  'auth_atom_id': atomId,
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {self.lastComment!r}.\n"

                        else:
                            for col, iat in enumerate(self.iat):
                                offset = col * 3 + 3

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {' '.join(g[offset:offset+3])!r}.\n"

                elif self.lastComment is not None:
                    if not self.__hasComments:
                        self.__hasComments = True

            # Amber 10: ambmask
            else:

                self.__hasComments = True

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None:

                    # 1st plane should be processed at first due to plane-point angle restraint
                    if self.__cur_subtype == 'plane':

                        for col, funcExpr in enumerate(self.inPlane_funcExprs):

                            atomSelection = []

                            if isinstance(funcExpr, dict):
                                if 'iat' in funcExpr:
                                    iat = funcExpr['iat']
                                    if iat in self.__atomNumberDict:
                                        atomSelection.append(self.__atomNumberDict[iat])
                                    else:
                                        self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                            f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file.\n"
                                else:  # ambmask format
                                    factor = self.getAtomNumberDictFromAmbmaskInfo(funcExpr['seq_id'], funcExpr['atom_id'])
                                    if factor is not None:
                                        atomSelection.append(factor)
                            else:  # list
                                rawExprs = []
                                for _funcExpr in funcExpr:
                                    if 'igr' in _funcExpr:
                                        rawExprs.append(str(_funcExpr['igr']))
                                    else:  # ambmask format
                                        rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                    f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as a plane-(point/plane) angle restraint.\n"
                                return

                            self.atomSelectionSet.append(atomSelection)

                    for col, funcExpr in enumerate(self.funcExprs):

                        atomSelection = []

                        if isinstance(funcExpr, dict):
                            if 'iat' in funcExpr:
                                iat = funcExpr['iat']
                                if iat in self.__atomNumberDict:
                                    atomSelection.append(self.__atomNumberDict[iat])
                                else:
                                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                        f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file.\n"
                            else:  # ambmask format
                                factor = self.getAtomNumberDictFromAmbmaskInfo(funcExpr['seq_id'], funcExpr['atom_id'])
                                if factor is not None:
                                    atomSelection.append(factor)
                        else:  # list
                            for _funcExpr in funcExpr:
                                if 'igr' in _funcExpr:
                                    igr = _funcExpr['igr']
                                    if igr in self.__atomNumberDict:
                                        atomSelection.append(self.__atomNumberDict[igr])
                                    else:
                                        self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                            f"'igr({col+1})={igr}' is not defined in the AMBER parameter/topology file.\n"
                                else:  # ambmask format
                                    factor = self.getAtomNumberDictFromAmbmaskInfo(_funcExpr['seq_id'], _funcExpr['atom_id'])
                                    if factor is not None:
                                        atomSelection.append(factor)

                        self.atomSelectionSet.append(atomSelection)

                    if self.lastComment is not None:
                        if self.__debug:
                            print('# ' + self.lastComment)

                    updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                    if self.__cur_subtype == 'dist':

                        dstFunc = self.validateDistanceRange(1.0)

                        if dstFunc is None:
                            return

                        # simple distance
                        if not self.inGenDist:
                            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                                  self.atomSelectionSet[1]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                          f"atom1={atom1} atom2={atom2} {dstFunc}")

                        # generalized distance
                        else:

                            for col, funcExpr in enumerate(self.inGenDist_funcExprs):

                                atomSelection = []

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__atomNumberDict:
                                            atomSelection.append(self.__atomNumberDict[iat])
                                        else:
                                            self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                                f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file.\n"
                                    else:  # ambmask format
                                        factor = self.getAtomNumberDictFromAmbmaskInfo(funcExpr['seq_id'], funcExpr['atom_id'])
                                        if factor is not None:
                                            atomSelection.append(factor)
                                else:  # list
                                    for _funcExpr in funcExpr:
                                        if 'igr' in _funcExpr:
                                            igr = _funcExpr['igr']
                                            if igr in self.__atomNumberDict:
                                                atomSelection.append(self.__atomNumberDict[igr])
                                            else:
                                                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                                    f"'igr({col+1})={igr}' is not defined in the AMBER parameter/topology file.\n"
                                        else:  # ambmask format
                                            factor = self.getAtomNumberDictFromAmbmaskInfo(_funcExpr['seq_id'], _funcExpr['atom_id'])
                                            if factor is not None:
                                                atomSelection.append(factor)

                                self.atomSelectionSet.append(atomSelection)

                            lenWeight = len(self.inGenDist_weight)

                            # generalized distance 2
                            if lenWeight == 2:
                                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                                    self.atomSelectionSet[1],
                                                                                    self.atomSelectionSet[2],
                                                                                    self.atomSelectionSet[3]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"{dstFunc}")

                            # generalized distance 3
                            elif lenWeight == 3:
                                for atom1, atom2, atom3, atom4, atom5, atom6 in itertools.product(self.atomSelectionSet[0],
                                                                                                  self.atomSelectionSet[1],
                                                                                                  self.atomSelectionSet[2],
                                                                                                  self.atomSelectionSet[3],
                                                                                                  self.atomSelectionSet[4],
                                                                                                  self.atomSelectionSet[5]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"|atom5={atom5} atom6={atom6}| "
                                              f"{dstFunc}")

                            # generalized distance 4
                            else:
                                for atom1, atom2, atom3, atom4, atom5, atom6, atom7, atom8 in itertools.product(self.atomSelectionSet[0],
                                                                                                                self.atomSelectionSet[1],
                                                                                                                self.atomSelectionSet[2],
                                                                                                                self.atomSelectionSet[3],
                                                                                                                self.atomSelectionSet[4],
                                                                                                                self.atomSelectionSet[5],
                                                                                                                self.atomSelectionSet[6],
                                                                                                                self.atomSelectionSet[7]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"|atom5={atom5} atom6={atom6}| "
                                              f"|atom7={atom7} atom8={atom8}| "
                                              f"{dstFunc}")

                            self.rstwt = [0.0, 0.0, 0.0, 0.0]

                    # angle
                    elif self.__cur_subtype == 'ang':
                        valid = True
                        for col, funcExpr in enumerate(self.funcExprs):
                            if isinstance(funcExpr, list):
                                rawExprs = []
                                for _funcExpr in funcExpr:
                                    if 'igr' in _funcExpr:
                                        rawExprs.append(str(_funcExpr['igr']))
                                    else:  # ambmask format
                                        rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                    f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as an angle restraint.\n"
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[0],
                                                                     self.atomSelectionSet[1],
                                                                     self.atomSelectionSet[2]):
                            if isLongRangeRestraint([atom1, atom2, atom3]):
                                continue
                            if self.__debug:
                                print(f"subtype={self.__cur_subtype} id={self.angRestraints} "
                                      f"atom1={atom1} atom2={atom2} atom_3={atom3} {dstFunc}")

                    # torsional angle
                    elif self.__cur_subtype == 'dihed':
                        valid = True
                        for col, funcExpr in enumerate(self.funcExprs):
                            if isinstance(funcExpr, list):
                                rawExprs = []
                                for _funcExpr in funcExpr:
                                    if 'igr' in _funcExpr:
                                        rawExprs.append(str(_funcExpr['igr']))
                                    else:  # ambmask format
                                        rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                    f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as a torsional angle restraint.\n"
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        if len(self.atomSelectionSet[0]) == 0:
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
                                print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} "
                                      f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

                    # plane-(point/plane) angle
                    else:

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        # plane-point angle
                        if self.inPlane_columnSel == 0:

                            for col, funcExpr in enumerate(self.funcExprs, 4):
                                if isinstance(funcExpr, list):
                                    rawExprs = []
                                    for _funcExpr in funcExpr:
                                        if 'igr' in _funcExpr:
                                            rawExprs.append(str(_funcExpr['igr']))
                                        else:  # ambmask format
                                            rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                        f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as a plane-point angle restraint.\n"
                                    return

                            for atom1, atom2, atom3, atom4, atom5 in itertools.product(self.atomSelectionSet[0],
                                                                                       self.atomSelectionSet[1],
                                                                                       self.atomSelectionSet[2],
                                                                                       self.atomSelectionSet[3],
                                                                                       self.atomSelectionSet[4]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.planeRestraints} "
                                          f"plane: |atom_1={atom1} atom_2={atom2} atom_3={atom3} atom_4={atom4}| "
                                          f"point: atom={atom5}"
                                          f"{dstFunc}")

                        # plane-plane angle
                        else:

                            # 2nd plane
                            for col, funcExpr in enumerate(self.inPlane_funcExprs2, 4):

                                atomSelection = []

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__atomNumberDict:
                                            atomSelection.append(self.__atomNumberDict[iat])
                                        else:
                                            self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                                                f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file.\n"
                                    else:  # ambmask format
                                        factor = self.getAtomNumberDictFromAmbmaskInfo(funcExpr['seq_id'], funcExpr['atom_id'])
                                        if factor is not None:
                                            atomSelection.append(factor)
                                else:  # list
                                    rawExprs = []
                                    for _funcExpr in funcExpr:
                                        if 'igr' in _funcExpr:
                                            rawExprs.append(str(_funcExpr['igr']))
                                        else:  # ambmask format
                                            rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                        f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as a plane-plane angle restraint.\n"
                                    return

                                self.atomSelectionSet.append(atomSelection)

                            for atom1, atom2, atom3, atom4, atom5, atom6, atom7, atom8 in itertools.product(self.atomSelectionSet[0],
                                                                                                            self.atomSelectionSet[1],
                                                                                                            self.atomSelectionSet[2],
                                                                                                            self.atomSelectionSet[3],
                                                                                                            self.atomSelectionSet[4],
                                                                                                            self.atomSelectionSet[5],
                                                                                                            self.atomSelectionSet[6],
                                                                                                            self.atomSelectionSet[7]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.planeRestraints} "
                                          f"plane_1: |atom_1={atom1} atom_2={atom2} atom_3={atom3} atom_4={atom4}| "
                                          f"plane_2: |atom_1={atom5} atom_2={atom6} atom_3={atom7} atom_4={atom8}| "
                                          f"{dstFunc}")

                # try to update AMBER atom number dictionary based on Sander comments
                elif self.__hasPolySeq:

                    if self.__cur_subtype == 'dist' and not self.inGenDist:
                        subtype_name = 'distance restraint'

                        g = None\
                            if self.lastComment is None or not self.dist_sander_pat.match(self.lastComment)\
                            else self.dist_sander_pat.search(self.lastComment).groups()

                        for col, funcExpr in enumerate(self.funcExprs):
                            offset = col * 3

                            if isinstance(funcExpr, dict):
                                if 'iat' in funcExpr:
                                    iat = funcExpr['iat']
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                f"based on Sander comment {' '.join(g[offset:offset+3])!r}.\n"

                            else:  # list
                                igr = [_funcExpr['igr'] for _funcExpr in funcExpr if 'igr' in _funcExpr]
                                mask = [_funcExpr['atom_id'] for _funcExpr in funcExpr if 'atom_id' in _funcExpr]
                                if len(igr) > 0 and len(mask) == 0:  # support igr solely
                                    if igr[0] not in self.__sanderAtomNumberDict:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'igr': igr
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                f"Couldn't specify 'igr({col+1})={igr}' in the coordinates "\
                                                f"based on Sander comment {' '.join(g[offset:offset+3])!r}.\n"

                    elif self.__cur_subtype == 'ang':
                        subtype_name = 'angle restraint'

                        g = None\
                            if self.lastComment is None or not self.ang_sander_pat.match(self.lastComment)\
                            else self.ang_sander_pat.search(self.lastComment).groups()

                        gn = None\
                            if self.lastComment is None or not self.ang_nang_sander_pat.match(self.lastComment)\
                            else self.ang_nang_sander_pat.search(self.lastComment).groups()

                        _gn = None\
                            if self.lastComment is not None or gn is not None or self.prevComment is None\
                            or not self.ang_nang_sander_pat.match(self.prevComment)\
                            else self.ang_nang_sander_pat.search(self.prevComment).groups()

                        if _gn is not None:
                            for col, funcExpr in enumerate(self.funcExprs):

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            seqId = int(_gn[0])
                                            atomId = self.ang_nang_atoms[1][col]
                                            _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                            if _factor is None:
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {self.prevComment!r}.\n"
                                                continue
                                            factor = {'auth_seq_id': seqId,
                                                      'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                      'auth_atom_id': atomId,
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {self.prevComment!r}.\n"

                            self.prevComment = None

                        elif gn is not None:
                            for col, funcExpr in enumerate(self.funcExprs):

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            seqId = int(_gn[0])
                                            atomId = self.ang_nang_atoms[0][col]
                                            _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                            if _factor is None:
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {self.lastComment!r}.\n"
                                                continue
                                            factor = {'auth_seq_id': seqId,
                                                      'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                      'auth_atom_id': atomId,
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {self.lastComment!r}.\n"

                        else:
                            for col, funcExpr in enumerate(self.funcExprs):
                                offset = col * 3 + 3

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            if g is None:
                                                self.reportSanderCommentIssue(subtype_name)
                                                return
                                            factor = {'auth_seq_id': int(g[offset + 0]),
                                                      'auth_comp_id': g[offset + 1],
                                                      'auth_atom_id': g[offset + 2],
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}.\n"

                    elif self.__cur_subtype == 'dihed':
                        subtype_name = 'torsional angle restraint'

                        g = None\
                            if self.lastComment is None or not self.dihed_sander_pat.match(self.lastComment)\
                            else self.dihed_sander_pat.search(self.lastComment).groups()

                        gc = None\
                            if self.lastComment is None or not self.dihed_chiral_sander_pat.match(self.lastComment)\
                            else self.dihed_chiral_sander_pat.search(self.lastComment).groups()

                        go = None\
                            if self.lastComment is None or not self.dihed_omega_sander_pat.match(self.lastComment)\
                            else self.dihed_omega_sander_pat.search(self.lastComment).groups()

                        if go is not None:
                            for col, funcExpr in enumerate(self.funcExprs):

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            seqId = int(go[0])
                                            if col >= 2:
                                                seqId -= 1
                                            atomId = self.dihed_omega_atoms[col]
                                            _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                            if _factor is None:
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {self.lastComment!r}.\n"
                                                continue
                                            factor = {'auth_seq_id': seqId,
                                                      'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                      'auth_atom_id': atomId,
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {self.lastComment!r}.\n"

                        elif gc is not None:
                            for col, funcExpr in enumerate(self.funcExprs):

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            seqId = int(gc[0])
                                            atomId = gc[col + 1]
                                            _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                            if _factor is None:
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {self.lastComment!r}.\n"
                                                continue
                                            factor = {'auth_seq_id': seqId,
                                                      'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                      'auth_atom_id': atomId,
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {self.lastComment!r}.\n"

                        else:
                            for col, funcExpr in enumerate(self.funcExprs):
                                offset = col * 3 + 3

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            if g is None:
                                                self.reportSanderCommentIssue(subtype_name)
                                                return
                                            factor = {'auth_seq_id': int(g[offset + 0]),
                                                      'auth_comp_id': g[offset + 1],
                                                      'auth_atom_id': g[offset + 2],
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "\
                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}.\n"

        finally:

            if self.lastComment is not None:
                self.prevComment = self.lastComment

            self.lastComment = None

    def validateDistanceRange(self, wt):
        """ Validate distance value range.
        """

        validRange = True
        dstFunc = {'weight': wt}

        if self.lowerLimit is not None:
            if DIST_ERROR_MIN <= self.lowerLimit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{self.lowerLimit}"
            else:
                if self.lowerLimit <= DIST_ERROR_MIN and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The lower limit value 'r2={self.lowerLimit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    self.lowerLimit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value 'r2={self.lowerLimit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if self.upperLimit is not None:
            if DIST_ERROR_MIN < self.upperLimit <= DIST_ERROR_MAX:
                dstFunc['upper_limit'] = f"{self.upperLimit}"
            else:
                if self.upperLimit > DIST_ERROR_MAX and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The upper limit value 'r3={self.upperLimit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    self.upperLimit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value 'r3={self.upperLimit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if self.lowerLinearLimit is not None:
            if DIST_ERROR_MIN <= self.lowerLinearLimit < DIST_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{self.lowerLinearLimit}"
            else:
                if self.lowerLinearLimit <= DIST_ERROR_MIN and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value 'r1={self.lowerLinearLimit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    self.lowerLinearLimit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if self.upperLinearLimit is not None:
            if DIST_ERROR_MIN < self.upperLinearLimit <= DIST_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{self.upperLinearLimit}"
            else:
                if self.upperLinearLimit > DIST_ERROR_MAX and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The upper linear limit value 'r4={self.upperLinearLimit}' is omitted because it is not  within range {DIST_RESTRAINT_ERROR}.\n"
                    self.upperLinearLimit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper linear limit value 'r4={self.upperLinearLimit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if self.lowerLimit is not None and self.upperLimit is not None:
            if self.lowerLimit > self.upperLimit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value 'r2={self.lowerLimit}' must be less than the upper limit value 'r3={self.upperLimit}'.\n"

        if self.lowerLinearLimit is not None and self.upperLimit is not None:
            if self.lowerLinearLimit > self.upperLimit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be less than the upper limit value 'r3={self.upperLimit}'.\n"

        if self.lowerLimit is not None and self.upperLinearLimit is not None:
            if self.lowerLimit > self.upperLinearLimit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value 'r2={self.lowerLimit}' must be less than the upper limit value 'r4={self.upperLinearLimit}'.\n"

        if self.lowerLinearLimit is not None and self.upperLinearLimit is not None:
            if self.lowerLinearLimit > self.upperLinearLimit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be less than the upper limit value 'r4={self.upperLinearLimit}'.\n"

        if self.lowerLimit is not None and self.lowerLinearLimit is not None:
            if self.lowerLinearLimit > self.lowerLimit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be less than the lower limit value 'r2={self.lowerLimit}'.\n"

        if self.upperLimit is not None and self.upperLinearLimit is not None:
            if self.upperLimit > self.upperLinearLimit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value 'r3={self.upperLimit}' must be less than the upper linear limit value 'r4={self.upperLinearLimit}'.\n"

        if not validRange:
            self.lastComment = None
            return None

        if self.lowerLimit is not None:
            if DIST_RANGE_MIN <= self.lowerLimit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value 'r2={self.lowerLimit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if self.upperLimit is not None:
            if DIST_RANGE_MIN <= self.upperLimit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value 'r3={self.upperLimit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if self.lowerLinearLimit is not None:
            if DIST_RANGE_MIN <= self.lowerLinearLimit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if self.upperLinearLimit is not None:
            if DIST_RANGE_MIN <= self.upperLinearLimit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value 'r4={self.upperLinearLimit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        return dstFunc

    def validateAngleRange(self, wt):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': wt}

        if self.lowerLimit is not None:
            if ANGLE_ERROR_MIN <= self.lowerLimit < ANGLE_ERROR_MAX:
                dstFunc['lower_limit'] = f"{self.lowerLimit}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value 'r2={self.lowerLimit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if self.upperLimit is not None:
            if ANGLE_ERROR_MIN < self.upperLimit <= ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{self.upperLimit}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value 'r3={self.upperLimit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if self.lowerLinearLimit is not None:
            if ANGLE_ERROR_MIN <= self.lowerLinearLimit < ANGLE_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{self.lowerLinearLimit}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if self.upperLinearLimit is not None:
            if ANGLE_ERROR_MIN < self.upperLinearLimit <= ANGLE_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{self.upperLinearLimit}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value 'r4={self.upperLinearLimit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if self.lowerLimit is not None and self.lowerLinearLimit is not None:
            if self.lowerLinearLimit > self.lowerLimit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be less than the lower limit value 'r2={self.lowerLimit}'.\n"

        if self.upperLimit is not None and self.upperLinearLimit is not None:
            if self.upperLimit > self.upperLinearLimit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value 'r3={self.upperLimit}' must be less than the upper linear limit value 'r4={self.upperLinearLimit}'.\n"

        if not validRange:
            self.lastComment = None
            return None

        if self.lowerLimit is not None:
            if ANGLE_RANGE_MIN <= self.lowerLimit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value 'r2={self.lowerLimit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if self.upperLimit is not None:
            if ANGLE_RANGE_MIN <= self.upperLimit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value 'r3={self.upperLimit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if self.lowerLinearLimit is not None:
            if ANGLE_RANGE_MIN <= self.lowerLinearLimit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if self.upperLinearLimit is not None:
            if ANGLE_RANGE_MIN <= self.upperLinearLimit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value 'r4={self.upperLinearLimit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        return dstFunc

    def validatePcsRange(self, n, wt, tolpro, mltpro):
        """ Validate PCS value range.
        """

        obs = self.obs[n]

        validRange = True
        dstFunc = {'weight': wt, 'tolerance': tolpro, 'multiplicity': mltpro}

        if obs is not None:
            if PCS_ERROR_MIN < obs < PCS_ERROR_MAX:
                dstFunc['target_value'] = f"{obs}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(self.nmpmc,n)}"\
                    f"The target value 'obs({n})={obs}' must be within range {PCS_RESTRAINT_ERROR}.\n"

        if not validRange:
            self.lastComment = None
            return None

        if obs is not None:
            if PCS_RANGE_MIN <= obs <= PCS_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(self.nmpmc,n)}"\
                    f"The target value 'obs({n})={obs}' should be within range {PCS_RESTRAINT_RANGE}.\n"

        return dstFunc

    def validateRdcRange(self, n, wt):
        """ Validate RDC value range.
        """

        dobsl = self.dobsl[n]
        dobsu = self.dobsu[n]

        validRange = True
        dstFunc = {'weight': wt}

        if dobsl is not None:
            if RDC_ERROR_MIN < dobsl < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{dobsl}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The lower limit value 'dobsl({n})={dobsl}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if dobsu is not None:
            if RDC_ERROR_MIN < dobsu < RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{dobsu}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The upper limit value 'dobsu({n})={dobsu}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if not validRange:
            self.lastComment = None
            return None

        if dobsl is not None:
            if RDC_RANGE_MIN <= dobsl <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The lower limit value 'dobsl({n})={dobsl}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if dobsu is not None:
            if RDC_RANGE_MIN <= dobsu <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The upper limit value 'dobsu({n})={dobsu}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        return dstFunc

    def validateCsaRange(self, n, wt):
        """ Validate CSA value range.
        """

        cobsl = self.cobsl[n]
        cobsu = self.cobsu[n]

        validRange = True
        dstFunc = {'weight': wt}

        if cobsl is not None:
            if CSA_ERROR_MIN < cobsl < CSA_ERROR_MAX:
                dstFunc['lower_limit'] = f"{cobsl}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The lower limit value 'cobsl({n})={cobsl}' must be within range {CSA_RESTRAINT_ERROR}.\n"

        if cobsu is not None:
            if CSA_ERROR_MIN < cobsu < CSA_ERROR_MAX:
                dstFunc['upper_limit'] = f"{cobsu}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The upper limit value 'cobsu({n})={cobsu}' must be within range {CSA_RESTRAINT_ERROR}.\n"

        if not validRange:
            self.lastComment = None
            return None

        if cobsl is not None:
            if CSA_RANGE_MIN <= cobsl <= CSA_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The lower limit value 'cobsl({n})={cobsl}' should be within range {CSA_RESTRAINT_RANGE}.\n"

        if cobsu is not None:
            if CSA_RANGE_MIN <= cobsu <= CSA_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The upper limit value 'cobsu({n})={cobsu}' should be within range {CSA_RESTRAINT_RANGE}.\n"

        return dstFunc

    def getAtomNumberDictFromAmbmaskInfo(self, seqId, atomId, useDefault=True):
        """ Return atom number dictionary like component from Amber 10 ambmask information.
        """
        if not self.__hasPolySeq:
            return None

        cifCheck = self.__hasCoord

        authAtomId = atomId

        factor = {}

        found = False

        for ps in (self.__polySeq if useDefault else self.__altPolySeq):
            chainId = ps['auth_chain_id']

            if seqId in (ps['seq_id'] if useDefault else ps['auth_seq_id']):
                compId = ps['comp_id'][ps['seq_id'].index(seqId) if useDefault else ps['auth_seq_id'].index(seqId)]
                cifSeqId = None if useDefault else ps['seq_id'][ps['auth_seq_id'].index(seqId)]

                if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                    authCompId = ps['auth_comp_id'][ps['auth_seq_id'].index(seqId)]
                    _, _, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, authCompId, atomId)

                atomId = translateToStdAtomName(atomId, compId, ccU=self.__ccU)

                atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId)[0]

                seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck)

                for _atomId in atomIds:
                    ccdCheck = not cifCheck

                    if cifCheck:
                        if coordAtomSite is not None:
                            if _atomId in coordAtomSite['atom_id']:
                                found = True
                            elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                found = True
                                # self.__authAtomId = 'auth_atom_id'
                            elif self.__preferAuthSeq:
                                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                if _coordAtomSite is not None:
                                    if _atomId in _coordAtomSite['atom_id']:
                                        found = True
                                        self.__preferAuthSeq = False
                                        # self.__authSeqId = 'label_seq_id'
                                        seqKey = _seqKey
                                    elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                        found = True
                                        self.__preferAuthSeq = False
                                        # self.__authSeqId = 'label_seq_id'
                                        # self.__authAtomId = 'auth_atom_id'
                                        seqKey = _seqKey

                        elif self.__preferAuthSeq:
                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                            if _coordAtomSite is not None:
                                if _atomId in _coordAtomSite['atom_id']:
                                    found = True
                                    self.__preferAuthSeq = False
                                    # self.__authSeqId = 'label_seq_id'
                                    seqKey = _seqKey
                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                    found = True
                                    self.__preferAuthSeq = False
                                    # self.__authSeqId = 'label_seq_id'
                                    # self.__authAtomId = 'auth_atom_id'
                                    seqKey = _seqKey

                        if found:
                            factor['chain_id'] = chainId
                            factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                            factor['comp_id'] = compId
                            factor['atom_id'] = _atomId
                            factor['auth_seq_id'] = seqId
                            factor['auth_atom_id'] = authAtomId
                            return factor

                        ccdCheck = True

                    if ccdCheck:
                        if self.__ccU.updateChemCompDict(compId):
                            cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                            if cca is not None:
                                factor['chain_id'] = chainId
                                factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                factor['comp_id'] = compId
                                factor['atom_id'] = _atomId
                                factor['auth_seq_id'] = seqId
                                factor['auth_atom_id'] = authAtomId
                                if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                    checked = False
                                    if factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                        if 'H1' in coordAtomSite['atom_id']:
                                            checked = True
                                    if _atomId[0] == 'H':
                                        ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                    if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                        if ccb is not None:
                                            bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                            if bondedTo[0] in ('N', 'O', 'S'):
                                                checked = True
                                    if not checked:
                                        self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                            f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"
                                return factor
                            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"
                            return None

        if not useDefault:
            for ps in self.__polySeq:
                chainId = ps['auth_chain_id']

                seqKey = (chainId, seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        compId = ps['comp_id'][ps['seq_id'].index(seqId)]

                        if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                            authCompId = ps['auth_comp_id'][ps['auth_seq_id'].index(seqId)]
                            _, _, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, authCompId, atomId)

                        atomId = translateToStdAtomName(atomId, compId, ccU=self.__ccU)

                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId)[0]

                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                        for _atomId in atomIds:
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        # self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            # self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    factor['chain_id'] = chainId
                                    factor['seq_id'] = seqId
                                    factor['comp_id'] = compId
                                    factor['atom_id'] = _atomId
                                    factor['auth_seq_id'] = seqId
                                    factor['auth_atom_id'] = authAtomId
                                    return factor

                                ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        factor['auth_seq_id'] = seqId
                                        factor['auth_atom_id'] = authAtomId
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            if factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                if 'H1' in coordAtomSite['atom_id']:
                                                    checked = True
                                            if _atomId[0] == 'H':
                                                ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                            if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                if ccb is not None:
                                                    bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                    if bondedTo[0] in ('N', 'O', 'S'):
                                                        checked = True
                                            if not checked:
                                                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"
                                        return factor
                                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"
                                    return None

        if not useDefault or self.__altPolySeq is None:
            return None

        return self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId, False)

    def reportSanderCommentIssue(self, subtype_name):
        """ Report Sander comment issue.
        """
        if self.lastComment is None:
            self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                "Failed to recognize AMBER atom numbers in the restraint file "\
                "because neither AMBER parameter/topology file nor Sander comment are available.\n"
        else:
            lastComment = str(self.lastComment)
            if 'AMB' in lastComment and (('-' in lastComment and ':' in lastComment) or '.' in lastComment):
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize AMBER atom numbers in the restraint file "\
                    f"To interpret Sander comment {lastComment!r} as a {subtype_name}, "\
                    "please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the AMBER restraint file.\n"
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize AMBER atom numbers in the restraint file "\
                    f"because Sander comment {lastComment!r} couldn't be interpreted as a {subtype_name}.\n"

    def updateSanderAtomNumberDict(self, factor, cifCheck=True, useDefault=True):
        """ Try to update Sander atom number dictionary.
        """
        if not self.__hasPolySeq:
            return False

        authCompId = factor['auth_comp_id'].upper() if 'auth_comp_id' in factor else 'None'
        authAtomId = factor['auth_atom_id']

        if self.__reasons is not None and 'ambig_atom_id_remap' in self.__reasons\
           and authCompId in self.__reasons['ambig_atom_id_remap'] and authAtomId in self.__reasons['ambig_atom_id_remap'][authCompId]:
            return self.updateSanderAtomNumberDictWithAmbigCode(factor, cifCheck, useDefault)

        if len(self.ambigAtomNameMapping) > 0\
           and authCompId in self.ambigAtomNameMapping and authAtomId in self.ambigAtomNameMapping[authCompId]:
            return self.updateSanderAtomNumberDictWithAmbigCode(factor, cifCheck, useDefault)

        if not self.__hasCoord:
            cifCheck = False

        found = False

        for ps in (self.__polySeq if useDefault else self.__altPolySeq):
            chainId = ps['auth_chain_id']

            if factor['auth_seq_id'] in (ps['seq_id'] if useDefault else ps['auth_seq_id']):
                seqId = factor['auth_seq_id']
                idx = ps['seq_id'].index(seqId) if useDefault else ps['auth_seq_id'].index(seqId)
                compId = ps['comp_id'][idx]
                origCompId = ps['auth_comp_id'][idx]
                cifSeqId = None if useDefault else ps['seq_id'][idx]

                if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                    _, authCompId, authAtomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, authCompId, authAtomId)

                if (((authCompId in (compId, origCompId, 'None') or compId not in monDict3) and useDefault) or not useDefault)\
                   or compId == translateToStdResName(authCompId):

                    seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck)

                    fixed = False
                    if self.__reasons is not None:
                        if 'unambig_atom_id_remap' in self.__reasons and authCompId in self.__reasons['unambig_atom_id_remap']\
                           and authAtomId in self.__reasons['unambig_atom_id_remap'][authCompId]:
                            atomIds = self.__reasons['unambig_atom_id_remap'][authCompId][authAtomId]
                            fixed = True
                    if len(self.unambigAtomNameMapping) > 0:
                        if authCompId in self.unambigAtomNameMapping\
                           and authAtomId in self.unambigAtomNameMapping[authCompId]:
                            atomIds = self.unambigAtomNameMapping[authCompId][authAtomId]
                            fixed = True

                    if not fixed:
                        authAtomId = translateToStdAtomName(authAtomId, compId, ccU=self.__ccU)

                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, authAtomId)[0]

                    if 'iat' in factor:
                        iat = factor['iat']
                        for _atomId in atomIds:
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        # self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            # self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    factor['chain_id'] = chainId
                                    factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                    factor['comp_id'] = compId
                                    factor['atom_id'] = _atomId
                                    del factor['iat']
                                    self.__sanderAtomNumberDict[iat] = factor
                                    return True

                                ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        del factor['iat']
                                        self.__sanderAtomNumberDict[iat] = factor
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            if factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                if 'H1' in coordAtomSite['atom_id']:
                                                    checked = True
                                            if _atomId[0] == 'H':
                                                ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                            if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                if ccb is not None:
                                                    bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                    if bondedTo[0] in ('N', 'O', 'S'):
                                                        checked = True
                                            if not checked:
                                                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"
                                        return True

                    elif 'igr' in factor:
                        for igr, _atomId in zip(sorted(factor['igr']), atomIds):
                            _factor = copy.copy(factor)
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        # self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            # self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    _factor['chain_id'] = chainId
                                    _factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                    _factor['comp_id'] = compId
                                    _factor['atom_id'] = _atomId
                                    del _factor['igr']
                                    self.__sanderAtomNumberDict[igr] = _factor
                                else:
                                    ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        found = True
                                        _factor['chain_id'] = chainId
                                        _factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                        _factor['comp_id'] = compId
                                        _factor['atom_id'] = _atomId
                                        del _factor['igr']
                                        self.__sanderAtomNumberDict[igr] = _factor
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            if _factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                if 'H1' in coordAtomSite['atom_id']:
                                                    checked = True
                                            if _atomId[0] == 'H':
                                                ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                            if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                if ccb is not None:
                                                    bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                    if bondedTo[0] in ('N', 'O', 'S'):
                                                        checked = True
                                            if not checked:
                                                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"

                        if found:
                            return True

        if self.__hasNonPoly and useDefault:

            for np in self.__nonPoly:
                chainId = np['auth_chain_id']

                if factor['auth_seq_id'] in np['auth_seq_id']:
                    idx = np['auth_seq_id'].index(factor['auth_seq_id'])
                    seqId = np['seq_id'][idx]
                    compId = np['comp_id'][idx]

                    authCompId = factor['auth_comp_id'].upper() if 'auth_comp_id' in factor else 'None'
                    authAtomId = factor['auth_atom_id']

                    if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                        _, compId, authAtomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, authCompId, authAtomId)

                    fixed = False
                    if self.__reasons is not None:
                        if 'unambig_atom_id_remap' in self.__reasons and authCompId in self.__reasons['unambig_atom_id_remap']\
                           and authAtomId in self.__reasons['unambig_atom_id_remap'][authCompId]:
                            atomIds = self.__reasons['unambig_atom_id_remap'][authCompId][authAtomId]
                            fixed = True
                    if len(self.unambigAtomNameMapping) > 0:
                        if authCompId in self.unambigAtomNameMapping\
                           and authAtomId in self.unambigAtomNameMapping[authCompId]:
                            atomIds = self.unambigAtomNameMapping[authCompId][authAtomId]
                            fixed = True

                    if not fixed:
                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, authAtomId)[0]

                    seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                    if 'iat' in factor:
                        iat = factor['iat']
                        for _atomId in atomIds:
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        # self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            # self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    factor['chain_id'] = chainId
                                    factor['seq_id'] = seqId
                                    factor['comp_id'] = compId
                                    factor['atom_id'] = _atomId
                                    del factor['iat']
                                    self.__sanderAtomNumberDict[iat] = factor
                                    return True

                                ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        del factor['iat']
                                        self.__sanderAtomNumberDict[iat] = factor
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            if factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                if 'H1' in coordAtomSite['atom_id']:
                                                    checked = True
                                            if _atomId[0] == 'H':
                                                ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                            if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                if ccb is not None:
                                                    bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                    if bondedTo[0] in ('N', 'O', 'S'):
                                                        checked = True
                                            if not checked:
                                                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"
                                        return True

                    elif 'igr' in factor:
                        for igr, _atomId in zip(sorted(factor['igr']), atomIds):
                            _factor = copy.copy(factor)
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        # self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            # self.__authSeqId = 'label_seq_id'
                                            # self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    _factor['chain_id'] = chainId
                                    _factor['seq_id'] = seqId
                                    _factor['comp_id'] = compId
                                    _factor['atom_id'] = _atomId
                                    del _factor['igr']
                                    self.__sanderAtomNumberDict[igr] = _factor
                                else:
                                    ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        found = True
                                        _factor['chain_id'] = chainId
                                        _factor['seq_id'] = seqId
                                        _factor['comp_id'] = compId
                                        _factor['atom_id'] = _atomId
                                        del _factor['igr']
                                        self.__sanderAtomNumberDict[igr] = _factor
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            if _factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                if 'H1' in coordAtomSite['atom_id']:
                                                    checked = True
                                            if _atomId[0] == 'H':
                                                ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                            if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                if ccb is not None:
                                                    bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                    if bondedTo[0] in ('N', 'O', 'S'):
                                                        checked = True
                                            if not checked:
                                                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"

                        if found:
                            return True

        if not useDefault or self.__altPolySeq is None:
            return False

        return self.updateSanderAtomNumberDict(factor, cifCheck, False)

    def updateSanderAtomNumberDictWithAmbigCode(self, factor, cifCheck=True, useDefault=True):
        """ Try to update Sander atom number dictionary.
        """
        if not self.__hasPolySeq:
            return False

        authCompId = factor['auth_comp_id'].upper() if 'auth_comp_id' in factor else 'None'
        authAtomId = factor['auth_atom_id']

        atomIdList = None

        try:

            if self.__reasons is not None and 'ambig_atom_id_remap' in self.__reasons\
               and authCompId in self.__reasons['ambig_atom_id_remap'] and authAtomId in self.__reasons['ambig_atom_id_remap'][authCompId]:
                atomIdList = self.__reasons['ambig_atom_id_remap'][authCompId][authAtomId]['atom_id_list']

            if len(self.ambigAtomNameMapping) > 0\
               and authCompId in self.ambigAtomNameMapping and authAtomId in self.ambigAtomNameMapping[authCompId]:
                atomIdList = self.ambigAtomNameMapping[authCompId][authAtomId]['atom_id_list']

        except KeyError:
            return False

        if atomIdList is None or len(atomIdList) == 0:
            return False

        if not self.__hasCoord:
            cifCheck = False

        allFound = True

        for atom in atomIdList:
            chainId = atom['chain_id']
            seqId = atom['seq_id']
            authCompId = atom['comp_id']
            authAtomId = atom['atom_id']

            found = False

            for ps in (self.__polySeq if useDefault else self.__altPolySeq):
                if ps['auth_chain_id'] != chainId:
                    continue

                if seqId in (ps['seq_id'] if useDefault else ps['auth_seq_id']):
                    idx = ps['seq_id'].index(seqId) if useDefault else ps['auth_seq_id'].index(seqId)
                    compId = ps['comp_id'][idx]
                    origCompId = ps['auth_comp_id'][idx]
                    cifSeqId = None if useDefault else ps['seq_id'][idx]

                    if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                        _, authCompId, authAtomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, authCompId, authAtomId)

                    if (((authCompId in (compId, origCompId, 'None') or compId not in monDict3) and useDefault) or not useDefault)\
                       or compId == translateToStdResName(authCompId):

                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck)

                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, authAtomId)[0]

                        if 'iat' in factor:
                            iat = factor['iat']
                            for _atomId in atomIds:
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    if coordAtomSite is not None:
                                        if _atomId in coordAtomSite['atom_id']:
                                            found = True
                                        elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                            found = True
                                            # self.__authAtomId = 'auth_atom_id'
                                        elif self.__preferAuthSeq:
                                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                            if _coordAtomSite is not None:
                                                if _atomId in _coordAtomSite['atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    # self.__authSeqId = 'label_seq_id'
                                                    seqKey = _seqKey
                                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    # self.__authSeqId = 'label_seq_id'
                                                    # self.__authAtomId = 'auth_atom_id'
                                                    seqKey = _seqKey

                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                    if found:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        del factor['iat']
                                        self.__sanderAtomNumberDict[iat] = factor
                                        break

                                    ccdCheck = True

                                if ccdCheck:
                                    if self.__ccU.updateChemCompDict(compId):
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if cca is not None:
                                            factor['chain_id'] = chainId
                                            factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                            factor['comp_id'] = compId
                                            factor['atom_id'] = _atomId
                                            del factor['iat']
                                            self.__sanderAtomNumberDict[iat] = factor
                                            if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                                checked = False
                                                if factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                    if 'H1' in coordAtomSite['atom_id']:
                                                        checked = True
                                                if _atomId[0] == 'H':
                                                    ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                                if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                    if ccb is not None:
                                                        bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                        if bondedTo[0] in ('N', 'O', 'S'):
                                                            checked = True
                                                if not checked:
                                                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"
                                            break

                        elif 'igr' in factor:
                            for igr, _atomId in zip(sorted(factor['igr']), atomIds):
                                _factor = copy.copy(factor)
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    if coordAtomSite is not None:
                                        if _atomId in coordAtomSite['atom_id']:
                                            found = True
                                        elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                            found = True
                                            # self.__authAtomId = 'auth_atom_id'
                                        elif self.__preferAuthSeq:
                                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                            if _coordAtomSite is not None:
                                                if _atomId in _coordAtomSite['atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    # self.__authSeqId = 'label_seq_id'
                                                    seqKey = _seqKey
                                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    # self.__authSeqId = 'label_seq_id'
                                                    # self.__authAtomId = 'auth_atom_id'
                                                    seqKey = _seqKey

                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                    if found:
                                        _factor['chain_id'] = chainId
                                        _factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                        _factor['comp_id'] = compId
                                        _factor['atom_id'] = _atomId
                                        del _factor['igr']
                                        self.__sanderAtomNumberDict[igr] = _factor
                                    else:
                                        ccdCheck = True

                                if ccdCheck:
                                    if self.__ccU.updateChemCompDict(compId):
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if cca is not None:
                                            found = True
                                            _factor['chain_id'] = chainId
                                            _factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                            _factor['comp_id'] = compId
                                            _factor['atom_id'] = _atomId
                                            del _factor['igr']
                                            self.__sanderAtomNumberDict[igr] = _factor
                                            if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                                checked = False
                                                if _factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                    if 'H1' in coordAtomSite['atom_id']:
                                                        checked = True
                                                if _atomId[0] == 'H':
                                                    ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                                if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                    if ccb is not None:
                                                        bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                        if bondedTo[0] in ('N', 'O', 'S'):
                                                            checked = True
                                                if not checked:
                                                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"

            if not found and self.__hasNonPoly and useDefault:

                for np in self.__nonPoly:
                    if np['auth_chain_id'] != chainId:
                        continue

                    if seqId in np['auth_seq_id']:
                        idx = np['auth_seq_id'].index(factor['auth_seq_id'])
                        seqId = np['seq_id'][idx]
                        compId = np['comp_id'][idx]

                        if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                            _, compId, authAtomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, authCompId, authAtomId)

                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, authAtomId)[0]

                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                        if 'iat' in factor:
                            iat = factor['iat']
                            for _atomId in atomIds:
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    if coordAtomSite is not None:
                                        if _atomId in coordAtomSite['atom_id']:
                                            found = True
                                        elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                            found = True
                                            # self.__authAtomId = 'auth_atom_id'
                                        elif self.__preferAuthSeq:
                                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                            if _coordAtomSite is not None:
                                                if _atomId in _coordAtomSite['atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    # self.__authSeqId = 'label_seq_id'
                                                    seqKey = _seqKey
                                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    # self.__authSeqId = 'label_seq_id'
                                                    # self.__authAtomId = 'auth_atom_id'
                                                    seqKey = _seqKey

                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                    if found:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        del factor['iat']
                                        self.__sanderAtomNumberDict[iat] = factor
                                        break

                                    ccdCheck = True

                                if ccdCheck:
                                    if self.__ccU.updateChemCompDict(compId):
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if cca is not None:
                                            factor['chain_id'] = chainId
                                            factor['seq_id'] = seqId
                                            factor['comp_id'] = compId
                                            factor['atom_id'] = _atomId
                                            del factor['iat']
                                            self.__sanderAtomNumberDict[iat] = factor
                                            if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                                checked = False
                                                if factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                    if 'H1' in coordAtomSite['atom_id']:
                                                        checked = True
                                                if _atomId[0] == 'H':
                                                    ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                                if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                    if ccb is not None:
                                                        bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                        if bondedTo[0] in ('N', 'O', 'S'):
                                                            checked = True
                                                if not checked:
                                                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"
                                            break

                        elif 'igr' in factor:
                            for igr, _atomId in zip(sorted(factor['igr']), atomIds):
                                _factor = copy.copy(factor)
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    if coordAtomSite is not None:
                                        if _atomId in coordAtomSite['atom_id']:
                                            found = True
                                        elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                            found = True
                                            # self.__authAtomId = 'auth_atom_id'
                                        elif self.__preferAuthSeq:
                                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                            if _coordAtomSite is not None:
                                                if _atomId in _coordAtomSite['atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    # self.__authSeqId = 'label_seq_id'
                                                    seqKey = _seqKey
                                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    # self.__authSeqId = 'label_seq_id'
                                                    # self.__authAtomId = 'auth_atom_id'
                                                    seqKey = _seqKey

                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                # self.__authSeqId = 'label_seq_id'
                                                # self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                    if found:
                                        _factor['chain_id'] = chainId
                                        _factor['seq_id'] = seqId
                                        _factor['comp_id'] = compId
                                        _factor['atom_id'] = _atomId
                                        del _factor['igr']
                                        self.__sanderAtomNumberDict[igr] = _factor
                                    else:
                                        ccdCheck = True

                                if ccdCheck:
                                    if self.__ccU.updateChemCompDict(compId):
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if cca is not None:
                                            found = True
                                            _factor['chain_id'] = chainId
                                            _factor['seq_id'] = seqId
                                            _factor['comp_id'] = compId
                                            _factor['atom_id'] = _atomId
                                            del _factor['igr']
                                            self.__sanderAtomNumberDict[igr] = _factor
                                            if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                                checked = False
                                                if _factor['seq_id'] == 1 and _atomId in ('H', 'HN'):
                                                    if 'H1' in coordAtomSite['atom_id']:
                                                        checked = True
                                                if _atomId[0] == 'H':
                                                    ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                                if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                    if ccb is not None:
                                                        bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                        if bondedTo[0] in ('N', 'O', 'S'):
                                                            checked = True
                                                if not checked:
                                                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.\n"

            if not found:
                allFound = False

        if allFound:
            return True

        if not useDefault or self.__altPolySeq is None:
            return False

        return self.updateSanderAtomNumberDictWithAmbigCode(factor, cifCheck, False)

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

    # Enter a parse tree produced by AmberMRParser#restraint_factor.
    def enterRestraint_factor(self, ctx: AmberMRParser.Restraint_factorContext):
        if ctx.IAT():
            varName = 'iat'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if decimal <= 0 or decimal > MAX_COL_IAT:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_IAT}.\n"
                    return
                if self.numIatCol > 0 and self.iresid == 0:
                    zeroCols = [col for col, val in enumerate(self.iat) if val == 0]
                    maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.iat) if val != 0 and col < maxCol])
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                        f"and '{varName}({decimal})={str(ctx.Integers())}', which will overwrite.\n"
                if self.setIatCol is None:
                    self.setIatCol = []
                if decimal in self.setIatCol and self.iresid == 0:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be unique. "\
                        f"'{varName}({decimal})={str(ctx.Integers())}' will overwrite.\n"
                else:
                    self.setIatCol.append(decimal)
                rawIntArray = str(ctx.Integers()).split(',')
                val = int(rawIntArray[0])
                if len(rawIntArray) > 1:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The '{varName}({decimal})={str(ctx.Integers())}' can not be an array of integers, "\
                        f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.\n"
                self.iat[decimal - 1] = val
                if val == 0:
                    self.setIatCol.remove(decimal)
                    if self.numIatCol >= decimal:
                        self.numIatCol = decimal - 1
                        self.__cur_subtype = ''
                else:
                    self.numIatCol = max(self.numIatCol, decimal)

            else:
                if ctx.Integers():
                    if self.setIatCol is not None and len(self.setIatCol) > 0 and self.iresid == 0:
                        valArray = ','.join([f"{varName}({valCol})={self.iat[valCol - 1]}"
                                             for valCol in self.setIatCol if self.iat[valCol - 1] != 0])
                        self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                            f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                            f"and '{varName}={str(ctx.Integers())}', which will overwrite.\n"
                    if self.numIatCol > 0 and self.iresid == 0:
                        zeroCols = [col for col, val in enumerate(self.iat) if val == 0]
                        maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                        valArray = ','.join([str(val) for col, val in enumerate(self.iat) if val != 0 and col < maxCol])
                        self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                            f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "\
                            f"and '{varName}={str(ctx.Integers())}', which will overwrite.\n"
                    rawIntArray = str(ctx.Integers()).split(',')
                    numIatCol = 0
                    for col, rawInt in enumerate(rawIntArray):
                        val = int(rawInt)
                        if val == 0:
                            break
                        self.iat[col] = val
                        numIatCol += 1
                    self.numIatCol = numIatCol
                elif ctx.MultiplicativeInt():
                    if self.setIatCol is not None and len(self.setIatCol) > 0 and self.iresid == 0:
                        valArray = ','.join([f"{varName}({valCol})={self.iat[valCol - 1]}"
                                             for valCol in self.setIatCol if self.iat[valCol - 1] != 0])
                        self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                            f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                            f"and '{varName}={str(ctx.MultiplicativeInt())}', which will overwrite.\n"
                    if self.numIatCol > 0 and self.iresid == 0:
                        zeroCols = [col for col, val in enumerate(self.iat) if val == 0]
                        maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                        valArray = ','.join([str(val) for col, val in enumerate(self.iat) if val != 0 and col < maxCol])
                        self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                            f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "\
                            f"and '{varName}={str(ctx.MultiplicativeInt())}', which will overwrite.\n"
                    offset = 0
                    for multiplicativeInt in str(ctx.MultiplicativeInt()).split(','):
                        rawMultInt = multiplicativeInt.split('*')
                        numIatCol = int(rawMultInt[0])
                        if offset + numIatCol <= 0 or offset + numIatCol > MAX_COL_IAT:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numIatCol})' derived from "\
                                f"'{str(ctx.MultiplicativeInt())}' must be in the range 1-{MAX_COL_IAT}.\n"
                            return
                        val = int(rawMultInt[1])
                        for col in range(0, numIatCol):
                            self.iat[offset + col] = val
                        if val != 0:
                            self.numIatCol = offset + numIatCol
                        else:
                            self.numIatCol = 0
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The '{varName}' values '{val}' derived from "\
                                f"'{str(ctx.MultiplicativeInt())}' must be non-zero integer.\n"
                            break
                        offset += numIatCol
                    if self.numIatCol in (2, 3, 5, 6):  # possible to specify restraint type, see also detectRestraintType()
                        self.detectRestraintType(self.numIatCol in (2, 6))

        elif ctx.IGR1() or ctx.IGR2() or ctx.IGR3() or ctx.IGR4()\
                or ctx.IGR5() or ctx.IGR6() or ctx.IGR7() or ctx.IGR8():
            varNum = 0
            if ctx.IGR1():
                varNum = 1
            if ctx.IGR2():
                varNum = 2
            if ctx.IGR3():
                varNum = 3
            if ctx.IGR4():
                varNum = 4
            if ctx.IGR5():
                varNum = 5
            if ctx.IGR6():
                varNum = 6
            if ctx.IGR7():
                varNum = 7
            if ctx.IGR8():
                varNum = 8

            varName = 'igr' + str(varNum)

            if self.igr is None:
                self.igr = {}
                self.numIgrCol = {}
                self.setIgrCol = {}

            if varNum not in self.igr:
                self.igr[varNum] = [0] * MAX_COL_IGR
                self.numIgrCol[varNum] = 0
                self.setIgrCol[varNum] = None

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if decimal <= 0 or decimal > MAX_COL_IGR:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_IGR}.\n"
                    return
                if self.numIgrCol[varNum] > 0:
                    nonpCols = [col for col, val in enumerate(self.igr[varNum]) if val <= 0]
                    maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.igr[varNum]) if val > 0 and col < maxCol])
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                        f"and '{varName}({decimal})={str(ctx.Integers())}', which will overwrite.\n"
                if self.setIgrCol[varNum] is None:
                    self.setIgrCol[varNum] = []
                if decimal in self.setIgrCol[varNum]:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be unique. "\
                        f"'{varName}({decimal})={str(ctx.Integers())}' will overwrite.\n"
                else:
                    self.setIgrCol[varNum].append(decimal)
                rawIntArray = str(ctx.Integers()).split(',')
                val = int(rawIntArray[0])
                if len(rawIntArray) > 1:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The '{varName}({decimal})={str(ctx.Integers())}' can not be an array of integers, "\
                        f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.\n"
                self.igr[varNum][decimal - 1] = val
                if val == 0:
                    self.setIgrCol[varNum].remove(decimal)
                    if self.numIgrCol[varNum] >= decimal:
                        self.numIgrCol[varNum] = decimal - 1

            else:
                if ctx.Integers():
                    if self.setIgrCol[varNum] is not None and len(self.setIgrCol[varNum]) > 0:
                        valArray = ','.join([f"{varName}({valCol})={self.igr[varNum][valCol - 1]}"
                                             for valCol in self.setIgrCol[varNum] if self.igr[varNum][valCol - 1] > 0])
                        self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                            f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                            f"and '{varName}={str(ctx.Integers())}', which will overwrite.\n"
                    if self.numIgrCol[varNum] > 0:
                        nonpCols = [col for col, val in enumerate(self.igr[varNum]) if val <= 0]
                        maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                        valArray = ','.join([str(val) for col, val in enumerate(self.igr[varNum]) if val > 0 and col < maxCol])
                        self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                            f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "\
                            f"and '{varName}={str(ctx.Integers())}', which will overwrite.\n"
                    rawIntArray = str(ctx.Integers()).split(',')
                    numIgrCol = 0
                    for col, rawInt in enumerate(rawIntArray):
                        val = int(rawInt)
                        if val <= 0:
                            break
                        self.igr[varNum][col] = val
                        numIgrCol += 1
                    self.numIgrCol[varNum] = numIgrCol
                elif ctx.MultiplicativeInt():
                    if self.setIgrCol[varNum] is not None and len(self.setIgrCol[varNum]) > 0:
                        valArray = ','.join([f"{varName}({valCol})={self.igr[varNum][valCol - 1]}"
                                             for valCol in self.setIgrCol[varNum] if self.igr[varNum][valCol - 1] > 0])
                        self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                            f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                            f"and '{varName}={str(ctx.MultiplicativeInt())}', which will overwrite.\n"
                    if self.numIgrCol[varNum] > 0:
                        nonpCols = [col for col, val in enumerate(self.igr[varNum]) if val <= 0]
                        maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                        valArray = ','.join([str(val) for col, val in enumerate(self.igr[varNum]) if val > 0 and col < maxCol])
                        self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                            f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "\
                            f"and '{varName}={str(ctx.MultiplicativeInt())}', which will overwrite.\n"
                    offset = 0
                    for multiplicativeInt in str(ctx.MultiplicativeInt()).split(','):
                        rawMultInt = multiplicativeInt.split('*')
                        numIgrCol = int(rawMultInt[0])
                        if offset + numIgrCol <= 0 or offset + numIgrCol > MAX_COL_IGR:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numIgrCol})' derived from "\
                                f"'{str(ctx.MultiplicativeInt())}' must be in the range 1-{MAX_COL_IGR}.\n"
                            return
                        val = int(rawMultInt[1])
                        for col in range(0, numIgrCol):
                            self.igr[varNum][offset + col] = val
                        if val > 0:
                            self.numIgrCol[varNum] = offset + numIgrCol
                        else:
                            self.numIgrCol[varNum] = 0
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The '{varName}' values '{val}' derived from "\
                                f"'{str(ctx.MultiplicativeInt())}' must be positive integer.\n"
                            break
                        offset += numIgrCol

        elif ctx.R1():
            self.lowerLinearLimit = float(str(ctx.Real()))

        elif ctx.R2():
            self.lowerLimit = float(str(ctx.Real()))

        elif ctx.R3():
            self.upperLimit = float(str(ctx.Real()))

        elif ctx.R4():
            self.upperLinearLimit = float(str(ctx.Real()))

        elif ctx.RSTWT():
            varName = 'rstwt'

            self.detectRestraintType(False)

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if decimal <= 0 or decimal > MAX_COL_RSTWT:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_RSTWT}.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                self.rstwt[decimal - 1] = val
                if decimal == 1:
                    self.detectRestraintType(True)

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > MAX_COL_RSTWT:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={','.join(rawRealArray)}' must not exceed {MAX_COL_RSTWT}.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray):
                        val = float(rawReal)
                        self.rstwt[col] = val
                        if col == 1:
                            self.detectRestraintType(True)
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > MAX_COL_RSTWT:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must not exceed {MAX_COL_RSTWT}.\n"
                            return
                        val = float(rawMultReal[1])
                        for col in range(0, numCol):
                            self.rstwt[offset + col] = val
                            if offset + col == 1:
                                self.detectRestraintType(True)
                        offset += numCol

        elif ctx.IALTD():
            self.detectRestraintType(True)

        elif ctx.RJCOEF():
            self.detectRestraintType(False)

        # Amber 10: ambmask
        elif ctx.RESTRAINT():
            self.hasFuncExprs = True
            self.inGenDist = False
            self.inPlane = False
            self.inPlane_columnSel = -1
            self.inCom = False
            self.funcExprs = []

        elif ctx.IXPK():
            self.ixpk = int(str(ctx.Integer()))

        elif ctx.NXPK():
            self.nxpk = int(str(ctx.Integer()))

        elif ctx.IRESID():
            self.iresid = int(str(ctx.BoolInt()))

        elif ctx.ATNAM():
            varName = 'atnam'

            if ctx.Qstrings():
                if self.setAtnamCol is not None and len(self.setAtnamCol) > 0:
                    valArray = ','.join([f"{varName}({valCol})={self.atnam[valCol - 1]}"
                                         for valCol in self.setAtnamCol if len(self.atnam[valCol - 1]) > 0])
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                        f"and '{varName}={str(ctx.Qstrings())}', which will overwrite.\n"
                if self.numAtnamCol > 0:
                    zeroCols = [col for col, val in enumerate(self.atnam) if len(val) == 0]
                    maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.atnam) if len(val) > 0 and col < maxCol])
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "\
                        f"and '{varName}={str(ctx.Qstrings())}', which will overwrite.\n"
                rawStrArray = str(ctx.Qstrings()).split(',')
                numAtnamCol = 0
                for col, rawStr in enumerate(rawStrArray):
                    val = stripOnce(stripOnce(rawStr, '\''), '"').rstrip()
                    if len(val) == 0:
                        break
                    self.atnam[col] = val
                    numAtnamCol += 1
                self.numAtnamCol = numAtnamCol

        elif ctx.ATNAM_Lp():
            varName = 'atnam'

            if ctx.Decimal_AP():
                decimal = int(str(ctx.Decimal_AP()))
                if decimal <= 0 or decimal > MAX_COL_IAT:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_IAT}.\n"
                    return
                if self.numAtnamCol > 0:
                    zeroCols = [col for col, val in enumerate(self.atnam) if len(val) == 0]
                    maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.atnam) if len(val) > 0 and col < maxCol])
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                        f"and '{varName}({decimal})={str(ctx.Qstring_AP())}', which will overwrite.\n"
                if self.setAtnamCol is None:
                    self.setAtnamCol = []
                if decimal in self.setAtnamCol:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be unique. "\
                        f"'{varName}({decimal})={str(ctx.Qstring_AP())}' will overwrite.\n"
                else:
                    self.setAtnamCol.append(decimal)
                rawStrArray = str(ctx.Qstring_AP()).split(',')
                val = stripOnce(stripOnce(rawStrArray[0], '\''), '"').rstrip()
                if len(rawStrArray) > 1:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The '{varName}({decimal})={str(ctx.Qstring_AP())}' can not be an array of strings, "\
                        f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.\n"
                self.atnam[decimal - 1] = val
                if len(val) == 0:
                    self.setAtnamCol.remove(decimal)
                    if self.numAtnamCol >= decimal:
                        self.numAtnamCol = decimal - 1

        elif ctx.GRNAM1() or ctx.GRNAM2() or ctx.GRNAM3() or ctx.GRNAM4()\
                or ctx.GRNAM5() or ctx.GRNAM6() or ctx.GRNAM7() or ctx.GRNAM8():
            varNum = 0
            if ctx.GRNAM1():
                varNum = 1
            if ctx.GRNAM2():
                varNum = 2
            if ctx.GRNAM3():
                varNum = 3
            if ctx.GRNAM4():
                varNum = 4
            if ctx.GRNAM5():
                varNum = 5
            if ctx.GRNAM6():
                varNum = 6
            if ctx.GRNAM7():
                varNum = 7
            if ctx.GRNAM8():
                varNum = 8

            varName = 'grnam' + str(varNum)

            if ctx.Qstrings():
                if self.setGrnamCol[varNum] is not None and len(self.setGrnamCol[varNum]) > 0:
                    valArray = ','.join([f"{varName}({valCol})={self.grnam[varNum][valCol - 1]}"
                                         for valCol in self.setGrnamCol[varNum] if len(self.grnam[varNum][valCol - 1]) > 0])
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                        f"and '{varName}={str(ctx.Qstrings())}', which will overwrite.\n"
                if self.numGrnamCol[varNum] > 0:
                    nonpCols = [col for col, val in enumerate(self.grnam[varNum]) if len(val) == 0]
                    maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.grnam[varNum]) if len(val) > 0 and col < maxCol])
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "\
                        f"and '{varName}={str(ctx.Qstrings())}', which will overwrite.\n"
                rawStrArray = str(ctx.Qstrings()).split(',')
                numGrnamCol = 0
                for col, rawStr in enumerate(rawStrArray):
                    val = stripOnce(stripOnce(rawStr, '\''), '"').rstrip()
                    if len(val) == 0:
                        break
                    self.grnam[varNum][col] = val
                    numGrnamCol += 1
                self.numGrnamCol[varNum] = numGrnamCol

        elif ctx.GRNAM1_Lp() or ctx.GRNAM2_Lp() or ctx.GRNAM3_Lp() or ctx.GRNAM4_Lp()\
                or ctx.GRNAM5_Lp() or ctx.GRNAM6_Lp() or ctx.GRNAM7_Lp() or ctx.GRNAM8_Lp():
            varNum = 0
            if ctx.GRNAM1_Lp():
                varNum = 1
            if ctx.GRNAM2_Lp():
                varNum = 2
            if ctx.GRNAM3_Lp():
                varNum = 3
            if ctx.GRNAM4_Lp():
                varNum = 4
            if ctx.GRNAM5_Lp():
                varNum = 5
            if ctx.GRNAM6_Lp():
                varNum = 6
            if ctx.GRNAM7_Lp():
                varNum = 7
            if ctx.GRNAM8_Lp():
                varNum = 8

            varName = 'grnam' + str(varNum)

            if self.grnam is None:
                self.grnam = {}
                self.numGrnamCol = {}
                self.setGrnamCol = {}

            if varNum not in self.grnam:
                self.grnam[varNum] = [''] * MAX_COL_IGR
                self.numGrnamCol[varNum] = 0
                self.setGrnamCol[varNum] = None

            if ctx.Decimal_AP():
                decimal = int(str(ctx.Decimal_AP()))
                if decimal <= 0 or decimal > MAX_COL_IGR:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_IGR}.\n"
                    return
                if self.numGrnamCol[varNum] > 0:
                    nonpCols = [col for col, val in enumerate(self.grnam[varNum]) if len(val) == 0]
                    maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.grnam[varNum]) if len(val) > 0 and col < maxCol])
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "\
                        f"and '{varName}({decimal})={str(ctx.Qstring_AP())}', which will overwrite.\n"
                if self.setGrnamCol[varNum] is None:
                    self.setGrnamCol[varNum] = []
                if decimal in self.setGrnamCol[varNum]:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be unique. "\
                        f"'{varName}({decimal})={str(ctx.Qstring_AP())}' will overwrite.\n"
                else:
                    self.setGrnamCol[varNum].append(decimal)
                rawStrArray = str(ctx.Qstring_AP()).split(',')
                val = stripOnce(stripOnce(rawStrArray[0], '\''), '"').rstrip()
                if len(rawStrArray) > 1:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The '{varName}({decimal})={str(ctx.Qstring_AP())}' can not be an array of strings, "\
                        f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.\n"
                self.grnam[varNum][decimal - 1] = val
                if len(val) == 0:
                    self.setGrnamCol[varNum].remove(decimal)
                    if self.numGrnamCol[varNum] >= decimal:
                        self.numGrnamCol[varNum] = decimal - 1

    def detectRestraintType(self, likeDist):
        self.likeDist = likeDist

        if len(self.__cur_subtype) > 0:
            return

        if self.numIatCol == COL_DIST:
            self.distRestraints += 1
            self.__cur_subtype = 'dist'

        elif self.numIatCol == COL_ANG:
            self.angRestraints += 1
            self.__cur_subtype = 'ang'

        elif self.numIatCol == COL_DIHED:  # torsional angle or generalized distance 2
            if likeDist:
                self.distRestraints += 1
                self.__cur_subtype = 'dist'
            else:
                self.dihedRestraints += 1
                self.__cur_subtype = 'dihed'

        elif self.numIatCol == COL_PLANE_POINT:
            self.planeRestraints += 1
            self.__cur_subtype = 'plane'

        elif self.numIatCol == COL_DIST_COORD3:  # generalized distance 3
            self.distRestraints += 1
            self.__cur_subtype = 'dist'

        elif self.numIatCol == COL_PLANE_PLANE:  # plane-plane angle or generalized distance 4
            if likeDist:
                self.distRestraints += 1
                self.__cur_subtype = 'dist'
            else:
                self.planeRestraints += 1
                self.__cur_subtype = 'plane'

    # Exit a parse tree produced by AmberMRParser#restraint_factor.
    def exitRestraint_factor(self, ctx: AmberMRParser.Restraint_factorContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#noeexp_statement.
    def enterNoeexp_statement(self, ctx: AmberMRParser.Noeexp_statementContext):  # pylint: disable=unused-argument
        self.noepkRestraints += 1
        self.__cur_subtype = 'noepk'

        self.ihp = {}
        self.jhp = {}
        self.aexp = {}
        self.arange = {}
        self.awt = {}
        self.emix = {}
        self.npeak = {}
        self.invwt1 = 0.0
        self.invwt2 = 0.0
        self.omega = 500.0  # MHz
        self.taurot = 1.0  # ns
        self.taumet = 0.0001  # ns
        self.id2o = 0

    # Exit a parse tree produced by AmberMRParser#noeexp_statement.
    def exitNoeexp_statement(self, ctx: AmberMRParser.Noeexp_statementContext):  # pylint: disable=unused-argument
        imixes = self.npeak.keys()
        if len(imixes) <= 0:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"No NOESY experiment exists.\n"
            return

        for imix in imixes:

            if imix not in self.emix:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The mixing time of the NOESY experiment emix({imix}) is unknown.\n"
                continue

            mix = self.emix[imix]

            for ipeak in range(1, self.npeak[imix] + 1):

                if ipeak not in self.ihp[imix]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The atom number involved in the NOESY peak ihp({imix},{ipeak}) was not set.\n"
                    continue

                if ipeak not in self.jhp[imix]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The atom number involved in the NOESY peak jhp({imix},{ipeak}) was not set.\n"
                    continue

                if ipeak not in self.aexp[imix]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The NOESY peak volume aexp({imix},{ipeak}) was not set.\n"
                    continue

                _iprot = self.ihp[imix][ipeak]
                _jprot = self.jhp[imix][ipeak]

                if _iprot <= 0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The atom number involved in the NOESY peak 'ihp({imix},{ipeak})={_iprot}' should be a positive integer.\n"
                    continue

                if _jprot <= 0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The atom number involved in the NOESY peak 'jhp({imix},{ipeak})={_jprot}' should be a positive integer.\n"
                    continue

                awt = 1.0
                if imix in self.awt and ipeak in self.awt[imix]:
                    awt = self.awt[imix][ipeak]
                    if awt <= 0.0:
                        awt = 1.0

                arange = 0.0
                if imix in self.arange and ipeak in self.arange[imix]:
                    arange = max(self.arange[imix][ipeak], 0.0)

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None:

                    self.atomSelectionSet = []

                    atomSelection = []

                    if _iprot in self.__atomNumberDict:
                        atomSelection.append(self.__atomNumberDict[_iprot])
                    else:
                        self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(imix,ipeak)}"\
                            f"'ihp({imix},{ipeak})={_iprot}' is not defined in the AMBER parameter/topology file.\n"
                        continue

                    chain_id = atomSelection[0]['chain_id']
                    seq_id = atomSelection[0]['seq_id']
                    comp_id = atomSelection[0]['comp_id']
                    atom_id = atomSelection[0]['atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    if atom_id[0] != 'H':
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                            f"({chain_id}:{seq_id}:{comp_id}:{atom_id} (derived from ihp) is not a proton.\n"
                        continue

                    atomSelection = []

                    if _jprot in self.__atomNumberDict:
                        atomSelection.append(self.__atomNumberDict[_jprot])
                    else:
                        self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(imix,ipeak)}"\
                            f"'jhp({imix},{ipeak})={_jprot}' is not defined in the AMBER parameter/topology file.\n"
                        continue

                    chain_id = atomSelection[0]['chain_id']
                    seq_id = atomSelection[0]['seq_id']
                    comp_id = atomSelection[0]['comp_id']
                    atom_id = atomSelection[0]['atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    if atom_id[0] != 'H':
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                            f"({chain_id}:{seq_id}:{comp_id}:{atom_id} (derived from jhp) is not a proton.\n"
                        continue

                    dstFunc = self.validateNoexpRange(imix, ipeak, awt, arange)

                    updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                    for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                          self.atomSelectionSet[1]):
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} dataset={imix} mixing_time={mix} peak={ipeak} "
                                  f"atom1={atom1} atom2={atom2} {dstFunc}")

                elif self.__hasPolySeq:
                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                        "Failed to recognize AMBER atom numbers in the NOESY volume restraint file "\
                        "because AMBER parameter/topology file is not available.\n"
                    return

    def validateNoexpRange(self, imix, ipeak, awt, arange):
        """ Validate NOESY peak volume range.
        """

        aexp = self.aexp[imix][ipeak]

        dstFunc = {'weight': awt, 'tolerance': arange}

        dstFunc['target_value'] = f"{aexp}"

        return dstFunc

    # Enter a parse tree produced by AmberMRParser#noeexp_factor.
    def enterNoeexp_factor(self, ctx: AmberMRParser.Noeexp_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#noeexp_factor.
    def exitNoeexp_factor(self, ctx: AmberMRParser.Noeexp_factorContext):
        if ctx.IHP():
            varName = 'ihp'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "\
                        f"regulated by 'npeak({imix})={self.npeak[imix]}'.\n"
                    return
                if imix not in self.ihp:
                    self.ihp[imix] = {}
                self.ihp[imix][ipeak] = int(str(ctx.Integer()))

        elif ctx.JHP():
            varName = 'jhp'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "\
                        f"regulated by 'npeak({imix})={self.npeak[imix]}'.\n"
                    return
                if imix not in self.jhp:
                    self.jhp[imix] = {}
                self.jhp[imix][ipeak] = int(str(ctx.Integer()))

        elif ctx.AEXP():
            varName = 'aexp'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "\
                        f"regulated by 'npeak({imix})={self.npeak[imix]}'.\n"
                    return
                if imix not in self.aexp:
                    self.aexp[imix] = {}
                self.aexp[imix][ipeak] = float(str(ctx.Real()))

        elif ctx.ARANGE():
            varName = 'arange'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "\
                        f"regulated by 'npeak({imix})={self.npeak[imix]}'.\n"
                    return
                if imix not in self.arange:
                    self.arange[imix] = {}
                val = float(str(ctx.Real()))
                if val < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The uncertainty of peak volume '{varName}({imix},{ipeak})={val}' must not be a negative value.\n"
                    return
                self.arange[imix][ipeak] = val

        elif ctx.AWT():
            varName = 'awt'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "\
                        f"regulated by 'npeak({imix})={self.npeak[imix]}'.\n"
                    return
                if imix not in self.awt:
                    self.awt[imix] = {}
                val = float(str(ctx.Real()))
                if val <= 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"\
                        f"The relative weight value '{varName}({imix},{ipeak})={val}' must not be a negative value.\n"
                    return
                self.awt[imix][ipeak] = val

        elif ctx.NPEAK():
            varName = 'npeak'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal(0)))
                rawIntArray = str(ctx.Integers()).split(',')
                val = int(rawIntArray[0])
                if len(rawIntArray) > 1:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The '{varName}({decimal})={str(ctx.Integers())}' can not be an array of integers, "\
                        f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.\n"
                if val > 0:
                    self.npeak[decimal] = val

            else:
                if ctx.Integers():
                    rawIntArray = str(ctx.Integers()).split(',')
                    for col, rawInt in enumerate(rawIntArray, start=1):
                        val = int(rawInt)
                        if val <= 0:
                            break
                        self.npeak[col] = val
                elif ctx.MultiplicativeInt():
                    offset = 1
                    for multiplicativeInt in str(ctx.MultiplicativeInt()).split(','):
                        rawMultInt = multiplicativeInt.split('*')
                        numNpeakCol = int(rawMultInt[0])
                        val = int(rawMultInt[1])
                        for col in range(0, numNpeakCol):
                            if val <= 0:
                                break
                            self.npeak[offset + col] = val
                        offset += numNpeakCol

        elif ctx.EMIX():
            varName = 'emix'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal(0)))
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if len(rawRealArray) > 1:
                    self.warningMessage += f"[Redundant data] {self.__getCurrentRestraint()}"\
                        f"The '{varName}({decimal})={str(ctx.Reals())}' can not be an array of reals, "\
                        f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.\n"
                if val <= 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The mixing time '{varName}({decimal})={val}' must be a positive value.\n"
                    return
                self.emix[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val <= 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The mixing time '{varName}({col})={val}' must be a positive value.\n"
                            break
                        self.emix[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 1
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numEmixCol = int(rawMultReal[0])
                        val = float(rawMultReal[1])
                        for col in range(0, numEmixCol):
                            if val <= 0.0:
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                    f"The mixing time '{varName}({col})={val}' must be a positive value.\n"
                                break
                            self.emix[offset + col] = val
                            offset += numEmixCol

        elif ctx.INVWT1():
            self.invwt1 = float(str(ctx.Real()))

        elif ctx.INVWT2():
            self.invwt2 = float(str(ctx.Real()))

        elif ctx.OMEGA():
            self.omega = float(str(ctx.Real()))

        elif ctx.TAUROT():
            self.taurot = float(str(ctx.Real()))

        elif ctx.TAUMET():
            self.taumet = float(str(ctx.Real()))

        elif ctx.ID2O():
            self.id2o = int(str(ctx.BoolInt()))

    # Enter a parse tree produced by AmberMRParser#shf_statement.
    def enterShf_statement(self, ctx: AmberMRParser.Shf_statementContext):  # pylint: disable=unused-argument
        self.procsRestraints += 1
        self.__cur_subtype = 'procs'

        self.iprot = {}
        self.obs = {}
        self.wt = {}
        self.nprot = -1

        self.shrang = {}
        self.iatr = {}
        self.natr = {}
        self.namr = {}
        self._str = {}
        self.nring = -1
        self.nter = 1
        self.cter = -1

    # Exit a parse tree produced by AmberMRParser#shf_statement.
    def exitShf_statement(self, ctx: AmberMRParser.Shf_statementContext):  # pylint: disable=unused-argument
        if self.nprot < 0 and len(self.iprot.keys()) > 0:  # pylint: disable=chained-comparison
            self.nprot = max(self.iprot.keys())

        if self.nprot <= 0:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The number of observed chemical shifts 'nprot' is the mandatory variable.\n"
            return

        for n in range(1, self.nprot + 1):

            if n not in self.iprot:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=n)}"\
                    f"The atom number involved in the chemical shifts nprot({n}) was not set.\n"
                continue

            if n not in self.obs:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=n)}"\
                    f"The observed chemical shift value obs({n}) was not set.\n"
                continue

            _iprot = self.iprot[n]

            if _iprot <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=n)}"\
                    f"The atom number involved in the chemical shift 'iprot({n})={_iprot}' should be a positive integer.\n"
                continue

            wt = 1.0
            if n in self.wt:
                wt = self.wt[n]
                if wt <= 0.0:
                    wt = 1.0

            shrang = 0.0
            if n in self.shrang:
                shrang = max(self.shrang[n], 0.0)

            # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
            if self.__atomNumberDict is not None:

                self.atomSelectionSet.clear()

                atomSelection = []

                if _iprot in self.__atomNumberDict:
                    atomSelection.append(self.__atomNumberDict[_iprot])
                else:
                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(n=n)}"\
                        f"'iprot({n})={_iprot}' is not defined in the AMBER parameter/topology file.\n"
                    continue

                chain_id = atomSelection[0]['chain_id']
                seq_id = atomSelection[0]['seq_id']
                comp_id = atomSelection[0]['comp_id']
                atom_id = atomSelection[0]['atom_id']

                self.atomSelectionSet.append(atomSelection)

                if atom_id[0] != 'H':
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=n)}"\
                        f"({chain_id}:{seq_id}:{comp_id}:{atom_id} is not a proton.\n"
                    continue

                dstFunc = self.validateShfRange(n, wt, shrang)

                if dstFunc is None:
                    return

                for atom in self.atomSelectionSet[0]:
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} n={n} "
                              f"atom={atom} {dstFunc}")

            elif self.__hasPolySeq:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize AMBER atom numbers in the chemical shift restraint file "\
                    "because AMBER parameter/topology file is not available.\n"
                return

        if self.nring <= 0:
            return

        for r in range(1, self.nring + 1):

            if r not in self.natr:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The number of atoms in a ring 'natr({r})' was not set.\n"
                continue

            for n in range(1, self.natr[r] + 1):

                if n not in self.iatr[r]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The ring atom 'iatr({n},{r})' was not set.\n"
                    continue

                _iat = self.iatr[r][n]

                if _iat <= 0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n)}"\
                        f"The atom number involved in the ring 'iatr({n},{r})={_iat}' should be a positive integer.\n"
                    continue

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None:

                    self.atomSelectionSet.clear()

                    atomSelection = []

                    if _iat in self.__atomNumberDict:
                        atomSelection.append(self.__atomNumberDict[_iat])
                    else:
                        self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                            f"The ring atom 'iatr({n},{r})={_iat}' is not defined in the AMBER parameter/topology file.\n"
                        continue

                    chain_id = atomSelection[0]['chain_id']
                    seq_id = atomSelection[0]['seq_id']
                    comp_id = atomSelection[0]['comp_id']
                    atom_id = atomSelection[0]['atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                    for atom in self.atomSelectionSet[0]:
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} iatr({n},{r}) "
                                  f"ring_atom={atom}")

                elif self.__hasPolySeq:
                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                        "Failed to recognize AMBER atom numbers in the chemical shift restraint file "\
                        "because AMBER parameter/topology file is not available.\n"
                    return

    def validateShfRange(self, n, wt, shrang):
        """ Validate chemical shift value range.
        """

        obs = self.obs[n]

        validRange = True
        dstFunc = {'weight': wt, 'tolerance': shrang}

        if obs is not None:
            if CS_ERROR_MIN < obs < CS_ERROR_MAX:
                dstFunc['target_value'] = f"{obs}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=n)}"\
                    f"The target value 'obs({n})={obs}' must be within range {CS_RESTRAINT_ERROR}.\n"

        if not validRange:
            self.lastComment = None
            return None

        if obs is not None:
            if CS_RANGE_MIN <= obs <= CS_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=n)}"\
                    f"The target value 'obs({n})={obs}' should be within range {CS_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by AmberMRParser#shf_factor.
    def enterShf_factor(self, ctx: AmberMRParser.Shf_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#shf_factor.
    def exitShf_factor(self, ctx: AmberMRParser.Shf_factorContext):
        if ctx.IPROT():
            varName = 'iprot'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                self.iprot[decimal] = int(str(ctx.Integer()))

        elif ctx.OBS():
            varName = 'obs'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                self.obs[decimal] = float(str(ctx.Real()))

        elif ctx.SHRANG():
            varName = 'shrang'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The uncertainty of observed shift '{varName}({decimal})={val}' must not be a negative value.\n"
                    return
                self.shrang[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nprot:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'nprot={self.nprot}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The uncertainty of observed shift '{varName}({col})={val}' must not be a negative.\n"
                            return
                        self.shrang[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nprot:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nprot}, "\
                                f"regulated by 'nprot={self.nprot}'.\n"
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The uncertainty of observed shift '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must not be a negative.\n"
                            return
                        for col in range(0, numCol):
                            self.shrang[offset + col + 1] = val
                        offset += numCol

        elif ctx.WT():
            varName = 'wt'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The relative weight value '{varName}({decimal})={val}' must not be a negative value.\n"
                    return
                if val == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The relative weight value '{varName}({decimal})={val}' should be a positive value.\n"
                self.wt[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nprot:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'nprot={self.nprot}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}({col})={val}' must not be a negative value.\n"
                            return
                        if val == 0.0:
                            self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}({col})={val}' should be a positive value.\n"
                        self.wt[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nprot:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nprot}, "\
                                f"regulated by 'nprot={self.nprot}'.\n"
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must not be a negative value.\n"
                            return
                        if val == 0.0:
                            self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' should be a positive value.\n"
                        for col in range(0, numCol):
                            self.wt[offset + col + 1] = val
                        offset += numCol

        elif ctx.NPROT():
            self.nprot = int(str(ctx.Integer()))
            if self.nprot <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The number of protons 'nprot={self.nprot}' must be a positive integer.\n"
                return

        elif ctx.IATR():
            varName = 'iatr'

            if ctx.Decimal(0) and ctx.Decimal(1):
                j = int(str(ctx.Decimal(0)))
                ring = int(str(ctx.Decimal(1)))
                if self.nring > 0 and ring > self.nring:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The second argument value of '{varName}({j},{ring})' must be in the range 1-{self.nring}, "\
                        f"regulated by 'nring={self.nring}'.\n"
                    return
                if ring in self.natr and j > self.natr[ring]:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The first argument value of '{varName}({j},{ring})' must be in the range 1-{self.natr[ring]}, "\
                        f"regulated by 'natr({ring})={self.natr[ring]}'.\n"
                    return
                self.iatr[ring][j] = int(str(ctx.Integer()))

        elif ctx.NATR():
            varName = 'natr'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nring > 0 and decimal > self.nring:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nring}, "\
                        f"regulated by 'nring={self.nring}'.\n"
                    return
                val = int(str(ctx.Integer()))
                if val < 0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The number of atoms in a ring '{varName}({decimal})={val}' must not be a negative integer.\n"
                    return
                self.natr[decimal] = val
                self.iatr[decimal] = {}

        elif ctx.STR():
            varName = 'str'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nring > 0 and decimal > self.nring:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nring}, "\
                        f"regulated by 'nring={self.nring}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val <= 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The relative strength value '{varName}({decimal})={val}' must be a positive value.\n"
                    return
                self._str[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nring:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'nring={self.nring}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val <= 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative strength value '{varName}({col})={val}' must be a positive value.\n"
                            return
                        self._str[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nring:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nring}, "\
                                f"regulated by 'nring={self.nring}'.\n"
                            return
                        val = float(rawMultReal[1])
                        if val <= 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative strength value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be a positive value.\n"
                            return
                        for col in range(0, numCol):
                            self._str[offset + col + 1] = val
                        offset += numCol

        elif ctx.NRING():
            self.nring = int(str(ctx.Integer()))
            if self.nring < 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The number of rings 'nring={self.nring}' must not be a negative integer.\n"
                return

        elif ctx.NTER():
            self.nter = int(str(ctx.Integer()))
            if self.cter is not None and self.nter >= self.cter:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The residue number of N-terminus 'nter={self.nter}' must be less than 'cter={self.cter}'.\n"
                return

        elif ctx.CTER():
            self.cter = int(str(ctx.Integer()))
            if self.nter >= self.cter:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The residue number of C-terminus 'cter={self.cter}' must be greater than 'nter={self.nter}'.\n"
                return

        elif ctx.NAMR():
            varName = 'namr'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nring > 0 and decimal > self.nring:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nring}, "\
                        f"regulated by 'nring={self.nring}'.\n"
                    return
                self.namr[decimal] = str(ctx.Qstring()).strip()

    # Enter a parse tree produced by AmberMRParser#pcshf_statement.
    def enterPcshf_statement(self, ctx: AmberMRParser.Pcshf_statementContext):  # pylint: disable=unused-argument
        self.pcsRestraints += 1
        self.__cur_subtype = 'pcs'

        self.iprot = {}
        self.obs = {}
        self.wt = {}
        self.tolpro = {}
        self.mltpro = {}
        self.nprot = -1
        self.nmpmc = 'undefined'
        self.optphi = {}
        self.opttet = {}
        self.optomg = {}
        self.opta1 = {}
        self.opta2 = {}
        self.optkon = 0.0
        self.nme = -1

    # Exit a parse tree produced by AmberMRParser#pcshf_statement.
    def exitPcshf_statement(self, ctx: AmberMRParser.Pcshf_statementContext):  # pylint: disable=unused-argument
        if self.nprot < 0 and len(self.iprot.keys()) > 0:  # pylint: disable=chained-comparison
            self.nprot = max(self.iprot.keys())

        if self.nprot <= 0:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The number of observed PCS values 'nprot' is the mandatory variable.\n"
            return

        if self.nme < 0 and len(self.optphi.keys()) > 0:  # pylint: disable=chained-comparison
            self.nme = max(self.optphi.keys())
        """
        if self.nme <= 0:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The number of paramagnetic centers 'nme' is the mandatory variable.\n"
            return
        """
        for n in range(1, self.nprot + 1):

            if n not in self.iprot:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,n)}"\
                    f"The atom number involved in the PCS nprot({n}) was not set.\n"
                continue

            if n not in self.obs:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,n)}"\
                    f"The observed PCS value obs({n}) was not set.\n"
                continue

            _iprot = self.iprot[n]

            if _iprot <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,n)}"\
                    f"The atom number involved in the PCS 'iprot({n})={_iprot}' should be a positive integer.\n"
                continue

            wt = 1.0
            if n in self.wt:
                wt = self.wt[n]
                if wt <= 0.0:
                    wt = 1.0

            tolpro = 1.0
            if n in self.tolpro:
                tolpro = self.tolpro[n]
                if tolpro <= 0.0:
                    tolpro = 1.0

            mltpro = 1
            if n in self.mltpro:
                mltpro = self.mltpro[n]
                if mltpro <= 0:
                    mltpro = 1

            # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
            if self.__atomNumberDict is not None:

                self.atomSelectionSet.clear()

                atomSelection = []

                if _iprot in self.__atomNumberDict:
                    atomSelection.append(self.__atomNumberDict[_iprot])
                else:
                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(self.nmpmc,n)}"\
                        f"'iprot({n})={_iprot}' is not defined in the AMBER parameter/topology file.\n"
                    continue

                chain_id = atomSelection[0]['chain_id']
                seq_id = atomSelection[0]['seq_id']
                comp_id = atomSelection[0]['comp_id']
                atom_id = atomSelection[0]['atom_id']

                self.atomSelectionSet.append(atomSelection)

                if atom_id[0] != 'H':
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,n)}"\
                        f"({chain_id}:{seq_id}:{comp_id}:{atom_id} is not a proton.\n"
                    continue

                dstFunc = self.validatePcsRange(n, wt, tolpro, mltpro)

                if dstFunc is None:
                    return

                updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                for atom in self.atomSelectionSet[0]:
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} dataset={self.nmpmc} n={n} "
                              f"atom={atom} {dstFunc}")

            elif self.__hasPolySeq:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize AMBER atom numbers in the Psuedocontact shift restraint file "\
                    "because AMBER parameter/topology file is not available.\n"
                return

    # Enter a parse tree produced by AmberMRParser#pcshf_factor.
    def enterPcshf_factor(self, ctx: AmberMRParser.Pcshf_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#pcshf_factor.
    def exitPcshf_factor(self, ctx: AmberMRParser.Pcshf_factorContext):
        if ctx.IPROT():
            varName = 'iprot'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                self.iprot[decimal] = int(str(ctx.Integer()))

        elif ctx.OBS():
            varName = 'obs'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                self.obs[decimal] = float(str(ctx.Real()))

        elif ctx.WT():
            varName = 'wt'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The relative weight value '{varName}({decimal})={val}' must not be a negative value.\n"
                    return
                if val == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The relative weight value '{varName}({decimal})={val}' should be a positive value.\n"
                self.wt[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nprot:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'nprot={self.nprot}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}({col})={val}' must not be a negative value.\n"
                            return
                        if val == 0.0:
                            self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}({col})={val}' should be a positive value.\n"
                        self.wt[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nprot:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nprot}, "\
                                f"regulated by 'nprot={self.nprot}'.\n"
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must not be a negative value.\n"
                            return
                        if val == 0.0:
                            self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' should be a positive value.\n"
                        for col in range(0, numCol):
                            self.wt[offset + col + 1] = val
                        offset += numCol

        elif ctx.TOLPRO():
            varName = 'tolpro'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val <= 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The relative tolerance value '{varName}({decimal})={val}' must be a positive value.\n"
                    return
                self.tolpro[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nprot:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'nprot={self.nprot}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val <= 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative tolerance value '{varName}({col})={val}' must be a positive value.\n"
                            return
                        self.tolpro[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nprot:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nprot}, "\
                                f"regulated by 'nprot={self.nprot}'.\n"
                            return
                        val = float(rawMultReal[1])
                        if val <= 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative tolerance value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be a positive value.\n"
                            return
                        for col in range(0, numCol):
                            self.tolpro[offset + col + 1] = val
                        offset += numCol

        elif ctx.MLTPRO():
            varName = 'mltpro'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "\
                        f"regulated by 'nprot={self.nprot}'.\n"
                    return
                val = int(str(ctx.Integer()))
                if val <= 0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The multiplicity of NMR signal of '{varName}({decimal})={val}' must be a positive integer.\n"
                    return
                self.mltpro[decimal] = val

        elif ctx.NPROT():
            self.nprot = int(str(ctx.Integer()))
            if self.nprot <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The number of protons 'nprot={self.nprot}' must be a positive integer.\n"
                return

        elif ctx.OPTPHI():
            varName = 'optphi'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "\
                        f"regulated by 'nme={self.nme}'.\n"
                    return
                self.optphi[decimal] = float(str(ctx.Real()))

        elif ctx.OPTTET():
            varName = 'opttet'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "\
                        f"regulated by 'nme={self.nme}'.\n"
                    return
                self.opttet[decimal] = float(str(ctx.Real()))

        elif ctx.OPTOMG():
            varName = 'optomg'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "\
                        f"regulated by 'nme={self.nme}'.\n"
                    return
                self.optomg[decimal] = float(str(ctx.Real()))

        elif ctx.OPTA1():
            varName = 'opta1'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "\
                        f"regulated by 'nme={self.nme}'.\n"
                    return
                self.opta1[decimal] = float(str(ctx.Real()))

        elif ctx.OPTA2():
            varName = 'opta2'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "\
                        f"regulated by 'nme={self.nme}'.\n"
                    return
                self.opta2[decimal] = float(str(ctx.Real()))

        elif ctx.OPTKON():
            self.optkon = float(str(ctx.Real()))

        elif ctx.NME():
            self.nme = int(str(ctx.Integer()))
            if self.nme <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The number of paramagnetic centers 'nme={self.nme}' must be a positive integer.\n"
                return

        elif ctx.NMPMC():
            self.nmpmc = str(ctx.Qstring()).strip()

    # Enter a parse tree produced by AmberMRParser#align_statement.
    def enterAlign_statement(self, ctx: AmberMRParser.Align_statementContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

        self.id = {}
        self.jd = {}
        self.dobsl = {}
        self.dobsu = {}
        self.dwt = {}
        self.gigj = {}
        self.dij = {}
        self.ndip = -1
        self.dataset = 1
        self.numDatasets = 1
        self.s11 = {}
        self.s12 = {}
        self.s13 = {}
        self.s22 = {}
        self.s23 = {}

    # Exit a parse tree produced by AmberMRParser#align_statement.
    def exitAlign_statement(self, ctx: AmberMRParser.Align_statementContext):  # pylint: disable=unused-argument
        if self.ndip < 0 and len(self.id.keys()) > 0:  # pylint: disable=chained-comparison
            self.ndip = max(self.id.keys())

        if self.ndip <= 0:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The number of observed dipolar couplings 'ndip' is the mandatory variable.\n"
            return

        for n in range(1, self.ndip + 1):

            if n not in self.id:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The first atom number involved in the dipolar coupling id({n}) was not set.\n"
                continue

            if n not in self.jd:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The second atom number involved in the dipolar coupling jd({n}) was not set.\n"
                continue

            if n not in self.dobsl:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The lower limit value for the observed dipolar coupling dobsl({n}) was not set.\n"
                continue

            if n not in self.dobsu:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The upper limit value for the observed dipolar coupling dobsu({n}) was not set.\n"
                continue

            _id = self.id[n]
            _jd = self.jd[n]

            if _id <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The first atom number involved in the dipolar coupling 'id({n})={_id}' should be a positive integer.\n"
                continue

            if _jd <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                    f"The second atom number involved in the dipolar coupling 'jd({n})={_jd}' should be a positive integer.\n"
                continue

            dwt = 1.0
            if n in self.dwt:
                dwt = self.dwt[n]
                if dwt <= 0.0:
                    dwt = 1.0

            # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
            if self.__atomNumberDict is not None:

                self.atomSelectionSet.clear()

                atomSelection = []

                if _id in self.__atomNumberDict:
                    atomSelection.append(self.__atomNumberDict[_id])
                else:
                    atom_id_i = None
                    if _jd in self.__atomNumberDict:
                        atom_sel_j = self.__atomNumberDict[_jd]
                        comp_id_j = atom_sel_j['comp_id']
                        atom_id_j = atom_sel_j['atom_id']
                        if self.__ccU.updateChemCompDict(comp_id_j):  # matches with comp_id in CCD
                            if atom_id_j[0] == 'H':
                                b = next((b for b in self.__ccU.lastBonds
                                          if atom_id_j in (b[self.__ccU.ccbAtomId1], b[self.__ccU.ccbAtomId2])), None)
                            else:
                                b = next((b for b in self.__ccU.lastBonds
                                          if (b[self.__ccU.ccbAtomId1] == atom_id_j and b[self.__ccU.ccbAtomId2][0] != 'H')
                                          or (b[self.__ccU.ccbAtomId2] == atom_id_j and b[self.__ccU.ccbAtomId1][0] != 'H')), None)
                            if b is not None:
                                atom_id_i = b[self.__ccU.ccbAtomId1] if b[self.__ccU.ccbAtomId1] != atom_id_j else b[self.__ccU.ccbAtomId2]
                                atom_sel_i = copy.copy(atom_sel_j)
                                atom_sel_i['auth_atom_id'] = atom_sel_i['atom_id'] = atom_id_i
                                self.__atomNumberDict[_id] = atom_sel_i
                                atomSelection.append(atom_sel_i)
                    if atom_id_i is None:
                        self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(self.dataset,n)}"\
                            f"'id({n})={_id}' is not defined in the AMBER parameter/topology file.\n"
                        continue

                chain_id_1 = atomSelection[0]['chain_id']
                seq_id_1 = atomSelection[0]['seq_id']
                comp_id_1 = atomSelection[0]['comp_id']
                atom_id_1 = atomSelection[0]['atom_id']

                self.atomSelectionSet.append(atomSelection)

                atomSelection = []

                if _jd in self.__atomNumberDict:
                    atomSelection.append(self.__atomNumberDict[_jd])
                else:
                    atom_id_j = None
                    if _id in self.__atomNumberDict:
                        atom_sel_i = self.__atomNumberDict[_id]
                        comp_id_i = atom_sel_i['comp_id']
                        atom_id_i = atom_sel_i['atom_id']
                        if self.__ccU.updateChemCompDict(comp_id_i):  # matches with comp_id in CCD
                            if atom_id_i[0] == 'H':
                                b = next((b for b in self.__ccU.lastBonds
                                          if atom_id_i in (b[self.__ccU.ccbAtomId1], b[self.__ccU.ccbAtomId2])), None)
                            else:
                                b = next((b for b in self.__ccU.lastBonds
                                          if (b[self.__ccU.ccbAtomId1] == atom_id_i and b[self.__ccU.ccbAtomId2][0] != 'H')
                                          or (b[self.__ccU.ccbAtomId2] == atom_id_i and b[self.__ccU.ccbAtomId1][0] != 'H')), None)
                            if b is not None:
                                atom_id_j = b[self.__ccU.ccbAtomId1] if b[self.__ccU.ccbAtomId1] != atom_id_i else b[self.__ccU.ccbAtomId2]
                                atom_sel_j = copy.copy(atom_sel_i)
                                atom_sel_j['auth_atom_id'] = atom_sel_j['atom_id'] = atom_id_j
                                self.__atomNumberDict[_jd] = atom_sel_j
                                atomSelection.append(atom_sel_j)
                    if atom_id_j is None:
                        self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(self.dataset,n)}"\
                            f"'jd({n})={_jd}' is not defined in the AMBER parameter/topology file.\n"
                        continue

                chain_id_2 = atomSelection[0]['chain_id']
                seq_id_2 = atomSelection[0]['seq_id']
                comp_id_2 = atomSelection[0]['comp_id']
                atom_id_2 = atomSelection[0]['atom_id']

                self.atomSelectionSet.append(atomSelection)

                if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                        f"Non-magnetic susceptible spin appears in RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    continue

                if chain_id_1 != chain_id_2:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                        f"Found inter-chain RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    continue

                if abs(seq_id_1 - seq_id_2) > 1:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                        f"Found inter-residue RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    continue

                if abs(seq_id_1 - seq_id_2) == 1:

                    if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                            ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                             or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                        pass

                    else:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                            "Found inter-residue RDC vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        continue

                elif atom_id_1 == atom_id_2:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                        "Found zero RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    continue

                elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                    if not any(b for b in self.__ccU.lastBonds
                               if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                                   or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                        if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"\
                                "Found an RDC vector over multiple covalent bonds; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                            continue

                dstFunc = self.validateRdcRange(n, dwt)

                if dstFunc is None:
                    return

                updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if isLongRangeRestraint([atom1, atom2]):
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} dataset={self.dataset} n={n} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")

            elif self.__hasPolySeq:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize AMBER atom numbers in the Direct dipolar coupling restraint file "\
                    "because AMBER parameter/topology file is not available.\n"
                return

        # Enter a parse tree produced by AmberMRParser#align_factor.
    def enterAlign_factor(self, ctx: AmberMRParser.Align_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#align_factor.
    def exitAlign_factor(self, ctx: AmberMRParser.Align_factorContext):
        if ctx.ID():
            varName = 'id'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                self.id[decimal] = int(str(ctx.Integer()))

        elif ctx.JD():
            varName = 'jd'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                self.jd[decimal] = int(str(ctx.Integer()))

        elif ctx.DOBSL():
            varName = 'dobsl'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                self.dobsl[decimal] = float(str(ctx.Real()))

        elif ctx.DOBSU():
            varName = 'dobsu'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                self.dobsu[decimal] = float(str(ctx.Real()))

        elif ctx.DOBS():
            varName = 'dobs'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                self.dobsl[decimal] = self.dobsu[decimal] = float(str(ctx.Real()))

        elif ctx.DWT():
            varName = 'dwt'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The relative weight value '{varName}({decimal})={val}' must not be a negative value.\n"
                    return
                if val == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The relative weight value '{varName}({decimal})={val}' should be a positive value.\n"
                self.dwt[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}({col})={val}' must not be a negative value.\n"
                            return
                        if val == 0.0:
                            self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}({col})={val}' should be a positive value.\n"
                        self.dwt[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.ndip:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.ndip}, "\
                                f"regulated by 'ndip={self.ndip}'.\n"
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must not be a negative value.\n"
                            return
                        if val == 0.0:
                            self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' should be a positive value.\n"
                        for col in range(0, numCol):
                            self.dwt[offset + col + 1] = val
                        offset += numCol

        elif ctx.GIGJ():
            varName = 'gigj'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.gigj[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.gigj[col] = float(rawReal)
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.ndip:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.ndip}, "\
                                f"regulated by 'ndip={self.ndip}'.\n"
                            return
                        val = float(rawMultReal[1])
                        for col in range(0, numCol):
                            self.gigj[offset + col + 1] = val
                        offset += numCol

        elif ctx.DIJ():
            varName = 'dij'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.dij[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.dij[col] = float(rawReal)
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.ndip:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.ndip}, "\
                                f"regulated by 'ndip={self.ndip}'.\n"
                            return
                        val = float(rawMultReal[1])
                        for col in range(0, numCol):
                            self.dij[offset + col + 1] = val
                        offset += numCol

        elif ctx.NDIP():
            self.ndip = int(str(ctx.Integer()))
            if self.ndip <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The argument value of 'ndip={self.ndip}' must be a positive integer.\n"
                return

        if ctx.DATASET():
            varName = 'dataset'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return

            self.dataset = int(str(ctx.Integer()))

            if self.dataset <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The argument value of '{varName}={self.dataset}' must be a positive integer.\n"
                return

            if self.dataset > self.numDatasets:
                self.numDatasets = self.dataset
                """
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The argument value of '{varName}={self.dataset}' must be in the range 1-{self.numDatasets}, "\
                    f"regulated by 'num_dataset={self.numDatasets}'.\n"
                return
                """
        elif ctx.NUM_DATASETS():
            self.numDatasets = int(str(ctx.Integer()))
            if self.numDatasets <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The argument value of 'num_dataset={self.numDatasets}' must be a positive integer.\n"
                return

        elif ctx.S11():
            varName = 's11'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s11[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s11[col] = float(rawReal)

        elif ctx.S12():
            varName = 's12'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s12[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s12[col] = float(rawReal)

        elif ctx.S13():
            varName = 's13'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s13[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s13[col] = float(rawReal)

        elif ctx.S22():
            varName = 's22'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s22[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s22[col] = float(rawReal)

        elif ctx.S23():
            varName = 's23'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "\
                        f"regulated by 'ndip={self.ndip}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s23[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s23[col] = float(rawReal)

    # Enter a parse tree produced by AmberMRParser#csa_statement.
    def enterCsa_statement(self, ctx: AmberMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        self.csaRestraints += 1
        self.__cur_subtype = 'csa'

        self.icsa = {}
        self.jcsa = {}
        self.kcsa = {}
        self.cobsl = {}
        self.cobsu = {}
        self.cwt = {}
        self.ncsa = -1
        self.datasetc = 1

    # Exit a parse tree produced by AmberMRParser#csa_statement.
    def exitCsa_statement(self, ctx: AmberMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        if self.ncsa < 0 and len(self.icsa.keys()) > 0:  # pylint: disable=chained-comparison
            self.ncsa = max(self.icsa.keys())

        if self.ncsa <= 0:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The number of observed CSA values 'ncsa' is the mandatory variable.\n"
            return

        for n in range(1, self.ncsa + 1):

            if n not in self.icsa:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The first atom number involved in the CSA icsa({n}) was not set.\n"
                continue

            if n not in self.jcsa:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The second atom number involved in the CSA jcsa({n}) was not set.\n"
                continue

            if n not in self.kcsa:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The second atom number involved in the CSA kcsa({n}) was not set.\n"
                continue

            if n not in self.cobsl:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The lower limit value for the observed CSA cobsl({n}) was not set.\n"
                continue

            if n not in self.cobsu:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The upper limit value for the observed CSA cobsu({n}) was not set.\n"
                continue

            _icsa = self.icsa[n]
            _jcsa = self.jcsa[n]
            _kcsa = self.kcsa[n]

            if _icsa <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The first atom number involved in the CSA 'icsa({n})={_icsa}' should be a positive integer.\n"
                continue

            if _jcsa <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The second atom number involved in the CSA 'jcsa({n})={_jcsa}' should be a positive integer.\n"
                continue

            if _kcsa <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                    f"The second atom number involved in the CSA 'kcsa({n})={_kcsa}' should be a positive integer.\n"
                continue

            cwt = 1.0
            if n in self.cwt:
                cwt = self.cwt[n]
                if cwt <= 0.0:
                    cwt = 1.0

            # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
            if self.__atomNumberDict is not None:

                self.atomSelectionSet.clear()

                atomSelection = []

                if _icsa in self.__atomNumberDict:
                    atomSelection.append(self.__atomNumberDict[_icsa])
                else:
                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                        f"'icsa({n})={_icsa}' is not defined in the AMBER parameter/topology file.\n"
                    continue

                chain_id_1 = atomSelection[0]['chain_id']
                seq_id_1 = atomSelection[0]['seq_id']
                comp_id_1 = atomSelection[0]['comp_id']
                atom_id_1 = atomSelection[0]['atom_id']

                self.atomSelectionSet.append(atomSelection)

                atomSelection = []

                if _jcsa in self.__atomNumberDict:
                    atomSelection.append(self.__atomNumberDict[_jcsa])
                else:
                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                        f"'jcsa({n})={_jcsa}' is not defined in the AMBER parameter/topology file.\n"
                    continue

                chain_id_2 = atomSelection[0]['chain_id']
                seq_id_2 = atomSelection[0]['seq_id']
                comp_id_2 = atomSelection[0]['comp_id']
                atom_id_2 = atomSelection[0]['atom_id']

                self.atomSelectionSet.append(atomSelection)

                atomSelection = []

                if _kcsa in self.__atomNumberDict:
                    atomSelection.append(self.__atomNumberDict[_kcsa])
                else:
                    self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                        f"'kcsa({n})={_kcsa}' is not defined in the AMBER parameter/topology file.\n"
                    continue

                chain_id_3 = atomSelection[0]['chain_id']
                seq_id_3 = atomSelection[0]['seq_id']
                comp_id_3 = atomSelection[0]['comp_id']
                atom_id_3 = atomSelection[0]['atom_id']

                self.atomSelectionSet.append(atomSelection)

                if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)\
                   or (atom_id_3[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                        f"Non-magnetic susceptible spin appears in CSA vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                        f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                    continue

                if chain_id_1 != chain_id_2 or chain_id_2 != chain_id_3:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                        f"Found inter-chain CSA vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                        f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                    continue

                if abs(seq_id_1 - seq_id_2) > 1 or abs(seq_id_2 - seq_id_3) > 1 or abs(seq_id_3 - seq_id_1) > 1:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                        f"Found inter-residue CSA vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                        f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                    continue

                if abs(seq_id_1 - seq_id_2) == 1:

                    if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                            ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                             or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')):
                        pass

                    else:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                            "Found inter-residue CSA vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                            f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                        continue

                elif abs(seq_id_2 - seq_id_3) == 1:

                    if self.__csStat.peptideLike(comp_id_2) and self.__csStat.peptideLike(comp_id_3) and\
                            ((seq_id_2 < seq_id_3 and atom_id_2 == 'C' and atom_id_3 in ('N', 'H', 'CA'))
                             or (seq_id_2 > seq_id_3 and atom_id_2 in ('N', 'H', 'CA') and atom_id_3 == 'C')):
                        pass

                    else:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                            "Found inter-residue CSA vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                            f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                        continue

                elif abs(seq_id_3 - seq_id_1) == 1:

                    if self.__csStat.peptideLike(comp_id_3) and self.__csStat.peptideLike(comp_id_1) and\
                            ((seq_id_3 < seq_id_1 and atom_id_3 == 'C' and atom_id_1 in ('N', 'H', 'CA'))
                             or (seq_id_3 > seq_id_1 and atom_id_3 in ('N', 'H', 'CA') and atom_id_1 == 'C')):
                        pass

                    else:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                            "Found inter-residue CSA vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                            f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                        continue

                elif atom_id_1 == atom_id_2 or atom_id_2 == atom_id_3 or atom_id_3 == atom_id_1:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                        "Found zero CSA vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                        f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                    continue

                else:

                    if self.__ccU.updateChemCompDict(comp_id_1) and seq_id_1 == seq_id_2:  # matches with comp_id in CCD

                        if not any(b for b in self.__ccU.lastBonds
                                   if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                                       or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                            if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                                    "Found an CSA vector over multiple covalent bonds; "\
                                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                                    f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                                continue

                    if self.__ccU.updateChemCompDict(comp_id_3) and seq_id_3 == seq_id_2:  # matches with comp_id in CCD

                        if not any(b for b in self.__ccU.lastBonds
                                   if ((b[self.__ccU.ccbAtomId1] == atom_id_3 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                                       or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_3))):

                            if self.__nefT.validate_comp_atom(comp_id_3, atom_id_3) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"\
                                    "Found an CSA vector over multiple covalent bonds; "\
                                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "\
                                    f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).\n"
                                continue

                dstFunc = self.validateCsaRange(n, cwt)

                if dstFunc is None:
                    return

                updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[0],
                                                             self.atomSelectionSet[1],
                                                             self.atomSelectionSet[2]):
                    if isLongRangeRestraint([atom1, atom2, atom3]):
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} dataset={self.datasetc} n={n} "
                              f"atom1={atom1} atom2(CSA central)={atom2} atom3={atom3} {dstFunc}")

            elif self.__hasPolySeq:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize AMBER atom numbers in the Residual CSA or psuedo-CSA restraint file "\
                    "because AMBER parameter/topology file is not available.\n"
                return

    # Enter a parse tree produced by AmberMRParser#csa_factor.
    def enterCsa_factor(self, ctx: AmberMRParser.Csa_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#csa_factor.
    def exitCsa_factor(self, ctx: AmberMRParser.Csa_factorContext):
        if ctx.ICSA():
            varName = 'icsa'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "\
                        f"regulated by 'ncsa={self.ncsa}'.\n"
                    return
                self.icsa[decimal] = int(str(ctx.Integer()))

        elif ctx.JCSA():
            varName = 'jcsa'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "\
                        f"regulated by 'ncsa={self.ncsa}'.\n"
                    return
                self.jcsa[decimal] = int(str(ctx.Integer()))

        elif ctx.KCSA():
            varName = 'kcsa'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "\
                        f"regulated by 'ncsa={self.ncsa}'.\n"
                    return
                self.kcsa[decimal] = int(str(ctx.Integer()))

        elif ctx.COBSL():
            varName = 'cobsl'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "\
                        f"regulated by 'ncsa={self.ncsa}'.\n"
                    return
                self.cobsl[decimal] = float(str(ctx.Real()))

        elif ctx.COBSU():
            varName = 'cobsu'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "\
                        f"regulated by 'ncsa={self.ncsa}'.\n"
                    return
                self.cobsu[decimal] = float(str(ctx.Real()))

        elif ctx.COBS():
            varName = 'cobs'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "\
                        f"regulated by 'ncsa={self.ncsa}'.\n"
                    return
                self.cobsl[decimal] = self.cobsu[decimal] = float(str(ctx.Real()))

        elif ctx.CWT():
            varName = 'cwt'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "\
                        f"regulated by 'ncsa={self.ncsa}'.\n"
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The relative weight value '{varName}({decimal})={val}' must not be a negative value.\n"
                    return
                if val == 0.0:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(self.datasetc,decimal)}"\
                        f"The relative weight value '{varName}({decimal})={val}' should be a positive value.\n"
                self.cwt[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ncsa:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The length of '{varName}={ctx.Reals()}' must not exceed 'ncsa={self.ncsa}'.\n"
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}({col})={val}' must not be a negative value.\n"
                            return
                        if val == 0.0:
                            self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}({col})={val}' should be a positive value.\n"
                        self.cwt[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.ncsa:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The argument value of '{varName}({numCol})' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.ncsa}, "\
                                f"regulated by 'ncsa={self.ncsa}'.\n"
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' must not be a negative value.\n"
                            return
                        if val == 0.0:
                            self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                                f"The relative weight value '{varName}={val}' derived from "\
                                f"'{str(ctx.MultiplicativeReal())}' should be a positive value.\n"
                        for col in range(0, numCol):
                            self.cwt[offset + col + 1] = val
                        offset += numCol

        elif ctx.NCSA():
            self.ncsa = int(str(ctx.Integer()))
            if self.ncsa <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The argument value of 'ncsa={self.ncsa}' must be a positive integer.\n"
                return

        elif ctx.DATASETC():
            self.datasetc = int(str(ctx.Integer()))
            if self.datasetc <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The argument value of 'datasetc={self.datasetc}' must be a positive integer.\n"
                return

        elif ctx.SIGMA11():
            self.sigma11 = float(str(ctx.Real()))

        elif ctx.SIGMA12():
            self.sigma12 = float(str(ctx.Real()))

        elif ctx.SIGMA13():
            self.sigma13 = float(str(ctx.Real()))

        elif ctx.SIGMA22():
            self.sigma22 = float(str(ctx.Real()))

        elif ctx.SIGMA23():
            self.sigma23 = float(str(ctx.Real()))

        elif ctx.FIELD():
            self.field = float(str(ctx.Real()))

    # Enter a parse tree produced by AmberMRParser#distance_rst_func_call.
    def enterDistance_rst_func_call(self, ctx: AmberMRParser.Distance_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_distance_rst_func")

        if self.depth == 0:
            self.distRestraints += 1
            self.__cur_subtype = 'dist'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#distance_rst_func_call.
    def exitDistance_rst_func_call(self, ctx: AmberMRParser.Distance_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_distance_rst_func")

    # Enter a parse tree produced by AmberMRParser#angle_rst_func_call.
    def enterAngle_rst_func_call(self, ctx: AmberMRParser.Angle_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_angle_rst_func")

        if self.depth == 0:
            self.angRestraints += 1
            self.__cur_subtype = 'ang'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#angle_rst_func_call.
    def exitAngle_rst_func_call(self, ctx: AmberMRParser.Angle_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_angle_rst_func")

    # Enter a parse tree produced by AmberMRParser#plane_point_angle_rst_func_call.
    def enterPlane_point_angle_rst_func_call(self, ctx: AmberMRParser.Plane_point_angle_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_plane_point_angle_rst_func")

        if self.depth == 0:
            self.angRestraints += 1
            self.__cur_subtype = 'plane'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#plane_point_angle_rst_func_call.
    def exitPlane_point_angle_rst_func_call(self, ctx: AmberMRParser.Plane_point_angle_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_plane_point_angle_rst_func")

    # Enter a parse tree produced by AmberMRParser#plane_plane_angle_rst_func_call.
    def enterPlane_plane_angle_rst_func_call(self, ctx: AmberMRParser.Plane_plane_angle_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_plane_plane_angle_rst_func")

        if self.depth == 0:
            self.angRestraints += 1
            self.__cur_subtype = 'plane'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#plane_plane_angle_rst_func_call.
    def exitPlane_plane_angle_rst_func_call(self, ctx: AmberMRParser.Plane_plane_angle_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_plane_plane_angle_rst_func")

    # Enter a parse tree produced by AmberMRParser#torsion_rst_func_call.
    def enterTorsion_rst_func_call(self, ctx: AmberMRParser.Torsion_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_torsion_rst_func")

        if self.depth == 0:
            self.dihedRestraints += 1
            self.__cur_subtype = 'dihed'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#torsion_rst_func_call.
    def exitTorsion_rst_func_call(self, ctx: AmberMRParser.Torsion_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_torsion_rst_func")

    # Enter a parse tree produced by AmberMRParser#coordinate2_rst_func_call.
    def enterCoordinate2_rst_func_call(self, ctx: AmberMRParser.Coordinate2_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_coordinate2_rst_func")

        if self.depth == 0:
            self.distRestraints += 1
            self.__cur_subtype = 'dist'

        self.depth += 1

        self.inGenDist = True
        self.inGenDist_funcExprs = []
        self.inGenDist_weight = [float(str(ctx.Real_F(0))),
                                 float(str(ctx.Real_F(1)))]

    # Exit a parse tree produced by AmberMRParser#coordinate2_rst_func_call.
    def exitCoordinate2_rst_func_call(self, ctx: AmberMRParser.Coordinate2_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_coordinate2_rst_func")

    # Enter a parse tree produced by AmberMRParser#coordinate3_rst_func_call.
    def enterCoordinate3_rst_func_call(self, ctx: AmberMRParser.Coordinate3_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_coordinate3_rst_func")

        if self.depth == 0:
            self.distRestraints += 1
            self.__cur_subtype = 'dist'

        self.depth += 1

        self.inGenDist = True
        self.inGenDist_funcExprs = []
        self.inGenDist_weight = [float(str(ctx.Real_F(0))),
                                 float(str(ctx.Real_F(1))),
                                 float(str(ctx.Real_F(2)))]

    # Exit a parse tree produced by AmberMRParser#coordinate3_rst_func_call.
    def exitCoordinate3_rst_func_call(self, ctx: AmberMRParser.Coordinate3_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_coordinate3_rst_func")

    # Enter a parse tree produced by AmberMRParser#coordinate4_rst_func_call.
    def enterCoordinate4_rst_func_call(self, ctx: AmberMRParser.Coordinate4_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_coordinate4_rst_func")

        if self.depth == 0:
            self.distRestraints += 1
            self.__cur_subtype = 'dist'

        self.depth += 1

        self.inGenDist = True
        self.inGenDist_funcExprs = []
        self.inGenDist_weight = [float(str(ctx.Real_F(0))),
                                 float(str(ctx.Real_F(1))),
                                 float(str(ctx.Real_F(2))),
                                 float(str(ctx.Real_F(3)))]

    # Exit a parse tree produced by AmberMRParser#coordinate4_rst_func_call.
    def exitCoordinate4_rst_func_call(self, ctx: AmberMRParser.Coordinate4_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_coordinate4_rst_func")

    # Enter a parse tree produced by AmberMRParser#restraint_func_expr.
    def enterRestraint_func_expr(self, ctx: AmberMRParser.Restraint_func_exprContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#restraint_func_expr.
    def exitRestraint_func_expr(self, ctx: AmberMRParser.Restraint_func_exprContext):
        funcExpr = {}

        if ctx.Integer_F():
            funcExpr['igr' if self.inCom else 'iat'] = int(str(ctx.Integer_F()))

        elif ctx.Ambmask_F():
            ambmask = str(ctx.Ambmask_F())[1:].split('@')
            funcExpr['seq_id'] = int(ambmask[0])
            funcExpr['atom_id'] = ambmask[1]

        elif ctx.com_rst_func_call():
            return

        if self.inCom:
            self.inCom_funcExprs.append(funcExpr)
            return

        if self.inPlane:
            if self.inPlane_columnSel == 0:
                self.inPlane_funcExprs.append(funcExpr)
            else:
                self.inPlane_funcExprs2.append(funcExpr)
            return

        if self.inGenDist:
            self.inGenDist_funcExprs.append(funcExpr)
            return

        self.funcExprs.append(funcExpr)

    # Enter a parse tree produced by AmberMRParser#plane_rst_func_call.
    def enterPlane_rst_func_call(self, ctx: AmberMRParser.Plane_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_plane_rst_func")

        self.depth += 1

        self.inPlane = True
        self.inPlane_columnSel += 1

        if self.inPlane_columnSel == 0:
            self.inPlane_funcExprs = []
        else:
            self.inPlane_funcExprs2 = []

    # Exit a parse tree produced by AmberMRParser#plane_rst_func_call.
    def exitPlane_rst_func_call(self, ctx: AmberMRParser.Plane_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_plane_rst_func")

        self.inPlane = False

    # Enter a parse tree produced by AmberMRParser#com_rst_func_call.
    def enterCom_rst_func_call(self, ctx: AmberMRParser.Com_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_com_rst_func")

        self.depth += 1

        self.inCom = True
        self.inCom_funcExprs = []

    # Exit a parse tree produced by AmberMRParser#com_rst_func_call.
    def exitCom_rst_func_call(self, ctx: AmberMRParser.Com_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_com_rst_func")

        self.inCom = False

        if self.inPlane:
            if self.inPlane_columnSel == 0:
                self.inPlane_funcExprs.append(self.inCom_funcExprs)
            else:
                self.inPlane_funcExprs2.append(self.inCom_funcExprs)
            return

        if self.inGenDist:
            self.inGenDist_funcExprs.append(self.inCom_funcExprs)
            return

        self.funcExprs.append(self.inCom_funcExprs)

    # Enter a parse tree produced by AmberMRParser#unambig_atom_name_mapping.
    def enterUnambig_atom_name_mapping(self, ctx: AmberMRParser.Unambig_atom_name_mappingContext):
        self.__cur_resname_for_mapping = str(ctx.Simple_name()).upper()

    # Exit a parse tree produced by AmberMRParser#unambig_atom_name_mapping.
    def exitUnambig_atom_name_mapping(self, ctx: AmberMRParser.Unambig_atom_name_mappingContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#mapping_list.
    def enterMapping_list(self, ctx: AmberMRParser.Mapping_listContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#mapping_list.
    def exitMapping_list(self, ctx: AmberMRParser.Mapping_listContext):
        atomName = str(ctx.Simple_name_MP(0)).upper()
        iupacName = set()

        i = 1
        while ctx.Simple_name_MP(i):
            iupacName.add(str(ctx.Simple_name_MP(i)).upper())
            i += 1

        if self.__cur_resname_for_mapping not in self.unambigAtomNameMapping:
            self.unambigAtomNameMapping[self.__cur_resname_for_mapping] = {}
        self.unambigAtomNameMapping[self.__cur_resname_for_mapping][atomName] = list(iupacName)

    # Enter a parse tree produced by AmberMRParser#ambig_atom_name_mapping.
    def enterAmbig_atom_name_mapping(self, ctx: AmberMRParser.Ambig_atom_name_mappingContext):
        self.__cur_resname_for_mapping = str(ctx.Simple_name()).upper()

    # Exit a parse tree produced by AmberMRParser#ambig_atom_name_mapping.
    def exitAmbig_atom_name_mapping(self, ctx: AmberMRParser.Ambig_atom_name_mappingContext):  # pylint: disable=unused-argument
        self.updateAmbigAtomNameMapping()

    # Enter a parse tree produced by AmberMRParser#ambig_list.
    def enterAmbig_list(self, ctx: AmberMRParser.Ambig_listContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#ambig_list.
    def exitAmbig_list(self, ctx: AmberMRParser.Ambig_listContext):
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

    def getRealChainSeqId(self, ps, seqId, compId=None, isPolySeq=True):  # pylint: disable=no-self-use
        if compId is not None:
            compId = translateToStdResName(compId)
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

    def assignCoordPolymerSequenceWithoutCompId(self, seqId, atomId=None):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = []
        _seqId = seqId

        for ps in self.__polySeq:
            chainId, seqId = self.getRealChainSeqId(ps, _seqId, None)
            if seqId in ps['auth_seq_id']:
                idx = ps['auth_seq_id'].index(seqId)
                cifCompId = ps['comp_id'][idx]
                if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.append((chainId, seqId, cifCompId))

        if self.__hasNonPoly:
            for np in self.__nonPoly:
                chainId, seqId = self.getRealChainSeqId(np, _seqId, None, False)
                if seqId in np['auth_seq_id']:
                    idx = np['auth_seq_id'].index(seqId)
                    cifCompId = np['comp_id'][idx]
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
                        if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))

            if self.__hasNonPoly:
                for np in self.__nonPoly:
                    chainId = np['auth_chain_id']
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            cifCompId = np['comp_id'][np['seq_id'].index(seqId)]
                            if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((np['auth_chain_id'], _seqId, cifCompId))

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    chainAssign.append((chainId, _seqId, cifCompId))

        if len(chainAssign) == 0:
            if seqId == 1 and atomId is not None and atomId in ('H', 'HN'):
                return self.assignCoordPolymerSequenceWithoutCompId(seqId, 'H1')
            if '-' in atomId and ':' in atomId:
                self.warningMessage += f"[Atom not found] "\
                    f"{_seqId}:{atomId} is not present in the coordinates. "\
                    "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the CYANA restraint file.\n"
            else:
                self.warningMessage += f"[Atom not found] "\
                    f"{_seqId}:{atomId} is not present in the coordinates.\n"

        return chainAssign

    def selectCoordAtoms(self, chainAssign, seqId, compId, atomId, allowAmbig=True, enableWarning=True):
        """ Select atoms of the coordinates.
        """

        atomSelection = []

        if compId is not None:
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
                    self.warningMessage += f"[Invalid atom nomenclature] "\
                        f"{seqId}:{compId}:{atomId} is invalid atom nomenclature.\n"
                continue
            if lenAtomId > 1 and not allowAmbig:
                if enableWarning:
                    self.warningMessage += f"[Invalid atom selection] "\
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
                if enableWarning:
                    self.warningMessage += f"[Atom not found] "\
                        f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinates.\n"

    def __getCurrentRestraint(self, dataset=None, n=None):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints] "
        if self.__cur_subtype == 'ang':
            return f"[Check the {self.angRestraints}th row of angle restraints] "
        if self.__cur_subtype == 'dihed':
            return f"[Check the {self.dihedRestraints}th row of torsional angle restraints] "
        if self.__cur_subtype == 'rdc':
            if dataset is None or n is None:
                return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
            return f"[Check the {n}th row of residual dipolar coupling restraints (dataset={dataset})] "
        if self.__cur_subtype == 'plane':
            return f"[Check the {self.planeRestraints}th row of plane-point/plane angle restraints] "
        if self.__cur_subtype == 'noepk':
            if dataset is None or n is None:
                return f"[Check the {self.noepkRestraints}th row of NOESY volume restraints] "
            return f"[Check the {n}th row of NOESY volume restraints (dataset={dataset})] "
        if self.__cur_subtype == 'procs':
            if n is None:
                return f"[Check the {self.procsRestraints}th row of chemical shift restraints] "
            return f"[Check the {n}th row of chemical shift restraints] "
        if self.__cur_subtype == 'pcs':
            if dataset is None or n is None:
                return f"[Check the {self.pcsRestraints}th row of pseudocontact shift restraints] "
            return f"[Check the {n}th row of pseudocontact shift restraints (name of paramagnetic center={dataset})] "
        if self.__cur_subtype == 'csa':
            if dataset is None or n is None:
                return f"[Check the {self.csaRestraints}th row of residual CSA or pseudo-CSA restraints] "
            return f"[Check the {n}th row of residual CSA or pseudo-CSA restraints (dataset={dataset})] "
        return f"[Check the {self.nmrRestraints}th row of NMR restraints] "

    def getContentSubtype(self):
        """ Return content subtype of AMBER MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'ang_restraint': self.angRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'plane_restraint': self.planeRestraints,
                          'noepk_restraint': self.noepkRestraints,
                          'procs_restraint': self.procsRestraints,
                          'pcs_restraint': self.pcsRestraints,
                          'csa_restraint': self.csaRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of AMBER MR file.
        """
        return self.__polySeqRst

    def getSequenceAlignment(self):
        """ Return sequence alignment between coordinates and AMBER MR.
        """
        return self.__seqAlign

    def getChainAssignment(self):
        """ Return chain assignment between coordinates and AMBER MR.
        """
        return self.__chainAssign

    def getAtomNumberDict(self):
        """ Return AMBER atomic number dictionary.
        """
        return self.__atomNumberDict

    def getSanderAtomNumberDict(self):
        """ Return AMBER atomic number dictionary based on Sander comments.
        """
        return self.__sanderAtomNumberDict

    def getReasonsForReparsing(self):
        """ Return reasons for re-parsing AMBER MR file.
        """
        return self.reasonsForReParsing

    def hasComments(self):
        """ Return whether Sander comments are available.
        """
        return self.__hasComments


# del AmberMRParser
