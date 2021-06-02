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
from gnuradio import gr
import pmt

class pdu_frame_format(gr.sync_block):
    """
    docstring for block pdu_frame_format
    """
    def __init__(self, packet_len, sync_word, repeat):
        gr.sync_block.__init__(self,
            name="pdu_frame_format",
            in_sig=[],
            out_sig=[])
        flag = 0
        self.flag = flag
        self.packet_len = packet_len
        self.sync_word = sync_word
        self.repeat = repeat
        self.message_port_register_in(pmt.intern("msg_in"))
        self.message_port_register_in(pmt.intern("en"))
        self.message_port_register_out(pmt.intern("msg_out"))
        self.set_msg_handler(pmt.intern("msg_in"), self.handle_msg)
        self.set_msg_handler(pmt.intern("en"), self.handle_msg_en)       

    def handle_msg(self, msg):
        self.flag = 1
        meta = pmt.to_python(msg)
        data = []
        for j in range(len(meta[1][:])):
            data.append(meta[1][j])
        data = data + [0]*(int(self.packet_len/8) - len(data) - (len(bin(self.sync_word)[2:]) + 7) // 8*8 )
        data.append(self.sync_word)
        send_pmt = pmt.make_u8vector(len(data), ord(' '))
        for j in range(len(data)):
            pmt.u8vector_set(send_pmt, j, ord(chr(data[j])))
        for k in range(self.repeat):
            self.message_port_pub(pmt.intern("msg_out"), pmt.cons(pmt.PMT_NIL, send_pmt))
        self.flag = 0

    def handle_msg_en(self, msg):
        if self.flag == 0:
            data = [0]*int(self.packet_len/8 - 1)
            data.append(self.sync_word)
            send_pmt = pmt.make_u8vector(len(data), ord(' '))
            for j in range(len(data)):
                pmt.u8vector_set(send_pmt, j, data[j])
            self.message_port_pub(pmt.intern("msg_out"), pmt.cons(pmt.PMT_NIL, send_pmt)) 

    def work(self, input_items, output_items):
        pass