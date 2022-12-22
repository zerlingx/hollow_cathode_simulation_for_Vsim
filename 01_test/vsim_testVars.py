###############################################
###
### This file is generated by txpp. Do not edit.
###
### Input file : vsim_test.pre
### Output file: vsim_test.in
### Translation: Sat, 08 Dec 2018 21:27:11
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
VPMW_COORDINATE_SYSTEM	=	"cartesian"
VPMW_GRID_SPACING	=	"uniform"
VPMW_NDIM	=	2
VPMW_PRECISION	=	"double"
VPMW_USE_GPU	=	False
VPMW_SIMULATION_TYPE	=	"no field solver"
VPMW_INCLUDE_PARTICLES	=	False
VPMW_RESTORE_GRID_BNDRY	=	True
VPMW_DECOMP	=	"default"
VPMW_TOP_LEVEL_VERBOSITY	=	127
VPMW_GRID_TYPE	=	"UniformCartesian"
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
VPMW_INCLUDE_PARTICLES	=	False
VPMW_BGN0	=	-0.0025
VPMW_BGN1	=	-0.0005
VPMW_L0	=	0.005
VPMW_L1	=	0.006
VPMW_N0	=	400
VPMW_N1	=	480
VPMW_UB0P1	=	401
VPMW_UB1P1	=	481
VPMW_UB2P1	=	13
VPMW_END0	=	0.0025
VPMW_END1	=	0.0055
VPMW_END2	=	1.0
VPMW_DL0	=	1.25e-05
VPMW_DL1	=	1.25e-05
VPMW_DL2	=	0.08333333333333333
VPMW_DLI0	=	80000.0
VPMW_DLI1	=	80000.0
VPMW_DLI2	=	12.0
VPMW_DLISQ	=	12800000000.0
VPMW_DLI	=	113137.0849898476
VPMW_PERIODIC_DIRS	=	[]
VPMW_PERIODICITY_BOOL	=	[False, False, False]
VPMW_BGNX	=	-0.0025
VPMW_DX	=	1.25e-05
VPMW_BGNY	=	-0.0005
VPMW_DY	=	1.25e-05
VPMW_BGNZ	=	0.0
VPMW_DZ	=	0.08333333333333333
VPMW_DLI	=	113137.0856262437
VPMW_DMFRAC	=	0.4
VPMW_CFL_NUMBER	=	0.95
VPMW_DT	=	1e-12
VPMW_NSTEPS	=	4000
VPMW_DUMP_PERIOD	=	500
VPMW_DUMP_GROUP_SIZE	=	1
Anode_VPM_PERMITTIVITY	=	"Iron_VPM_PERMITTIVITY"
Cathode_VPM_PERMITTIVITY	=	"Iron_VPM_PERMITTIVITY"

