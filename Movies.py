from ast import Delete, Nonlocal, main
from ctypes import alignment
import tkinter as tk
from tkinter import Label, ttk
from tkinter import ttk
from tkinter import CENTER, END, Toplevel, messagebox
import re
import csv

movies = []

class MovieManagement:
    def delete_movie(self):

        def searchanddel():
            a = e1.get()
            index = -1
            for i in range(len(movies)):
                if(movies[i][0].casefold() == a.casefold()):
                    index = i
                    movies.pop(index)
                    messagebox.showinfo("Success", "Movie Successfully Deleted.")
            if(index == -1):
                messagebox.showerror("failure", "No such movie exists, please check the spelling of the movie in the database or retry with another movie")
        if(len(movies) == 0):   
            messagebox.showerror("Failure", "Please enter a movie before trying to delete any!")
            return None
        deletem = tk.Toplevel(root)
        deletem.title("Delete a Movie")
        width = deletem.winfo_screenwidth()
        height = deletem.winfo_screenheight()
        deletem.geometry("%dx%d" % (width, height))
        deletem.configure(bg = "#F1E4F3")
        l1 = tk.Label(deletem, text = "Movie to be Deleted: ", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        e1 = tk.Entry(deletem, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge")
        b1 = tk.Button(deletem, text = "Enter", bg = "#F686BD", fg = "black", font = ("garamond", 18), activeforeground = "white", activebackground = "#FE5D9F", width = 10 ,height = 2, command = searchanddel)
        l1.place(x = 300, y = 250)
        e1.place(x = 550, y = 250)
        b1.place(x = 570, y = 350)
        deletem.protocol("WM_DELETE_WINDOW", self.close_all_windows)

    def update_movie(self):
        global index 
        global index1
        
        index1 = -1
        def searchandup():
            index = -1
            a = e1.get()
            for i in range(len(movies)):
                if(movies[i][0].casefold() == a.casefold()):
                    index = i
                    l2.place(x = 200, y = 250)
                    e2.place(x = 450, y = 250)
                    b2.place(x = 950, y = 240)
            if(index == -1):
                messagebox.showerror("Failure", "No such movie exists, please check the spelling of the movie in the database or retry with another movie")

        def insert(event):
            def consolidate():
                b = e3.get()
                movies[index][index1] = b 
                messagebox.showinfo("Success", "Entry Updated!")
            a = selecteddata.get()
            l4 = tk.Label(updatem, text = "Enter the Updated Value:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
            l3 = tk.Label(updatem, text = (a+":"), font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
            e3 = tk.Entry(updatem, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge")
            b3 = tk.Button(updatem, text = "Enter", bg = "#F686BD", fg = "black", font = ("garamond", 18), activeforeground = "white", activebackground = "#FE5D9F", width = 10 ,height = 1, command = consolidate)
            if(a == "Name of the Movie"):
                index1 = 0
            elif(a == "Name of the Director"):
                index1 = 1
            elif(a == "Production House"):
                index1 = 2
            elif(a == "Gross Income"):
                index1 = 3
            elif(a == "IMDb Rating"):
                index1 = 4
            elif(a == "Protagonist 1"):
                index1 = 5
            elif(a == "Protagonist 2"):
                index1 = 6
            elif(a == "Duration"):
                index1 = 7
            elif(a == "Genre"):
                index1 = 8
            elif(a == "Year of Release"):
                index1 = 9
            l4.place(x = 550, y = 350)
            l3.place(x = 200, y = 450)
            e3.place(x = 450, y = 450)
            b3.place(x = 950, y = 440)

        if(len(movies) == 0):   
            messagebox.showerror("Failure", "Please enter a movie before trying to update it!")
            return None
        updatem = tk.Toplevel(root)
        updatem.title("Update a Movie")
        width = updatem.winfo_screenwidth()
        height = updatem.winfo_screenheight()
        updatem.geometry("%dx%d" % (width, height))
        updatem.configure(bg = "#F1E4F3")
        l1 = tk.Label(updatem, text = "Movie to be Updated: ", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        e1 = tk.Entry(updatem, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge")
        b1 = tk.Button(updatem, text = "Enter", bg = "#F686BD", fg = "black", font = ("garamond", 18), activeforeground = "white", activebackground = "#FE5D9F", width = 10 ,height = 1, command = searchandup)
        l2 = tk.Label(updatem, text = "Field to be updated: ", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        data = ["Name of the Movie", "Name of the Director", "Production House", "Gross Income", "IMDb Rating", "Protagonist 1", "Protagonist 2", "Duration", "Genre", "Year of Release"]
        selecteddata = tk.StringVar()
        e2 = ttk.Combobox(updatem, width = 40, font = ("garamond", 16), values = data, textvariable = selecteddata, state = "readonly")
        e2.bind("<<ComboboxSelected>>", insert)
        b2 = tk.Button(updatem, text = "Choose", bg = "#F686BD", fg = "black", font = ("garamond", 18), activeforeground = "white", activebackground = "#FE5D9F", width = 10 ,height = 1)
        l1.place(x = 200, y = 150)
        e1.place(x = 450, y = 150)
        b1.place(x = 950, y = 140)
        l2.place_forget()
        e2.place_forget()
        b2.place_forget()
        updatem.protocol("WM_DELETE_WINDOW", self.close_all_windows)

    def display_movie(self):
        if(len(movies) == 0):   
            messagebox.showerror("Failure", "Please enter a movie before trying to display!")
            return None
        display = tk.Toplevel(root)
        display.title("Movie Display")
        width = display.winfo_screenwidth()
        height = display.winfo_screenheight()
        display.geometry("%dx%d" % (width, height))
        style = ttk.Style()
        style.configure("Treeview", background="#F1E4F3")
        table = ttk.Treeview(display, selectmode="browse", style = "Treeview")
        table["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        table["show"] = "headings"
        table.column("1", width = 200, anchor="center")
        table.column("2", width = 200, anchor="center") 
        table.column("3", width = 200, anchor="center")
        table.column("4", width = 120, anchor="center")
        table.column("5", width = 120, anchor="center")
        table.column("6", width = 200, anchor="center")
        table.column("7", width = 200, anchor="center")
        table.column("8", width = 200, anchor="center")
        table.column("9", width = 100, anchor="center")
        table.column("10", width = 100, anchor="center")
        table.heading("#1", text = "Name of the Movie")
        table.heading("#2", text = "Director Name")
        table.heading("#3", text = "Production House")
        table.heading("#4", text = "Gross Income")
        table.heading("#5", text = "IMDb Rating")
        table.heading("#6", text = "Protagonist 1")
        table.heading("#7", text = "Protagonist 2")
        table.heading("#8", text = "Duration")
        table.heading("#9", text = "Genre")
        table.heading("#10", text = "Year of Release")

        hrscrbar = tk.Scrollbar(display, orient="horizontal", command=table.xview)
        hrscrbar.pack(side="bottom", fill="x")
        table.configure(xscrollcommand=hrscrbar.set)  # Use xscrollcommand for horizontal scrollbar

        # Adjust your columns and headings here

        for i in range(len(movies)):
            table.insert("", "end", values=movies[i])
    
        # Place the table within the window
        table.pack(fill="both", expand=True)

        display.protocol("WM_DELETE_WINDOW", self.close_all_windows)

    def close_all_windows(self):
        root.quit()

    def insert_movie(self):

        #name of the movie functions
        def check_name(P):
            #name = namee.get()
            name_pattern = r"^(?![\s.]+$)[\w\s.'\",!?&()/-]{2,}(?<![\s.])$"
            if(re.match(name_pattern, P)):
                namee.configure(fg = "green")
                errorname.place_forget()
                return 1
            else:
                namee.configure(fg = "red")
                errorname.place(x = 1000, y = 25)
                return 0
        def on_focus_in_name(event):
            namee.configure(fg = 'black')
            errorname.place_forget()

        #name of the director functions
        def check_dir(P):
            #name = directore.get()
            name_pattern = r"^(?![\s.'-]*$)(?!.*[\s.'-]{2})[A-Z][A-Za-z\s.'-]*$"
            if(re.match(name_pattern, P)):
                directore.configure(fg = "green")
                errordir.place_forget()
                return 1
            else:
                directore.configure(fg = "red")
                errordir.place(x = 1000, y = 80)
                return 0
        def on_focus_in_dir(event):
            directore.configure(fg = "black")
            errordir.place_forget()

        #name of the production house functions
        def check_pro(P):
            #name = productione.get()
            name_pattern = r"^(?![\s.'-]*$)[\w\s.'-]{2,}$"
            if(re.match(name_pattern, P)):
                productione.configure(fg = "green")
                errorpro.place_forget()
                return 1
            else:
                productione.configure(fg = "red")
                errorpro.place(x = 1000, y = 135)
                return 0
        def on_focus_in_pro(event):
            productione.configure(fg = "black")
            errorpro.place_forget()

        #year of release functions
        def check_year(P):
            #name = yeare.get()
            name_pattern = r"\b(?:19\d\d|20(?:[0-2]\d|3[0-3]))\b"
            if(re.match(name_pattern, P)):
                yeare.configure(fg = "green")
                erroryear.place_forget()
                return 1
            else:
                yeare.configure(fg = "red")
                erroryear.place(x = 1000, y = 190)
                return 0
        def on_focus_in_year(event):
            yeare.configure(fg = "black")
            erroryear.place_forget()

        #income functions
        def check_income(P):
            #name =  incomee.get()
            name_pattern = r"^(\$)?(\d{1,3}(,\d{3})*(\.\d{1,2})?|\.\d{1,2})$"
            if(re.match(name_pattern, P)):
                incomee.configure(fg = "green")
                errorincome.place_forget()
                return 1
            else:
                incomee.configure(fg = "red")
                errorincome.place(x = 1000, y = 245)
                return 0
        def on_focus_in_income(event):
            incomee.configure(fg = "black")
            errorincome.place_forget()

        #genre functions
        def check_genre(P):
            #name = genree.get()
            name_pattern = r"^(?!.*\s{2})[A-Za-z0-9\s\-&',.()!$]+$"
            if(re.match(name_pattern, P)):
                genree.configure(fg = "green")
                errorgenre.place_forget()
                return 1
            else:
                genree.configure(fg = "red")
                errorgenre.place(x = 1000, y = 300)
                return 0
        def on_focus_in_genre(event):
            genree.configure(fg = "black")
            errorgenre.place_forget()

        #imdb functions
        def check_imdb(P):
            #name = imdbe.get()
            name_pattern = r"^\d+(\.\d+)?$"
            if(re.match(name_pattern, P)):
                imdbe.configure(fg = "green")
                errorimdb.place_forget()
                return 1
            else: 
                imdbe.configure(fg = "red")
                errorimdb.place(x = 1000, y = 355)
                return 0
        def on_focus_in_imdb(event):
            imdbe.configure(fg = "black")
            errorimdb.place_forget()

        #protagonist 1 functions
        def check_protagonist1(P):
            #name = protagonist1e.get()
            name_pattern = r"^(?![\s.'-]*$)(?!.*[\s.'-]{2})[A-Z][A-Za-z\s.'-]*$"
            if(re.match(name_pattern, P)):
                protagonist1e.configure(fg = "green")
                errorpro1.place_forget()
                return 1
            else:
                protagonist1e.configure(fg = "red")
                errorpro1.place(x = 1000, y = 410)
                return 0
        def on_focus_in_pr1(event):
            protagonist1e.configure(fg = "black")
            errorpro1.place_forget()

        #protagonist 2 functions
        def check_protagonist2(P):
            #name = protagonist2e.get()
            name_pattern = r"^(?![\s.'-]*$)(?!.*[\s.'-]{2})[A-Z][A-Za-z\s.'-]*$"
            if(re.match(name_pattern, P)):
                protagonist2e.configure(fg = "green")
                errorpro2.place_forget()
                return 1
            else:
                protagonist2e.configure(fg = "red")
                errorpro2.place(x = 1000, y = 465)
                return 0
        def on_focus_in_pr2(event):
            protagonist2e.configure(fg = "black")
            errorpro2.place_forget()

        #duration functions
        def check_duration(P):
            #name = duratione.get()
            name_pattern = r"(\d+)\s*hours?\s*(\d*)\s*minutes?"
            if(re.match(name_pattern, P)):
                duratione.configure(fg = "green")
                errordur.place_forget()
                return 1
            else:
                duratione.configure(fg = "red")
                errordur.place(x = 1000, y = 520)
                return 0
        def on_focus_in_dur(event):
            duratione.configure(fg = "black")
            errordur.place_forget()

        def check_form(self):
            a = check_name(namee.get())
            b = check_dir(directore.get())
            c = check_pro(productione.get())
            d = check_income(incomee.get())
            e = check_imdb(imdbe.get())
            f = check_protagonist1(protagonist1e.get())
            g = check_protagonist2(protagonist2e.get())
            h = check_duration(duratione.get())
            i = check_genre(genree.get())
            j = check_year(yeare.get())
            num = a+b+c+d+e+f+g+h+i+j
            if(num == 10):
                movie = [namee.get(), directore.get(), productione.get(), incomee.get(), imdbe.get(), protagonist1e.get(), protagonist2e.get(), duratione.get(), genree.get(), yeare.get()]
                movies.append(movie)
                messagebox.showinfo("Success", "Movie Added Successfully.")
            else:
                messagebox.showerror("Failure", "Some Invalid Input was give, please check and re-enter.")

        insert = tk.Toplevel(root)
        insert.title("Movie Insertion")
        width = insert.winfo_screenwidth()
        height = insert.winfo_screenheight()
        insert.geometry("%dx%d" % (width, height))
        insert.configure(bg = "#F1E4F3")

        #name of the movie
        namel = tk.Label(insert, text = "Name of the Movie:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        namee = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        namee["validatecommand"] = (namee.register(check_name), '%P')
        namel.place(x = 270, y = 25)
        namee.place(x = 580, y = 25)
        namee.bind("<FocusIn>", on_focus_in_name)
        errorname = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        errorname.place_forget()

        #name of the director
        directorl = tk.Label(insert, text = "Name of the Director:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        directore = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        directore["validatecommand"] = (directore.register(check_dir), '%P')
        directorl.place(x = 270, y = 80)
        directore.place(x = 580, y = 80)
        directore.bind("<FocusIn>", on_focus_in_dir)
        errordir = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        errordir.place_forget()
    
        #name of the producer
        productionl = tk.Label(insert, text = "Name of the Production House:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        productione = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        productione["validatecommand"] = (productione.register(check_pro), '%P')
        productionl.place(x = 270, y = 135)
        productione.place(x = 580, y = 135)
        productione.bind("<FocusIn>", on_focus_in_pro)
        errorpro = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        errorpro.place_forget()
    
        #year of release
        yearl = tk.Label(insert, text = "Year of Release:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        yeare = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        yeare["validatecommand"] = (yeare.register(check_year), '%P')
        yearl.place(x = 270, y = 190)
        yeare.place(x = 580, y = 190)
        yeare.bind("<FocusIn>", on_focus_in_year)
        erroryear = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        erroryear.place_forget()
    
        #gross income
        incomel = tk.Label(insert, text = "Gross Income:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        incomee = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        incomee["validatecommand"] = (incomee.register(check_income),"%P")
        incomel.place(x = 270, y = 245)
        incomee.place(x = 580, y = 245)
        incomee.bind("<FocusIn>", on_focus_in_income)
        errorincome = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        errorincome.place_forget()
    
        #genre of the movie
        genrel = tk.Label(insert, text = "Genre:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        genree = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        genree["validatecommand"] = (genree.register(check_genre), "%P")
        genrel.place(x = 270, y = 300)
        genree.place(x = 580, y = 300)
        genree.bind("<FocusIn>", on_focus_in_genre)
        errorgenre = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        errorgenre.place_forget()
    
        #imdb rating of the movie
        imdbl = tk.Label(insert, text = "IMDb Rating:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        imdbe = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        imdbe["validatecommand"] = (imdbe.register(check_imdb), "%P")
        imdbl.place(x = 270, y = 355)
        imdbe.place(x = 580, y = 355)
        imdbe.bind("<FocusIn>", on_focus_in_imdb)
        errorimdb = tk.Label(insert,text = "Invalid Input", fg = "red", bg = "#F1E4F3",font = ("garamond", 18))
        errorimdb.place_forget()
    
        #Protagonist 1
        protagonist1l = tk.Label(insert, text = "Protagonist 1:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        protagonist1e = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        protagonist1e["validatecommand"] = (protagonist1e.register(check_protagonist1), "%P")
        protagonist1l.place(x = 270, y = 410)
        protagonist1e.place(x = 580, y = 410)
        protagonist1e.bind("<FocusIn>", on_focus_in_pr1)
        errorpro1 = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        errorpro1.place_forget()
    
        #Protagonist 2
        protagonist2l = tk.Label(insert, text = "Protagonist 2:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        protagonist2e = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        protagonist2e["validatecommand"] = (protagonist2e.register(check_protagonist2), "%P")
        protagonist2l.place(x = 270, y = 465)
        protagonist2e.place(x = 580, y = 465)
        protagonist2e.bind("<FocusIn>", on_focus_in_pr2)
        errorpro2 = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        errorpro2.place_forget()
    
        #duration of the movie
        durationl = tk.Label(insert, text = "Duration of the Movie:", font = ("garamond", 18), fg = "black", bg = "#F1E4F3")
        duratione = tk.Entry(insert, width = 40, font = ("garamond", 16), bd = 2, bg = "#D6D2D2", fg = "black", relief = "ridge", validate = "focusout")
        duratione["validatecommand"] = (duratione.register(check_duration), "%P")
        durationl.place(x = 270, y = 520)
        duratione.place(x = 580, y = 520)
        duratione.bind("<FocusIn>", on_focus_in_dur)
        errordur = tk.Label(insert, text = "Invalid Input", fg = "red", bg = "#F1E4F3", font = ("garamond", 18))
        errordur.place_forget()
    
        #submit button
        b1 = tk.Button(insert, text = "Submit", bg = "#F686BD", fg = "black", font = ("garamond", 18), activeforeground = "white", activebackground = "#FE5D9F", width = 10 ,height = 2)
        b1.place(x = 590, y = 560)
        b1.bind("<Button-1>", check_form)
        insert.protocol("WM_DELETE_WINDOW", self.close_all_windows)

    def main(self):
        root.title("Movie Management System")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.configure(bg = "#F1E4F3")
        b1 = tk.Button(root, text = "Insert a new movie", command = self.insert_movie, bg = "#F686BD", fg = "black", font = ("garamond", 24, 'bold'), activeforeground = "white", activebackground = "#FE5D9F", width = 17 ,height = 3)
        b1.place(x = 500, y = 25)
        b2 = tk.Button(root, text = "Delete a movie", command = self.delete_movie, bg = "#F686BD", fg = "black", font = ("garamond", 24, 'bold'), activeforeground = "white", activebackground = "#FE5D9F", width = 17 ,height = 3)
        b2.place(x = 500, y = 175)
        b3 = tk.Button(root, text = "Update a movie", command = self.update_movie, bg = "#F686BD", fg = "black", font = ("garamond", 24, 'bold'), activeforeground = "white", activebackground = "#FE5D9F", width = 17 ,height = 3)
        b3.place(x = 500, y = 325)
        b4 = tk.Button(root, text = "Display all the movies", command = self.display_movie, bg = "#F686BD", fg = "black", font = ("garamond", 24, 'bold'), activeforeground = "white", activebackground = "#FE5D9F", width = 17 ,height = 3)
        b4.place(x = 500, y = 475)
        root.protocol("WM_DELETE_WINDOW", self.close_all_windows)
        root.mainloop()

if __name__ == "__main__":

    root = tk.Tk()
    app = MovieManagement()
    app.main()
