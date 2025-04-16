#Getting Input with the Entry Widget(Convertign kilometers to miles)
import tkinter as tk
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Kilometer Converter")
        
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        
        self.prompt_label = tk.Label(self.top_frame, text = 'Enter a distance in kilometers:', font = ('Arial',20))
        self.kilo_entry = tk.Entry(self.top_frame, width = 30, font =('Arial', 20))
        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')
        
        self.calc_button = tk.Button(self.bottom_frame, text='Convert', width=10, font=('Arial',20), command = self.convert)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', width=10, font=('Arial', 20), command = self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.bottom_frame.place(relx=0.5, rely=0.65, anchor='center')
        
        tkinter.mainloop()
        
    def convert(self):
        try:
            kilo = float(self.kilo_entry.get())
        except ValueError:
            tkinter.messagebox.showerror("Error",'Invalid input.Please enter a number.')
            return
    
        miles = kilo * 0.6214
        tkinter.messagebox.showinfo('Results',f'{kilo} kilometers is equal to {miles:.2f}.')
        
if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()
        