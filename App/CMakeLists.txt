cmake_minimum_required(VERSION 2.8.11)
project(EuRoC_test)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/../bin)

# =========================
# run front-end + back-end with EuRoC dataset
# =========================
add_executable(ice_ba_euroc
    ../App/EuRoC_test.cpp
)
target_link_libraries(ice_ba_euroc
    IBA
    OF
)
if (CVD_FOUND)
 target_link_libraries(ice_ba_euroc
     IBAVis
)
endif(CVD_FOUND)


# =========================
# run front-end + back-end with FPV dataset
# =========================
add_executable(ice_ba_fpv
    ../App/FPV_test.cpp
)
target_link_libraries(ice_ba_fpv
    IBA
    OF
)
if (CVD_FOUND)
 target_link_libraries(ice_ba_fpv
     IBAVis
)
endif(CVD_FOUND)


# =========================
# run back-end only with .dat file
# =========================
add_executable(back_end
    ../App/run_backend.cpp
)
target_include_directories(back_end PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${GLOBAL_IBA_INCLUDE_DIRS}
    ${EIGEN_INCLUDE_DIR}
)
target_link_libraries(back_end
    IBA
    OF
)
if (CVD_FOUND)
 target_include_directories(back_end PUBLIC
     ${GLOBAL_VISUALIZATION_INCLUDE_DIR}
 )
 target_link_libraries(back_end
     IBAVis
 )
endif (CVD_FOUND)
