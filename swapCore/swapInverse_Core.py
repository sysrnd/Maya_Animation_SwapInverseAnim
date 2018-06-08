import maya.cmds as cmds
import pymel.core as pm
import json


class swapInverse(object):

	def __init__(self):

		#self.arms = ['DRIVER_HOMBRO_IZQ_FK', 'DRIVER_CODO_IZQ_FK', 'DRIVER_MANO_IZQ_FK']
		self.axes = ['X', 'Y', 'Z']
		self.attributes = {'translate': 0, 'rotate': 3}

		self.controls = {'arms':{
		'DRIVER_CLAVICULA_IZQ':(1, -1, -1, 1, -1, -1), 'DRIVER_HOMBRO_IZQ_FK':(1, -1, -1, 1, -1, -1), 'DRIVER_CODO_IZQ':(1, -1, -1, 1, -1, -1), 'DRIVER_CODO_IZQ_FK':(1, -1, -1, 1, -1, -1), 
		'DRIVER_MANO_IZQ':(1, -1, -1, 1, -1, -1), 'DRIVER_MANO_IZQ_FK':(1, -1, -1, 1, -1, -1), 'DRIVER_CANCEL_IZQ_1':(1, 1, 1, 1, 1, 1), 'DRIVER_INDEX_IZQ_1':(1, 1, 1, 1, 1, 1), 
		'DRIVER_MIDDLE_IZQ_1':(1, 1, 1, 1, 1, 1), 'DRIVER_PINKY_SEC_IZQ':(1, 1, 1, 1, 1, 1), 'DRIVER_PINKY_IZQ_1':(1, 1, 1, 1, 1, 1), 'DRIVER_THUMB_IZQ_1':(1, 1, 1, 1, 1, 1)},
						'spine':{
		'DRIVER_COLUMNA_TOP':(1, 1, 1, 1, 1, -1), 'DRIVER_COLUMNA_MIDDLE':(1, 1, 1, 1, 1, -1), 'DRIVER_COLUMNA_BOTTOM':(1, 1, 1, 1, 1, -1), 'DRIVER_ROOT':(-1, 1, 1, 1, -1, -1),
		'DRIVER_CINTURA':(1, 1, 1, 1, 1, -1)},
						'legs':{
		'DRIVER_BALL_IZQ':(1, -1, -1, 1, 1, 1), 'DRIVER_HEEL_IZQ':(1, -1, -1, 1, 1, 1), 'DRIVER_PIE_IZQ':(-1, 1, 1, 1, -1, 1), 'DRIVER_RODILLA_IZQ':(-1, 1, 1, 1, 1, 1), 
		'DRIVER_TOE_FINGERS_IZQ':(1, -1, -1, 1, 1, 1), 'DRIVER_TOE_IZQ':(1, -1, -1, 1, 1, 1)},
						'head':{'DRIVER_CABEZA':(1, 1, 1, 1, 1, -1)}}

		self.dummy = ''

	def findRefs(self):
		'''
		queries all reference paths
		'''
		refs = cmds.file(q=True, r=True)

		return refs

	def getNamespace(self, ref):

		namespace = cmds.file(ref, q=True, ns=True)
		return namespace

	def createDummy(self):
		self.dummy = cmds.spaceLocator(n='dummyKeysHolder')[0]
		return self.dummy

	def deleteDummy(self):
		try:
			cmds.delete(self.dummy)

		except:
			locs = cmds.ls(et='locator')
			for loc in locs:
				if loc.find('dummyKeysHolder') != -1:
					locParent = cmds.listRelatives(loc, p=True)[0]
					cmds.delete(locParent)


	def reverseKeys(self, ctrl):

		keyframes = pm.keyframe(ctrl, attribute='rotateZ', time=(0,20), query=True, valueChange=True, timeChange=True)

		for key in keyframes:
			pm.keyframe(ctrl, attribute='rotateZ', time=key[0], edit=True, valueChange= (key[1] * -1))

	def inverseKeys(self, current, section, keyword):

		for arm in self.controls[section]:

			armParsed = current + ':' + arm
			
			if keyword != None:
				armParsed = current + ':' + arm.replace('IZQ', keyword)

			for attr in self.attributes:
				for i, axis in enumerate(self.axes):

					ii = i + self.attributes[attr]
					axisMult = self.controls[section][arm][ii]

					keyframes = pm.keyframe(armParsed, a=True, attribute=attr + axis, query=True, valueChange=True, timeChange=True)

					for key in keyframes:
						pm.keyframe(armParsed, a=True, attribute=attr + axis, time=key[0], edit=True, valueChange= (key[1] * axisMult))
	
	def swapKeys(self, current, section):
		for arm in self.controls[section]:

			armLeft = current + ':' + arm
			armRight = armLeft.replace('IZQ', 'DER')

			for attr in self.attributes:
				for i, axis in enumerate(self.axes):

					dummyRight = self.createDummy()
					dummyLeft = self.createDummy()

					self.moveKeys(armLeft, dummyRight, attr, axis)
					self.moveKeys(armRight, dummyLeft, attr, axis)
					self.moveKeys(dummyLeft, armLeft, attr, axis)
					self.moveKeys(dummyRight, armRight, attr, axis)

					cmds.delete(dummyRight)
					cmds.delete(dummyLeft)

	def moveKeys(self, src, dest, attr, axis):

		areThereKeys = pm.keyframe(src, attribute=attr + axis, query=True, valueChange=True)

		if len(areThereKeys) > 0:
			pm.cutKey(src, attribute=attr + axis)
			pm.pasteKey(dest, attribute=attr + axis)