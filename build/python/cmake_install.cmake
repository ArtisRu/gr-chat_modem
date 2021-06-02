# Install script for directory: /home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/chat_modem" TYPE FILE FILES
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/python/__init__.py"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/python/pdu_add_sync_word.py"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/python/pdu_char_to_ascii.py"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/python/pdu_frame_format.py"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/python/pdu_correlate.py"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/python/pdu_print_ascii.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/chat_modem" TYPE FILE FILES
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/__init__.pyc"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_add_sync_word.pyc"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_char_to_ascii.pyc"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_frame_format.pyc"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_correlate.pyc"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_print_ascii.pyc"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/__init__.pyo"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_add_sync_word.pyo"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_char_to_ascii.pyo"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_frame_format.pyo"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_correlate.pyo"
    "/home/artis/Documents/gnuradio_crap/OOT/gr-chat_modem/build/python/pdu_print_ascii.pyo"
    )
endif()

