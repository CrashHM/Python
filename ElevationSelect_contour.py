#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:07:32 2020

@author: beowulf
"""

#This script was intended to be run by the Calculate Field tool in ArcPro. It was intended to improve the completeness of the column containing elAct.

# It was designed to validate and select the most appropriate value from the 3 inputs (elAct, elUP, elDown). elAct is the field being updated.

#elUP and elDOWN are data stored else where, which may or may not be more current.

 

 

 

def invertL(elAct,elActD,elUP,elDOWN,elPipeD):###contour values must be assessed against OakLocal datum

    def contourCK(elVal,maxInvert,contour):

        if elVal >= contour:

            return 0

    elif elVal < contour:

        depthInvert = contour - elVal# this line may be problematic if maxInvert is set to less than 30

        if depthInvert > maxInvert:

            return 0

        else:

            return elVal

                #converts date to 8 digit integer for comparison       

    def dateStripper(date):

        dateStr = str(date)

        dateStr = dateStr[:8]

        dateInt = int(dateStr)

        return dateInt

#########

def invertL(elAct,elUP,elDOWN):# elAct(invert el) is from structures, elUP(upstream el) and elDOWN(downstream el) are from collection system   

    if not( elAct == 0):#if structures cell has a value leave it alone

        return elAct

    elif ((elUP >= elDOWN) and not(elDOWN == 0)):#if the upstream value is greater than downstream value and downstream has a value set cell to downstream

        return elDOWN

    elif ((elUP <= elDOWN) and not(elUP == 0)):#if downstream value is less than upstream value and upstream has a value set cell to upstream

        return elUP

    elif elDOWN == 0:# if downstream is zero set cell to upstream

        return elUP

    elif elUP ==0:# if upstream is zero set set cell to downstream

        return elDOWN

    else:#if somehow nothing above executes don't change cell value

        return elAct

########       

                #Selects most current edit.

    def mostCurrent(elActD,elPipeD,elAct,elPipe):

        if elActD > elPipeD:

            return elAct

        elif elActD < elPipeD:

            return elPipe

        else:

            return elAct

 

    maxInvert = 30

                # this number is the maximum depth of any know structure in the system. This is used to discard unreasonable values in contourCK()

    #using a value less than 30 may create issues with depths below sea level

   

               

                contour = contour-5.7

                #Correction from NAVD88 to Oakland datum

   

                #This is the main body of the function. It executes the above functions.

    elAct = contourCK(elAct,maxInvert,contour)

    elUP = contourCK(elUP,maxInvert,contour)

    elDOWN = contourCK(elDOWN,maxInvert,contour)
    elActD = dateStripper(elActD)
    elPipeD = dateStripper(elPipeD)
    elPipe = pipeLogic(elUp,elDOWN)

   

    # following IF block has assumed hierarchy. elAct>elUP>elDown. If a non zero value is present it will favor that value for the moment and move on.

   

                if elAct == 0 or elAct == None:#if elAct is 0 or null it is assumed that a value has no been inserted

        if not (elPipe ==0):#checks that elUP does not = 0

            elAct = elPipe

    else:

        elAct = mostCurrent(elActD,elPipeD,elAct,elPipe)

    return elAct

               

 

 