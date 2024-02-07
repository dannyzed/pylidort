import pylidort


def test_lidort():
    fixed = pylidort.FixedInputs()
    modified = pylidort.ModifiedInputs()

    fixed_lin = pylidort.FixedLinInputs()
    modified_lin = pylidort.ModifiedLinInputs()

    fixed.Cont.TS_LIDORT_ACCURACY = 1e99

    modified_lin.MCont.TS_DO_LINEARIZATION = False
    modified_lin.MCont.TS_DO_PROFILE_LINEARIZATION = False

    fixed_lin.Optical.TS_L_DELTAU_VERT_INPUT[:] = 1
    fixed_lin.Cont.TS_LAYER_VARY_FLAG[:] = False
    fixed_lin.Cont.TS_LAYER_VARY_NUMBER[:] = 0

    fixed.Optical.TS_DELTAU_VERT_INPUT[:] = 0.01
    modified.MOptical.TS_OMEGA_TOTAL_INPUT[:] = 0.9

    fixed.Cont.TS_NLAYERS = 200
    fixed.Cont.TS_NSTREAMS = 20

    modified.MUserVal.TS_USER_OBSGEOMS_INPUT[0, :] = (30.0, 20.0, 0.0)

    fixed.Optical.TS_PHASMOMS_TOTAL_INPUT[0, :] = 1.0
    fixed.Optical.TS_PHASMOMS_TOTAL_INPUT[2, :] = 0.5

    _ = pylidort.run_lidort(
        fixed=fixed,
        modified=modified,
        fixed_lin=fixed_lin,
        modified_lin=modified_lin,
        num_repeat=100,
    )
