from dataclasses import asdict

from .._core import internal_lidort as _lidort
from .input.fixed import FixedInputs, FixedLinInputs
from .input.modified import ModifiedInputs, ModifiedLinInputs


def run_lidort(
    fixed: FixedInputs,
    modified: ModifiedInputs,
    fixed_lin: FixedLinInputs,
    modified_lin: ModifiedLinInputs,
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

    _lidort(**inputs)
