#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer1.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer1.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer2.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer2.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer3.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer3.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer4.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer4.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer5.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer5.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer6.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer6.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer7.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer7.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer8.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer8.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer9.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer9.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer10.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer10.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer11.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer11.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer12.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer12.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer13.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer13.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer14.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer14.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer15.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer15.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer16.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer16.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer17.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer17.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer18.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer18.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer19.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer19.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer20.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer20.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer21.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer21.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer22.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer22.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer23.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer23.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer24.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer24.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer25.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer25.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer26.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer26.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer27.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer27.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer28.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer28.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer29.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer29.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer30.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer30.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer31.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer31.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer32.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer32.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer33.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer33.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer34.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer34.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer35.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer35.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer36.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer36.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer37.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer37.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer38.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer38.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer39.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer39.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer40.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer40.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer41.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer41.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer42.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer42.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer43.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer43.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer44.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer44.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer45.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer45.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer46.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer46.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer47.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer47.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer48.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer48.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer49.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer49.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)


#
# This scripts is the IronPython counterpart of the create_dfs2 Matlab script

import clr
from math import *
import array

clr.AddReference("DHI.Generic.MikeZero.DFS");
clr.AddReference("DHI.Generic.MikeZero.EUM");
clr.AddReference("System");
import System
from System import Array
from DHI.Generic.MikeZero import eumUnit, eumItem, eumQuantity
from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *

# create relative grid coordinates and create a 2D coordinate set using meshgrid
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)

# Creates a new dfs2 file.
filename = 'layer50.dfs2';

# Create an empty dfs2 file object
factory = DfsFactory();
builder = Dfs2Builder.Create('Matlab dfs2 file','Matlab DFS',0);

# Set up the header
builder.SetDataType(0);
builder.SetGeographicalProjection(factory.CreateProjectionGeoOrigin('NON-UTM', 286981, 4250114, 30));# geological information
builder.SetTemporalAxis(factory.CreateTemporalEqCalendarAxis(eumUnit.eumUsec,System.DateTime(1993,12,02,0,0,0),0,86400));
builder.SetSpatialAxis(factory.CreateAxisEqD2(eumUnit.eumUmeter,103,0,1000,213,0,1000)); #unclear
builder.DeleteValueFloat = -1e-30;

# Add custom block 
# M21_Misc : {orientation (should match projection), drying depth, -900=has projection, land value, 0, 0, 0}
cbdata = Array.CreateInstance(System.Single, 7)
cbdata[0] = 327
cbdata[1] = 0.2
cbdata[2] = -900
cbdata[3] = 10
cbdata[4] = 0
cbdata[5] = 0
cbdata[6] = 0
builder.AddCustomBlock(factory.CreateCustomBlock('M21_Misc', cbdata));

builder.AddDynamicItem('tprogs1', eumQuantity.Create(eumItem.eumIWaterLevel, eumUnit.eumUmeter), DfsSimpleType.Float, DataValueType.Instantaneous);

# Create the file ready for data
builder.CreateFile(filename);

a1 = []
with open('layer50.txt') as f:
    for line in f:
        data = line.split()
        a1.append(int(data[0]))
print(a1)


# Add one static item, containing bathymetry data
data = Array.CreateInstance(System.Single, xysize)
xyi = 0
for y in yv:
  for x in xv:
    data[xyi] = a1[xyi]
    xyi = xyi+1
builder.AddStaticItem('Static item', eumQuantity.UnDefined, data);

dfs = builder.GetFile();

# create coordinates
xv = array.array('f',range(0,103000,1000)) # 1001 to assure that 1000 is included
yv = array.array('f',range(0,213000,1000)) # 1001 to assure that 1000 is included
xysize = len(xv)*len(yv)
# Put some data in the file
for i in range(0,1):
  data1 = Array.CreateInstance(System.Single, xysize)
  xyi = 0;
  for y in yv:
    for x in xv:
      data1[xyi] = a1[xyi]
      xyi = xyi+1
  
  dfs.WriteItemTimeStepNext(0, data1);  

dfs.Close();

print "\nFile created: {0}\n".format(filename)

print(a1)

