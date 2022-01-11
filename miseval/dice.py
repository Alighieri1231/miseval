#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2022 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# External modules
import numpy as np
# Internal modules
from miseval.confusion_matrix import calc_ConfusionMatrix

#-----------------------------------------------------#
#         Calculate : Dice Similarity Matrix          #
#-----------------------------------------------------#
def calc_DSC(truth, pred, c=1):
    try:
        # Obtain sets with associated class
        gt = np.equal(truth, c)
        pd = np.equal(pred, c)
        # Calculate Dice
        dice = 2*np.logical_and(pd, gt).sum() / (pd.sum() + gt.sum())
    except ZeroDivisionError:
        dice = 0.0
    # Return computed Dice
    return dice

#-----------------------------------------------------#
#              Calculate : DSC Variant #2             #
#-----------------------------------------------------#
def calc_DSC_v2(truth, pred, c=1):
    try:
        # Obtain confusion mat
        tp, tn, fp, fn = calc_ConfusionMatrix(truth, pred, c)
        # Calculate Dice
        dice = 2*tp / (2*tp + fp + fn)
    except ZeroDivisionError:
        dice = 0.0
    # Return computed Dice
    return dice