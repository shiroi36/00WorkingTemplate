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




max=3;
scale1=20

fn=20;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/ac04.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/ac04p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=20;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/ac08.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/ac08p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


fn=33;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/as04.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/as04p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=33;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/as08.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/as08p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=33;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/bs04.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/bs04p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=33;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/bs08.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/bs08p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


fn=33;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/cs04.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/cs04p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=33;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/cs08.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/cs08p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))



fn=33;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/ds04.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/ds04p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

fn=33;
path='F:/�������֌W/Dropbox (SSLUoT)/abaqus/00_jsce16/ver3/final/ds08.odb';
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
session.printToFile(fileName='F:/�������֌W/Dropbox (SSLUoT)/�X�N���[���V���b�g/ds08p.png', 
format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
