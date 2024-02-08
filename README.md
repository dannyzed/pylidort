# pylidort
A Python interface to the (V)LIDORT family of radiative transfer models.

## Installation
After cloning the repository, the model can be installed with

```
pip install .
```

If you have `numpy` and a Fortran compiler installed.

## Usage
`pylidort` is designed to mimic the (V)LIDORT Fortran interfaces as closely as possible, for example

```python
import pylidort


fixed = pylidort.FixedInputs()
modified = pylidort.ModifiedInputs()

fixed_lin = pylidort.FixedLinInputs()
modified_lin = pylidort.ModifiedLinInputs()

output = pylidort.Outputs()
lin_output = pylidort.LinOutputs()

fixed.Optical.TS_DELTAU_VERT_INPUT[:] = 0.01
modified.MOptical.TS_OMEGA_TOTAL_INPUT[:] = 0.9

fixed.Cont.TS_NLAYERS = 200
fixed.Cont.TS_NSTREAMS = 4

modified.MUserVal.TS_USER_OBSGEOMS_INPUT[0, :] = (30.0, 20.0, 0.0)

fixed.Optical.TS_PHASMOMS_TOTAL_INPUT[0, :] = 1.0
fixed.Optical.TS_PHASMOMS_TOTAL_INPUT[2, :] = 0.5

pylidort.run_lidort(
    fixed=fixed,
    modified=modified,
    fixed_lin=fixed_lin,
    modified_lin=modified_lin,
    output=output,
    lin_ouput=lin_output
)

print(output.Main.TS_INTENSITY)
```

For information on (V)LIDORT and the input/output parameters we encourage users to obtain their respective user manuals.


## Disclaimer
This project is not officially associated with the developers of (V)LIDORT (http://www.rtslidort.com/about_overview.html).
Any issues related to the model itself and not the wrapper should be raised to the (V)LIDORT developers.

## License
`pylidort` is made available under the GPL-3 license (see [License](https://github.com/usask-arg/sasktran2/blob/main/license.txt))

The bundled (V)LIDORT code bases are also available under the same GPL-3 license.
