import math
from typing import Optional

MINIMUM_LIQUIDITY = 1000
SLOPE_SWAP_RATE = 1000
# https://github.com/DeFiCh/ain/blob/master/src/chainparams.cpp
BAY_FRONT_GARDENS_HEIGHT = 488300
FORT_CANNING_HILL_HEIGHT = 1604999

class ArithUint256:
    # https://github.com/bitcoin/bitcoin/blob/master/src/arith_uint256.cpp

    __slots__ = '_value', '_compact'

    def __init__(self, value: int) -> None:
        self._value = value
        self._compact: Optional[int] = None

    @classmethod
    def from_compact(cls, compact) -> 'ArithUint256':
        size = compact >> 24
        word = compact & 0x007fffff
        if size <= 3:
            return cls(word >> 8 * (3 - size))
        else:
            return cls(word << 8 * (size - 3))

    @property
    def value(self) -> int:
        return self._value

    @property
    def compact(self) -> int:
        if self._compact is None:
            self._compact = self._calculate_compact()
        return self._compact

    @property
    def negative(self) -> int:
        return self._calculate_compact(negative=True)

    @property
    def bits(self) -> int:
        """ Returns the position of the highest bit set plus one. """
        bits = bin(self._value)[2:]
        for i, d in enumerate(bits):
            if d:
                return (len(bits) - i) + 1
        return 0

    @property
    def low64(self) -> int:
        return self._value & 0xffffffffffffffff

    def _calculate_compact(self, negative=False) -> int:
        size = (self.bits + 7) // 8
        if size <= 3:
            compact = self.low64 << 8 * (3 - size)
        else:
            compact = ArithUint256(self._value >> 8 * (size - 3)).low64
        # The 0x00800000 bit denotes the sign.
        # Thus, if it is already set, divide the mantissa by 256 and increase the exponent.
        if compact & 0x00800000:
            compact >>= 8
            size += 1
        assert (compact & ~0x007fffff) == 0
        assert size < 256
        compact |= size << 24
        if negative and compact & 0x007fffff:
            compact |= 0x00800000
        return compact

    def __mul__(self, x):
        # Take the mod because we are limited to an unsigned 256 bit number
        return ArithUint256((self._value * x) % 2 ** 256)
    
    def __add__(self, x):
        # Take the mod because we are limited to an unsigned 256 bit number
        return ArithUint256((self._value + x) % 2 ** 256)
    
    def __sub__(self, x):
        # Take the mod because we are limited to an unsigned 256 bit number
        return ArithUint256((self._value - x))

    def __truediv__(self, x):
        return ArithUint256(int(self._value / x))

    def __gt__(self, other):
        return self._value > other

    def __lt__(self, other):
        return self._value < other

def addPoolLiquidity(amountA,amountB,reserveA,reserveB,totalLiquidity):
    # No Checks included! Only useable for valid block transactions!
    # https://github.com/DeFiCh/ain/blob/a7d914f15f762d121ac2c5d07d38d30cf7e09d4d/src/masternodes/poolpairs.cpp
    if totalLiquidity == 0:
        liq = ArithUint256(amountA) * amountB
        liquidity = int(math.floor(math.sqrt(liq.low64)))
        if liquidity < MINIMUM_LIQUIDITY:
            return 0
        else:
            return liquidity - MINIMUM_LIQUIDITY
    
    totalLiquidity = totalLiquidity + MINIMUM_LIQUIDITY
    
    liqA = ArithUint256(amountA) * totalLiquidity / reserveA
    liqB = ArithUint256(amountB) * totalLiquidity / reserveB

    return min(liqA.low64, liqB.low64)

def addPoolLiquidityOptimiser():
    # TODO: build opitimiser
    # How to get max liquidity(tokens) from amountA, amountB input
    #########################
    # liquidity -= MINIMUM_LIQUIDITY;
    #     // MINIMUM_LIQUIDITY is a hack for non-zero division
    #     totalLiquidity = MINIMUM_LIQUIDITY;
    ####################################
    # if ((std::max(liqA, liqB) - liquidity) * 100 / liquidity >= 3) {
    #             return Res::Err("Exceeds max ratio slippage protection of 3%%");
    #         }
    pass

def removePoolLiquidity(liquidity,reserveA,reserveB,totalLiquidity):
    # No Checks included! Only useable for valid block transactions!
    # https://github.com/DeFiCh/ain/blob/a7d914f15f762d121ac2c5d07d38d30cf7e09d4d/src/masternodes/poolpairs.cpp
    amountA = ArithUint256(liquidity) * reserveA / totalLiquidity
    amountB =  ArithUint256(liquidity) * reserveB / totalLiquidity

    return amountA.low64,amountB.low64

def poolSwap(block,tokenFrom,poolSymbol,fromAmount,reserveA,reserveB,commission=0,dexfeeInPct=0):
    # No Checks included! Only useable for valid block transactions!
    # https://github.com/DeFiCh/ain/blob/a7d914f15f762d121ac2c5d07d38d30cf7e09d4d/src/masternodes/poolpairs.cpp


    # bool const forward = in.nTokenId == idTokenA;
    # auto& reserveF = forward ? reserveA : reserveB;
    # auto& reserveT = forward ? reserveB : reserveA;
    if tokenFrom == poolSymbol.split('-')[0]:
        bForward = True
    else:
        bForward = False

    if bForward:
        reserveF = reserveA
        reserveT = reserveB
    else:
        reserveT = reserveA
        reserveF = reserveB

    # claim trading fee
    tradeFee = int(fromAmount * commission)
    fromAmount = fromAmount - tradeFee

    # claim dex fee
    dexfeeInAmount = int(fromAmount * dexfeeInPct)
    fromAmount = fromAmount - dexfeeInAmount

    unswapped = fromAmount
    swapped = 0
    poolFrom = reserveF
    poolTo = reserveT
    if poolFrom/SLOPE_SWAP_RATE < unswapped:
        chunk = poolFrom/SLOPE_SWAP_RATE
    else:
        chunk = unswapped
    if block < BAY_FRONT_GARDENS_HEIGHT:
        while unswapped > 0:
            stepFrom = min(chunk,unswapped)
            stepTo = poolTo * stepFrom / poolFrom
            poolFrom = poolFrom + stepFrom
            poolTo = poolTo - stepTo
            unswapped = unswapped - stepFrom
            swapped = swapped + stepTo
    else:
        # Better results without ArithUint256 (2022/08/11)
        #swapped = (ArithUint256(poolTo) * poolFrom / (poolFrom + unswapped)) * -1 + poolTo
        swapped = poolTo - (poolTo * poolFrom / (poolFrom + unswapped))
        if block >= FORT_CANNING_HILL_HEIGHT and swapped != 0:
            #swapped = math.floor(swapped.value)
            swapped = math.floor(swapped)

        poolFrom = poolFrom + unswapped
        poolTo = poolTo - swapped
    
    return int(poolFrom),int(poolTo),int(swapped)

# TEST FIRST FOUR DAX-DUSD TX
# if __name__ == '__main__':
#     amountA = 20000000
#     amountB = 456000000
#     reserveA = 0
#     reserveB = 0
#     totalLiq = 0
#     i = addPoolLiquidity(amountA,amountB,reserveA,reserveB,totalLiq)
#     print(i)

#     reserveA = amountA
#     reserveB = amountB
#     totalLiq = i
#     amountA = 1000000
    
#     poolF,poolT,swapped = poolSwap(2102372,'DUSD','DAX-DUSD',amountA,reserveA,reserveB,0.002,0.001)
#     print(swapped)
#     reserveA = poolT + 1 #correction
#     reserveB = poolF
#     amountA = 5000000
    
#     poolF,poolT,swapped = poolSwap(2102378,'DUSD','DAX-DUSD',amountA,reserveA,reserveB,0.002,0.001)
#     print(swapped)
    
#     reserveA = poolT + 2
#     reserveB = poolF
#     amountA = 3300000
#     amountB = 75569367
#     i = addPoolLiquidity(amountA,amountB,reserveA,reserveB,totalLiq)
#     print(i)
