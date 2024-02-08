from .._core import internal_lidort as _lidort
from .input.fixed import FixedInputs, FixedLinInputs
from .input.modified import ModifiedInputs, ModifiedLinInputs
from .output import LinOutputs, Outputs


def run_lidort(
    fixed: FixedInputs,
    modified: ModifiedInputs,
    fixed_lin: FixedLinInputs,
    modified_lin: ModifiedLinInputs,
    output: Outputs,
    lin_ouput: LinOutputs,
    num_repeat: int = 1,
):
    inputs = {
        **fixed.Bool.__dict__,
        **fixed.Cont.__dict__,
        **fixed.Sunrays.__dict__,
        **fixed.Chapman.__dict__,
        **fixed.Optical.__dict__,
        **fixed.Write.__dict__,
        **fixed.UserVal.__dict__,
        **modified.MBool.__dict__,
        **modified.MChapman.__dict__,
        **modified.MCont.__dict__,
        **modified.MSunrays.__dict__,
        **modified.MUserVal.__dict__,
        **modified.MOptical.__dict__,
        **fixed_lin.Cont.__dict__,
        **fixed_lin.Optical.__dict__,
        **modified_lin.MCont.__dict__,
        **output.Main.__dict__,
        **lin_ouput.Atmos.__dict__,
        **lin_ouput.Surf.__dict__,
        "num_repeat": num_repeat,
    }

    _lidort(**{k.lower(): v for k, v in inputs.items()})
