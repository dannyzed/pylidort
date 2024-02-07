! #############################################################
! #                                                           #
! #                     LIDORT_3p8p3                          #
! #                                                           #
! #    (LInearized Discrete Ordinate Radiative Transfer)      #
! #     --         -        -        -         -              #
! #                                                           #
! #############################################################

! #############################################################
! #                                                           #
! #  Authors :     Robert  J. D. Spurr (1)                    #
! #                Matthew J. Christi                         #
! #                                                           #
! #  Address (1) : RT Solutions, Inc.                         #
! #                9 Channing Street                          #
! #                Cambridge, MA 02138, USA                   #
! #                                                           #
! #  Tel:          (617) 492 1183                             #
! #  Email :       rtsolutions@verizon.net                    #
! #                                                           #
! #  This Version :   LIDORT_3p8p3                            #
! #  Release Date :   31 March 2021                           #
! #                                                           #
! #  Previous LIDORT Versions under Standard GPL 3.0:         #
! #  ------------------------------------------------         #
! #                                                           #
! #      3.7   F90, released        June  2014                #
! #      3.8   F90, released        March 2017                #
! #      3.8.1 F90, released        June  2019                #
! #      3.8.2 F90, limited release May   2020                #
! #                                                           #
! #  Features Summary of Recent LIDORT Versions               #
! #  ------------------------------------------               #
! #                                                           #
! #      NEW: THERMAL SUPPLEMENT INCLUDED    (3.2)            #
! #      NEW: OUTGOING SPHERICITY CORRECTION (3.2)            #
! #      NEW: TOTAL COLUMN JACOBIANS         (3.3)            #
! #      VLIDORT COMPATIBILITY               (3.4)            #
! #      THREADED/OPTIMIZED F90 code         (3.5)            #
! #      EXTERNAL SS / NEW I/O STRUCTURES    (3.6)            #
! #                                                           #
! #      Surface-leaving, BRDF Albedo-scaling     (3.7)       #
! #      Taylor series, BBF Jacobians, ThreadSafe (3.7)       #
! #      New Water-Leaving Treatment              (3.8)       #
! #      BRDF-Telescoping, enabled                (3.8)       #
! #      Several Performance Enhancements         (3.8)       #
! #      Water-leaving coupled code               (3.8.1)     #
! #      Planetary problem, media properties      (3.8.1)     #
! #      Doublet geometry post-processing         (3.8.2)     #
! #      Reduction zeroing, dynamic memory        (3.8.2)     #
! #                                                           #
! #  Features Summary of This VLIDORT Version                 #
! #  ----------------------------------------                 #
! #                                                           #
! #  3.8.3, released 31 March 2021.                           #
! #    ==> Sphericity Corrections using MS source terms       #
! #    ==> BRDF upgrades, including new snow reflectance      #
! #    ==> SLEAVE Upgrades, extended water-leaving treatment  #
! #                                                           #
! #############################################################

! ###################################################################
! #                                                                 #
! # This is Version 3.8.3 of the LIDORT software library.           #
! # This library comes with the Standard GNU General Public License,#
! # Version 3.0, 29 June 2007. Please read this license carefully.  #
! #                                                                 #
! #      LIDORT Copyright (c) 1999-2021.                            #
! #          Robert Spurr, RT Solutions, Inc.                       #
! #          9 Channing Street, Cambridge, MA 02138, USA.           #
! #                                                                 #
! #                                                                 #
! # This file is part of LIDORT_3p8p3 ( Version 3.8.3. )            #
! #                                                                 #
! # LIDORT_3p8p3 is free software: you can redistribute it          #
! # and/or modify it under the terms of the Standard GNU GPL        #
! # (General Public License) as published by the Free Software      #
! # Foundation, either version 3.0 of this License, or any          #
! # later version.                                                  #
! #                                                                 #
! # LIDORT_3p8p3 is distributed in the hope that it will be         #
! # useful, but WITHOUT ANY WARRANTY; without even the implied      #
! # warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR         #
! # PURPOSE. See the Standard GNU General Public License (GPL)      #
! # for more details.                                               #
! #                                                                 #
! # You should have received a copy of the Standard GNU General     #
! # Public License (GPL) Version 3.0, along with the LIDORT_3p8p3   #
! # code package. If not, see <http://www.gnu.org/licenses/>.       #
! #                                                                 #
! ###################################################################

      MODULE LIDORT_Lin_Sup_SS_def_m

!  Version 3.7, Internal threading removed, 02 May 2014
!  Version 3.8.1, Upgrade June 2019

!  This module contains the following structures,
!  with intents :

!  2/28/21. Version 3.8.3. No Changes.

!     LIDORT_LinSup_SS_Atmos    nested in LIDORT_LinSup_SS_InOut
!      LIDORT_LinSup_SS_Surf    nested in LIDORT_LinSup_SS_InOut
!     LIDORT_LinSup_SS_InOut    Intent(InOut)

      USE LIDORT_PARS_m, only : fpk, MAX_ATMOSWFS, MAX_USER_LEVELS, &
                                MAX_GEOMETRIES, MAX_DIRECTIONS, &
                                MAXLAYERS, MAX_SURFACEWFS

      IMPLICIT NONE

! #####################################################################
! #####################################################################

      TYPE LIDORT_LinSup_SS_Atmos

!  SS atmospheric column weighting functions

      REAL(fpk), dimension ( MAX_ATMOSWFS, MAX_USER_LEVELS, &
        MAX_GEOMETRIES, MAX_DIRECTIONS ) :: TS_COLUMNWF_SS

!  DB atmospheric column weighting functions

      REAL(fpk), dimension ( MAX_ATMOSWFS, MAX_USER_LEVELS, &
        MAX_GEOMETRIES ) :: TS_COLUMNWF_DB

!  SS atmospheric profile weighting functions

      REAL(fpk), dimension ( MAX_ATMOSWFS, MAXLAYERS, MAX_USER_LEVELS, &
        MAX_GEOMETRIES, MAX_DIRECTIONS ) :: TS_PROFILEWF_SS

!  DB atmospheric profile weighting functions

      REAL(fpk), dimension ( MAX_ATMOSWFS, MAXLAYERS, MAX_USER_LEVELS, &
        MAX_GEOMETRIES ) :: TS_PROFILEWF_DB

      END TYPE LIDORT_LinSup_SS_Atmos

! #####################################################################
! #####################################################################

      TYPE LIDORT_LinSup_SS_Surf

!  SS surface weighting functions

!      REAL(fpk), dimension ( MAX_SURFACEWFS, MAX_USER_LEVELS, &
!        MAX_GEOMETRIES, MAX_DIRECTIONS ) :: TS_SURFACEWF_SS

!  DB surface weighting functions

      REAL(fpk), dimension ( MAX_SURFACEWFS, MAX_USER_LEVELS, &
        MAX_GEOMETRIES ) :: TS_SURFACEWF_DB

      END TYPE LIDORT_LinSup_SS_Surf

! #####################################################################
! #####################################################################

      TYPE LIDORT_LinSup_SS

      TYPE(LIDORT_LinSup_SS_Atmos) :: Atmos
      TYPE(LIDORT_LinSup_SS_Surf)  :: Surf

      END TYPE LIDORT_LinSup_SS

! #####################################################################
! #####################################################################

!  EVERYTHING PUBLIC HERE

      PRIVATE
      PUBLIC :: LIDORT_LinSup_SS_Atmos,&
                LIDORT_LinSup_SS_Surf,&
                LIDORT_LinSup_SS

      END MODULE LIDORT_Lin_Sup_SS_def_m
