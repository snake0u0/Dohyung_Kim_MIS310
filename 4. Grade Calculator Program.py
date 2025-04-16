#Grade Program
import tkinter as tk

class GradeProgram:
    def __init__(self):
        self.main_window = tk.Tk()
        
        self.frame_test1 = tk.Frame(self.main_window)
        self.frame_test2 = tk.Frame(self.main_window)
        self.frame_test3 = tk.Frame(self.main_window)
        self.frame_average = tk.Frame(self.main_window)
        self.frame_button = tk.Frame(self.main_window)        
        
        self.test1_label = tk.Label(self.frame_test1, text = "Enter the score for test 1:")
        self.test1_entry = tk.Entry(self.frame_test1, width =10)
        self.test1_label.pack(side = 'left')
        self.test1_entry.pack(side = 'left')
        
        self.test2_label = tk.Label(self.frame_test2, text = "Enter the score for test 2:")
        self.test2_entry = tk.Entry(self.frame_test2, width =10)
        self.test2_label.pack(side = 'left')
        self.test2_entry.pack(side = 'left')
        
        self.test3_label = tk.Label(self.frame_test3, text = "Enter the score for test 3:")
        self.test3_entry = tk.Entry(self.frame_test3, width =10)
        self.test3_label.pack(side = 'left')
        self.test3_entry.pack(side = 'left')
        
        self.average_label = tk.Label(self.frame_average, text = "Average")
        self.value = tk.StringVar()
        self.show_average_label = tk.Label(self.frame_average, textvariable = self.value)      
        self.average_label.pack(side = 'left')
        self.show_average_label.pack(side = 'left')
        
        self.btn_average = tk.Button(self.frame_button, text = "Average", command = self.average)
        self.btn_quit = tk.Button(self.frame_button, text = "Quit", command = self.main_window.destroy)
        self.btn_average.pack(side = "left")
        self.btn_quit.pack(side = "left")
        
        self.frame_test1.pack()
        self.frame_test2.pack()
        self.frame_test3.pack()
        self.frame_average.pack()
        self.frame_button.pack()
        
        self.main_window.mainloop()
        
    def average(self):
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())
        average = (test1 + test2 + test3) / 3
        
        self.value.set(average)
    
if __name__ == '__main__':
    grade_result = GradeProgram()