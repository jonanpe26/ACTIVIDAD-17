import tkinter as tk

class Participante:
    def __init__(self, nombre, institucion):
        self.nombre=nombre
        self.institucion=institucion

    def mostrar_informacion(self):
        return (f"{self.nombre}-{self.institucion}")

class BandaEscolar(Participante):
    def __int__(self,nombre,institucion, categoria):
        Participante.__init__(self, nombre, institucion)
        Categoria_Valida=["primaria","basico","diversificado"]
        if categoria in Categoria_Valida:
            self.categoria=categoria
        else:
            self.categoria="categoria invalida"
        self.puntajes={}

    def registrar_puntajes(self, puntajes):
        Criterio_Valido=["ritmo","uniformidad","coreografia","alineacion","puntualidad"]
        for c in Criterio_Valido:
            if c not in puntajes:
                print("error: faltan cirterios")
                return

        for c in puntajes:
            if c not in Criterio_Valido:
                print("error: cirterios invalido", c)
                return

        for valor in puntajes.values():
            if valor <0 or valor >10:
                print("error: puntajes solo de 0 a 10")
                return

        self.puntajes=puntajes

    def total(self):
        total = 0
        for v in self.puntajes.values():
            total+=v
        return total

    def promedio(self):
        if len(self.puntajes)>0:
            return self.total()/len(self.puntajes)
        return 0

    def mostrar_informacion(self):
        info=(f"{self.nombre}-{self.institucion}-{self.categoria}")
        if len(self.puntajes)>0:
            info += (f" | Total: {self.total()} | Promedio: {self.promedio():.2f}")
        return info

class Concurso:
    def __int__(self,nombre,fecha):
        self.nombre=nombre
        self.fecha=fecha
        self.bandas={}

    def inscribir_bandas(self,banda):
        if banda.nombre in self.bandas:
            print("Ya existe una banda con este nombre.")
        else:
            self.bandas[banda.nombre] = banda

    def registrar_evaluacion(self,nombre_banda,puntajes):
        if nombre_banda not in self.bandas:
            print("la banda no esta inscrita")
        else:
            self.bandas[nombre_banda].registrar_puntajes(puntajes)

    def listar_bandas(self):
        lista=[]
        for b in self.bandas.values():
            lista.append(b.mostrar_informacion())
        return lista

    def ranking(self):
        bandas_lista=list(self.bandas.values())
        for i in range (len(bandas_lista)):
            for j in range(i+1, len(bandas_lista)):
                if bandas_lista[i].total()<bandas_lista[j].total():
                    bandas_lista[i],bandas_lista[j]=bandas_lista[j],bandas_lista[i]
        return bandas_lista

class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        tk.Toplevel(self.ventana).title("Inscribir Banda")

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        tk.Toplevel(self.ventana).title("Registrar Evaluación")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Listado de Bandas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()
