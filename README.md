## Description
Some OOT modules combined with pre installed gr3.8 blocks to create real-time chat application between 2 SDR's. Tested with Adalm Pluto and HackRF One. Code for OOT modules is written in python. Some examples are included in /examples folder.

System responsiveness is limited by gnuradio's pmt interface. Need to rewrite blocks so that they use regular streaming interface.

## Installation
Blocks are written for GNU Radio v3.8.2 (compiled from gnuradio's source maint-3.8
branch). This will NOT work with gnuradio 3.8.1.0 (default ubuntu 20.04 apt install version) because of bug).

```
 git clone https://github.com/ArtisRu/gr-chat_modem
 cd gr-chat_modem
 mkdir build
 cd build
 cmake ../
 make
 sudo make install
 sudo ldconfig
```
Some examples are included in /examples folder. In examples I use 7bit Barker code for packet sync and GMSK modulation. Main applications are SDR_tx.grc and SDR_rx.grc. Sometimes SDR_rx will not sync properly and output random chars, if that's the case both sdr_tx and sdr_rx should be restarted.

![Example](/docs/example.png)

