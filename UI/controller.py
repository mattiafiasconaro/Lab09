import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def analizzaAeroporti(self, e):
        self._view.txt_result.clean()
        distMin= self._view.txt_distanza.value
        if distMin=="":
            self._view.controls.append(ft.Text(
                "inserire un valore numerico",color="red"
            ))
            self._view.update_page()
            return
        try:
            intero=int(distMin)
        except ValueError:
            self._controls.append(ft.Text(
                "inserire un valore intero",color="red"
            ))
            self._view.update_page()

        if  intero <=0 :
            self._view.controls.append(
                ft.Text("inserire un valore positivo",color="red")

            )
            self._view.update_page()
            return


        self._model.buildGraph(intero)
        nodi,archi =self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(
            "grafo corettamente eseguito",color="green"
        ))
        self._view.txt_result.controls.append(ft.Text(
            f"numero di nodi {nodi} - numero di archi {archi}",color="green"
        ))
        self._view.update_page()



