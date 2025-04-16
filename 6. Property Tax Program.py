import tkinter as tk

class PropertyTax:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Property Tax Program")
        self.main_window.geometry('300x100')
        
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.mid2_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.mid2_frame.pack()
        self.bottom_frame.pack()
        
        self.property_label = tk.Label(self.top_frame, text = 'Enter the property value:')
        self.property_entry = tk.Entry(self.top_frame, width = 15)
        self.property_label.pack(side = 'left')
        self.property_entry.pack(side = 'left')
        
        self.assessment_label = tk.Label(self.mid_frame, text = 'Assessment Value:')
        self.assessment_value = tk.StringVar()
        self.assessment_result = tk.Label(self.mid_frame, textvariable= self.assessment_value)
        self.assessment_label.pack(side='left')
        self.assessment_result.pack(side='left')
        
        self.property_tax_label = tk.Label(self.mid2_frame, text = 'Property Tax:')
        self.tax_value = tk.StringVar()
        self.property_tax_result = tk.Label(self.mid2_frame, textvariable= self.tax_value)
        self.property_tax_label.pack(side ='left')
        self.property_tax_result.pack(side = 'left')
        
        self.calc_btn = tk.Button(self.bottom_frame, text='Calculate', command = self.calculation)
        self.quit_btn = tk.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)
        self.calc_btn.pack(side = 'left')
        self.quit_btn.pack(side = 'left')
        
        tk.mainloop()
        
    def calculation(self):
        property_value_v = float(self.property_entry.get())
        assessment_value_v = property_value_v * 0.6
        property_tax_v = assessment_value_v * 0.0075
        
        self.assessment_value.set('$ '+str(assessment_value_v))
        self.tax_value.set('$ '+str(property_tax_v))
        
if __name__ == '__main__':
    propertyTax = PropertyTax()
        