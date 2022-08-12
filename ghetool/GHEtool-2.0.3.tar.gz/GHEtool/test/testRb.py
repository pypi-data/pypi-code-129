import pygfunction as gt
import math

mflow = 0.03  # l/s
Cp = 3930
rho = 1033
visc = 0.0079
kf = 0.475
mflow = mflow * rho / 1000
kp = 0.42
rout = 0.032/2
rin = 0.032/2-0.002

V = mflow / rho / (rin*rin*3.141569)

print("Re", rho * rin * 2 * V/ visc)

Rp = gt.pipes.conduction_thermal_resistance_circular_pipe(rin, rout, kp)
h_f = gt.pipes.convective_heat_transfer_coefficient_circular_pipe(mflow, rin, visc, rho, kf, Cp, 1e-6)
Rfpar = 1/(h_f * 2 * math.pi * rin)
print(Rp + Rfpar)

borehole = gt.boreholes.Borehole(150, 0, 0.13/2, 0, 0)
singleU = gt.pipes.SingleUTube(((0.089/2, 0), (-0.089/2, 0)), rin, rout, borehole, 1.9, 2, Rp+Rfpar, 10)
gt.pipes.thermal_resistances()
result = gt.pipes.borehole_thermal_resistance(singleU, mflow, 3930)
print(result)