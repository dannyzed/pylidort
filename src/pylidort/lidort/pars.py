MAXSTREAMS = 20
MAXLAYERS = 200
MAXFINELAYERS = 4
MAXMOMENTS_INPUT = 200
MAX_THERMAL_COEFFS = 2
MAXBEAMS = 8
MAX_USER_STREAMS = 1
MAX_USER_RELAZMS = 1
MAX_USER_OBSGEOMS = 8
MAX_USER_LEVELS = 2
MAX_PARTLAYERS = 2
MAX_TAYLOR_TERMS = 7
MAX_DIRECTIONS = 2
MAX_BRDF_KERNELS = 4

MAX_BRDF_PARAMETERS = 4

MAXSTREAMS_BRDF = 2
MAXSTREAMS_BRDF = 100

MAX_MSRS_MUQUAD = 50
MAX_MSRS_PHIQUAD = 100

MAXSTREAMS_SCALING = 24
MAX_ATMOSWFS = 3

MAX_SURFACEWFS = 1


MAX_SLEAVEWFS = 1


MAX_GEOMETRIES = MAX_USER_STREAMS * MAX_USER_RELAZMS * MAXBEAMS


MAX_ALLSTRMS = MAX_USER_STREAMS + MAXSTREAMS

MAX_ALLSTRMS_P1 = MAX_ALLSTRMS + MAXBEAMS


MAX_ALLSTRMS_P1 = MAX_ALLSTRMS + MAXBEAMS * MAXLAYERS

MAXMOMENTS = 2 * MAXSTREAMS
MAXFOURIER = 2 * MAXSTREAMS - 1

MAXSTHALF_BRDF = MAXSTREAMS_BRDF / 2

MAXSTREAMS_2 = 2 * MAXSTREAMS
MAXSTREAMS_P1 = MAXSTREAMS + 1

MAXTOTAL = MAXLAYERS * MAXSTREAMS_2
MAXBANDTOTAL = 9 * MAXSTREAMS - 2