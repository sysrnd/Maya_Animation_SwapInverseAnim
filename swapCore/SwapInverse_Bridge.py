

import  Animacion.Maya_Animation_SwapInverseAnim.swapCore.swapInverse_Core
reload( Animacion.Maya_Animation_SwapInverseAnim.swapCore.swapInverse_Core)
from  Animacion.Maya_Animation_SwapInverseAnim.swapCore.swapInverse_Core import swapInverse

from Modules.Qt import QtCore, QtGui, QtWidgets
from functools import partial

class swapInverseBridge(object):
	def __init__(self, window):
		'''
		'''

		self.window = window
		self.window.setFixedSize(340, 250)

		self.swapInverse = swapInverse()

		self.window.btn_all_swap.clicked.connect(self.swapAll)
		self.window.btn_arms_swap.clicked.connect(self.swapArms)
		self.window.btn_legs_swap.clicked.connect(self.swapLegs)

		self.window.btn_rightArm.clicked.connect(partial(self.inverse, 'arms', 'DER'))
		self.window.btn_leftArm.clicked.connect(partial(self.inverse, 'arms', 'IZQ'))
		self.window.btn_leftLeg.clicked.connect(partial(self.inverse, 'legs', 'IZQ'))
		self.window.btn_rightLeg.clicked.connect(partial(self.inverse, 'legs', 'IZQ'))
		self.window.btn_rightLeg.clicked.connect(partial(self.inverse, 'legs', 'IZQ'))
		self.window.btn_spine.clicked.connect(partial(self.inverse, 'spine', None))
		self.window.btn_head.clicked.connect(partial(self.inverse, 'head', None))

		self.populateUI()

	def populateUI(self):

		refs = self.swapInverse.findRefs()

		for ref in refs:
			namespace = self.swapInverse.getNamespace(ref)
			if namespace.find('RG_') != -1:
				self.window.cmbBox_currChar.addItem(namespace)


	def inverse(self, section, side):
		self.currChar = self.window.cmbBox_currChar.currentText()
		self.swapInverse.inverseKeys(self.currChar, section, side)

	def swapArms(self):
		self.currChar = self.window.cmbBox_currChar.currentText()
		self.swapInverse.inverseKeys(self.currChar, 'arms', 'IZQ')
		self.swapInverse.inverseKeys(self.currChar, 'arms', 'DER')
		self.swapInverse.swapKeys(self.currChar, 'arms')

	def swapLegs(self):
		self.currChar = self.window.cmbBox_currChar.currentText()
		self.swapInverse.inverseKeys(self.currChar, 'legs', 'IZQ')
		self.swapInverse.inverseKeys(self.currChar, 'legs', 'DER')
		self.swapInverse.swapKeys(self.currChar, 'legs')

	def swapAll(self):
		self.currChar = self.window.cmbBox_currChar.currentText()

		self.swapInverse.inverseKeys(self.currChar, 'legs', 'IZQ')
		self.swapInverse.inverseKeys(self.currChar, 'legs', 'DER')
		self.swapInverse.swapKeys(self.currChar, 'legs')

		self.swapInverse.inverseKeys(self.currChar, 'arms', 'IZQ')
		self.swapInverse.inverseKeys(self.currChar, 'arms', 'DER')
		self.swapInverse.swapKeys(self.currChar, 'arms')

		self.swapInverse.inverseKeys(self.currChar, 'spine', None)
		self.swapInverse.inverseKeys(self.currChar, 'head', None)