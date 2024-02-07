from dataclasses import asdict

from .._core import internal_lidort as _lidort
from .input.fixed import FixedInputs, FixedLinInputs
from .input.modified import ModifiedInputs, ModifiedLinInputs
from .output import Outputs


def run_lidort(
    fixed: FixedInputs,
    modified: ModifiedInputs,
    fixed_lin: FixedLinInputs,
    modified_lin: ModifiedLinInputs,
    output: Outputs,
    num_repeat: int = 1,
):
    inputs = {
        **asdict(fixed.Bool),
        **asdict(fixed.Cont),
        **asdict(fixed.Sunrays),
        **asdict(fixed.Chapman),
        **asdict(fixed.Optical),
        **asdict(fixed.Write),
        **asdict(fixed.UserVal),
        **asdict(modified.MBool),
        **asdict(modified.MChapman),
        **asdict(modified.MCont),
        **asdict(modified.MSunrays),
        **asdict(modified.MUserVal),
        **asdict(modified.MOptical),
        **asdict(fixed_lin.Cont),
        **asdict(fixed_lin.Optical),
        **asdict(modified_lin.MCont),
        "num_repeat": num_repeat,
    }

    inputs = {k.lower(): v for k, v in inputs.items()}

    (
        output.Main.TS_INTENSITY,
        output.Main.TS_MEANI_DIFFUSE,
        output.Main.TS_FLUX_DIFFUSE,
        output.Main.TS_DNMEANI_DIRECT,
        output.Main.TS_DNFLUX_DIRECT,
        output.Main.TS_ALBMED_USER,
        output.Main.TS_TRNMED_USER,
        output.Main.TS_ALBMED_FLUXES,
        output.Main.TS_TRNMED_FLUXES,
        output.Main.TS_PLANETARY_TRANSTERM,
        output.Main.TS_PLANETARY_SBTERM,
        output.Main.TS_PATHGEOMS,
        output.Main.TS_LOSTRANS,
        output.Main.TS_LAYER_MSSTS,
        output.Main.TS_SURF_MSSTS,
        output.Main.TS_CONTRIBS,
    ) = _lidort(**inputs)
