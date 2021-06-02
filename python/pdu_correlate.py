#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 gr-chat_modem author.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy as np
import pmt
from gnuradio import gr

class pdu_correlate(gr.sync_block):
    """
    docstring for block pdu_correlate
    """
    def __init__(self, sync_word, print_corr):
        gr.sync_block.__init__(self,
            name="pdu_correlate",
            in_sig=[],
            out_sig=[])
        self.print_corr = print_corr
        self.sync_word = bin(sync_word)[2:]
        self.sync_word_bits = []
        for i in range(len(bin(sync_word)[2:])):
            self.sync_word_bits.append(np.uint8(bin(sync_word)[2:][i]))
        self.message_port_register_in(pmt.intern("msg_in"))
        self.message_port_register_out(pmt.intern("msg_out"))
        self.set_msg_handler(pmt.intern("msg_in"), self.handle_msg)

    def handle_msg(self, msg):
        meta = pmt.to_python(msg)
        data = []
        for j in range(len(meta[1][:])):
            data.append(meta[1][j])
        #print(data)
        corr = np.correlate(data, self.sync_word_bits, mode = "valid")
        max_index = np.where(corr == np.amax(corr))[0][0]
        if self.print_corr == 1:
            print("data:", data)
            print("correlation with sync_word:", corr)
            print("index of correlation maxima:", max_index)
        
        #data = data[max_index+len(self.sync_word_bits):]
        data = data[max_index:] + data[:max_index]
        send_pmt = pmt.make_u8vector(len(data), ord(' '))
        for k in range(len(data)):
            pmt.u8vector_set(send_pmt, k, ord(chr(data[k])))
        self.message_port_pub(pmt.intern("msg_out"), pmt.cons(pmt.PMT_NIL, send_pmt))

    def work(self, input_items, output_items):
        pass

