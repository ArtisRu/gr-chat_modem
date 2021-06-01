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

class pdu_add_sync_word(gr.sync_block):
    """
    docstring for block pdu_add_sync_word
    """

    def __init__(self, sync_word):
        gr.sync_block.__init__(self,
            name="pdu_add_sync_word",
            in_sig=[],
            out_sig=[])
        #self.sync_word = self.int2bit_array(sync_word)
        self.sync_word = sync_word
        self.message_port_register_in(pmt.intern("msg_in"))
        self.message_port_register_out(pmt.intern("msg_out"))
        self.set_msg_handler(pmt.intern("msg_in"), self.handle_msg)

    def handle_msg(self, msg):
        meta = pmt.to_python(msg)
        data = []
        for j in range(len(meta[1][:])):
            data.append(meta[1][j])
        data.append(self.sync_word)
        send_pmt = pmt.make_u8vector(len(data), ord(' '))
        for i in range(len(data)):
            pmt.u8vector_set(send_pmt, i, ord(chr(data[i])))
        self.message_port_pub(pmt.intern("msg_out"), pmt.cons(pmt.PMT_NIL, send_pmt))                   

    def work(self, input_items, output_items):
        pass

