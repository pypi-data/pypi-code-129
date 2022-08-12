##
# File: AlignUtil.py
# Date: 18-Feb-2022
#
# Updates:
""" Utilities for pairwise alignment.
    @author: Masashi Yokochi
"""
import copy

# criterion for low sequence coverage
LOW_SEQ_COVERAGE = 0.3


# criterion for minimum sequence coverage when conflict occurs (NMR conventional deposition)
MIN_SEQ_COVERAGE_W_CONFLICT = 0.95


# empty value
emptyValue = (None, '', '.', '?', 'null')


# true value
trueValue = ('true', 't', 'yes', 'y', '1')


# taken from wwpdb.utils.align.SequenceReferenceData.py
monDict3 = {'ALA': 'A',
            'ARG': 'R',
            'ASN': 'N',
            'ASP': 'D',
            'ASX': 'B',
            'CYS': 'C',
            'GLN': 'Q',
            'GLU': 'E',
            'GLX': 'Z',
            'GLY': 'G',
            'HIS': 'H',
            'ILE': 'I',
            'LEU': 'L',
            'LYS': 'K',
            'MET': 'M',
            'PHE': 'F',
            'PRO': 'P',
            'SER': 'S',
            'THR': 'T',
            'TRP': 'W',
            'TYR': 'Y',
            'VAL': 'V',
            'DA': 'A',
            'DC': 'C',
            'DG': 'G',
            'DT': 'T',
            'DU': 'U',
            'DI': 'I',
            'A': 'A',
            'C': 'C',
            'G': 'G',
            'I': 'I',
            'T': 'T',
            'U': 'U'
            }

MAJOR_ASYM_ID_SET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LEN_MAJOR_ASYM_ID_SET = len(MAJOR_ASYM_ID_SET)


def hasLargeSeqGap(polySeq1, polySeq2):
    """ Return whether large gap in combined sequence of polySeq1 and polySeq2.
    """

    _s = sorted(set(polySeq1['seq_id']) | set(polySeq2['seq_id']))

    for idx, seqId in enumerate(_s):
        if idx > 0 and seqId - _s[idx - 1] > 20:
            return True

    return False


def fillBlankCompId(polySeq1, polySeq2):
    """ Fill blanked comp ID in polySeq2 against polySeq1.
    """

    _s = sorted(set(polySeq1['seq_id']) | set(polySeq2['seq_id']))
    _c = []

    for seqId in _s:
        if seqId in polySeq2['seq_id']:
            idx = polySeq2['seq_id'].index(seqId)
            if idx < len(polySeq2['comp_id']):
                _c.append(polySeq2['comp_id'][idx])
            else:
                _c.append('.')
        else:
            _c.append('.')

    return {'chain_id': polySeq2['chain_id'], 'seq_id': _s, 'comp_id': _c}


def fillBlankCompIdWithOffset(ps, offset):
    """ Fill blanked comp ID with offset.
    """

    _s = list(range(ps['seq_id'][0] - offset, ps['seq_id'][-1] + 1))
    _c = []

    for seqId in _s:
        if seqId in ps['seq_id']:
            idx = ps['seq_id'].index(seqId)
            if idx < len(ps['comp_id']):
                _c.append(ps['comp_id'][idx])
            else:
                _c.append('.')
        else:
            _c.append('.')

    return {'chain_id': ps['chain_id'], 'seq_id': _s, 'comp_id': _c}


def beautifyPolySeq(polySeq1, polySeq2):
    """ Truncate negative seq IDs and insert spacing between the large gap.
    """

    _polySeq1 = fillBlankCompId(polySeq2, polySeq1)  # pylint: disable=arguments-out-of-order
    _polySeq2 = fillBlankCompId(polySeq1, polySeq2)  # pylint: disable=arguments-out-of-order

    if _polySeq1['seq_id'] != _polySeq2['seq_id']:
        return _polySeq1, _polySeq2

    _s = [seqId for seqId in _polySeq1['seq_id'] if seqId > 0]
    _c1 = [compId for seqId, compId
           in zip(_polySeq1['seq_id'], _polySeq1['comp_id']) if seqId > 0]
    _c2 = [compId for seqId, compId
           in zip(_polySeq1['seq_id'], _polySeq2['comp_id']) if seqId > 0]

    gapS = []
    gapP = []

    lenSpacer = 5  # DAOTHER-7465, issue #2

    for idx, seqId in enumerate(_s):
        if idx > 0 and seqId - _s[idx - 1] > 20:
            prevSeqId = _s[idx - 1]
            for sp in range(1, lenSpacer + 1):
                gapS.append(prevSeqId + sp)
                gapS.append(seqId - sp)
            gapP.append(idx)

    if len(gapS) == 0:
        return {'chain_id': _polySeq1['chain_id'], 'seq_id': _s, 'comp_id': _c1},\
               {'chain_id': _polySeq2['chain_id'], 'seq_id': _s, 'comp_id': _c2}

    _s.extend(gapS)
    _s.sort()

    for p in reversed(gapP):
        for sp in range(1, lenSpacer + 1):
            _c1.insert(p, '.')
            _c2.insert(p, '.')

    return {'chain_id': _polySeq1['chain_id'], 'seq_id': _s, 'comp_id': _c1},\
           {'chain_id': _polySeq2['chain_id'], 'seq_id': _s, 'comp_id': _c2}


def getMiddleCode(seqIdList1, seqIdList2):
    """ Return array of middle code of sequence alignment.
    """

    middleCode = ''

    for idx, seqId in enumerate(seqIdList1):
        if idx < len(seqIdList2):
            middleCode += '|' if seqId == seqIdList2[idx] and seqId != '.' else ' '
        else:
            middleCode += ' '

    return middleCode


def getGaugeCode(seqIdList, offset=0):
    """ Return gauge code for a give sequence.
    """

    if offset > 0:
        _seqIdList = list(range(1, offset + 1))
        for idx, seqId in enumerate(seqIdList):
            if idx < offset:
                continue
            _seqIdList.append(seqId)
        seqIdList = _seqIdList

    lenSeqId = len([seqId for seqId in seqIdList if seqId is not None])
    lenCode = 0

    chars = []

    for seqId in seqIdList:

        if seqId is None:
            chars.append('-')
            continue

        if seqId >= 0 and seqId % 10 == 0 and lenCode == 0:

            code = str(seqId)
            lenCode = len(code)

            for p in range(lenCode):
                chars.append(code[p])

        if lenCode > 0:
            lenCode -= 1
        else:
            chars.append('-')

    lenChars = len(chars)

    for idx, seqId in enumerate(seqIdList):

        if seqId is None or seqId % 10 != 0:
            continue

        code = str(seqId)
        lenCode = len(code)

        if idx - lenCode > 0:
            for p in range(lenCode):
                if idx + p - lenCode + 1 >= 0 and idx + p < lenChars:
                    chars[idx + p - lenCode + 1] = chars[idx + p]
                    chars[idx + p] = '-'

    if offset > 0:
        for p in range(offset):
            chars[p] = '-'

    gaugeCode = ''.join(chars)

    if lenSeqId == len(seqIdList):
        return gaugeCode[:lenSeqId]

    _lenSeqId = len(seqIdList)

    offset = 0
    for idx, seqId in enumerate(seqIdList):

        if seqId is None:
            p = idx + offset
            gaugeCode = gaugeCode[0:p] + ' ' + gaugeCode[p:]
            offset += 1

    return gaugeCode[:_lenSeqId]


def getScoreOfSeqAlign(myAlign):
    """ Return score of sequence alignment.
    """

    length = len(myAlign)

    aligned = [True] * length

    for p in range(length):
        myPr = myAlign[p]
        myPr0 = str(myPr[0])
        myPr1 = str(myPr[1])
        if myPr0 == '.' or myPr1 == '.':
            aligned[p] = False
        elif myPr0 != myPr1:
            pass
        else:
            break

    notAligned = True
    offset1 = 0
    offset2 = 0

    unmapped = 0
    conflict = 0
    matched = 0
    for p in range(length):
        myPr = myAlign[p]
        myPr0 = str(myPr[0])
        myPr1 = str(myPr[1])
        if myPr0 == '.' or myPr1 == '.':
            if notAligned and not aligned[p]:
                if myPr0 == '.' and myPr1 != '.'\
                   and offset2 == 0:  # DAOTHER-7421
                    offset1 += 1
                if myPr0 != '.' and myPr1 == '.'\
                   and offset1 == 0:  # DAOTHER-7421
                    offset2 += 1
                if myPr0 == '.' and myPr1 == '.':  # DAOTHER-7465
                    if offset2 == 0:
                        offset1 += 1
                    if offset1 == 0:
                        offset2 += 1
            unmapped += 1
        elif myPr0 != myPr1:
            conflict += 1
        else:
            notAligned = False
            matched += 1

    return matched, unmapped, conflict, offset1, offset2


def getOneLetterCode(compId):
    """ Convert comp ID to 1-letter code.
    """

    compId = compId.upper()

    if compId in monDict3:
        return monDict3[compId]

    if compId in emptyValue:
        return '.'

    return 'X'


def getOneLetterCodeSequence(compIdList):
    """ Convert array of comp IDs to 1-letter code sequence.
    """

    compCode = ''

    for compId in compIdList:
        compCode += getOneLetterCode(compId)

    return compCode


def letterToDigit(code, minDigit=0):
    """ Return digit from a given chain code.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    unit = 1
    digit = 0

    for char in ''.join(reversed(code.lower())):

        if char.isdigit():
            digit += unit * int(char)
        elif char.isalpha():
            digit += unit * (alphabet.index(char) + 1)
        else:
            continue

        unit *= 27

    return digit if digit > minDigit else minDigit


def indexToLetter(index):
    """ Return chain code from a given index (0 based).
    """

    if index < 0:
        return '.'

    if index > 19683:
        index = index % 19683

    if index < 27:
        return str(chr(65 + index))

    if index < 729:
        return str(chr(64 + (index // 27)))\
            + str(chr(65 + (index % 27)))

    return str(chr(64 + (index // 729)))\
        + str(chr(64 + ((index % 729) // 27)))\
        + str(chr(65 + (index % 27)))


def updatePolySeqRst(polySeqRst, chainId, seqId, compId):
    """ Update polymer sequence of the current MR file.
    """

    ps = next((ps for ps in polySeqRst if ps['chain_id'] == chainId), None)
    if ps is None:
        polySeqRst.append({'chain_id': chainId, 'seq_id': [], 'comp_id': []})
        ps = polySeqRst[-1]

    if seqId not in ps['seq_id']:
        ps['seq_id'].append(seqId)
        ps['comp_id'].append(compId)


def updatePolySeqRstFromAtomSelectionSet(polySeqRst, atomSelectionSet):
    """ Update polymer sequence of the current MR file.
    """

    if len(atomSelectionSet) == 0:
        return

    for atomSelection in atomSelectionSet:
        if len(atomSelection) == 0:
            continue
        for atom in atomSelection:
            chainId = atom['chain_id']
            seqId = atom['seq_id']
            compId = atom['comp_id']

            updatePolySeqRst(polySeqRst, chainId, seqId, compId)


def sortPolySeqRst(polySeqRst):
    """ Sort polymer sequence of the current MR file by sequence number.
    """

    if polySeqRst is None:
        return

    for ps in polySeqRst:
        minSeqId = min(ps['seq_id'])
        maxSeqId = max(ps['seq_id'])

        _seqIds = list(range(minSeqId, maxSeqId + 1))
        _compIds = ["."] * (maxSeqId - minSeqId + 1)

        for idx, seqId in enumerate(ps['seq_id']):
            _compIds[_seqIds.index(seqId)] = ps['comp_id'][idx]

        ps['seq_id'] = _seqIds
        ps['comp_id'] = _compIds


def alignPolymerSequence(pA, polySeqModel, polySeqRst, conservative=True, resolvedMultimer=False):
    """ Align polymer sequence of the coordinates and restraints.
    """

    compIdMapping = []

    if pA is None or polySeqModel is None or polySeqRst is None:
        return None, None

    seqAlign = []

    tabooList = []
    inhibitList = []

    hasMultimer = False

    for i1, s1 in enumerate(polySeqModel):
        chain_id = s1['auth_chain_id']

        if i1 >= LEN_MAJOR_ASYM_ID_SET:
            continue

        for i2, s2 in enumerate(polySeqRst):
            chain_id2 = s2['chain_id']

            if i2 >= LEN_MAJOR_ASYM_ID_SET:
                continue

            pA.setReferenceSequence(s1['comp_id'], 'REF' + chain_id)
            pA.addTestSequence(s2['comp_id'], chain_id)
            pA.doAlign()

            myAlign = pA.getAlignment(chain_id)

            length = len(myAlign)

            if length == 0:
                tabooList.append({chain_id, chain_id2})
                continue

            _matched, unmapped, conflict, offset_1, offset_2 = getScoreOfSeqAlign(myAlign)

            if conflict > 0:

                if any(c2 for c2 in s2['comp_id'] if c2.endswith('?')):  # AMBER/GROMACS topology
                    s2_comp_id_copy = copy.copy(s2['comp_id'])
                    for p in range(length):
                        myPr = myAlign[p]
                        myPr0 = str(myPr[0])
                        myPr1 = str(myPr[1])
                        if myPr0 != myPr1 and myPr1.endswith('?'):
                            idx = s2_comp_id_copy.index(myPr1)
                            s2_seq_id = s2['seq_id'][idx]
                            s2_auth_comp_id = s2['auth_comp_id'][idx]
                            s2_comp_id_copy[idx] = myPr0

                            pA.setReferenceSequence(s1['comp_id'], 'REF' + chain_id)
                            pA.addTestSequence(s2_comp_id_copy, chain_id)
                            pA.doAlign()

                            myAlign = pA.getAlignment(chain_id)

                            _matched, unmapped, _conflict, offset_1, offset_2 = getScoreOfSeqAlign(myAlign)

                            if _conflict < conflict:
                                s2['comp_id'] = s2_comp_id_copy
                                conflict = _conflict
                                compIdMapping.append({'chain_id': chain_id2, 'seq_id': s2_seq_id,
                                                      'comp_id': myPr0, 'auth_comp_id': s2_auth_comp_id})

                if conflict > 0:
                    tabooList.append({chain_id, chain_id2})

            if length == unmapped + conflict or _matched <= conflict:
                inhibitList.append({chain_id, chain_id2})
                continue

            _s1 = s1 if offset_1 == 0 else fillBlankCompIdWithOffset(s1, offset_1)
            _s2 = s2 if offset_2 == 0 else fillBlankCompIdWithOffset(s2, offset_2)

            if conflict > 0 and hasLargeSeqGap(_s1, _s2):
                __s1, __s2 = beautifyPolySeq(_s1, _s2)
                _s1_ = __s1
                _s2_ = __s2

                pA.setReferenceSequence(_s1_['comp_id'], 'REF' + chain_id)
                pA.addTestSequence(_s2_['comp_id'], chain_id)
                pA.doAlign()

                myAlign = pA.getAlignment(chain_id)

                length = len(myAlign)

                _matched, unmapped, _conflict, _offset_1, _offset_2 = getScoreOfSeqAlign(myAlign)

                if _conflict == 0 and len(__s2['comp_id']) - len(s2['comp_id']) == conflict:
                    conflict = 0
                    offset_1 = _offset_1
                    offset_2 = _offset_2
                    _s1 = __s1
                    _s2 = __s2

            ref_length = len(s1['seq_id'])

            ref_code = getOneLetterCodeSequence(_s1['comp_id'])
            test_code = getOneLetterCodeSequence(_s2['comp_id'])
            mid_code = getMiddleCode(ref_code, test_code)
            ref_gauge_code = getGaugeCode(_s1['seq_id'])
            test_gauge_code = getGaugeCode(_s2['seq_id'])

            if any((__s1, __s2) for (__s1, __s2, __c1, __c2)
                   in zip(_s1['seq_id'], _s2['seq_id'], _s1['comp_id'], _s2['comp_id'])
                   if __c1 != '.' and __c2 != '.' and __c1 != __c2):
                seq_id1 = []
                seq_id2 = []
                comp_id1 = []
                comp_id2 = []
                idx1 = 0
                idx2 = 0
                for i in range(length):
                    myPr = myAlign[i]
                    myPr0 = str(myPr[0])
                    myPr1 = str(myPr[1])
                    if myPr0 != '.':
                        while idx1 < len(_s1['seq_id']):
                            if _s1['comp_id'][idx1] == myPr0:
                                seq_id1.append(_s1['seq_id'][idx1])
                                comp_id1.append(myPr0)
                                idx1 += 1
                                break
                            idx1 += 1
                    else:
                        seq_id1.append(None)
                        comp_id1.append('.')
                    if myPr1 != '.':
                        while idx2 < len(_s2['seq_id']):
                            if _s2['comp_id'][idx2] == myPr1:
                                seq_id2.append(_s2['seq_id'][idx2])
                                comp_id2.append(myPr1)
                                idx2 += 1
                                break
                            idx2 += 1
                    else:
                        seq_id2.append(None)
                        comp_id2.append('.')
                ref_code = getOneLetterCodeSequence(comp_id1)
                test_code = getOneLetterCodeSequence(comp_id2)
                mid_code = getMiddleCode(ref_code, test_code)
                ref_gauge_code = getGaugeCode(seq_id1, offset_1)
                test_gauge_code = getGaugeCode(seq_id2, offset_2)
                if ' ' in ref_gauge_code:
                    for p, g in enumerate(ref_gauge_code):
                        if g == ' ':
                            ref_code = ref_code[0:p] + '-' + ref_code[p + 1:]
                if ' ' in test_gauge_code:
                    for p, g in enumerate(test_gauge_code):
                        if g == ' ':
                            test_code = test_code[0:p] + '-' + test_code[p + 1:]

            matched = mid_code.count('|')

            seq_align = {'ref_chain_id': chain_id, 'test_chain_id': chain_id2, 'length': ref_length,
                         'matched': matched, 'conflict': conflict, 'unmapped': unmapped,
                         'sequence_coverage': float(f"{float(length - (unmapped + conflict)) / ref_length:.3f}"),
                         'ref_seq_id': _s1['seq_id'], 'test_seq_id': _s2['seq_id'],
                         'ref_gauge_code': ref_gauge_code, 'ref_code': ref_code, 'mid_code': mid_code,
                         'test_code': test_code, 'test_gauge_code': test_gauge_code}

            if 'identical_chain_id' in s1:
                hasMultimer = True

            seqAlign.append(seq_align)

    if len(tabooList) > 0:
        _seqAlign = copy.copy(seqAlign)
        for sa in _seqAlign:
            if {sa['ref_chain_id'], sa['test_chain_id']} in tabooList:
                seqAlign.remove(sa)

    if len(inhibitList) > 0 and conservative:
        _seqAlign = copy.copy(seqAlign)
        for sa in _seqAlign:
            if {sa['ref_chain_id'], sa['test_chain_id']} in inhibitList:
                seqAlign.remove(sa)

    if hasMultimer and resolvedMultimer:
        _seqAlign = copy.copy(seqAlign)
        seqAlign = []
        for sa in _seqAlign:
            ref_chain_id = sa['ref_chain_id']
            test_chain_id = sa['test_chain_id']
            s1 = next(ps for ps in polySeqModel if ps['auth_chain_id'] == ref_chain_id)
            if 'identical_chain_id' not in s1 or ref_chain_id == test_chain_id:
                seqAlign.append(sa)

    return seqAlign, compIdMapping


def assignPolymerSequence(pA, ccU, fileType, polySeqModel, polySeqRst, seqAlign):
    """ Assign polymer sequences of restraints.
    """

    warningMessage = ''

    if pA is None or polySeqModel is None or polySeqRst is None or seqAlign is None:
        return None, warningMessage

    if fileType == 'nm-res-xpl':
        _mr_format_name = 'XPLOR-NIH'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    elif fileType == 'nm-res-cns':
        _mr_format_name = 'CNS'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    elif fileType == 'nm-res-amb':
        _mr_format_name = 'AMBER'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    elif fileType == 'nm-aux-amb':
        _mr_format_name = 'AMBER'
        _a_mr_format_name = 'the ' + _mr_format_name + ' parameter/topology'
    elif fileType == 'nm-res-cya':
        _mr_format_name = 'CYANA'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    elif fileType == 'nm-res-ros':
        _mr_format_name = 'ROSETTA'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    elif fileType == 'nm-res-bio':
        _mr_format_name = 'BIOSYM'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    elif fileType == 'nm-res-gro':
        _mr_format_name = 'GROMACS'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    elif fileType == 'nm-aux-gro':
        _mr_format_name = 'GROMACS'
        _a_mr_format_name = 'the ' + _mr_format_name + ' parameter/topology'
    elif fileType == 'nm-res-dyn':
        _mr_format_name = 'DYNAMO/PALES/TALOS'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    elif fileType == 'nm-res-syb':
        _mr_format_name = 'SYBYL'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'
    else:
        _mr_format_name = 'MR'
        _a_mr_format_name = 'the ' + _mr_format_name + ' restraint'

    mr_chains = len(polySeqRst) if len(polySeqRst) < LEN_MAJOR_ASYM_ID_SET else LEN_MAJOR_ASYM_ID_SET

    mat = []
    indices = []

    for i1, s1 in enumerate(polySeqModel):
        chain_id = s1['auth_chain_id']

        if i1 >= LEN_MAJOR_ASYM_ID_SET:
            continue

        cost = [0 for i in range(mr_chains)]

        for i2, s2 in enumerate(polySeqRst):
            chain_id2 = s2['chain_id']

            if i2 >= LEN_MAJOR_ASYM_ID_SET:
                continue

            result = next((seq_align for seq_align in seqAlign
                           if seq_align['ref_chain_id'] == chain_id
                           and seq_align['test_chain_id'] == chain_id2), None)

            if result is not None:
                cost[polySeqRst.index(s2)] = result['unmapped'] + result['conflict'] - result['length']
                if result['length'] >= len(s1['seq_id']) - result['unmapped']:
                    indices.append((polySeqModel.index(s1), polySeqRst.index(s2)))

        mat.append(cost)

    chainAssignSet = []

    for row, column in indices:

        if mat[row][column] >= 0:
            _cif_chains = []
            for _row, _column in indices:
                if column == _column:
                    _cif_chains.append(polySeqModel[_row]['auth_chain_id'])

            if len(_cif_chains) > 1:
                chain_id2 = polySeqRst[column]['chain_id']

                warningMessage += f"[Concatenated sequence] The chain ID {chain_id2!r} of the sequences in {_a_mr_format_name} file "\
                    f"will be re-assigned to the chain IDs {_cif_chains} in the coordinates during biocuration.\n"

        chain_id = polySeqModel[row]['auth_chain_id']
        chain_id2 = polySeqRst[column]['chain_id']

        result = next(seq_align for seq_align in seqAlign
                      if seq_align['ref_chain_id'] == chain_id and seq_align['test_chain_id'] == chain_id2)

        chainAssign = {'ref_chain_id': chain_id, 'test_chain_id': chain_id2, 'length': result['length'],
                       'matched': result['matched'], 'conflict': result['conflict'], 'unmapped': result['unmapped'],
                       'sequence_coverage': result['sequence_coverage']}

        s1 = next(s for s in polySeqModel if s['auth_chain_id'] == chain_id)
        s2 = next(s for s in polySeqRst if s['chain_id'] == chain_id2)

        pA.setReferenceSequence(s1['comp_id'], 'REF' + chain_id)
        pA.addTestSequence(s2['comp_id'], chain_id)
        pA.doAlign()

        myAlign = pA.getAlignment(chain_id)

        length = len(myAlign)

        _matched, unmapped, conflict, offset_1, offset_2 = getScoreOfSeqAlign(myAlign)

        _s1 = s1 if offset_1 == 0 else fillBlankCompIdWithOffset(s1, offset_1)
        _s2 = s2 if offset_2 == 0 else fillBlankCompIdWithOffset(s2, offset_2)

        if conflict > 0 and hasLargeSeqGap(_s1, _s2):
            __s1, __s2 = beautifyPolySeq(_s1, _s2)
            _s1 = __s1
            _s2 = __s2

            pA.setReferenceSequence(_s1['comp_id'], 'REF' + chain_id)
            pA.addTestSequence(_s2['comp_id'], chain_id)
            pA.doAlign()

            myAlign = pA.getAlignment(chain_id)

            length = len(myAlign)

            _matched, unmapped, _conflict, _, _ = getScoreOfSeqAlign(myAlign)

            if _conflict == 0 and len(__s2['comp_id']) - len(s2['comp_id']) == conflict:
                result['conflict'] = 0
                s2 = __s2

        if result['unmapped'] > 0 or result['conflict'] > 0:

            aligned = [True] * length
            seq_id1 = []
            seq_id2 = []

            j = 0
            for i in range(length):
                if str(myAlign[i][0]) != '.':
                    seq_id1.append(s1['seq_id'][j])
                    j += 1
                else:
                    seq_id1.append(None)

            j = 0
            for i in range(length):
                if str(myAlign[i][1]) != '.':
                    seq_id2.append(s2['seq_id'][j])
                    j += 1
                else:
                    seq_id2.append(None)

            for i in range(length):
                myPr = myAlign[i]
                myPr0 = str(myPr[0])
                myPr1 = str(myPr[1])
                if myPr0 == '.' or myPr1 == '.':
                    aligned[i] = False
                elif myPr0 != myPr1:
                    pass
                else:
                    break

            for i in reversed(range(length)):
                myPr = myAlign[i]
                myPr0 = str(myPr[0])
                myPr1 = str(myPr[1])
                if myPr0 == '.' or myPr1 == '.':
                    aligned[i] = False
                elif myPr0 != myPr1:
                    pass
                else:
                    break

            _conflicts = 0

            for i in range(length):
                myPr = myAlign[i]
                if myPr[0] == myPr[1]:
                    continue

                cif_comp_id = str(myPr[0])
                mr_comp_id = str(myPr[1])

                if mr_comp_id == '.' and cif_comp_id != '.':
                    pass

                elif mr_comp_id != cif_comp_id and aligned[i]:
                    _conflicts += 1

            if fileType.startswith('nm-aux') and _conflicts > chainAssign['unmapped'] and chainAssign['sequence_coverage'] < MIN_SEQ_COVERAGE_W_CONFLICT:
                continue

            if _conflicts + offset_1 > _matched and chainAssign['sequence_coverage'] < LOW_SEQ_COVERAGE:  # DAOTHER-7825 (2lyw)
                continue

            unmapped = []
            conflict = []

            for i in range(length):
                myPr = myAlign[i]
                if myPr[0] == myPr[1]:
                    continue

                cif_comp_id = str(myPr[0])
                mr_comp_id = str(myPr[1])

                if mr_comp_id == '.' and cif_comp_id != '.':

                    unmapped.append({'ref_seq_id': seq_id1[i], 'ref_comp_id': cif_comp_id})
                    # """ unmapped residue is not error """
                    # if not aligned[i]:

                    #     if not ccU.updateChemCompDict(cif_comp_id):
                    #         continue

                    #     if ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] != 'REL':
                    #         continue

                    #     cif_seq_code = f"{chain_id}:{seq_id1[i]}:{cif_comp_id}"

                    #     warningMessage += f"[Sequence mismatch] {cif_seq_code} is not present "\
                    #         f"in {_a_mr_format_name} data (chain_id {chain_id2}).\n"
                    #
                elif mr_comp_id != cif_comp_id and aligned[i]:

                    conflict.append({'ref_seq_id': seq_id1[i], 'ref_comp_id': cif_comp_id,
                                     'test_seq_id': seq_id2[i], 'test_comp_id': mr_comp_id})

                    cif_seq_code = f"{chain_id}:{seq_id1[i]}:{cif_comp_id}"
                    if cif_comp_id == '.':
                        cif_seq_code += ', insertion error'
                    mr_seq_code = f"{chain_id2}:{seq_id2[i]}:{mr_comp_id}"
                    if mr_comp_id == '.':
                        mr_seq_code += ', insertion error'

                    if cif_comp_id != '.':

                        if not ccU.updateChemCompDict(cif_comp_id):
                            continue

                        if ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] != 'REL':
                            continue

                        if getOneLetterCode(cif_comp_id) == 'X':
                            continue

                    warningMessage += f"[Sequence mismatch] Sequence alignment error between the coordinate ({cif_seq_code}) "\
                        f"and {_a_mr_format_name} data ({mr_seq_code}). "\
                        "Please verify the two sequences and re-upload the correct file(s) if required.\n"

            if len(unmapped) > 0:
                chainAssign['unmapped_sequence'] = unmapped

            if len(conflict) > 0:
                chainAssign['conflict_sequence'] = conflict
                chainAssign['conflict'] = len(conflict)
                chainAssign['unmapped'] = chainAssign['unmapped'] - len(conflict)
                if chainAssign['unmapped'] < 0:
                    chainAssign['conflict'] -= chainAssign['unmapped']
                    chainAssign['unmapped'] = 0

                result['conflict'] = chainAssign['conflict']
                result['unmapped'] = chainAssign['unmapped']

        chainAssignSet.append(chainAssign)

    if len(chainAssignSet) > 0 and len(polySeqModel) > 1:

        if any(s for s in polySeqModel if 'identical_chain_id' in s):

            _chainAssignSet = copy.copy(chainAssignSet)

            for chainAssign in _chainAssignSet:

                if chainAssign['conflict'] > 0:
                    continue

                chain_id = chainAssign['ref_chain_id']

                try:
                    identity = next(s['identical_chain_id'] for s in polySeqModel
                                    if s['auth_chain_id'] == chain_id and 'identical_chain_id' in s)

                    for chain_id in identity:

                        if not any(_chainAssign for _chainAssign in chainAssignSet if _chainAssign['ref_chain_id'] == chain_id):
                            _chainAssign = copy.copy(chainAssign)
                            _chainAssign['ref_chain_id'] = chain_id
                            chainAssignSet.append(_chainAssign)

                except StopIteration:
                    pass

    return chainAssignSet, warningMessage


def trimSequenceAlignment(seqAlign, chainAssignSet):
    """ Trim ineffective sequence alignments.
    """

    if seqAlign is None or chainAssignSet is None:
        return

    ineffSeqAlignIdx = list(range(len(seqAlign) - 1, -1, -1))

    for chainAssign in chainAssignSet:
        ref_chain_id = chainAssign['ref_chain_id']
        test_chain_id = chainAssign['test_chain_id']

        effSeqAlignIdx = next((idx for idx, seq_align in enumerate(seqAlign)
                              if seq_align['ref_chain_id'] == ref_chain_id
                              and seq_align['test_chain_id'] == test_chain_id), None)

        if effSeqAlignIdx is not None and effSeqAlignIdx in ineffSeqAlignIdx:
            ineffSeqAlignIdx.remove(effSeqAlignIdx)

    if len(ineffSeqAlignIdx) > 0:
        for idx in ineffSeqAlignIdx:
            del seqAlign[idx]


def retrieveAtomIdentFromMRMap(mrAtomNameMapping, seqId, compId, atomId):
    """ Retrieve atom identifiers from atom name mapping of public MR file.
    """

    try:
        item = next(item for item in mrAtomNameMapping
                    if item['original_seq_id'] == seqId
                    and item['original_comp_id'] == compId
                    and item['original_atom_id'] == atomId)
        return item['auth_seq_id'], item['auth_comp_id'], item['auth_atom_id']
    except StopIteration:
        return seqId, compId, atomId


def retrieveAtomIdFromMRMap(mrAtomNameMapping, cifSeqId, cifCompId, atomId):
    """ Retrieve atom_id from atom name mapping of public MR file.
    """

    try:
        item = next(item for item in mrAtomNameMapping
                    if item['auth_seq_id'] == cifSeqId
                    and item['auth_comp_id'] == cifCompId
                    and item['original_atom_id'] == atomId)
        return item['auth_atom_id']
    except StopIteration:
        return atomId


def retrieveRemappedSeqId(seqIdRemap, chainId, seqId):
    """ Retrieve seq_id from mapping dictionary based on sequence alignments.
    """

    try:
        if chainId is None:
            item = next(item for item in seqIdRemap if seqId in item['seq_id_dict'])
        else:
            item = next(item for item in seqIdRemap if seqId in item['seq_id_dict'] and item['chain_id'] == chainId)
        return item['chain_id'], item['seq_id_dict'][seqId]
    except StopIteration:
        return chainId, seqId


def splitPolySeqRstForMultimers(pA, polySeqModel, polySeqRst, chainAssignSet):
    """ Split polymer sequence of the current MR file for multimers.
    """

    if polySeqModel is None or polySeqRst is None or chainAssignSet is None:
        return None, None

    target_test_chain_id = {}
    for chainAssign in chainAssignSet:
        if chainAssign['conflict'] == 0 and chainAssign['unmapped'] > 0:
            ref_chain_id = chainAssign['ref_chain_id']
            test_chain_id = chainAssign['test_chain_id']
            if test_chain_id not in target_test_chain_id:
                target_test_chain_id[test_chain_id] = []
            target_test_chain_id[test_chain_id].append(ref_chain_id)

    if len(target_test_chain_id) == 0:
        return None, None

    split = False

    _polySeqRst = copy.copy(polySeqRst)
    _chainIdMapping = {}

    for test_chain_id, ref_chain_ids in target_test_chain_id.items():

        total_gaps = len(ref_chain_ids) - 1

        if total_gaps == 0:
            continue

        ref_seq_lengths = []

        for ref_seq_id in ref_chain_ids:
            ref_ps = next(ps for ps in polySeqModel if ps['auth_chain_id'] == ref_chain_id)
            ref_seq_lengths.append(len(ref_ps['seq_id']))

        sum_ref_seq_lengths = sum(ref_seq_lengths)

        test_ps = next(ps for ps in _polySeqRst if ps['chain_id'] == test_chain_id)
        len_test_ps = len(test_ps['seq_id'])

        if sum_ref_seq_lengths < len_test_ps:
            half_gap = (len_test_ps - sum_ref_seq_lengths) // (total_gaps * 2)

            _test_ps = copy.copy(test_ps)

            _polySeqRst.remove(test_ps)

            offset = 0

            for idx, ref_chain_id in enumerate(ref_chain_ids):
                ref_ps = next(ps for ps in polySeqModel if ps['auth_chain_id'] == ref_chain_id)
                half_len_ref_ps = len(ref_ps['seq_id']) // 2

                beg = offset
                end = offset + len(ref_ps['seq_id'])

                if len_test_ps - end < half_len_ref_ps or idx == total_gaps:
                    end = len_test_ps

                while True:
                    if _test_ps['comp_id'][beg] != '.':
                        break
                    beg += 1
                    if beg == end:
                        return None, None

                end = beg + len(ref_ps['seq_id']) + half_gap

                if len_test_ps - end < half_len_ref_ps or idx == total_gaps:
                    end = len_test_ps

                while True:
                    if _test_ps['comp_id'][end - 1] != '.':
                        break
                    end -= 1
                    if end == beg:
                        return None, None

                _test_ps_ = {'chain_id': ref_chain_id,
                             'seq_id': _test_ps['seq_id'][beg:end],
                             'comp_id': _test_ps['comp_id'][beg:end]}

                pA.setReferenceSequence(ref_ps['comp_id'], 'REF' + ref_chain_id)
                pA.addTestSequence(_test_ps_['comp_id'], ref_chain_id)
                pA.doAlign()

                myAlign = pA.getAlignment(ref_chain_id)

                length = len(myAlign)

                if length == 0:
                    return None, None

                _, _, conflict, _, _ = getScoreOfSeqAlign(myAlign)

                if conflict > 0:
                    return None, None

                _polySeqRst.append(_test_ps_)

                ref_seq_ids = []
                test_seq_ids = []
                idx1 = 0
                idx2 = 0
                for i in range(length):
                    myPr = myAlign[i]
                    myPr0 = str(myPr[0])
                    myPr1 = str(myPr[1])
                    if myPr0 != '.':
                        while idx1 < len(ref_ps['auth_seq_id']):
                            if ref_ps['comp_id'][idx1] == myPr0:
                                ref_seq_ids.append(ref_ps['auth_seq_id'][idx1])
                                idx1 += 1
                                break
                            idx1 += 1
                    else:
                        ref_seq_ids.append(None)
                    if myPr1 != '.':
                        while idx2 < len(_test_ps_['seq_id']):
                            if _test_ps_['comp_id'][idx2] == myPr1:
                                test_seq_ids.append(_test_ps_['seq_id'][idx2])
                                idx2 += 1
                                break
                            idx2 += 1
                    else:
                        test_seq_ids.append(None)

                for ref_seq_id, test_seq_id in zip(ref_seq_ids, test_seq_ids):
                    if ref_seq_id is not None and test_seq_id is not None:
                        _chainIdMapping[test_seq_id] = {'chain_id': ref_chain_id, 'seq_id': ref_seq_id}

                split = True

                offset = end + half_gap

    if not split:
        return None, None

    return _polySeqRst, _chainIdMapping


def retrieveRemappedChainId(chainIdRemap, seqId):
    """ Retrieve chain_id and seq_id from mapping dictionary based on sequence alignments.
    """

    try:

        item = chainIdRemap[seqId]

        return item['chain_id'], item['seq_id']

    except KeyError:
        return None, None
