###############################################
###
### This file is generated by txpp. Do not edit.
###
### Input file : cylHallThruster.pre
### Output file: cylHallThruster.in
### Translation: Sat, 22 Dec 2018 19:41:18
###
###############################################

##########
#
# Import needed modules
#
##########

import sys
sys.path.append(".")
import math

TXPP_RANK	=	0
TXPP_NUM_RANKS	=	4
PI	=	3.141592653589793
PIO2	=	1.5707963267948966
TWOPI	=	6.283185307179586
LIGHTSPEED	=	299792458.0
C2	=	8.987551787368176e+16
MU0	=	1.2566370614359173e-06
EPSILON0	=	8.854187817620389e-12
ELECMASS	=	9.10938215e-31
PROTMASS	=	1.672621637e-27
MUONMASS	=	1.8835313e-28
ELEMCHARGE	=	1.602176487e-19
KB	=	1.3806504e-23
PROTON_GMA	=	1.7928473508
ELECTRON_GMA	=	0.00115965218091
ELECCHARGE	=	-1.602176487e-19
ELECMASSEV	=	510998.90984764055
B0	=	0.6
anodeV	=	300.0
channelEndZ	=	0.0005
innerRad	=	0.0007
maxXeGasDens	=	1e+21
outerRad	=	0.001
rMax	=	0.0011
rMin	=	0.0005
xeMaxDensity	=	5e+22
xenonCharge	=	8.65175e-18
xenonMass	=	2.19615e-25
zMax	=	0.0007
zMin	=	0.0
VPMW_COORDINATE_SYSTEM	=	"cylindrical"
VPMW_GRID_SPACING	=	"uniform"
VPMW_NDIM	=	2
VPMW_PRECISION	=	"double"
VPMW_USE_GPU	=	False
VPMW_SIMULATION_TYPE	=	"electrostatic"
VPMW_INCLUDE_PARTICLES	=	True
VPMW_MAX_ELECTRON_DENSITY	=	1.e20
VPMW_MAX_ELECTRON_TEMP_EV	=	1.0
VPMW_DUMP_NODAL_FIELDS	=	True
VPMW_COLLISIONS_FRAMEWORK	=	"reduced"
VPMW_RESTORE_GRID_BNDRY	=	True
VPMW_DECOMP	=	"default"
VPMW_TOP_LEVEL_VERBOSITY	=	127
VPMW_GRID_TYPE	=	"Cylindrical"
VPMW_DISP_FIELD_NAME_I	=	"concatenate(E,I)"
VPMW_DUMP_PERIOD	=	None
VPMW_PERIODIC_DIRS	=	None
VPMW_PERIODICITY_BOOL	=	[False, False, False]
VPMW_USE_MOVING_WINDOW	=	None
VPMW_CFL_NUMBER	=	1.0
VPMW_DMFRAC	=	0.5
VPMW_PRECISION	=	"double"
VPMW_HAS_DIELECTRICS	=	False
VPMW_DISP_FIELD_NAME	=	"E"
VPMW_HAS_DIELECTRICS	=	True
VPMW_DISP_FIELD_NAME	=	"D"
VPMW_DIELECTRIC_SHAPE_NAME_ARRAY	=	""
VPMW_DIELECTRIC_SHAPE_BOUNDARY_NAME_ARRAY	=	""
VPMW_DIELECTRIC_SHAPE_MATERIAL_ARRAY	=	""
VPMW_PERMITTIVITIES_DICT	=	""
true	=	1
TRUE	=	1
false	=	0
FALSE	=	0
VPMW_ELEC_POTENTIAL_FIELD_NAME	=	"Phi"
VPMW_CHARGE_DENSITY_FIELD_NAME	=	"ChargeDensity"
VPMW_PRE_CONDITIONER	=	""
VPMW_NUM_GUARD_CELLS	=	1
VPMW_NUM_GUARD_CELLSP1	=	2
VPMW_N0	=	10
VPMW_N1	=	11
VPMW_N2	=	12
VPMW_L0	=	1
VPMW_L1	=	1
VPMW_L2	=	1
VPMW_BGN0	=	0.0
VPMW_BGN1	=	0.0
VPMW_BGN2	=	0.0
VPMW_L0	=	1.0
VPMW_L1	=	1.0
VPMW_L2	=	1.0
VPMW_EXTERNAL_FIELD	=	False
By	=	"(H(0.0005-x)*H(y-0.0007)*H(0.001-y)*0.6*(0.0007/y)*exp(-16.0*(x/0.0005-1.0)*(x/0.0005-1.0))+H(x-0.0005)*H(y-0.0007)*H(0.001-y)*0.6*(0.0007/y)*exp(-16.0*((x-0.0005)/0.0005)*((x-0.0005)/0.0005)))"
initialGasDensity	=	"(5e+22*(0.1+(1.0-x/0.0005))*H(0.0005-x)*H(y-0.0007)*H(0.001-y)+H(x-0.0005)*5e+22*0.1*(1.0-(x-0.0005)/0.0005))"
relPermFunc	=	"((1.0+3.6*H(0.0007-y)*H(0.0005-x)+3.6*H(y-0.001)*H(0.0005-x)))"
velocityFunctionZ	=	-2965000.0
velocityFunctionR	=	"(1.48e6*gauss())"
VPMW_NUM_GUARD_CELLS	=	2
VPMW_NUM_GUARD_CELLSP1	=	3
VPMW_BGN0	=	0.0
VPMW_BGN1	=	0.0005
VPMW_L0	=	0.0007
VPMW_L1	=	0.0006000000000000001
VPMW_N0	=	128
VPMW_N1	=	80
VPMW_UB0P1	=	129
VPMW_UB1P1	=	81
VPMW_UB2P1	=	13
VPMW_END0	=	0.0007
VPMW_END1	=	0.0011
VPMW_END2	=	1.0
VPMW_DL0	=	5.46875e-06
VPMW_DL1	=	7.500000000000001e-06
VPMW_DL2	=	0.08333333333333333
VPMW_DLI0	=	182857.14285714287
VPMW_DLI1	=	133333.3333333333
VPMW_DLI2	=	12.0
VPMW_DLISQ	=	51214512471.65533
VPMW_DLI	=	226306.23604234887
VPMW_PERIODIC_DIRS	=	[]
VPMW_PERIODICITY_BOOL	=	[False, False, False]
VPMW_BGNZ	=	0.0
VPMW_BGNR	=	0.0005
VPMW_DZ	=	5.46875e-06
VPMW_DR	=	7.500000000000001e-06
VPMW_DLI	=	182857.14285714287
VPMW_DMFRAC	=	0.5
VPMW_CFL_NUMBER	=	1
VPMW_DT	=	3.7251800000e-13
VPMW_NSTEPS	=	6000
VPMW_DUMP_PERIOD	=	1000
VPMW_DUMP_GROUP_SIZE	=	1
VPMW_EXTERNAL_FIELD	=	True

