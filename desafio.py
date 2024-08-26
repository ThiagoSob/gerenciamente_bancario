class Conta:
    def __init__(self, numero_conta , titular_conta , saldo:float):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = saldo
        self.conta = []
    
    def deposito(self):
        pass
    
    def saque(self):
        pass
    
    def exibir_saldo(self):
        pass
    
    def resumo(self):
        pass
    
class Conta_Corrente(Conta):
    def __init__(self , numero_conta , titular_conta , saldo:float , taxa_manutencao: float , limite_cheque_especial: float):
        self.taxa_manutencao = taxa_manutencao
        self.limite_cheque_especial = limite_cheque_especial
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = saldo
        
    def deposito(self):
        deposito = float(input('Quanto deseja depositar: '))
        self.saldo += deposito
        
    
    def saque(self):
        saque = float(input('Quanto deseja sacar: '))
        
        if self.saldo > saque or self.saldo + self.limite_cheque_especial > saque:
            self.saldo -= saque
            
        else:
            print('Você não possui saldo suficiente para sacar!')
    
    def exibir_saldo(self):
        print(f'Saldo: R${self.saldo:.2f}')
        
    def resumo(self):
        print(f'Tipo de Conto: Conta Corrente\nTitular: {self.titular_conta}\nConta: {self.numero_conta}\nSaldo:{self.saldo:.2f}')
        
        
class Conta_Poupanca(Conta):
    def __init__(self , numero_conta , titular_conta , saldo:float , taxa_jurus: float , rendimento):
        self.taxa_jurus = taxa_jurus
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = saldo
        self.rendime = rendimento
        
        
    def rendimento(self):
        n = int(input('Quantos meses rendeu: '))
        while True:
            if n == 0:
                rendimento = 0
                break
            elif n < 0:
                print('Não pode ser negativo!')
                continue
            else:
                rendimento = 1000 * ((1 + self.taxa_jurus)**n)
                break
        self.rendime = rendimento    
        self.saldo += rendimento
        
        
    def deposito(self):
        deposito = float(input('Quanto deseja depositar: '))
        self.saldo += deposito
        
    
    def saque(self):
        saque = float(input('Quanto deseja sacar: '))
        if self.saldo >= saque:
            self.saldo -= saque
        
        else:
            print('Você não possui saldo suficiente para sacar!')
        
    def exibir_saldo(self):
        print(f'Saldo: R${self.saldo:.2f}')
        
    def resumo(self):
        print(f'Tipo de Conto: Conta Poupança\nTitular: {self.titular_conta}\nConta: {self.numero_conta}\nSaldo:R${self.saldo:.2f}\nRendimento: {self.rendime:.2f}')
        
        

c1 = Conta_Corrente(numero_conta='01122332-X' , titular_conta='Thiago' , saldo=0 , taxa_manutencao=40 , limite_cheque_especial=300)
c2 = Conta_Poupanca(numero_conta='00223478-1' , titular_conta='Thiago' , saldo=0 , taxa_jurus=0.005 , rendimento=0)

print('====='*10)
print('')
print('Operação 1:')
print('')
c1.deposito()
print('')
c1.exibir_saldo()
print('')
c1.saque()
print('')
c1.exibir_saldo()
print('')
print('Resumo da Conta:')
print('')
c1.resumo()
print('')

print('====='*10)
print('')
print('Operação 2:')
print('')
c2.deposito()
print('')
c2.rendimento()
print('')
c2.exibir_saldo()
print('')
c2.saque()
print('')
c2.rendimento()
print('')
c2.exibir_saldo()
print('')
print('Resumo da Conta:')
print('')
c2.resumo()
print('')
print('FIM')