#!/usr/bin/env python3
# Copyright (c) 2019 The NavCoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

#
# Expanded helper routines for regression testing of the NAV Coin community fund
#

from test_framework.util import *

def whenISupportAnswers(node=None, hash=None, answers=None):

  if node is None or hash is None:
    assert(False)

  blocksPerCycle = node.cfundstats()["consensus"]["blocksPerVotingCycle"]  
  assert(isinstance(blocksPerCycle, int) and blocksPerCycle > 0)

  print(node.getblockcount)

  node.support(hash)
  slow_gen(node, blocksPerCycle)

  print(node.getblockcount)

  consult = node.getconsultation(hash)

  print(consult)
