INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_CHAT_MODEM chat_modem)

FIND_PATH(
    CHAT_MODEM_INCLUDE_DIRS
    NAMES chat_modem/api.h
    HINTS $ENV{CHAT_MODEM_DIR}/include
        ${PC_CHAT_MODEM_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    CHAT_MODEM_LIBRARIES
    NAMES gnuradio-chat_modem
    HINTS $ENV{CHAT_MODEM_DIR}/lib
        ${PC_CHAT_MODEM_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/chat_modemTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(CHAT_MODEM DEFAULT_MSG CHAT_MODEM_LIBRARIES CHAT_MODEM_INCLUDE_DIRS)
MARK_AS_ADVANCED(CHAT_MODEM_LIBRARIES CHAT_MODEM_INCLUDE_DIRS)
