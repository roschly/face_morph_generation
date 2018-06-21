# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 581,799 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Input data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Fill out ONLY folder 1:\nEvery image is morphed with every other image in the same folder\n\nFill out folder 1 AND 2:\nEach image is only morphed with images from the other folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Folder 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial" ) )
		
		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_dirPicker_in_1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer1.Add( self.m_dirPicker_in_1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Folder 2 (leave blank if you want option 1)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_dirPicker_in_2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer1.Add( self.m_dirPicker_in_2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Output data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Choose output folder for morphed images", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_dirPicker_out = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer1.Add( self.m_dirPicker_out, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Morphing methods", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		bSizer3.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Choose method", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"full_image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn1.SetValue( True ) 
		bSizer3.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"face_swap_morph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Choose parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Blend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 5, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer1.Add( self.m_slider1, 0, wx.ALL, 5 )
		
		self.m_staticText_slider_1 = wx.StaticText( self, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_slider_1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText_slider_1, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( fgSizer1, 0, 0, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Warp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_slider2 = wx.Slider( self, wx.ID_ANY, 5, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer2.Add( self.m_slider2, 0, wx.ALL, 5 )
		
		self.m_staticText_slider_2 = wx.StaticText( self, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_slider_2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_slider_2, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( fgSizer2, 0, 0, 5 )
		
		
		gSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Post processing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Choose filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		m_choice1Choices = [ u"None", u"Sharpen", u"Blur", u"Smooth", u"Smooth_more", u"Detail", u"Edge_enhance" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer4.Add( self.m_choice1, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Width:\nResize morphed images to certain width in pixels (aspect ratio is maintained). \nLeave blank if you don't want a particular width.\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer4.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_textCtrl_width = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl_width, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Generate morphs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Generate!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( fgSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Total nr of morphs:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer3.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( fgSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		bSizer2.Add( self.m_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_dirPicker_in_1.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_dir_in_1_changed )
		self.m_dirPicker_in_2.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_dir_in_2_changed )
		self.m_slider1.Bind( wx.EVT_SCROLL_CHANGED, self.slider_1_on_scroll_changed )
		self.m_slider2.Bind( wx.EVT_SCROLL_CHANGED, self.slider_2_on_scroll_changed )
		self.m_button1.Bind( wx.EVT_BUTTON, self.on_button_click_generate )
		self.m_button2.Bind( wx.EVT_BUTTON, self.on_button_click_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_dir_in_1_changed( self, event ):
		event.Skip()
	
	def on_dir_in_2_changed( self, event ):
		event.Skip()
	
	def slider_1_on_scroll_changed( self, event ):
		event.Skip()
	
	def slider_2_on_scroll_changed( self, event ):
		event.Skip()
	
	def on_button_click_generate( self, event ):
		event.Skip()
	
	def on_button_click_cancel( self, event ):
		event.Skip()
	

