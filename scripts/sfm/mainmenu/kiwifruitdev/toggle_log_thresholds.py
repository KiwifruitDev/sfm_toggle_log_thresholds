# SFM Toggle Log Thresholds Script by KiwifruitDev
# https://github.com/KiwifruitDev/sfm_toggle_log_thresholds
# This software is licensed under the MIT License.
# MIT License
# 
# Copyright (c) 2025 KiwifruitDev
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sfm
import vs
from PySide import QtGui

def toggle_log_thresholds():
    # Detecting if we already ran this script
    disabled = vs.movieobjects.CDmeVector3Log.GetValueThreshold() == 0

    # These are the default thresholds
    threshold_vector3 = 0.01
    threshold_qangle = 0.001
    threshold_quaternion = 0.001

    # Set to 0 to disable
    if not disabled:
        threshold_vector3 = 0
        threshold_qangle = 0
        threshold_quaternion = 0
        disabled = True
    else:
        disabled = False

    # Only these elements seem to be affected by the log threshold
    vs.movieobjects.CDmeVector3Log.SetValueThreshold(threshold_vector3)
    vs.movieobjects.CDmeQAngleLog.SetValueThreshold(threshold_qangle)
    vs.movieobjects.CDmeQuaternionLog.SetValueThreshold(threshold_quaternion)

    # Create a pop-up message box to inform the user what happened
    message = "Log thresholds are now " + ("disabled" if disabled else "enabled") + "."
    msgBox = QtGui.QMessageBox()
    msgBox.setWindowTitle("Toggle Log Thresholds")
    msgBox.setText(message)
    msgBox.exec_()

    # Print the same message to the console
    sfm.Msg(message + "\n")

# Run the function and that'll be it!
toggle_log_thresholds()
