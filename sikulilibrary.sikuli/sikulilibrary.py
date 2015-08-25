from __future__ import with_statement
from sikuli import *
from sikuliwrapper import *
import common
import xlrd

setBundlePath("sikulilibrary.sikuli")
addImagePath("sikulilibrary.sikuli/../Images_Library")
addImagePath(common.cfgImageLibrary)
Settings.OcrTextSearch = True
Settings.OcrTextRead = True
s = Screen()

class SikuliMethods(BaseLogger):
	def __init__(self):

		self.appCoordinates = (0, 0, 2560, 1440)
		
	def replaceText(self, *args):
		return args[0].replace(args[1], args[2])
		
	def startApp(self, argApp):
		App.open(argApp)
		
	def setAppFocus(self, argApp):
		myApp = App(argApp)
		myApp.focus()
			
	def terminateApp(self, argAppName):
		App.open("taskkill /f /im %s" % (argAppName,))
		
	def getImageRegionCoordinates(self, argImage):
		s.find(argImage)
		match = s.getLastMatch()
		self.appCoordinates = (match.getX(), match.getY(), match.getW(), match.getH())
		appRegion = Region(*self.appCoordinates)
		
	def by_y(match):
		return match.y
	
	def getPatternsInRegion(self, *args):
		reg = self.getImageRegionCoordinates(args[0])
		listOfPatterns = []
		listOfSortedPatterns = []
		with reg.findAll(args[1]) as foundImages:
			while foundImages.hasNext():
				listOfPatterns.append(foundImages.next())
			listOfSortedPatterns = sorted(listOfPatterns, key=by_y)
		return listOfSortedPatterns
	
	def clickAllPatternsInRegion(self, *args):
		for pattern in getPatternsInRegion(args[0], args[1]):
			click(pattern)
			
	def getImageBasedOnReferenceImage(self, *args): # arguments: spatial location, reference image, target image
		if (args[0] == "left"):
			return s.find(args[1]).left().find(args[2])
		elif (args[0] == "right"):
			return s.find(args[1]).right().find(args[2])
		elif (args[0] == "above"):
			return s.find(args[1]).above().find(args[2])
		elif (args[0] == "below"):
			return s.find(args[1]).below().find(args[2])
		elif (args[0] == "inside"):
			return s.find(args[1]).inside().find(args[2])
		elif (args[0] == "nearby"):
			return s.find(args[1]).nearby().find(args[2])
		else:
			return None
		
	def userActionOnImageBasedOnReference(self, *args): # arguments: action, spatial location, reference image, target image
		if (args[0] == "click"):
			click(self.getImageBasedOnReferenceImage(args[1], args[2], args[3]))
		elif (args[0] == "doubleClick"):
			doubleClick(self.getImageBasedOnReferenceImage(args[1], args[2], args[3]))
		elif (args[0] == "rightClick"):
			rightClick(self.getImageBasedOnReferenceImage(args[1], args[2], args[3]))
		elif (args[0] == "type"):
			type(self.getImageBasedOnReferenceImage(args[1], args[2], args[3]), args[4])
		elif (args[0] == "paste"):
			paste(self.getImageBasedOnReferenceImage(args[1], args[2], args[3]), args[4])
		elif (args[0] == "dragDrop"):
			dragDrop(self.getImageBasedOnReferenceImage(args[1], args[2], args[3]), args[4])
			
	def setWaitValue(self, argDelay):
		s.wait(int(argDelay))

	def setSleepValue(self, argSleep):
		s.sleep(int(argSleep))
		
	def verifyApp(self, *args):
		# check application
		if s.exists(args[0]):
			self.log.passed("'%s' window appeared." % (args[1],))
		else:
			self.log.failed("No visible '%s' window." % (args[1],))
		MyApp = App(args[2])
		MyApp.focus()
		s.wait(1)
				
	def getXLSCellValue(self, *args):
		xls_file = str(args[0])
		xls_workbook = xlrd.open_workbook(xls_file)
		xls_sheet = xls_workbook.sheet_by_name(str(args[1]))
		cellValue = xls_sheet.cell(int(args[2]),int(args[3])).value
		return cellValue

	def imageExists(self, args):
		try:
			s.find(Pattern(args).exact())
			return True
		except FindFailed:
			return False
			
	def imageExistsInReferenceToAnotherImage(self, *args):
		try:
			s.find(self.getImageBasedOnReferenceImage(args[0], args[1], args[2]))
			return True
		except FindFailed:
			return False
        
	def getResultFromClipboard(self):
		type('c', KEY_CTRL)
		return str(Env.getClipboard())
		
	def pressKey(self, argKey):
		self.setFocus()
		if (argKey == "DOWN"):
			SCREEN.type(Key.DOWN)
		elif (argKey == "ENTER"):
			SCREEN.type(Key.ENTER)
		elif (argKey == "TAB"):
			SCREEN.type(Key.TAB)
		elif (argKey == "ESC"):
			SCREEN.type(Key.ESC)
		elif (argKey == "SPACE"):
			SCREEN.type(Key.SPACE)
		elif (argKey == "UP"):
			SCREEN.type(Key.UP)
		elif (argKey == "DOWN"):
			SCREEN.type(Key.DOWN)
		elif (argKey == "LEFT"):
			SCREEN.type(Key.LEFT)
		elif (argKey == "RIGHT"):
			SCREEN.type(Key.RIGHT)
		elif (argKey == "DELETE"):
			SCREEN.type(Key.DELETE)
		elif (argKey == "INSERT"):
			SCREEN.type(Key.INSERT)
		elif (argKey == "PAGE_UP"):
			SCREEN.type(Key.PAGE_UP)
		elif (argKey == "PAGE_DOWN"):
			SCREEN.type(Key.PAGE_DOWN)
		elif (argKey == "HOME"):
			SCREEN.type(Key.HOME)
		elif (argKey == "END"):
			SCREEN.type(Key.END)
		elif (argKey == "F1"):
			SCREEN.type(Key.F1)
		elif (argKey == "F2"):
			SCREEN.type(Key.F2)
		elif (argKey == "F3"):
			SCREEN.type(Key.F3)
		elif (argKey == "F4"):
			SCREEN.type(Key.F4)
		elif (argKey == "F5"):
			SCREEN.type(Key.F5)
		elif (argKey == "F6"):
			SCREEN.type(Key.F6)
		elif (argKey == "F7"):
			SCREEN.type(Key.F7)
		elif (argKey == "F8"):
			SCREEN.type(Key.F8)
		elif (argKey == "F9"):
			SCREEN.type(Key.F9)
		elif (argKey == "F10"):
			SCREEN.type(Key.F10)
		elif (argKey == "F11"):
			SCREEN.type(Key.F11)
		elif (argKey == "F12"):
			SCREEN.type(Key.F12)
			
	def pressCtrlAltPlusKey(self, argKey):
		self.setFocus()
		if (argKey == "DELETE"):
			SCREEN.type(Key.DELETE, KeyModifier.CTRL | KeyModifier.ALT)
		elif (argKey == "ESC"):
			SCREEN.type(Key.ESC, KeyModifier.CTRL | KeyModifier.ALT)
			
	def pressCtrlPlusKey(self, argKey):
		self.setFocus()
		SCREEN.type(argKey, KeyModifier.CTRL)
		sleep(1)
			
	def pressKeyNTimes(self, *args):
	  if(int(args[1]) < 1):
		wait(0)
	  else:
		pressCount = 1
		while( pressCount <= int(args[1])):
		  self.pressKey(args[0])
		  pressCount = pressCount + 1
			
	def clearTextField(self):
		self.pressCtrlPlusKey("a")
		self.pressKey("DELETE")
		
	def clearComboboxField(self):
		self.pressCtrlPlusKey("DELETE")
		
	#def clearComboboxField2(self):
		#if s.exists("Buttons/Global/ClearComboBoxField.png"):
			#s.click("Buttons/Global/ClearComboBoxField.png")
			
	def clickImage(self, argImage):
		try:
			img = s.find(Pattern(argImage).exact())
			s.click(img)
		except FindFailed:
			self.log.failed("'%s' does not exist." % (argImage,))
		
	def clickImageinXY(self, *args):
		try:
			s.find(Pattern(args[0]).exact())
			s.click(Pattern(args[0]).exact().targetOffset(int(args[1]), int(args[2])))
		except FindFailed:
			self.log.failed("'%s' does not exist." % (args[0],))
	
	def doubleClickImage(self, argImage):
		try:
			img = s.find(Pattern(argImage).exact())
			s.doubleClick(img)
		except FindFailed:
			self.log.failed("'%s' does not exist." % (argImage,))
	
	def doubleClickImageinXY(self, *args):
		try:
			s.find(Pattern(args[0]).exact())
			s.doubleClick(Pattern(args[0]).exact().targetOffset(int(args[1]), int(args[2])))
		except FindFailed:
			self.log.failed("'%s' does not exist." % (args[0],))
		
	def rightClickImage(self, argImage):
		try:
			img = s.find(Pattern(argImage).exact())
			s.rightClick(img)
		except FindFailed:
			self.log.failed("'%s' does not exist." % (argImage,))	
	
	def rightClickImageinXY(self, *args):
		try:
			s.find(Pattern(args[0]).exact())
			s.rightClick(Pattern(args[0]).exact().targetOffset(int(args[1]), int(args[2])))
		except FindFailed:
			self.log.failed("'%s' does not exist." % (args[0],))
		
	def waitForImageToBeVisible(self, *args):
		if (args[1] == 'FOREVER'):			
			s.wait(args[0], FOREVER)
			#self.assertImageExists(args[0])
		else:
			s.wait(args[0], int(args[1]))
			#self.assertImageExists(args[0])
		
	def waitForImageToVanish(self, *args):#arguments: image(path or filename), time (s)
		if (args[1] == 'FOREVER'):			
			s.waitVanish(args[0], FOREVER)
			#self.assertImageNotExists(args[0])
		else:
			s.waitVanish(args[0], int(args[1]))
			#self.assertImageNotExists(args[0])
		
	def typeText(self, argText):
		s.type(argText)

	def typeTextInsideImageXY(self, *args):
		try:
			s.find(Pattern(args[0]).exact())
			s.type(Pattern(args[0]).exact().targetOffset(int(args[1]), int(args[2])), args[3])
		except FindFailed:
			self.log.failed("'%s' does not exist." % (args[0],))

	def pasteText(self, argText):
		s.paste(argText)
		
	def pasteTextInsideImageXY(self, *args):
		try:
			s.find(Pattern(args[0]).exact())
			s.paste(Pattern(args[0]).exact().targetOffset(int(args[1]), int(args[2])), args[3])
		except FindFailed:
			self.log.failed("'%s' does not exist." % (args[0],))	
		
	def assertImageExists(self, argImage): #arguments: image(path or filename), time (s)	
		assert(exists(argImage))

	def assertImageNotExists(self, argImage): #arguments: image(path or filename), time (s)
		assert not exists(argImage)
		
	def readText(self, *args): #arguments: image(path or filename), offset (pixels), spatial location
		offsetVal = int(args[1])
		try:
			if(args[2] == 'Right'):
				s.find(Pattern(args[0]).exact())
				return s.find(args[0]).right(offsetVal).text()
			elif(args[2] == 'Left'):
				s.find(Pattern(args[0]).exact())
				return s.find(args[0]).left(offsetVal).text()
			elif(args[2] == 'Above'):
				s.find(Pattern(args[0]).exact())
				return s.find(args[0]).above(offsetVal).text()
			elif(args[2] == 'Below'):
				s.find(Pattern(args[0]).exact())
				return s.find(args[0]).below(offsetVal).text()
		except FindFailed:
			self.log.failed("'%s' does not exist." % (args[0],))