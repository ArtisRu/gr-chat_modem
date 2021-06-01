#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: char2ascii_pdu_add_syncw_example
# Author: artis
# GNU Radio version: v3.8.2.0-113-g729d5a98

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import chat_modem

from gnuradio import qtgui

class char2ascii_pdu_add_syncw_example(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "char2ascii_pdu_add_syncw_example")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("char2ascii_pdu_add_syncw_example")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "char2ascii_pdu_add_syncw_example")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.qpsk_const = qpsk_const = digital.constellation_qpsk().base()

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_edit_box_msg_0 = qtgui.edit_box_msg(qtgui.STRING, 'a', '', False, False, '')
        self._qtgui_edit_box_msg_0_win = sip.wrapinstance(self.qtgui_edit_box_msg_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_edit_box_msg_0_win)
        self.chat_modem_pdu_char_to_ascii_0 = chat_modem.pdu_char_to_ascii(16)
        self.chat_modem_pdu_add_sync_word_0 = chat_modem.pdu_add_sync_word(114)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern(chr(170)), 10)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/artis/Downloads/pdu_char2ascii_add_sync.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.chat_modem_pdu_char_to_ascii_0, 'msg_in'))
        self.msg_connect((self.chat_modem_pdu_add_sync_word_0, 'msg_out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.chat_modem_pdu_char_to_ascii_0, 'msg_out'), (self.chat_modem_pdu_add_sync_word_0, 'msg_in'))
        self.msg_connect((self.qtgui_edit_box_msg_0, 'msg'), (self.chat_modem_pdu_char_to_ascii_0, 'msg_in'))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_file_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "char2ascii_pdu_add_syncw_example")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_qpsk_const(self):
        return self.qpsk_const

    def set_qpsk_const(self, qpsk_const):
        self.qpsk_const = qpsk_const





def main(top_block_cls=char2ascii_pdu_add_syncw_example, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
