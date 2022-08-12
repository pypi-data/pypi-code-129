import complex

HBAR = 1
hbar = complex.ToComplex(HBAR)
hbarSquared = hbar.square()
halfhbar = complex.ToComplex(.5 * HBAR)
ihbar = complex.i * hbar
isubhbar = complex.i / hbar

C = 299792458
c = complex.ToComplex(C)

DELTA = .001
delta = complex.ToComplex(DELTA)