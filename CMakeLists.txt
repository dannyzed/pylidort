project(pylidort)
cmake_minimum_required(VERSION 3.20.0)

# Convenience
if(UNIX AND NOT APPLE)
  set(LINUX TRUE)
endif()

enable_language(Fortran)

set(LIDORT_DEF_SOURCES
    lib/lidort_def/lidort_inputs_def.f90
    lib/lidort_def/lidort_io_defs.f90
    lib/lidort_def/lidort_lin_inputs_def.f90
    lib/lidort_def/lidort_lin_io_defs.f90
    lib/lidort_def/lidort_lin_outputs_def.f90
    lib/lidort_def/lidort_lin_sup_brdf_def.f90
    lib/lidort_def/lidort_lin_sup_def.f90
    lib/lidort_def/lidort_lin_sup_sleave_def.f90
    lib/lidort_def/lidort_lin_sup_ss_def.f90
    lib/lidort_def/lidort_outputs_def.f90
    lib/lidort_def/lidort_pars.f90
    lib/lidort_def/lidort_sup_brdf_def.f90
    lib/lidort_def/lidort_sup_def.f90
    lib/lidort_def/lidort_sup_sleave_def.f90
    lib/lidort_def/lidort_sup_ss_def.f90)

set(LIDORT_FO_SOURCES
    lib/lidort_focode/FO_DTWPgeometry_master.f90
    lib/lidort_focode/FO_geometry_Generic.f90
    lib/lidort_focode/FO_Planckfunc.f90
    lib/lidort_focode/FO_ScalarSS_RTCalcs_I.f90
    lib/lidort_focode/FO_ScalarSS_RTCalcs_ILCS.f90
    lib/lidort_focode/FO_ScalarSS_RTCalcs_ILPS.f90
    lib/lidort_focode/FO_ScalarSS_Spherfuncs.f90
    lib/lidort_focode/FO_SSWPgeometry_master.f90
    lib/lidort_focode/FO_Taylor.f90
    lib/lidort_focode/FO_Thermal_RTCalcs_I.f90
    lib/lidort_focode/FO_Thermal_RTCalcs_ILCS.f90
    lib/lidort_focode/FO_Thermal_RTCalcs_ILPS.f90
    lib/lidort_focode/FO_WPgeometry_Routines.f90
    lib/lidort_focode/SFO_LinMasters.f90
    lib/lidort_focode/SFO_Master.f90)

set(LIDORT_LIN_SOURCES
    lib/lidort_main/linearized/lidort_l_inputs.f90
    lib/lidort_main/linearized/lidort_l_thermalsup.f90
    lib/lidort_main/linearized/lidort_l_writemodules.f90
    lib/lidort_main/linearized/lidort_la_miscsetups.f90
    lib/lidort_main/linearized/lidort_lbbf_jacobians.f90
    lib/lidort_main/linearized/lidort_lc_bvproblem.f90
    lib/lidort_main/linearized/lidort_lc_mediaprops.f90
    lib/lidort_main/linearized/lidort_lc_miscsetups.f90
    lib/lidort_main/linearized/lidort_lc_PostProcessing.f90
    lib/lidort_main/linearized/lidort_lc_wfatmos.f90
    lib/lidort_main/linearized/lidort_lcs_converge.f90
    lib/lidort_main/linearized/lidort_lcs_masters_V3p8p3.f90
    lib/lidort_main/linearized/lidort_lp_bvproblem.f90
    lib/lidort_main/linearized/lidort_lp_mediaprops.f90
    lib/lidort_main/linearized/lidort_lp_miscsetups.f90
    lib/lidort_main/linearized/lidort_lp_PostProcessing.f90
    lib/lidort_main/linearized/lidort_lp_wfatmos.f90
    lib/lidort_main/linearized/lidort_lpc_solutions.f90
    lib/lidort_main/linearized/lidort_lps_converge.f90
    lib/lidort_main/linearized/lidort_lps_masters_V3p8p3.f90
    lib/lidort_main/linearized/lidort_ls_wfsleave.f90
    lib/lidort_main/linearized/lidort_ls_wfsurface.f90
    lib/lidort_main/linearized/lidort_sfo_lcs_interface.f90
    lib/lidort_main/linearized/lidort_sfo_lps_interface.f90)

set(LIDORT_REG_SOURCES
    lib/lidort_main/regular/lidort_aux.f90
    lib/lidort_main/regular/lidort_bvproblem.f90
    lib/lidort_main/regular/lidort_converge.f90
    lib/lidort_main/regular/lidort_geometry.f90
    lib/lidort_main/regular/lidort_getplanck.f90
    lib/lidort_main/regular/lidort_inputs.f90
    lib/lidort_main/regular/lidort_intensity.f90
    lib/lidort_main/regular/lidort_masters_V3p8p3.f90
    lib/lidort_main/regular/lidort_mediaprops.f90
    lib/lidort_main/regular/lidort_miscsetups.f90
    lib/lidort_main/regular/lidort_PostProcessing.f90
    lib/lidort_main/regular/lidort_sfo_interface.f90
    lib/lidort_main/regular/lidort_solutions.f90
    lib/lidort_main/regular/lidort_Taylor.f90
    lib/lidort_main/regular/lidort_thermalsup.f90
    lib/lidort_main/regular/lidort_writemodules.f90)

set(LIDORT_SOURCES ${LIDORT_DEF_SOURCES} ${LIDORT_FO_SOURCES}
                   ${LIDORT_LIN_SOURCES} ${LIDORT_REG_SOURCES})

add_library(lidort STATIC ${LIDORT_DEF_SOURCES} ${LIDORT_FO_SOURCES}
                          ${LIDORT_LIN_SOURCES} ${LIDORT_REG_SOURCES})

if(SKBUILD)
  set(fortran_src_file lib/lidort_f2py/lidort.f90)

  list(TRANSFORM fortran_src_file PREPEND ${CMAKE_CURRENT_SOURCE_DIR}/)

  # scikit-build style includes

  find_package(Python REQUIRED COMPONENTS Interpreter Development.Module NumPy)

  # Grab the variables from a local Python installation F2PY headers
  execute_process(
    COMMAND "${Python_EXECUTABLE}" -c
            "import numpy.f2py; print(numpy.f2py.get_include())"
    OUTPUT_VARIABLE F2PY_INCLUDE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE)

  # Prepping the module
  set(f2py_module_name "_core")
  set(f2py_module_c "${f2py_module_name}module.c")

  # Target for enforcing dependencies
  add_custom_target(genpyf DEPENDS "${fortan_src_file}")
  add_custom_command(
    OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/${f2py_module_c}"
    COMMAND ${Python_EXECUTABLE} -m "numpy.f2py" "${fortran_src_file}" -m
            "_core" --lower --f2cmap fortran_mappings.txt # Important
    WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
    DEPENDS "${fortran_src_file}" # Fortran source
  )

  python_add_library(
    _core MODULE WITH_SOABI "${f2py_module_name}module.c"
    "${F2PY_INCLUDE_DIR}/fortranobject.c" "${fortran_src_file}")

  target_link_libraries(_core PRIVATE lidort)

  target_include_directories(_core PUBLIC ${F2PY_INCLUDE_DIR})
  target_link_libraries(_core PUBLIC Python::NumPy)

  add_dependencies(_core genpyf)

  install(TARGETS _core DESTINATION pylidort)
endif()
