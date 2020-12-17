# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 13:42:23 2020

@author: nidhi
"""
import numpy as np
import pickle
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.button import Button
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty


Window.size=(400,600)


Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'main'
    MDLabel:
        text: 'Self Triage App'
        font_style: 'H2'
        pos_hint: {'center_x': 0.6, 'center_y': 0.9}
    MDTextField:
        id: input_1
        hint_text: 'Enter Age'
        helper_text: 'Enter numeric value from 1-110'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: True
    MDRaisedButton:
        id: input_2
        text: 'Male'
        pos_hint: {'center_x': 0.45, 'center_y': 0.7}
        width: 250
        on_press: self.text
    MDRaisedButton:
        id: input_3
        text: 'Female'
        width: 250
        pos_hint: {'center_x': 0.55, 'center_y': 0.7}
        on_press: self.text
    MDTextField:
        id: input_4
        hint_text: 'Type problem and choose department if applicable'
        helper_text: 'Mention why you want to visit the hospital'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: True
    MDRaisedButton:
        id: input_5
        text: 'Neuro'
        width: 100
        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
        on_press: self.text
    MDRaisedButton:
        id: input_5
        text: 'Nephro'
        width: 100
        pos_hint: {'center_x': 0.466, 'center_y': 0.6}
        on_press: self.text
    MDRaisedButton:
        id: input_5
        text: 'Eye'
        width: 100
        pos_hint: {'center_x': 0.533, 'center_y': 0.6}
        on_press: self.text
    MDRaisedButton:
        id: input_5
        text: 'Ear'
        width: 100
        pos_hint: {'center_x': 0.6, 'center_y': 0.6}
        on_press: self.text
    MDRaisedButton:
        id: input_5
        text: 'Gastro'
        width: 100
        pos_hint: {'center_x': 0.4, 'center_y': 0.55}
        on_press: self.text
    MDRaisedButton:
        id: input_5
        text: 'Cardio'
        width: 100
        pos_hint: {'center_x': 0.466, 'center_y': 0.55}
        on_press: self.text
    MDRaisedButton:
        id: input_5
        text: 'Resp'
        width: 100
        pos_hint: {'center_x': 0.533, 'center_y': 0.55}
        on_press: self.text
    MDRaisedButton:
        id: input_5
        text: 'Cannot Say'
        width: 100
        pos_hint: {'center_x': 0.6, 'center_y': 0.55}
        on_press: self.text
    MDTextField:
        id: input_6
        hint_text: 'Enter Pain on Scale (0-10)'
        helper_text: 'Enter level of Pain 0: No Pain, 10: Very Severe'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: True
    MDTextField:
        id: input_7
        hint_text: 'Enter Body Temp if available'
        helper_text: 'Enter Temp in Farenheit'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: False
    MDTextField:
        id: input_8
        hint_text: 'Enter Heart Rate if available'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: False
    MDTextField:
        id: input_9
        hint_text: 'Enter Resp Rate if available'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: False
    MDTextField:
        id: input_10
        hint_text: 'Enter Systolic BP if available'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: False
    MDTextField:
        id: input_11
        hint_text: 'Enter Diastolic BP if available'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: False
    MDTextField:
        id: input_12
        hint_text: 'Enter Sp02 if available'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        size_hint_x: None
        width: 500
        icon_right: "account-search"
        required: False
    MDRaisedButton:
        text: 'Predict'
        on_press: app.predict()
            
    MDLabel:
        pos_hint:  {'center_x': 0.5, 'center_y': 0.1}
        text: ''
        id: output_text


'''

class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))

class MainApp(MDApp):

    
    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        return self.help_string 


    def predict(self):
        result_age = self.help_string.get_screen('main').ids.input_1.text
        result_temp = self.help_string.get_screen('main').ids.input_7.text
        result_hr = self.help_string.get_screen('main').ids.input_8.text
        result_rr = self.help_string.get_screen('main').ids.input_9.text
        result_sbp= self.help_string.get_screen('main').ids.input_10.text
        result_dbp = self.help_string.get_screen('main').ids.input_11.text
        result_spo = self.help_string.get_screen('main').ids.input_12.text
        result_pain = self.help_string.get_screen('main').ids.input_6.text
        if self.help_string.get_screen('main').ids.input_7.text == '' :
            result_temp = 100
        if self.help_string.get_screen('main').ids.input_8.text == '' :
            result_hr = 80
        if self.help_string.get_screen('main').ids.input_9.text == '' :
            result_rr = 15
        if self.help_string.get_screen('main').ids.input_10.text == '' :
            result_sbp = 120
        if self.help_string.get_screen('main').ids.input_11.text == '' :
            result_dbp = 80 
        if self.help_string.get_screen('main').ids.input_12.text == '' :
            result_spo = 98
        if self.help_string.get_screen('main').ids.input_2.text == 'Male' :
            result_male = 1
            result_female = 0
        if self.help_string.get_screen('main').ids.input_3.text == 'Female' :
            result_male = 0
            result_female = 1
        if result_age:
            # self.log.AppendText("Nickname: " + dlg.result_problem+"\n")
            filename = 'finalized_model.sav'
            loaded_model = pickle.load(open(filename, 'rb'))
            li = [int(result_age),int(result_temp),int(result_hr),int(result_rr),int(result_sbp),int(result_dbp),int(result_spo),int(result_pain),1,1,1,1,2,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000000e+00,0.000000e+00,-4.440892e-16,-8.881784e-16,0.000000e+00,1.300000e+01,15.0,6.0000,7.0,result_male,result_female]
            u = np.array(li)
            u = np.reshape(u,(1,35))
            print(u.shape)
            y_pred = loaded_model.predict(u)
            a = np.argmax(y_pred,axis=1)
            if a==0:
                res = "hospital visit highly recommended"
            if a==1:
                res = "hospital visit highly recommended"
            if a==2:
                res = "hospital recommended"
            if a==3:
                res = "can visit hospital"
            self.help_string.get_screen('main').ids.output_text.text = res



MainApp().run()
