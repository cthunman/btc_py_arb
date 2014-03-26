btc_py_arb
==========

Simple program in python for doing trivial arb searches between bitfinex, btcsx, and btce

It doesn't take into account any fees or anything, but it's kind of interesting if you hook it up to a cron.  I haven't figured out if anything it finds is significant enough to act on yet.

I'm hoping to make this into something quite a bit more robust at some point... doing a graph search that takes into account fees and transfer costs. 

*/5 * * * * python /path/to/project/arb.py >> /path/to/project/arblog
