# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'C:\Users\ASUSarturo\Desktop\RnD\MKF\Animacion\Maya_Animation_SwapInverseAnim\swapUI\Resources\swapInverse_UI_v003.ui'

#

# Created by: PyQt4 UI code generator 4.11.4

#

# WARNING! All changes made in this file will be lost!



from Modules.Qt import QtCore, QtGui, QtWidgets


try:

    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):

        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):

        return QtCore.QCoreApplication.translate(context, text, disambig)



class Ui_window_SwapInverseAnim(object):

    def setupUi(self, window_SwapInverseAnim):

        window_SwapInverseAnim.setObjectName("window_SwapInverseAnim")

        window_SwapInverseAnim.resize(397, 278)

        window_SwapInverseAnim.setWindowOpacity(1.0)

        self.widget_swapAnim = QtWidgets.QWidget(window_SwapInverseAnim)

        self.widget_swapAnim.setObjectName("widget_swapAnim")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_swapAnim)

        self.verticalLayout.setObjectName("verticalLayout")

        self.lyt_horizontalChar = QtWidgets.QHBoxLayout()

        self.lyt_horizontalChar.setObjectName("lyt_horizontalChar")

        self.lbl_currChar = QtWidgets.QLabel(self.widget_swapAnim)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.lbl_currChar.sizePolicy().hasHeightForWidth())

        self.lbl_currChar.setSizePolicy(sizePolicy)

        font = QtGui.QFont()

        font.setItalic(True)

        self.lbl_currChar.setFont(font)

        self.lbl_currChar.setObjectName("lbl_currChar")

        self.lyt_horizontalChar.addWidget(self.lbl_currChar)

        self.cmbBox_currChar = QtWidgets.QComboBox(self.widget_swapAnim)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.cmbBox_currChar.sizePolicy().hasHeightForWidth())

        self.cmbBox_currChar.setSizePolicy(sizePolicy)

        self.cmbBox_currChar.setObjectName("cmbBox_currChar")

        self.lyt_horizontalChar.addWidget(self.cmbBox_currChar)

        self.verticalLayout.addLayout(self.lyt_horizontalChar)

        self.lyt_vertical_tabs = QtWidgets.QVBoxLayout()

        self.lyt_vertical_tabs.setObjectName("lyt_vertical_tabs")

        self.widget_tabs = QtWidgets.QTabWidget(self.widget_swapAnim)

        self.widget_tabs.setEnabled(True)

        self.widget_tabs.setObjectName("widget_tabs")

        self.tab_inverse = QtWidgets.QWidget()

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.tab_inverse.sizePolicy().hasHeightForWidth())

        self.tab_inverse.setSizePolicy(sizePolicy)

        self.tab_inverse.setObjectName("tab_inverse")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_inverse)

        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lyt_grid_inverseCheckboxes = QtWidgets.QGridLayout()

        self.lyt_grid_inverseCheckboxes.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

        self.lyt_grid_inverseCheckboxes.setHorizontalSpacing(25)

        self.lyt_grid_inverseCheckboxes.setVerticalSpacing(10)

        self.lyt_grid_inverseCheckboxes.setObjectName("lyt_grid_inverseCheckboxes")

        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.lyt_grid_inverseCheckboxes.addItem(spacerItem, 1, 0, 1, 1)

        self.btn_leftLeg = QtWidgets.QPushButton(self.tab_inverse)

        self.btn_leftLeg.setObjectName("btn_leftLeg")

        self.lyt_grid_inverseCheckboxes.addWidget(self.btn_leftLeg, 2, 0, 1, 1)

        self.btn_selected = QtWidgets.QPushButton(self.tab_inverse)

        self.btn_selected.setEnabled(False)

        font = QtGui.QFont()

        font.setBold(True)

        font.setWeight(75)

        self.btn_selected.setFont(font)

        self.btn_selected.setObjectName("btn_selected")

        self.lyt_grid_inverseCheckboxes.addWidget(self.btn_selected, 0, 1, 1, 1)

        self.btn_rightArm = QtWidgets.QPushButton(self.tab_inverse)

        self.btn_rightArm.setObjectName("btn_rightArm")

        self.lyt_grid_inverseCheckboxes.addWidget(self.btn_rightArm, 3, 1, 1, 1)

        self.btn_all = QtWidgets.QPushButton(self.tab_inverse)
        self.btn_all.setEnabled(False)

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setItalic(False)

        font.setWeight(75)

        self.btn_all.setFont(font)

        self.btn_all.setAutoDefault(False)

        self.btn_all.setObjectName("btn_all")

        self.lyt_grid_inverseCheckboxes.addWidget(self.btn_all, 0, 0, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.lyt_grid_inverseCheckboxes.addItem(spacerItem1, 1, 1, 1, 1)

        self.btn_rightLeg = QtWidgets.QPushButton(self.tab_inverse)

        self.btn_rightLeg.setObjectName("btn_rightLeg")

        self.lyt_grid_inverseCheckboxes.addWidget(self.btn_rightLeg, 2, 1, 1, 1)

        self.btn_leftArm = QtWidgets.QPushButton(self.tab_inverse)

        self.btn_leftArm.setObjectName("btn_leftArm")

        self.lyt_grid_inverseCheckboxes.addWidget(self.btn_leftArm, 3, 0, 1, 1)

        self.btn_spine = QtWidgets.QPushButton(self.tab_inverse)

        self.btn_spine.setObjectName("btn_spine")

        self.lyt_grid_inverseCheckboxes.addWidget(self.btn_spine, 4, 0, 1, 1)

        self.btn_head = QtWidgets.QPushButton(self.tab_inverse)

        self.btn_head.setObjectName("btn_head")

        self.lyt_grid_inverseCheckboxes.addWidget(self.btn_head, 4, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.lyt_grid_inverseCheckboxes)

        self.widget_tabs.addTab(self.tab_inverse, "")

        self.tabSwap = QtWidgets.QWidget()

        self.tabSwap.setObjectName("tabSwap")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabSwap)

        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.lyt_grid_swapCheckBoxes = QtWidgets.QGridLayout()

        self.lyt_grid_swapCheckBoxes.setHorizontalSpacing(25)

        self.lyt_grid_swapCheckBoxes.setObjectName("lyt_grid_swapCheckBoxes")

        self.btn_legs_swap = QtWidgets.QPushButton(self.tabSwap)

        self.btn_legs_swap.setObjectName("btn_legs_swap")

        self.lyt_grid_swapCheckBoxes.addWidget(self.btn_legs_swap, 1, 0, 1, 1)

        self.btn_arms_swap = QtWidgets.QPushButton(self.tabSwap)

        self.btn_arms_swap.setObjectName("btn_arms_swap")

        self.lyt_grid_swapCheckBoxes.addWidget(self.btn_arms_swap, 1, 1, 1, 1)

        self.btn_all_swap = QtWidgets.QPushButton(self.tabSwap)

        font = QtGui.QFont()

        font.setBold(True)

        font.setWeight(75)

        self.btn_all_swap.setFont(font)

        self.btn_all_swap.setObjectName("btn_all_swap")

        self.lyt_grid_swapCheckBoxes.addWidget(self.btn_all_swap, 0, 0, 1, 2)

        self.verticalLayout_5.addLayout(self.lyt_grid_swapCheckBoxes)

        self.widget_tabs.addTab(self.tabSwap, "")

        self.lyt_vertical_tabs.addWidget(self.widget_tabs)

        self.verticalLayout.addLayout(self.lyt_vertical_tabs)

        window_SwapInverseAnim.setCentralWidget(self.widget_swapAnim)

        self.menubar = QtWidgets.QMenuBar(window_SwapInverseAnim)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 21))

        self.menubar.setObjectName("menubar")

        window_SwapInverseAnim.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(window_SwapInverseAnim)

        self.statusbar.setObjectName("statusbar")

        window_SwapInverseAnim.setStatusBar(self.statusbar)



        self.retranslateUi(window_SwapInverseAnim)

        self.widget_tabs.setCurrentIndex(1)

        QtCore.QMetaObject.connectSlotsByName(window_SwapInverseAnim)



    def retranslateUi(self, window_SwapInverseAnim):

        window_SwapInverseAnim.setWindowTitle(_translate("window_SwapInverseAnim", "Swap & Inverse Animation", None))

        self.lbl_currChar.setText(_translate("window_SwapInverseAnim", "Current Character:   ", None))

        self.btn_leftLeg.setText(_translate("window_SwapInverseAnim", "Left Leg", None))

        self.btn_selected.setText(_translate("window_SwapInverseAnim", "Selected on Scene", None))

        self.btn_rightArm.setText(_translate("window_SwapInverseAnim", "Right Arm", None))

        self.btn_all.setText(_translate("window_SwapInverseAnim", "All", None))

        self.btn_rightLeg.setText(_translate("window_SwapInverseAnim", "Right Leg", None))

        self.btn_leftArm.setText(_translate("window_SwapInverseAnim", "Left Arm", None))

        self.btn_spine.setText(_translate("window_SwapInverseAnim", "Spine", None))

        self.btn_head.setText(_translate("window_SwapInverseAnim", "Head", None))

        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.tab_inverse), _translate("window_SwapInverseAnim", "Inverse", None))

        self.btn_legs_swap.setText(_translate("window_SwapInverseAnim", "Legs", None))

        self.btn_arms_swap.setText(_translate("window_SwapInverseAnim", "Arms", None))

        self.btn_all_swap.setText(_translate("window_SwapInverseAnim", "All", None))

        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.tabSwap), _translate("window_SwapInverseAnim", "Swap", None))



