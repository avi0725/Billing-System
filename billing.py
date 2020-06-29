from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        bg_color = "#074463"
        title = Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        F1 = LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F1.place(x=0,y=80,relwidth=1)
        #---------Variables-------------------
        #---------Burger Variables
        self.atb = IntVar()
        self.ab = IntVar()
        self.cb = IntVar()
        self.vjb = IntVar()
        self.pb = IntVar()
        self.kb = IntVar()

        # ---------Maggi Variables
        self.sm = IntVar()
        self.vtm = IntVar()
        self.cm = IntVar()
        self.am = IntVar()
        self.crnm = IntVar()
        self.tm = IntVar()

        # ---------Mojito Variables
        self.gam = IntVar()
        self.bcm = IntVar()
        self.vm = IntVar()
        self.wmm = IntVar()
        self.mpm = IntVar()
        self.kbm = IntVar()

        # ---------Total Price Variables
        self.tbp = StringVar()
        self.tmp = StringVar()
        self.tmhp = StringVar()

        # ---------Tax Variables
        self.gst = StringVar()
        self.sgst = StringVar()
        self.cgst = StringVar()

        #------------------Customer Detail Variables

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_bill = StringVar()
        x = random.randint(1, 10000000)
        self.c_bill.set(str(x))

        self.search_bill = StringVar()

        #------Customer Details------------

        c_name_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        c_name_text = Entry(F1,width=15,bd=7,relief=SUNKEN,font=("arial",15),textvariable=self.c_name).grid(row=0,column=1,pady=5,padx=10)

        c_phone_lbl = Label(F1, text="Phone Number", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        c_phone_text = Entry(F1, width=15, bd=7, textvariable=self.c_phone,relief=SUNKEN, font=("arial", 15)).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_text = Entry(F1, width=15, bd=7,textvariable=self.search_bill, relief=SUNKEN, font=("arial", 15)).grid(row=0, column=5 , pady=5, padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font=("arial 12 bold")).grid(row=0,column=6,pady=10,padx=15)

        #-----------Burgers--------------

        F2 = LabelFrame(self.root, text="Burgers", bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 15, "bold"))
        F2.place(x=5, y=180, width=325,height=380)

        atb_lbl = Label(F2,text="Aloo Tikki",font=("times new roman", 16, "bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        atb_text= Entry(F2,width=13,font=("times new roman", 16, "bold"),bd=5,relief=SUNKEN,textvariable=self.atb).grid(row=0,column=1,padx=10,pady=10)

        ab_lbl = Label(F2, text="Achari", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        ab_text = Entry(F2, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.ab).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)

        cb_lbl = Label(F2, text="Cheese", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        cb_text = Entry(F2, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.cb).grid(row=2, column=1,
                                                                                                       padx=10, pady=10)

        vjb_lbl = Label(F2, text="Veg Jumbo", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        vjb_text = Entry(F2, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.vjb).grid(row=3, column=1,
                                                                                                      padx=10, pady=10)

        pb_lbl = Label(F2, text="Paneer", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        pb_text = Entry(F2, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.pb).grid(row=4, column=1,
                                                                                                       padx=10, pady=10)

        kb_lbl = Label(F2, text="King", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        kb_text = Entry(F2, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.kb).grid(row=5, column=1,
                                                                                                      padx=10, pady=10)

        # -----------Maggi--------------

        F3 = LabelFrame(self.root, text="Maggi", bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 15, "bold"))
        F3.place(x=330, y=180, width=325, height=380)

        sm_lbl = Label(F3, text="Simple", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        sm_text = Entry(F3, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.sm).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        vtm_lbl = Label(F3, text="Veg Tadka", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        vtm_text = Entry(F3, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.vtm).grid(row=1, column=1,
                                                                                                      padx=10, pady=10)

        cm_lbl = Label(F3, text="Cheese", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        cm_text = Entry(F3, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.cm).grid(row=2, column=1,
                                                                                                      padx=10, pady=10)

        am_lbl = Label(F3, text="Achari", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        am_text = Entry(F3, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.am).grid(row=3, column=1,
                                                                                                       padx=10, pady=10)

        crnm_lbl = Label(F3, text="Corn", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        crnm_text = Entry(F3, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.crnm).grid(row=4, column=1,
                                                                                                      padx=10, pady=10)

        tm_lbl = Label(F3, text="Tandoori", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        tm_text = Entry(F3, width=13, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.tm).grid(row=5, column=1,
                                                                                                      padx=10, pady=10)

        # -----------Mojito --------------

        F4 = LabelFrame(self.root, text="Mojito", bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 15, "bold"))
        F4.place(x=655, y=180, width=325, height=380)

        gam_lbl = Label(F4, text="Green Apple", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        gam_text = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.gam).grid(row=0, column=1,
                                                                                                      padx=10, pady=10)

        bcm_lbl = Label(F4, text="Blue Curacao", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        bcm_text = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.bcm).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)

        vm_lbl = Label(F4, text="Virgin", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        vm_text = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.vm).grid(row=2, column=1,
                                                                                                      padx=10, pady=10)

        wmm_lbl = Label(F4, text="Water Melon", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        wmm_text = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.wmm).grid(row=3, column=1,
                                                                                                      padx=10, pady=10)

        mpm_lbl = Label(F4, text="Mango Punch", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        mpm_text = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.mpm).grid(row=4, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)

        kbm_lbl = Label(F4, text="Kya Bear", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        kbm_text = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN,textvariable=self.kbm).grid(row=5, column=1,
                                                                                                      padx=10, pady=10)


        #----------------Bill Area---------------------------

        F5 = Frame(self.root, bd=10, relief=GROOVE, bg="white")
        F5.place(x=980, y=180, width=382, height=380)

        bill_title=Label(F5,text="BILL AREA",font=("arial", 15," bold"),relief=GROOVE,bd=7).pack(fill=X)

        scrol_y=Scrollbar(F5,orient=VERTICAL)

        self.textarea=Text(F5,yscrollcommand=scrol_y.set)

        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #-----Button Frame--------------

        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 15, "bold"))
        F6.place(x=5, y=560, relwidth=1, height=180)

        tbp_lbl=Label(F6,text="Total Burger Price",font=("times new roman " ,14 ,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")

        tbp_txt=Entry(F6, width=18, font=("arial", 10, "bold"), bd=7, relief=SUNKEN,textvariable=self.tbp).grid(row=0, column=1,
                                                                                                      padx=10,pady=5)

        tmp_lbl = Label(F6, text="Total Maggi Price", font=("times new roman ", 14, "bold"), bg=bg_color,
                        fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")

        tmp_txt = Entry(F6, width=18, font=("arial", 10, "bold"), bd=7, relief=SUNKEN,textvariable=self.tmp).grid(row=1, column=1,
                                                                                            padx=10, pady=5)

        tmhp_lbl = Label(F6, text="Total Mojito Price", font=("times new roman ", 14, "bold"), bg=bg_color,
                        fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")

        tmhp_txt = Entry(F6, width=18, font=("arial", 10, "bold"), bd=7, relief=SUNKEN,textvariable=self.tmhp).grid(row=2, column=1,
                                                                                            padx=10, pady=5)



        gst_lbl = Label(F6, text="Total GST ", font=("times new roman ", 14, "bold"), bg=bg_color,
                        fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")

        gst_txt = Entry(F6, width=18, font=("arial", 10, "bold"), bd=7, relief=SUNKEN,textvariable=self.gst).grid(row=0, column=3,
                                                                                            padx=10, pady=1)

        sgst_lbl = Label(F6, text="Total SGST ", font=("times new roman ", 14, "bold"), bg=bg_color,
                        fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")

        sgst_txt = Entry(F6, width=18, font=("arial", 10, "bold"), bd=7, relief=SUNKEN,textvariable=self.sgst).grid(row=1, column=3,
                                                                                            padx=10, pady=1)

        cgst_lbl = Label(F6, text="Total CGST ", font=("times new roman ", 14, "bold"), bg=bg_color,
                        fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="w")

        cgst_txt = Entry(F6, width=18, font=("arial", 10, "bold"), bd=7, relief=SUNKEN,textvariable=self.cgst).grid(row=2, column=3,
                                                                                            padx=10, pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=590,height=140)

        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=9,font=("arial",15,"bold"),bd=3).grid(row=0,column=0,padx=5,pady=5)

        gb_btn = Button(btn_F, text="Generate Bill", command=self.bill_area,bg="cadetblue", fg="white", pady=15, width=11,
                           font=("arial", 15, "bold"), bd=3).grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15, width=9,
                           font=("arial", 15, "bold"), bd=3).grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_F, text="Exit",command=self.Exit_app, bg="cadetblue", fg="white", pady=15, width=9,
                           font=("arial", 15, "bold"), bd=3).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.total_burger_price= float(
            (self.atb.get()*58)+
            (self.ab.get() * 69) +
            (self.cb.get() * 79) +
            (self.vjb.get() * 79) +
            (self.pb.get() * 109) +
            (self.kb.get() * 149)
        )


        self.tbp.set("Rs "+str(self.total_burger_price))
        self.total_maggi_price = float(
                (self.sm.get() * 99) +
                (self.vtm.get() * 119) +
                (self.cm.get() * 119) +
                (self.am.get() * 119) +
                (self.crnm.get() * 119) +
                (self.tm.get() * 119)
        )


        self.tmp.set("Rs "+str(self.total_maggi_price))
        self.total_mojito_price =float (
                (self.gam.get() * 99) +
                (self.bcm.get() * 99) +
                (self.vm.get() * 99) +
                (self.wmm.get() * 99) +
                (self.mpm.get() * 99) +
                (self.kbm.get() * 99)
        )
        self.tmhp.set("Rs "+str(self.total_mojito_price))
        self.total_gst=round((self.total_mojito_price+self.total_maggi_price+self.total_burger_price)*0.18,2)
        self.gst.set("Rs "+str(self.total_gst))
        self.total_sgst=round((self.total_mojito_price + self.total_maggi_price + self.total_burger_price)*0.09,2)
        self.sgst.set("Rs "+str(self.total_sgst))
        self.total_cgst=round((self.total_mojito_price + self.total_maggi_price + self.total_burger_price)*0.09,2)
        self.cgst.set("Rs "+str(self.total_cgst))

        self.total_bill=float(
            self.total_burger_price+
            self.total_maggi_price+
            self.total_mojito_price+
            self.total_gst
        )
        self.total_bill=round(self.total_bill,2)



    def welcome_bill(self):
        self.textarea.delete('1.0',END)

        self.textarea.insert(END,"\t\tSpicy Saga\n")
        self.textarea.insert(END, f"\nBill Number : {self.c_bill.get()}")
        self.textarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\nPhone Number : {self.c_phone.get()}")

        self.textarea.insert(END, f"\n==========================================")
        self.textarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n==========================================")




    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Please fill the Customer Details")
        elif self.tbp.get()=="Rs 0.0" and self.tmp.get()=="Rs 0.0" and self.tmhp.get()=="Rs 0.0":
            messagebox.showerror("Error", "Please select items ")

        self.welcome_bill()
        if self.atb.get()!=0:
            self.textarea.insert(END, f"\nAloo Tikki Burger\t\t{self.atb.get()}\t\t{self.atb.get()*58}")
        if self.ab.get()!=0:
            self.textarea.insert(END, f"\nAchari Burger\t\t{self.ab.get()}\t\t{self.ab.get()*69}")
        if self.cb.get()!=0:
            self.textarea.insert(END, f"\nCheese Burger\t\t{self.cb.get()}\t\t{self.cb.get()*79}")
        if self.vjb.get()!=0:
            self.textarea.insert(END, f"\nVeg Jambo Burger\t\t{self.vjb.get()}\t\t{self.vjb.get()*79}")
        if self.pb.get()!=0:
            self.textarea.insert(END, f"\nPanner Burger\t\t{self.pb.get()}\t\t{self.pb.get()*109}")
        if self.kb.get()!=0:
            self.textarea.insert(END, f"\nKing Burger\t\t{self.kb.get()}\t\t{self.kb.get()*149}")


        if self.sm.get()!=0:
            self.textarea.insert(END, f"\nSimple Maggi\t\t{self.sm.get()}\t\t{self.sm.get()*99}")
        if self.vtm.get()!=0:
            self.textarea.insert(END, f"\nVeg Tadka Maggi\t\t{self.vtm.get()}\t\t{self.vtm.get()*119}")
        if self.cm.get()!=0:
            self.textarea.insert(END, f"\nCheese Maggi\t\t{self.cm.get()}\t\t{self.cm.get()*119}")
        if self.am.get()!=0:
            self.textarea.insert(END, f"\nAchari Maggi\t\t{self.am.get()}\t\t{self.am.get()*119}")
        if self.crnm.get()!=0:
            self.textarea.insert(END, f"\nCorn Maggi\t\t{self.crnm.get()}\t\t{self.crnm.get()*119}")
        if self.tm.get()!=0:
            self.textarea.insert(END, f"\nTandoori Maggi\t\t{self.tm.get()}\t\t{self.tm.get()*119}")


        if self.gam.get()!=0:
            self.textarea.insert(END, f"\nGreen Apple Mojito\t\t{self.gam.get()}\t\t{self.gam.get()*99}")
        if self.bcm.get()!=0:
            self.textarea.insert(END, f"\nBlue Curacao Mojito\t\t{self.bcm.get()}\t\t{self.bcm.get()*99}")
        if self.vm.get()!=0:
            self.textarea.insert(END, f"\nVirgin Mojito\t\t{self.vm.get()}\t\t{self.vm.get()*99}")
        if self.wmm.get()!=0:
            self.textarea.insert(END, f"\nWatermelon Mojito\t\t{self.wmm.get()}\t\t{self.wmm.get()*99}")
        if self.mpm.get()!=0:
            self.textarea.insert(END, f"\nMango Punch\t\t{self.mpm.get()}\t\t{self.mpm.get()*99}")
        if self.kbm.get()!=0:
            self.textarea.insert(END, f"\nKya Bear\t\t{self.kbm.get()}\t\t{self.kbm.get()*99}")

        self.textarea.insert(END, f"\n----------------------------------------")
        if self.gst.get()!="Rs 0.0":
            self.textarea.insert(END, f"\nGST :\t\t\t\t{self.gst.get()}")
        if self.sgst.get() != "Rs 0.0":
            self.textarea.insert(END, f"\nSGST :\t\t\t\t{self.sgst.get()}")
        if self.cgst.get() != "Rs 0.0":
            self.textarea.insert(END, f"\nCGST :\t\t\t\t{self.cgst.get()}")
        self.textarea.insert(END, f"\nTotal Amount :\t\t\t Rs {str(self.total_bill)}")
        self.textarea.insert(END, f"\n----------------------------------------")
        self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill ?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.c_bill.get())+'.txt',"w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Done",f"Bill:{self.c_bill.get()} saved Successfully")
        else:
            return
    def find_bill(self):
        present="no"

        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"

        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to Clear Data?")
        if op > 0:
            self.atb.set(0)
            self.ab.set(0)
            self.cb.set(0)
            self.vjb.set(0)
            self.pb.set(0)
            self.kb.set(0)

            # ---------Maggi Variables
            self.sm.set(0)
            self.vtm.set(0)
            self.cm.set(0)
            self.am.set(0)
            self.crnm.set(0)
            self.tm.set(0)

            # ---------Mojito Variables
            self.gam.set(0)
            self.bcm.set(0)
            self.vm.set(0)
            self.wmm.set(0)
            self.mpm.set(0)
            self.kbm.set(0)

            # ---------Total Price Variables
            self.tbp.set('')
            self.tmp.set('')
            self.tmhp.set('')

            # ---------Tax Variables
            self.gst.set('')
            self.sgst.set('')
            self.cgst.set('')

            # ------------------Customer Detail Variables

            self.c_name.set('')
            self.c_phone.set('')
            self.c_bill.set('')
            x = random.randint(1, 10000000)
            self.c_bill.set(str(x))

            self.search_bill.set('')
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to Exit?")
        if op>0:
            self.root.destroy()




























root = Tk()
obj = Bill_App(root)
root.mainloop()
