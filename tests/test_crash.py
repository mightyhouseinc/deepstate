from __future__ import print_function
import deepstate_base
import logrun


class CrashTest(deepstate_base.DeepStateTestCase):
  def run_deepstate(self, deepstate):
    (r, output) = logrun.logrun([deepstate, "build/examples/Crash"],
                  "deepstate.out", 1800)
    self.assertEqual(r, 0)

    self.assertTrue("Passed: Crash_SegFault" in output)
    foundCrashSave = any(("Saved test case" in line) and (".crash" in line)
                         for line in output.split("\n"))
    self.assertTrue(foundCrashSave)

