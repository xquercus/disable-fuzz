# Copyright (C) 2018 Jeff Stevens
# This software is licensed under the GNU GPL v3 https://www.gnu.org/licenses/gpl-3.0.html

# See README for more information
# MINIMUM_INTERVAL = -1 : Disables fuzz entirely.  This is the default.
# MINIMUM_INTERVAL = [non_negative_integer] : Fuzz only intervals greater than or equal to `non_negative_integer`.
MINIMUM_INTERVAL = -1
LOG_LEVEL = 0

import sys
import anki
from anki import version
from anki.sched import Scheduler


def log_info(message):
    if LOG_LEVEL >= 1:
        sys.stdout.write(message)


def new_fuzzIvlRange(self, ivl):
    if MINIMUM_INTERVAL < 0:
        log_info("fuzz=no    ivl {0:<5} <  MINIMUM_INTERVAL {1:<5}\n".format(ivl, MINIMUM_INTERVAL))
        return [ivl,ivl]
    elif ivl < MINIMUM_INTERVAL:
        log_info("fuzz=no    ivl {0:<5} <  MINIMUM_INTERVAL {1:<5}\n".format(ivl, MINIMUM_INTERVAL))
        return [ivl, ivl]
    else:
        log_info("fuzz=yes   ivl {0:<5} >= MINIMUM_INTERVAL {1:<5}\n".format(ivl, MINIMUM_INTERVAL))
        return orig_fuzzIvlRange(self, ivl)


def new_v2_fuzzIvlRange(self, ivl):
    if MINIMUM_INTERVAL < 0:
        log_info("fuzz=no    ivl {0:<5} <  MINIMUM_INTERVAL {1:<5}\n".format(ivl, MINIMUM_INTERVAL))
        return [ivl,ivl]
    elif ivl < MINIMUM_INTERVAL:
        log_info("fuzz=no    ivl {0:<5} <  MINIMUM_INTERVAL {1:<5}\n".format(ivl, MINIMUM_INTERVAL))
        return [ivl, ivl]
    else:
        log_info("fuzz=yes   ivl {0:<5} >= MINIMUM_INTERVAL {1:<5}\n".format(ivl, MINIMUM_INTERVAL))
        return orig_v2_fuzzIvlRange(self, ivl)


# Patch Anki 2.0 and Anki 2.1 default scheduler
orig_fuzzIvlRange = anki.sched.Scheduler._fuzzIvlRange
anki.sched.Scheduler._fuzzIvlRange = new_fuzzIvlRange

# Patch Anki 2.1 experimental v2 scheduler
if version.startswith("2.1"):
    from anki.schedv2 import Scheduler
    orig_v2_fuzzIvlRange = anki.schedv2.Scheduler._fuzzIvlRange
    anki.schedv2.Scheduler._fuzzIvlRange = new_v2_fuzzIvlRange

