# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
import os


session.View(name='User-1', nearPlane=6495.7, farPlane=7130.6, width=1959, 
height=1192.5, projection=PARALLEL, cameraPosition=(103.49, 64.69, 
6801.5), cameraUpVector=(-1, 0, 0), cameraTarget=(103.49, 64.69, 
0.010254), viewOffsetX=0, viewOffsetY=0, autoFit=OFF)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])

session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)

session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
visibleEdges=FEATURE)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
spectrum='Black to white')


session.viewports['Viewport: 1'].lightOptions.lights[0].setValues(enabled=False)
session.viewports['Viewport: 1'].lightOptions.lights[1].setValues( enabled=False)
session.viewports['Viewport: 1'].lightOptions.lights[2].setValues(enabled=False)
session.viewports['Viewport: 1'].lightOptions.setValues(materialShininess=125)
session.viewports['Viewport: 1'].lightOptions.setValues(materialShininess=125)
session.viewports['Viewport: 1'].lightOptions.setValues(materialShininess=128)
session.viewports['Viewport: 1'].lightOptions.setValues(materialShininess=128)
session.viewports['Viewport: 1'].lightOptions.setValues(ambientColor='White')
session.viewports['Viewport: 1'].lightOptions.setValues(ambientColor='White')


session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Material']
cmap.updateOverrides(overrides={'SM490':(True, '#CCCCCC', 'Default', 
'#CCCCCC'), 'SS400':(True, '#FFFFFF', 'Default', '#FFFFFF')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Material']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()





max=0.6;
scale1=100

fn=5;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/ac04.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/ac04e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=5;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/ac08.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/ac08e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=19;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/as04.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/as04e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=19;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/as08.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/as08e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


fn=19;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/bs04.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/bs04e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=19;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/bs08.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/bs08e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


fn=19;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/cs04.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/cs04e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=19;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/cs08.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/cs08e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


fn=19;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/ds04.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/ds04e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=19;
path='F:/研究室関係/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/ds08.odb';
odb = session.odbs[path]
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
step='Step-2', frame=fn)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
deformationScaling=UNIFORM, uniformScaleFactor=scale1)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
maxAutoCompute=OFF, maxValue=max, minAutoCompute=OFF, minValue=-1*max)
session.pngOptions.setValues(imageSize=(4096, 1837))
session.printToFile(fileName='F:/研究室関係/Dropbox (SSLUoT)/スクリーンショット/ds08e.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))






