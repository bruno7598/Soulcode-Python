from modules.veiculo import Veiculo


class Carro(Veiculo):
    motor = ""
    
    def print_motor(self):
        print(self.motor)