from typing import Dict, Any

class AnalizadorEventos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.eventos = []

    def procesar_eventos(self) -> Dict[str, Any]:
        # Inicializar diccionarios para estadísticas
        total_eventos = 0
        eventos_por_tipo = {}
        eventos_por_servidor = {}

        # Abrir y leer el archivo
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.strip():  # Ignorar líneas en blanco
                    if linea.startswith("Tipo de evento:"):
                        # Procesar línea que contiene información del evento
                        total_eventos += 1
                        tipo_evento = linea.split(": ")[1].strip()
                        eventos_por_tipo[tipo_evento] = eventos_por_tipo.get(tipo_evento, 0) + 1
                    elif linea.startswith("Servidor:"):
                        nombre_servidor = linea.split(": ")[1].strip()
                        eventos_por_servidor[nombre_servidor] = eventos_por_servidor.get(nombre_servidor, 0) + 1

        estadisticas = {
            "Total de eventos registrados": total_eventos,
            "Eventos por tipo": eventos_por_tipo,
            "Eventos por servidor": eventos_por_servidor
        }

        return estadisticas