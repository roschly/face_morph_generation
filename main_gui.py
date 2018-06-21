import wx
import os
from main_cli import main
import threading

import wx_layout as layout

class MainFrame(layout.MyFrame1):
    def __init__(self, parent):
        layout.MyFrame1.__init__(self, parent)
        self.cancel_morph_generation = False

    def slider_1_on_scroll_changed(self, event):
        self.m_staticText_slider_1.SetLabel( str(self.m_slider1.GetValue()/10) )

    def slider_2_on_scroll_changed(self, event):
        self.m_staticText_slider_2.SetLabel( str(self.m_slider2.GetValue()/10) )

    def callback(self, generated, total):
        if generated == -1 and total == -1: # morph generation cancelled confirmation
            self.m_gauge1.SetValue(0)
            self.m_staticText17.SetLabel( "..." )
        else:
            self.m_staticText17.SetLabel( str(total) )
            self.m_gauge1.SetValue( generated/total*100 )
            return self.cancel_morph_generation

    def on_button_click_cancel(self, event):
        self.cancel_morph_generation = True

    def on_button_click_generate(self, event):
        self.cancel_morph_generation = False

        INPUT_DIR = self.m_dirPicker_in_1.GetPath()
        INPUT_DIR_2 = self.m_dirPicker_in_2.GetPath()
        INPUT_DIR_2 = None if INPUT_DIR_2 == "" else INPUT_DIR_2
        OUTPUT_DIR = self.m_dirPicker_out.GetPath()

        full_image = self.m_radioBtn1.GetValue()
        face_swap_morph = self.m_radioBtn2.GetValue()
        MORPH_METHOD = "full_image" if full_image else "face_swap_morph"

        BLEND = self.m_slider1.GetValue() / 10
        WARP = self.m_slider2.GetValue() / 10

        FILTER = self.m_choice1.GetString( self.m_choice1.GetSelection() ).lower()

        width = self.m_textCtrl_width.GetValue()
        # ensure width is a positive int, otherwise set to -1 (which is ignored by method)
        try:
            width = int(width)
        except:
            width = -1
        if width > 0:
            MORPH_WIDTH = width
        else:
            MORPH_WIDTH = -1

        # start morph generation in thread, to keep UI responsive
        t = threading.Thread(target=main, args=(INPUT_DIR, INPUT_DIR_2, OUTPUT_DIR, BLEND, WARP, MORPH_METHOD, FILTER, MORPH_WIDTH), kwargs={'CALLBACK': self.callback} )
        t.daemon = True
        t.start()


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()
