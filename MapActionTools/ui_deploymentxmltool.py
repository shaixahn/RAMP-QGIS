# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_deploymentxmltool.ui'
#
# Created: Tue Oct 16 20:08:59 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DeploymentXmlTool(object):
    def setupUi(self, DeploymentXmlTool):
        DeploymentXmlTool.setObjectName(_fromUtf8("DeploymentXmlTool"))
        DeploymentXmlTool.resize(574, 588)
        DeploymentXmlTool.setSizeGripEnabled(False)
        self.label = QtGui.QLabel(DeploymentXmlTool)
        self.label.setGeometry(QtCore.QRect(180, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnCreateSave = QtGui.QPushButton(DeploymentXmlTool)
        self.btnCreateSave.setGeometry(QtCore.QRect(470, 550, 75, 23))
        self.btnCreateSave.setObjectName(_fromUtf8("btnCreateSave"))
        self.btnCancel = QtGui.QPushButton(DeploymentXmlTool)
        self.btnCancel.setGeometry(QtCore.QRect(390, 550, 75, 23))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.tabWidget = QtGui.QTabWidget(DeploymentXmlTool)
        self.tabWidget.setGeometry(QtCore.QRect(20, 160, 531, 381))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabSection1 = QtGui.QWidget()
        self.tabSection1.setObjectName(_fromUtf8("tabSection1"))
        self.label_17 = QtGui.QLabel(self.tabSection1)
        self.label_17.setGeometry(QtCore.QRect(20, 50, 145, 13))
        self.label_17.setBaseSize(QtCore.QSize(0, 0))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.txtPath2Active = QtGui.QLineEdit(self.tabSection1)
        self.txtPath2Active.setGeometry(QtCore.QRect(170, 110, 300, 20))
        self.txtPath2Active.setObjectName(_fromUtf8("txtPath2Active"))
        self.label_14 = QtGui.QLabel(self.tabSection1)
        self.label_14.setGeometry(QtCore.QRect(20, 140, 145, 13))
        self.label_14.setBaseSize(QtCore.QSize(0, 0))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_12 = QtGui.QLabel(self.tabSection1)
        self.label_12.setGeometry(QtCore.QRect(20, 200, 145, 16))
        self.label_12.setBaseSize(QtCore.QSize(0, 0))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.txtOperationName = QtGui.QLineEdit(self.tabSection1)
        self.txtOperationName.setGeometry(QtCore.QRect(170, 20, 300, 20))
        self.txtOperationName.setObjectName(_fromUtf8("txtOperationName"))
        self.txtPathMxd = QtGui.QLineEdit(self.tabSection1)
        self.txtPathMxd.setGeometry(QtCore.QRect(170, 170, 300, 20))
        self.txtPathMxd.setObjectName(_fromUtf8("txtPathMxd"))
        self.label_13 = QtGui.QLabel(self.tabSection1)
        self.label_13.setGeometry(QtCore.QRect(20, 170, 145, 13))
        self.label_13.setBaseSize(QtCore.QSize(0, 0))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_15 = QtGui.QLabel(self.tabSection1)
        self.label_15.setGeometry(QtCore.QRect(20, 110, 145, 13))
        self.label_15.setBaseSize(QtCore.QSize(0, 0))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.txtPath1Original = QtGui.QLineEdit(self.tabSection1)
        self.txtPath1Original.setGeometry(QtCore.QRect(170, 80, 300, 20))
        self.txtPath1Original.setObjectName(_fromUtf8("txtPath1Original"))
        self.txtDefaultLanguage = QtGui.QLineEdit(self.tabSection1)
        self.txtDefaultLanguage.setGeometry(QtCore.QRect(170, 290, 300, 20))
        self.txtDefaultLanguage.setObjectName(_fromUtf8("txtDefaultLanguage"))
        self.label_9 = QtGui.QLabel(self.tabSection1)
        self.label_9.setGeometry(QtCore.QRect(20, 290, 145, 13))
        self.label_9.setBaseSize(QtCore.QSize(0, 0))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.txtOperationId = QtGui.QLineEdit(self.tabSection1)
        self.txtOperationId.setGeometry(QtCore.QRect(170, 50, 300, 20))
        self.txtOperationId.setObjectName(_fromUtf8("txtOperationId"))
        self.txtPathLayerStyles = QtGui.QLineEdit(self.tabSection1)
        self.txtPathLayerStyles.setGeometry(QtCore.QRect(170, 230, 300, 20))
        self.txtPathLayerStyles.setObjectName(_fromUtf8("txtPathLayerStyles"))
        self.txtDefaultCountry = QtGui.QLineEdit(self.tabSection1)
        self.txtDefaultCountry.setGeometry(QtCore.QRect(170, 320, 300, 20))
        self.txtDefaultCountry.setObjectName(_fromUtf8("txtDefaultCountry"))
        self.label_11 = QtGui.QLabel(self.tabSection1)
        self.label_11.setGeometry(QtCore.QRect(20, 230, 145, 13))
        self.label_11.setBaseSize(QtCore.QSize(0, 0))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.txtPathExportProducts = QtGui.QLineEdit(self.tabSection1)
        self.txtPathExportProducts.setGeometry(QtCore.QRect(170, 200, 300, 20))
        self.txtPathExportProducts.setObjectName(_fromUtf8("txtPathExportProducts"))
        self.label_16 = QtGui.QLabel(self.tabSection1)
        self.label_16.setGeometry(QtCore.QRect(20, 80, 145, 13))
        self.label_16.setBaseSize(QtCore.QSize(0, 0))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_10 = QtGui.QLabel(self.tabSection1)
        self.label_10.setGeometry(QtCore.QRect(20, 260, 145, 13))
        self.label_10.setBaseSize(QtCore.QSize(0, 0))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_8 = QtGui.QLabel(self.tabSection1)
        self.label_8.setGeometry(QtCore.QRect(20, 320, 145, 13))
        self.label_8.setBaseSize(QtCore.QSize(0, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lblOperationName = QtGui.QLabel(self.tabSection1)
        self.lblOperationName.setGeometry(QtCore.QRect(20, 20, 145, 16))
        self.lblOperationName.setBaseSize(QtCore.QSize(0, 0))
        self.lblOperationName.setObjectName(_fromUtf8("lblOperationName"))
        self.txtSourceOrganisation = QtGui.QLineEdit(self.tabSection1)
        self.txtSourceOrganisation.setGeometry(QtCore.QRect(170, 260, 300, 20))
        self.txtSourceOrganisation.setObjectName(_fromUtf8("txtSourceOrganisation"))
        self.txtPath3Mapping = QtGui.QLineEdit(self.tabSection1)
        self.txtPath3Mapping.setGeometry(QtCore.QRect(170, 140, 300, 20))
        self.txtPath3Mapping.setObjectName(_fromUtf8("txtPath3Mapping"))
        self.btnPathMxd = QtGui.QToolButton(self.tabSection1)
        self.btnPathMxd.setGeometry(QtCore.QRect(480, 170, 25, 19))
        self.btnPathMxd.setObjectName(_fromUtf8("btnPathMxd"))
        self.btnPath2Active = QtGui.QToolButton(self.tabSection1)
        self.btnPath2Active.setGeometry(QtCore.QRect(480, 110, 25, 19))
        self.btnPath2Active.setObjectName(_fromUtf8("btnPath2Active"))
        self.btnPath3Mapping = QtGui.QToolButton(self.tabSection1)
        self.btnPath3Mapping.setGeometry(QtCore.QRect(480, 140, 25, 19))
        self.btnPath3Mapping.setObjectName(_fromUtf8("btnPath3Mapping"))
        self.btnPath1Original = QtGui.QToolButton(self.tabSection1)
        self.btnPath1Original.setGeometry(QtCore.QRect(480, 80, 25, 19))
        self.btnPath1Original.setObjectName(_fromUtf8("btnPath1Original"))
        self.tabWidget.addTab(self.tabSection1, _fromUtf8("Section 1"))
        self.tabSection2 = QtGui.QWidget()
        self.tabSection2.setObjectName(_fromUtf8("tabSection2"))
        self.txtDefaultPdfFilePattern = QtGui.QLineEdit(self.tabSection2)
        self.txtDefaultPdfFilePattern.setGeometry(QtCore.QRect(170, 80, 300, 20))
        self.txtDefaultPdfFilePattern.setText(_fromUtf8(""))
        self.txtDefaultPdfFilePattern.setObjectName(_fromUtf8("txtDefaultPdfFilePattern"))
        self.txtDefaultKmzFilePattern = QtGui.QLineEdit(self.tabSection2)
        self.txtDefaultKmzFilePattern.setGeometry(QtCore.QRect(170, 230, 300, 20))
        self.txtDefaultKmzFilePattern.setObjectName(_fromUtf8("txtDefaultKmzFilePattern"))
        self.label_5 = QtGui.QLabel(self.tabSection2)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 145, 13))
        self.label_5.setBaseSize(QtCore.QSize(0, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtDefaultQcLevel = QtGui.QLineEdit(self.tabSection2)
        self.txtDefaultQcLevel.setGeometry(QtCore.QRect(170, 110, 300, 20))
        self.txtDefaultQcLevel.setObjectName(_fromUtf8("txtDefaultQcLevel"))
        self.txtPointContact = QtGui.QLineEdit(self.tabSection2)
        self.txtPointContact.setGeometry(QtCore.QRect(170, 260, 300, 20))
        self.txtPointContact.setObjectName(_fromUtf8("txtPointContact"))
        self.label_20 = QtGui.QLabel(self.tabSection2)
        self.label_20.setGeometry(QtCore.QRect(20, 140, 145, 13))
        self.label_20.setBaseSize(QtCore.QSize(0, 0))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_19 = QtGui.QLabel(self.tabSection2)
        self.label_19.setGeometry(QtCore.QRect(20, 110, 145, 13))
        self.label_19.setBaseSize(QtCore.QSize(0, 0))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.txtDefaultJpegDpi = QtGui.QLineEdit(self.tabSection2)
        self.txtDefaultJpegDpi.setGeometry(QtCore.QRect(170, 170, 300, 20))
        self.txtDefaultJpegDpi.setObjectName(_fromUtf8("txtDefaultJpegDpi"))
        self.label_18 = QtGui.QLabel(self.tabSection2)
        self.label_18.setGeometry(QtCore.QRect(20, 170, 145, 13))
        self.label_18.setBaseSize(QtCore.QSize(0, 0))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.txtMetadataContact = QtGui.QLineEdit(self.tabSection2)
        self.txtMetadataContact.setGeometry(QtCore.QRect(170, 290, 300, 20))
        self.txtMetadataContact.setObjectName(_fromUtf8("txtMetadataContact"))
        self.txtDefaultPdfDpi = QtGui.QLineEdit(self.tabSection2)
        self.txtDefaultPdfDpi.setGeometry(QtCore.QRect(170, 200, 300, 20))
        self.txtDefaultPdfDpi.setObjectName(_fromUtf8("txtDefaultPdfDpi"))
        self.txtGlideNo = QtGui.QLineEdit(self.tabSection2)
        self.txtGlideNo.setGeometry(QtCore.QRect(170, 140, 300, 20))
        self.txtGlideNo.setObjectName(_fromUtf8("txtGlideNo"))
        self.label_25 = QtGui.QLabel(self.tabSection2)
        self.label_25.setGeometry(QtCore.QRect(20, 230, 145, 13))
        self.label_25.setBaseSize(QtCore.QSize(0, 0))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.tabSection2)
        self.label_26.setGeometry(QtCore.QRect(20, 260, 145, 13))
        self.label_26.setBaseSize(QtCore.QSize(0, 0))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_28 = QtGui.QLabel(self.tabSection2)
        self.label_28.setGeometry(QtCore.QRect(20, 290, 145, 13))
        self.label_28.setBaseSize(QtCore.QSize(0, 0))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.tabSection2)
        self.label_29.setGeometry(QtCore.QRect(20, 200, 145, 13))
        self.label_29.setBaseSize(QtCore.QSize(0, 0))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.txtDefaultMapStatus = QtGui.QLineEdit(self.tabSection2)
        self.txtDefaultMapStatus.setGeometry(QtCore.QRect(170, 20, 300, 20))
        self.txtDefaultMapStatus.setObjectName(_fromUtf8("txtDefaultMapStatus"))
        self.label_7 = QtGui.QLabel(self.tabSection2)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 145, 13))
        self.label_7.setBaseSize(QtCore.QSize(0, 0))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.txtDefaultJpegFilePattern = QtGui.QLineEdit(self.tabSection2)
        self.txtDefaultJpegFilePattern.setGeometry(QtCore.QRect(170, 50, 300, 20))
        self.txtDefaultJpegFilePattern.setText(_fromUtf8(""))
        self.txtDefaultJpegFilePattern.setObjectName(_fromUtf8("txtDefaultJpegFilePattern"))
        self.label_6 = QtGui.QLabel(self.tabSection2)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 145, 13))
        self.label_6.setBaseSize(QtCore.QSize(0, 0))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget.addTab(self.tabSection2, _fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(DeploymentXmlTool)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 531, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.toolButton_4 = QtGui.QToolButton(self.groupBox)
        self.toolButton_4.setEnabled(False)
        self.toolButton_4.setGeometry(QtCore.QRect(480, 50, 25, 19))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.txtExistingFilePath = QtGui.QLineEdit(self.groupBox)
        self.txtExistingFilePath.setEnabled(False)
        self.txtExistingFilePath.setGeometry(QtCore.QRect(170, 50, 300, 20))
        self.txtExistingFilePath.setObjectName(_fromUtf8("txtExistingFilePath"))
        self.txtNewFilePath = QtGui.QLineEdit(self.groupBox)
        self.txtNewFilePath.setGeometry(QtCore.QRect(170, 20, 300, 20))
        self.txtNewFilePath.setObjectName(_fromUtf8("txtNewFilePath"))
        self.radbtnCreateNewFile = QtGui.QRadioButton(self.groupBox)
        self.radbtnCreateNewFile.setGeometry(QtCore.QRect(30, 20, 101, 17))
        self.radbtnCreateNewFile.setChecked(True)
        self.radbtnCreateNewFile.setObjectName(_fromUtf8("radbtnCreateNewFile"))
        self.radbtngrpOptions = QtGui.QButtonGroup(DeploymentXmlTool)
        self.radbtngrpOptions.setObjectName(_fromUtf8("radbtngrpOptions"))
        self.radbtngrpOptions.addButton(self.radbtnCreateNewFile)
        self.radbtnEditExistingFile = QtGui.QRadioButton(self.groupBox)
        self.radbtnEditExistingFile.setEnabled(False)
        self.radbtnEditExistingFile.setGeometry(QtCore.QRect(30, 50, 101, 17))
        self.radbtnEditExistingFile.setObjectName(_fromUtf8("radbtnEditExistingFile"))
        self.radbtngrpOptions.addButton(self.radbtnEditExistingFile)
        self.txtConnectConfigUrl = QtGui.QLineEdit(self.groupBox)
        self.txtConnectConfigUrl.setEnabled(True)
        self.txtConnectConfigUrl.setGeometry(QtCore.QRect(170, 80, 301, 20))
        self.txtConnectConfigUrl.setObjectName(_fromUtf8("txtConnectConfigUrl"))
        self.btnConnectConfigUrl = QtGui.QToolButton(self.groupBox)
        self.btnConnectConfigUrl.setEnabled(True)
        self.btnConnectConfigUrl.setGeometry(QtCore.QRect(480, 80, 26, 21))
        self.btnConnectConfigUrl.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MapActionTools/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConnectConfigUrl.setIcon(icon)
        self.btnConnectConfigUrl.setObjectName(_fromUtf8("btnConnectConfigUrl"))
        self.btnNewFilePathDir = QtGui.QToolButton(self.groupBox)
        self.btnNewFilePathDir.setEnabled(True)
        self.btnNewFilePathDir.setGeometry(QtCore.QRect(480, 20, 25, 19))
        self.btnNewFilePathDir.setObjectName(_fromUtf8("btnNewFilePathDir"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(DeploymentXmlTool)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DeploymentXmlTool)
        DeploymentXmlTool.setTabOrder(self.txtNewFilePath, self.txtExistingFilePath)
        DeploymentXmlTool.setTabOrder(self.txtExistingFilePath, self.txtOperationName)
        DeploymentXmlTool.setTabOrder(self.txtOperationName, self.txtOperationId)
        DeploymentXmlTool.setTabOrder(self.txtOperationId, self.txtPath1Original)
        DeploymentXmlTool.setTabOrder(self.txtPath1Original, self.txtPath2Active)
        DeploymentXmlTool.setTabOrder(self.txtPath2Active, self.txtPath3Mapping)
        DeploymentXmlTool.setTabOrder(self.txtPath3Mapping, self.txtPathMxd)
        DeploymentXmlTool.setTabOrder(self.txtPathMxd, self.txtPathExportProducts)
        DeploymentXmlTool.setTabOrder(self.txtPathExportProducts, self.txtPathLayerStyles)
        DeploymentXmlTool.setTabOrder(self.txtPathLayerStyles, self.txtSourceOrganisation)
        DeploymentXmlTool.setTabOrder(self.txtSourceOrganisation, self.txtDefaultLanguage)
        DeploymentXmlTool.setTabOrder(self.txtDefaultLanguage, self.txtDefaultCountry)
        DeploymentXmlTool.setTabOrder(self.txtDefaultCountry, self.txtDefaultMapStatus)
        DeploymentXmlTool.setTabOrder(self.txtDefaultMapStatus, self.txtDefaultJpegFilePattern)
        DeploymentXmlTool.setTabOrder(self.txtDefaultJpegFilePattern, self.txtDefaultPdfFilePattern)
        DeploymentXmlTool.setTabOrder(self.txtDefaultPdfFilePattern, self.txtDefaultQcLevel)
        DeploymentXmlTool.setTabOrder(self.txtDefaultQcLevel, self.txtGlideNo)
        DeploymentXmlTool.setTabOrder(self.txtGlideNo, self.txtDefaultJpegDpi)
        DeploymentXmlTool.setTabOrder(self.txtDefaultJpegDpi, self.txtDefaultPdfDpi)
        DeploymentXmlTool.setTabOrder(self.txtDefaultPdfDpi, self.txtDefaultKmzFilePattern)
        DeploymentXmlTool.setTabOrder(self.txtDefaultKmzFilePattern, self.txtPointContact)
        DeploymentXmlTool.setTabOrder(self.txtPointContact, self.txtMetadataContact)
        DeploymentXmlTool.setTabOrder(self.txtMetadataContact, self.btnCancel)
        DeploymentXmlTool.setTabOrder(self.btnCancel, self.btnCreateSave)
        DeploymentXmlTool.setTabOrder(self.btnCreateSave, self.btnPathMxd)
        DeploymentXmlTool.setTabOrder(self.btnPathMxd, self.toolButton_4)
        DeploymentXmlTool.setTabOrder(self.toolButton_4, self.btnPath2Active)
        DeploymentXmlTool.setTabOrder(self.btnPath2Active, self.btnPath3Mapping)
        DeploymentXmlTool.setTabOrder(self.btnPath3Mapping, self.radbtnEditExistingFile)
        DeploymentXmlTool.setTabOrder(self.radbtnEditExistingFile, self.tabWidget)
        DeploymentXmlTool.setTabOrder(self.tabWidget, self.radbtnCreateNewFile)
        DeploymentXmlTool.setTabOrder(self.radbtnCreateNewFile, self.btnPath1Original)

    def retranslateUi(self, DeploymentXmlTool):
        DeploymentXmlTool.setWindowTitle(QtGui.QApplication.translate("DeploymentXmlTool", "MapAction Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Deployment XML Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCreateSave.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Operation ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Path of 3_Mapping", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Path of Exported Products", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Path of MXD", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Path of 2_Active", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default Languages", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Path of Layer Style files", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Path of 1_Original", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Source Organisation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default Countries", None, QtGui.QApplication.UnicodeUTF8))
        self.lblOperationName.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Operation Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPathMxd.setText(QtGui.QApplication.translate("DeploymentXmlTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPath2Active.setText(QtGui.QApplication.translate("DeploymentXmlTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPath3Mapping.setText(QtGui.QApplication.translate("DeploymentXmlTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPath1Original.setText(QtGui.QApplication.translate("DeploymentXmlTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default PDF filename Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Glide Number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default QC Level", None, QtGui.QApplication.UnicodeUTF8))
        self.txtDefaultJpegDpi.setText(QtGui.QApplication.translate("DeploymentXmlTool", "300", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default JPEG Resolution DPI", None, QtGui.QApplication.UnicodeUTF8))
        self.txtDefaultPdfDpi.setText(QtGui.QApplication.translate("DeploymentXmlTool", "150", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default KMZ filename Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Point of Contact", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Metadata Contact", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default PDF Resolution DPI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default Map Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Default JPEG filename Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSection2), QtGui.QApplication.translate("DeploymentXmlTool", "Section 2", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DeploymentXmlTool", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setText(QtGui.QApplication.translate("DeploymentXmlTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.txtNewFilePath.setToolTip(QtGui.QApplication.translate("DeploymentXmlTool", "Directory to save the new file", None, QtGui.QApplication.UnicodeUTF8))
        self.radbtnCreateNewFile.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Create new file", None, QtGui.QApplication.UnicodeUTF8))
        self.radbtnEditExistingFile.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Edit existing file", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNewFilePathDir.setText(QtGui.QApplication.translate("DeploymentXmlTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DeploymentXmlTool", "Update from URL", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DeploymentXmlTool = QtGui.QDialog()
    ui = Ui_DeploymentXmlTool()
    ui.setupUi(DeploymentXmlTool)
    DeploymentXmlTool.show()
    sys.exit(app.exec_())

