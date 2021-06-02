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

class pdu_print_ascii(gr.sync_block):
    """
    docstring for block pdu_print_ascii
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="pdu_print_ascii",
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern("msg_in"))
        self.set_msg_handler(pmt.intern("msg_in"), self.handle_msg)

    def handle_msg(self, msg):
        meta = pmt.to_python(msg)
        for j in range(0,len(meta[1][:]),8):
            byte = meta[1][j:j+8]
            byte = ''.join(str(i) for i in byte) 
            if byte == "11100100" or byte == "00000000":
                pass
            else:
                byte = byte[-1:]+byte[0:-1]
                print(chr(int(byte,2)))

    def work(self, input_items, output_items):
        pass

