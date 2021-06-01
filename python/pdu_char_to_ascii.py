#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 artis r.
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
from gnuradio import gr
import pmt

class pdu_char_to_ascii(gr.sync_block):
    """
    docstring for block pdu_char_to_ascii
    """
    # TO-DO
    # 1) add warning if input str is too long, print only on first handle_msg call
    def __init__(self, packet_len):
        gr.sync_block.__init__(self,
            name="pdu_char_to_ascii",
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern("msg_in"))
        self.message_port_register_out(pmt.intern("msg_out"))
        self.set_msg_handler(pmt.intern("msg_in"), self.handle_msg)
        self.packet_len = packet_len
        #self.first_send = first_send

    def handle_msg(self, msg):
        meta = pmt.to_python(msg)
        data = []
        input_data_bit_count = 0

        for i in range(len(meta)):
            data.append(ord(meta[i]))
        #if (len(data) > self.packet_len/8):
        #    print("WARNING: pdu_char_to_ascii")
        #    print("Lengt of input string should NOT be higher than packet_len, read doc!")
        # Add 0b0's so that output PDU is of length self.packet_len
        data = data + [0]*(int(self.packet_len/8) - len(data))
        #print("data", data)
        send_pmt = pmt.make_u8vector(len(data), ord(' '))
        for j in range(len(data)):
            pmt.u8vector_set(send_pmt, j, data[j])
        self.message_port_pub(pmt.intern("msg_out"), pmt.cons(pmt.PMT_NIL, send_pmt))
        
        #self.message_port_pub(pmt.intern("msg_out"), pmt.to_pmt(data))
    def work(self, input_items, output_items):
        pass

