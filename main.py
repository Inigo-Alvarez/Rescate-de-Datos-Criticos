class Tarea:
    def __init__(self, nombre, descripcion, duracion, dependencias=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.dependencias = dependencias if dependencias else []
        self.completada = False

class ProyectoRescate:
    def __init__(self):
        self.tareas = []
        self.tecnicos_disponibles = 3
        self.tiempo_total = 120
        self._crear_tareas()

    def _crear_tareas(self):
        self.tareas = [
            Tarea("A", "Identificar servidores afectados", 15),
            Tarea("B", "Priorizar datos críticos", 20, ["A"]),
            Tarea("C", "Activar protocolo de recuperación", 10, ["A"]),
            Tarea("D", "Asignar técnicos a servidores", 5, ["B", "C"]),
            Tarea("E", "Recuperar datos de servidor 1", 30, ["D"]),
            Tarea("F", "Recuperar datos de servidor 2", 25, ["D", "E"]),
            Tarea("G", "Validar integridad de datos recuperados", 15, ["F"]),
            Tarea("H", "Generar informe preliminar para dirección", 10, ["G"]),
            Tarea("I", "Comunicar a clientes afectados", 20, ["G"]),
            Tarea("J", "Coordinar con equipo legal", 15, ["G"]),
            Tarea("K", "Preparar plan de contingencia", 25, ["G"]),
        ]

    def mostrar_objetivo(self):
        print("Objetivo: Rescatar los datos médicos críticos en 120 minutos antes del reinicio del sistema.")

    def mostrar_diagrama_flujo(self):
        print("\nDiagrama de Flujo del Cronograma:")
        for tarea in self.tareas:
            deps = ", ".join(tarea.dependencias) if tarea.dependencias else "Ninguna"
            print(f"{tarea.nombre}: {tarea.descripcion} ({tarea.duracion} min) | Depende de: {deps}")

    def nivelar_recursos(self):
        print("\nNivelación de Recursos:")
        print(f"Técnicos disponibles: {self.tecnicos_disponibles}")
        print("Solo se puede recuperar datos de un servidor a la vez.")
        print("Las tareas H, I, J y K inician tras validar datos (G).")

    def plan_comunicacion(self):
        print("\nPlan de Comunicación de Crisis:")
        print("- Informe preliminar a dirección tras validación de datos.")
        print("- Comunicación a clientes afectados tras validación.")
        print("- Coordinación con equipo legal tras validación.")
        print("- Preparación de plan de contingencia tras validación.")

    def resumen(self):
        self.mostrar_objetivo()
        self.mostrar_diagrama_flujo()
        self.nivelar_recursos()
        self.plan_comunicacion()

if __name__ == "__main__":
    proyecto = ProyectoRescate()
    proyecto.resumen()