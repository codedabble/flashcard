import geniusflash
import kivy
kivy.require('1.1.3')

from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 
from kivy.uix.widget import Widget
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock

class LoadDialog(FloatLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)

class FlashcardApp(App):
    
    def __init__(self, **kwargs):
        super(FlashcardApp, self).__init__(**kwargs)
	self.mycardlist = geniusflash.readcards()
        self.currcard= geniusflash.getrandomcard(self.mycardlist)
	self.toggle = 0

    def on_pause(self):
        return True
 
    def dismiss_popup(self):
	self._popup.dismiss()
   
    def updateLoad(self, *args):
	content = FileChooserIconView()
	popup = Popup(content=content, title='Answer',
                      size_hint=(None, None), size=(300, 300),
                      auto_dismiss=True)	
	popup.open()
    
    def saveCard(self, *args):
	self.mycardlist.append(geniusflash.addCard("", self.questionTI.text, self.answerTI.text, ""))
	self.addpopup.dismiss()

    def addCard(self, *args):
	content = BoxLayout(orientation='vertical')
	self.questionTI = TextInput()
	self.answerTI = TextInput()
	lowbox = BoxLayout(height=50)
	btnsave = Button(text='Save', height=50)
	btnsave.bind(on_release=self.saveCard)

	btncancel = Button(text='Cancel', height=50)
#	content.add_widget(HSeparator(text='Question'))
	content.add_widget(self.questionTI)
#	content.add_widget(HSeparator(text='Answer'))
	content.add_widget(self.answerTI)
	
	lowbox.add_widget(btnsave)
	lowbox.add_widget(btncancel)

	content.add_widget(lowbox)

	self.addpopup = Popup(content=content, title='New card',
                      size_hint=(.7, .4),
                      auto_dismiss=False, anchor_y='top')
        btncancel.bind(on_release=self.addpopup.dismiss)
	self.addpopup.open()
	

    def updateAnsLabel(self, *args):
	if (self.toggle):
		answerTxt = geniusflash.getquestion(self.currcard) 
	else:
		answerTxt = geniusflash.getanswer(self.currcard) 
	content = Label(text=answerTxt, font_size=72, halign='center', text_size=(780, None));
	popup = Popup(content=content, title='Answer',
                      size_hint=(None, None), size=(300, 300),
                      auto_dismiss=True)	
	popup.open()
	return self.wordtxt
    
    def updateToggle(self, *args):
	if (self.toggle):
		self.toggle = 0;
		self.wordtxt = geniusflash.getquestion(self.currcard)
		self.toggleButton.text = "A->B"
	else:
		self.toggle = 1;
		self.wordtxt = geniusflash.getanswer(self.currcard)
		self.toggleButton.text = "B->A"
	self.questionLabel.text = self.wordtxt 

	
    def updateCard(self, *args):
        self.currcard= geniusflash.getrandomcard(self.mycardlist)
	if (self.toggle == 0):
		self.wordtxt = geniusflash.getquestion(self.currcard)
	else:
		self.wordtxt = geniusflash.getanswer(self.currcard)
	self.questionLabel.text = self.wordtxt 
	self.notesLabel.text = geniusflash.getnotes(self.currcard) 
	return self.currcard

    def drawstuff(self, labeltxt):
	root = BoxLayout(orientation='vertical')
	topbox = BoxLayout(orientation='vertical')
	lowerbox = BoxLayout()
	self.questionLabel = Label(text=labeltxt, font_size=72, text_size=(780, None));
	notetxt = geniusflash.getnotes(self.currcard)
	if len(notetxt):
		self.notesLabel = Label(text=notetxt, font_size=32)
	topbox.add_widget(self.questionLabel)
	if len(notetxt):
		topbox.add_widget(self.notesLabel)
	root.add_widget(topbox)

#	loadFileButton = Button(text='Load', size_hint_y=None, height=70)
#	loadFileButton.bind(on_release=self.updateLoad)
#	lowerbox.add_widget(loadFileButton)

	addFileButton = Button(text='Add', size_hint_y=None, height=70)
	addFileButton.bind(on_release=self.addCard)
	lowerbox.add_widget(addFileButton)

	answerButton = Button(text='Answer', size_hint_y=None, height=70)
	answerButton.bind(on_release=self.updateAnsLabel)
	lowerbox.add_widget(answerButton)

	self.toggleButton = Button(text='A->B', size_hint_y=None, height=70)
	self.toggleButton.bind(on_release=self.updateToggle)
	lowerbox.add_widget(self.toggleButton)

	nextButton = Button(text='Next', size_hint_y=None, height=70)
	nextButton.bind(on_release=self.updateCard)
	lowerbox.add_widget(nextButton)
	root.add_widget(lowerbox)

	return root;

    def build(self):
	self.wordtxt = geniusflash.getquestion(self.currcard)
	self.rootbox = self.drawstuff(self.wordtxt)
	return self.rootbox
     
if __name__ == '__main__':
    FlashcardApp().run()
