project(
  'pylidort',
  'c',
  license: 'GPL-3',
  version: '0.0.0',
  meson_version: '>= 1.1.0',
  default_options: [
    'c_std=c99',
    'cpp_std=c++17',
  ],
)

py3 = import('python').find_installation(pure: false)
py3_dep = py3.dependency()

cc = meson.get_compiler('c')

# Adding at project level causes many spurious -lgfortran flags.
add_languages('fortran', native: false)
ff = meson.get_compiler('fortran')
if ff.has_argument('-Wno-conversion')
  add_project_arguments('-Wno-conversion', language: 'fortran')
endif

if host_machine.system() == 'darwin' and cc.has_link_argument('-Wl,-ld_classic')
  # New linker introduced in macOS 14 not working yet, see gh-19357 and gh-19387
  add_project_link_arguments('-Wl,-ld_classic', language : ['c', 'cpp', 'fortran'])
endif

lidort_sources = [
    'lib/lidort_def/lidort_inputs_def.f90',
    'lib/lidort_def/lidort_io_defs.f90',
    'lib/lidort_def/lidort_lin_inputs_def.f90',
    'lib/lidort_def/lidort_lin_io_defs.f90',
    'lib/lidort_def/lidort_lin_outputs_def.f90',
    'lib/lidort_def/lidort_lin_sup_brdf_def.f90',
    'lib/lidort_def/lidort_lin_sup_def.f90',
    'lib/lidort_def/lidort_lin_sup_sleave_def.f90',
    'lib/lidort_def/lidort_lin_sup_ss_def.f90',
    'lib/lidort_def/lidort_outputs_def.f90',
    'lib/lidort_def/lidort_pars.f90',
    'lib/lidort_def/lidort_sup_brdf_def.f90',
    'lib/lidort_def/lidort_sup_def.f90',
    'lib/lidort_def/lidort_sup_sleave_def.f90',
    'lib/lidort_def/lidort_sup_ss_def.f90',
    'lib/lidort_focode/FO_DTWPgeometry_master.f90',
    'lib/lidort_focode/FO_geometry_Generic.f90',
    'lib/lidort_focode/FO_Planckfunc.f90',
    'lib/lidort_focode/FO_ScalarSS_RTCalcs_I.f90',
    'lib/lidort_focode/FO_ScalarSS_RTCalcs_ILCS.f90',
    'lib/lidort_focode/FO_ScalarSS_RTCalcs_ILPS.f90',
    'lib/lidort_focode/FO_ScalarSS_Spherfuncs.f90',
    'lib/lidort_focode/FO_SSWPgeometry_master.f90',
    'lib/lidort_focode/FO_Taylor.f90',
    'lib/lidort_focode/FO_Thermal_RTCalcs_I.f90',
    'lib/lidort_focode/FO_Thermal_RTCalcs_ILCS.f90',
    'lib/lidort_focode/FO_Thermal_RTCalcs_ILPS.f90',
    'lib/lidort_focode/FO_WPgeometry_Routines.f90',
    'lib/lidort_focode/SFO_LinMasters.f90',
    'lib/lidort_focode/SFO_Master.f90',
    'lib/lidort_main/linearized/lidort_l_inputs.f90',
    'lib/lidort_main/linearized/lidort_l_thermalsup.f90',
    'lib/lidort_main/linearized/lidort_l_writemodules.f90',
    'lib/lidort_main/linearized/lidort_la_miscsetups.f90',
    'lib/lidort_main/linearized/lidort_lbbf_jacobians.f90',
    'lib/lidort_main/linearized/lidort_lc_bvproblem.f90',
    'lib/lidort_main/linearized/lidort_lc_mediaprops.f90',
    'lib/lidort_main/linearized/lidort_lc_miscsetups.f90',
    'lib/lidort_main/linearized/lidort_lc_PostProcessing.f90',
    'lib/lidort_main/linearized/lidort_lc_wfatmos.f90',
    'lib/lidort_main/linearized/lidort_lcs_converge.f90',
    'lib/lidort_main/linearized/lidort_lcs_masters_V3p8p3.f90',
    'lib/lidort_main/linearized/lidort_lp_bvproblem.f90',
    'lib/lidort_main/linearized/lidort_lp_mediaprops.f90',
    'lib/lidort_main/linearized/lidort_lp_miscsetups.f90',
    'lib/lidort_main/linearized/lidort_lp_PostProcessing.f90',
    'lib/lidort_main/linearized/lidort_lp_wfatmos.f90',
    'lib/lidort_main/linearized/lidort_lpc_solutions.f90',
    'lib/lidort_main/linearized/lidort_lps_converge.f90',
    'lib/lidort_main/linearized/lidort_lps_masters_V3p8p3.f90',
    'lib/lidort_main/linearized/lidort_ls_wfsleave.f90',
    'lib/lidort_main/linearized/lidort_ls_wfsurface.f90',
    'lib/lidort_main/linearized/lidort_sfo_lcs_interface.f90',
    'lib/lidort_main/linearized/lidort_sfo_lps_interface.f90',
    'lib/lidort_main/regular/lidort_aux.f90',
    'lib/lidort_main/regular/lidort_bvproblem.f90',
    'lib/lidort_main/regular/lidort_converge.f90',
    'lib/lidort_main/regular/lidort_geometry.f90',
    'lib/lidort_main/regular/lidort_getplanck.f90',
    'lib/lidort_main/regular/lidort_inputs.f90',
    'lib/lidort_main/regular/lidort_intensity.f90',
    'lib/lidort_main/regular/lidort_masters_V3p8p3.f90',
    'lib/lidort_main/regular/lidort_mediaprops.f90',
    'lib/lidort_main/regular/lidort_miscsetups.f90',
    'lib/lidort_main/regular/lidort_PostProcessing.f90',
    'lib/lidort_main/regular/lidort_sfo_interface.f90',
    'lib/lidort_main/regular/lidort_solutions.f90',
    'lib/lidort_main/regular/lidort_Taylor.f90',
    'lib/lidort_main/regular/lidort_thermalsup.f90',
    'lib/lidort_main/regular/lidort_writemodules.f90'
]

liblidort = static_library('lidort', lidort_sources)


py_mod = import('python')
py = py_mod.find_installation(pure: false)
py_dep = py.dependency()

incdir_numpy = run_command(py,
  ['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

incdir_f2py = run_command(py,
    ['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get_include())'],
    check : true
).stdout().strip()

lidort_wrapper_source = custom_target('_coremodule.c',
  input : ['lib/lidort_f2py/lidort.f90'],  # .f so no F90 wrappers
  output : ['_coremodule.c', '_core-f2pywrappers.f'],
  command : [py, '-m', 'numpy.f2py', '@INPUT@', '-m', '_core', '--lower']
)

inc_np = include_directories(incdir_numpy, incdir_f2py)

py.extension_module('_core',
  ['lib/lidort_f2py/lidort.f90', lidort_wrapper_source],
  incdir_f2py / 'fortranobject.c',
  include_directories: inc_np,
  dependencies : py_dep,
  link_with: liblidort,
  install : true,
  subdir: 'pylidort'
)

py.install_sources([
    'src/pylidort/__init__.py',
    'src/pylidort/_version.py',
],
subdir: 'pylidort'
)

py.install_sources([
    'src/pylidort/lidort/__init__.py',
    'src/pylidort/lidort/pars.py',
],
subdir: 'pylidort/lidort'
)

py.install_sources([
    'src/pylidort/lidort/input/__init__.py',
    'src/pylidort/lidort/input/fixed.py',
    'src/pylidort/lidort/input/modified.py',
],
subdir: 'pylidort/lidort/input'
)

py.install_sources([
    'src/pylidort/lidort/output/__init__.py',
],
subdir: 'pylidort/lidort/output'
)
