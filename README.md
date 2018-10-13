# Disable Fuzz

**This is alpha code.  Do not use.** *Disable Fuzz* is an add-on that disables the random "fuzz" applied by the Anki [spaced repetition algorithm](https://apps.ankiweb.net/docs/manual.html#what-spaced-repetition-algorithm-does-anki-use). Alternatively, it can be configured to fuzz only intervals greater than or equal to a user specified value. It is compatible with:
* Anki v2.0
* Anki v2.1 with the default scheduler
* Anki v2.1 with the [experimental v2 scheduler](https://anki.tenderapp.com/kb/anki-ecosystem/experiment-scheduling-changes-in-anki-21)

## Installation

To install follow the instructions...

## Configuration

Configuration is via setting `MINIMUM_INTERVAL`.  The following options are available:

* `MINIMUM_INTERVAL = -1` : Disables fuzz entirely.  This is the default.
* `MINIMUM_INTERVAL = [non_negative_integer]` : Fuzz only intervals greater than or equal to `non_negative_integer`. For example `MINIMUM_INTERVAL = 30` will fuzz intervals of 30 or larger.  Intervals of less than 30 will not be fuzzed.

## Load Balanced Scheduler Compatibility

*Load Balanced Scheduler* will not perform load balancing for intervals which are not fuzzed.

## Bugs and Support

If you encounter a bug or need support please see the official [README](https://github.com/xquercus/disable-fuzz). Please report bugs through [github](https://github.com/xquercus/disable-fuzz/issues).  Please don't use the review section of the AnkiWeb add-on page for support as I won't receive a notification and there is no way for me to respond.

## Revision History

* Version 1.0.0 -- ....
  * ...