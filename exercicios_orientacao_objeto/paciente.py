# ==================== EXERCICIO 9 ==============================
# Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a 
# idade e o histórico de consultas de um paciente. Implemente métodos para adicionar 
# uma nova consulta ao histórico e exibir as consultas realizadas

class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []

    def nova_consulta(self, consulta):
        self.historico.append(consulta)

    def mostrar_historico(self):
        if not self.historico:
            print(f"O paciente {self.nome} ainda não tem nenhuma consulta")
        else:
            print(f"O paciente {self.nome} possui as consultas: ")
            for i, consulta in enumerate(self.historico, 1):
                print(f"{i} - {consulta}")


paciente_1 = Paciente("Paciente 1", 10)
paciente_1.nova_consulta("Pediatra")
paciente_1.nova_consulta("Ortopedista")
paciente_1.mostrar_historico()
