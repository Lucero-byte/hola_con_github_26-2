from tkinter import ttk
import tkinter as tk

class Login(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ven = ventana
        self.ven.geometry("350x450")
        self.ven.title("Sistema Login")
        self.ven.config(bg = "#00ddff")
        self.ven.resizable(False, False)
        self.ven.wm_attributes("-alpha", 0.92)
        self.ven.iconbitmap("iconos/icono.ico")

        #Quitamos la barra del menú
        self.ven.overrideredirect(True)

        def Salir():
            self.ven.destroy()

        #ponemos un botón para cerrar la ventana
        self.btnSalir= tk.Button(self.ven, text="X", width=6, height=2, command=Salir)
        self.btnSalir.place(x=290, y=5)
        self.btnSalir.config(bg="#ffaa00")

        #variables
        self.user = tk.StringVar()
        self.pas = tk.StringVar()

        #imagenes 
        self.img = tk.PhotoImage(file="imagenes/logo.png")

        #etiquetas
        #etiqueta para la imagen de logo
        self.lblLogo = tk.Label(self.ven, image=self.img)
        self.lblLogo.place(x=140, y=60)
        self.lblLogo.config(bg="#00ddff")

        self.lblTitulo = tk.Label(self.ven, text="ACCESO", font=("Arial", 20, "bold"))
        self.lblTitulo.place(x=140, y=170)
        self.lblTitulo.config(bg="#00ddff")

        self.lblUser = tk.Label(self.ven, text="USUARIO:", font=("Arial", 17, "bold"))
        self.lblUser.place(x=40, y=210)
        self.lblUser.config(bg="#00ddff")
        self.txtUser = tk.Entry(self.ven, textvariable=self.user, font=("Arial", 17, "bold"))
        self.txtUser.place(x=40, y=250)
        self.txtUser.config(bg="#FFFFFF")

        self.lblPass = tk.Label(self.ven, text="CONTRASEÑA:", font=("Arial", 17, "bold"))
        self.lblPass.place(x=40, y=290)
        self.lblPass.config(bg="#00ddff")
        self.txtPass = tk.Entry(self.ven, textvariable=self.pas, font=("Arial", 17, "bold"), show="*")
        self.txtPass.place(x=40, y=330)
        self.txtPass.config(bg="#FFFFFF")

        self.btnIngresar = tk.Button(self.ven, text="INGRESAR", font=("Arial", 19, "bold"), width="17")
        self.btnIngresar.place(x=40, y=370)
        self.btnIngresar.config(bg="#3ad606")