from dataclasses import dataclass, field

import numpy as np

from .. import pars


@dataclass
class FixedBoolean:
    """
    Wrapper around the (V)LIDORT Input Class (V)LIDORT_Fixed_Boolean
    """

    TS_DO_FULLRAD_MODE: bool = True  # Full radiance calculation

    TS_DO_THERMAL_EMISSION: bool = False  # Thermal emission calculation
    TS_DO_SURFACE_EMISSION: bool = False  # Surface emission calculation

    TS_DO_PLANE_PARALLEL: bool = (
        True  # Beam particular solution pseudo-spherical options
    )

    TS_DO_BRDF_SURFACE: bool = False  # BRDF surface control

    TS_DO_UPWELLING: bool = True  # Directional control
    TS_DO_DNWELLING: bool = False

    TS_DO_TOA_CONTRIBS: (
        bool  # Version 3.8.3. Introduce TOA Contributions flag (SPECIALIST OPTION)
    ) = False

    TS_DO_SURFACE_LEAVING: bool = False  # Surface leaving control
    TS_DO_SL_ISOTROPIC: bool = False

    TS_DO_WATER_LEAVING: bool = False  # Water leaving flag
    TS_DO_FLUORESCENCE: bool = False  # Fluorescence flag

    TS_DO_TF_ITERATION: bool = False  # Water-leaving transmittance interation flag

    TS_DO_WLADJUSTED_OUTPUT: bool = False  # Water-leaving output flag

    TS_DO_TOA_ILLUMINATION: bool = False  # TOA illumination flag
    TS_DO_BOA_ILLUMINATION: bool = False  # BOA illumination flag

    TS_DO_ALBTRN_MEDIA: np.array = (
        False,
        False,
    )  # Computing medium albedos and transmissivities for isotropic sources at TOA/BOA,  1 = Isotropic illumination from Top, 2 = Isotropic illumination from BOA

    TS_DO_PLANETARY_PROBLEM: bool = False  # Flag for the Planetary problem calculation

    TS_DO_MSSTS: bool = (
        False  # Flag for calculating MSSTs output (Multiple scattering source terms)
    )


@dataclass
class FixedControl:
    """
    Wrapper around the (V)LIDORT_Fixed_Control class
    """

    TS_TAYLOR_ORDER: int = 3  # Taylor ordering parameter. Should be set to 2 or 3

    TS_NSTREAMS: int = 8  # Number of discrete ordinate streams

    TS_NLAYERS: int = 1  # Number of computational layers

    TS_NFINELAYERS: int = (
        3  # Number of fine layers subdividing all computational layers (only required for the outdiong spherical correction algorithm)
    )

    TS_N_THERMAL_COEFFS: int = (
        0  # Number of thermal coefficients (2 should be the default)
    )

    TS_LIDORT_ACCURACY: float = 0  # Accuracy for convergence of Fourier series

    TS_ASYMTX_TOLERANCE: float = 1e-20  # ASYMTX tolerance variable

    TS_TF_MAXITER: int = (
        0  # Water leaving: Control for iterative calculation of transmittance
    )
    TS_TF_CRITERION: float = (
        0.0  # Water leaving: Convergence criterion for iterative calculation of transmittance
    )

    TS_TOA_ILLUMINATION: float = (
        0.0  # TOA Isotropic illumination, must be solar-flux normalized
    )
    TS_BOA_ILLUMINATION: float = (
        0.0  # BOA Isotropic illumination, must be solar-flux normalized
    )


@dataclass
class FixedSunrays:
    """
    Wrapper around the (V)LIDORT_Fixed_Sunrays class
    """

    TS_FLUX_FACTOR: float = (
        1.0  # Solar flux factor (should be 1.0 or pi, same for all solar beams)
    )


@dataclass
class FixedUserValues:
    """
    Wrapper around the (V)LIDORT_Fixed_UserValues class
    """

    TS_N_USER_LEVELS: int = 1  # User-defined vertical level output


@dataclass
class FixedChapman:
    """
    Wrapper around the (V)LIDORT_Fixed_Chapman class
    """

    TS_HEIGHT_GRID: np.array = field(
        default_factory=lambda: np.linspace(
            1, 0, pars.MAXLAYERS + 1, endpoint=True, dtype=float
        )
    )  # Multilayer Height inputs in [km], size (MAXLAYERS+1)

    TS_PRESSURE_GRID: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXLAYERS + 1, dtype=float, order="F")
    )  # Multilayer Pressure inputs in [mb], size (MAXLAYERS+1), required for refractive geometry
    TS_TEMPERATURE_GRID: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXLAYERS + 1, dtype=float, order="F")
    )  # Multilayer Temperature inputs in [K], size (MAXLAYERS+1), required for refractive geometry

    TS_FINEGRID: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXLAYERS)
    )  # Number of fine-layer gradations, size (MAXLAYERS), required for refractive geometry

    TS_RFINDEX_PARAMETER: float = 0.000288  # Refractive index parameter


@dataclass
class FixedOptical:
    """
    Wrapper around the LIDORT_Fixed_Optical class
    """

    TS_DELTAU_VERT_INPUT: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXLAYERS)
    )  # Multilayer optical property (bulk), size (MAXLAYERS)

    TS_PHASMOMS_TOTAL_INPUT: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAXMOMENTS_INPUT + 1, pars.MAXLAYERS), order="F"
        )
    )  # Phase function Legendre-polynomial expansion coefficients, include all that you require for exact single scatter calculations (MAXMOMENTS_INPUT+1, MAXLAYERS)

    TS_PHASFUNC_INPUT_UP: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAXLAYERS, pars.MAX_GEOMETRIES), order="F"
        )
    )  # Phase function input as an alternative to the use of expansion coefficients in the single-scatter codes, shape (MAXLAYERS, MAX_GEOMETRIES)
    TS_PHASFUNC_INPUT_DN: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAXLAYERS, pars.MAX_GEOMETRIES), order="F"
        )
    )  # Phase function input as an alternative to the use of expansion coefficients in the single-scatter codes, shape (MAXLAYERS, MAX_GEOMETRIES)

    TS_LAMBERTIAN_ALBEDO: float = 0.0  # Lambertian surface control

    TS_THERMAL_BB_INPUT: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXLAYERS + 1)
    )  # Thermal black body functions (MAXLAYERS+1)

    TS_SURFACE_BB_INPUT: float = 0.0  # Surface black body inputs

    TS_ATMOS_WAVELENGTH: float = 0.76  # Add wavelength (microns) as a Diagnostic


@dataclass
class FixedWrite:
    """
    Wrapper around the LIDORT_Fixed_Write class
    """

    TS_DO_DEBUG_WRITE: bool = False  # Debug control

    TS_DO_WRITE_INPUT: bool = False  # Input file
    TS_INPUT_WRITE_FILENAME: str = ""  # Input file name

    TS_DO_WRITE_SCENARIO: bool = False  # Scene file
    TS_SCENARIO_WRITE_FILENAME: str = ""  # Scen file

    TS_DO_WRITE_FOURIER: bool = False  # Fourier component results file
    TS_FOURIER_WRITE_FILENAME: str = ""

    TS_DO_WRITE_RESULTS: bool = False  # Results file
    TS_RESULTS_WRITE_FILENAME: str = ""


@dataclass
class FixedInputs:
    """
    Wrapper around the LIDORT_Fixed_Inputs class
    """

    Bool: FixedBoolean = field(default_factory=FixedBoolean)
    Cont: FixedControl = field(default_factory=FixedControl)
    Sunrays: FixedSunrays = field(default_factory=FixedSunrays)
    UserVal: FixedUserValues = field(default_factory=FixedUserValues)
    Chapman: FixedChapman = field(default_factory=FixedChapman)
    Optical: FixedOptical = field(default_factory=FixedOptical)
    Write: FixedWrite = field(default_factory=FixedWrite)


@dataclass
class FixedLinControl:
    """
    Wrapper around the LIDORT_Fixed_LinControl class
    """

    TS_LAYER_VARY_FLAG: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXLAYERS, dtype=bool)
    )  # Layer vary flag
    TS_LAYER_VARY_NUMBER: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXLAYERS, dtype=int)
    )  # Layer vary number

    TS_N_TOTALCOLUMN_WFS: int = 0  # Total number of column weighting functions
    TS_N_SURFACE_WFS: int = 0  # Number of surface weighting functions
    TS_N_SLEAVE_WFS: int = 0

    TS_COLUMNWF_NAMES: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_ATMOSWFS, dtype=str)
    )  # Column weighting function names
    TS_PROFILEWF_NAMES: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_ATMOSWFS, dtype=str)
    )  # Profile weighting function names


@dataclass
class FixedLinOptical:
    """
    Wrapper around the LIDORT_Fixed_LinOptical class
    """

    TS_L_DELTAU_VERT_INPUT: np.array = field(
        default_factory=lambda: np.zeros((pars.MAX_ATMOSWFS, pars.MAXLAYERS))
    )
    TS_L_OMEGA_TOTAL_INPUT: np.array = field(
        default_factory=lambda: np.zeros((pars.MAX_ATMOSWFS, pars.MAXLAYERS))
    )
    TS_L_PHASMOMS_TOTAL_INPUT: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXMOMENTS_INPUT + 1, pars.MAXLAYERS)
        )
    )

    TS_L_PHASFUNC_INPUT_UP: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXLAYERS, pars.MAX_GEOMETRIES)
        )
    )
    TS_L_PHASFUNC_INPUT_DN: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXLAYERS, pars.MAX_GEOMETRIES)
        )
    )


@dataclass
class FixedLinInputs:
    """
    Wrapper around the LIDORT_Fixed_LinInputs class
    """

    Cont: FixedLinControl = field(default_factory=FixedLinControl)
    Optical: FixedLinOptical = field(default_factory=FixedLinOptical)
