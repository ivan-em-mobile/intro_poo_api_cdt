### **Guia de Atividade: Tratamento de Erros (Módulo 09)**
A lidar com `Exceptions` (erros). Usaremos a estrutura `try`, `except`, `else` e `finally` para que o nosso código seja "à prova de erros".

# 🚀 Tutorial Completo: Tratamento de Erros

## 1. O Básico: Divisão Segura
Captura erros de matemática e de digitação.
```python
def aula_tratamento_erros():
    print("--- Início da Aula de Exceções ---")
    
    try:
        # 1. Tentamos obter dados do utilizador
        numerador = int(input("Digita o numerador (número em cima): "))
        denominador = int(input("Digita o denominador (número em baixo): "))
        
        # 2. Tentamos realizar a operação
        resultado = numerador / denominador

    except ValueError:
        # Este bloco corre se o utilizador digitar algo que não seja um número inteiro
        print("Erro: Por favor, digita apenas números inteiros!")

    except ZeroDivisionError:
        # Este bloco corre se o denominador for zero
        print("Erro: Matemática básica! Não pode dividir um número por zero.")

    except Exception as erro:
        # Este é um 'apanha-tudo' para erros inesperados
        print(f"Ocorreu um erro inesperado: {erro}")

    else:
        # Só corre se o bloco 'try' NÃO disparar nenhum erro
        print(f"Sucesso! O resultado da divisão é: {resultado}")

    finally:
        # Corre SEMPRE, independentemente de ter havido erro ou não
        print("--- Fim da operação de tratamento ---")

# Executar a função
aula_tratamento_erros()
```

## 2. POO: Convertendo Duração
Trata o erro quando o utilizador escreve o tempo por extenso.
```python
class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = True # Vamos começar com ele ligado
        self.bateria = 100 

    def fazer_chamada(self, duracao):
        try:
            # Tenta converter a duração para número (pode dar erro se for texto)
            gasto = int(duracao) * 2 
            
            if self.bateria >= gasto:
                self.bateria -= gasto
                print(f"Chamada de {duracao} min efetuada! Bateria: {self.bateria}%")
            else:
                print("Bateria insuficiente para esta chamada.")

        except ValueError:
            # Se o utilizador passar "muito tempo" em vez de "10"
            print("Erro: A duração da chamada deve ser um número inteiro!")
            
        except TypeError:
            # Se o atributo bateria estiver corrompido (ex: for uma string)
            print("Erro crítico: O sistema de bateria encontrou um erro de tipo.")
            
        except Exception as e:
            # Qualquer outro erro inesperado
            print(f"Ocorreu um erro desconhecido: {e}")

# --- IMPLEMENTAÇÃO ---
meu_celular = Celular("Samsung", "S24")

# Teste com erro de valor (mandando uma letra onde devia ser número)
meu_celular.fazer_chamada("Dez")
```

## 3. POO: Proteção de Tipos
Usa o `TypeError` para evitar que o sistema tente subtrair texto de números.
```python
class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = True
        self.bateria = 100

    def fazer_chamada(self, custo_bateria):
        print(f"\n--- Iniciando chamada no {self.modelo} ---")
        
        try:
            # PASSO 1: Tentar fazer a conta
            # Se 'custo_bateria' não for um número, o Python gera um erro aqui!
            self.bateria -= custo_bateria
            
        except TypeError:
            # PASSO 2: Capturar o erro se o valor for inválido (ex: uma letra)
            print("ERRO: Você tentou usar um valor que não é um número!")
            print("Dica: Use números inteiros para o custo da bateria.")
            
        else:
            # PASSO 3: Se a conta deu certo, avisamos o utilizador
            print(f"Chamada concluída com sucesso!")
            print(f"Bateria restante: {self.bateria}%")
            
        finally:
            # PASSO 4: Acontece sempre (bom para logs ou fechar processos)
            print("Sistema de chamadas finalizado.")

# --- TESTANDO NA PRÁTICA ---

meu_celular = Celular("Samsung", "S24")

# CASO 1: Tudo certo (passando o número 10)
meu_celular.fazer_chamada(10)

# CASO 2: Erro propositado (passando uma palavra em vez de número)
meu_celular.fazer_chamada("muito")
```

## 4. O Desafio Final: Status da Bateria
Mistura tratamento de `float` com lógica de decisão `if/elif/else`.
```python
class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def verificar_status(self):
        try:
            # 1. Tentamos ler o que o utilizador digita
            entrada = input(f"Quanto de bateria tem o seu {self.modelo}? ")
            
            # 2. Convertemos para número (aqui pode ocorrer o erro!)
            nivel = float(entrada)

            # 3. Lógica de decisão baseada nos teus requisitos
            if nivel < 0 or nivel > 100:
                print("Aviso: Por favor, digite um valor entre 0 e 100.")
            
            elif nivel < 15:
                print(f"⚠️ Bateria em {nivel}%! Por favor, coloque o telemóvel a carregar.")
            
            elif nivel > 85:
                print(f"✅ Bateria em {nivel}%. Está com carga máxima, pronto para uso intenso!")
            
            else:
                print(f"📱 Bateria em {nivel}%. O telemóvel está normal para uso.")

        except ValueError:
            # Captura se o utilizador digitar "dez" em vez de "10"
            print("Erro Crítico: Você não digitou um número válido. Tente novamente.")

# --- Execução ---
meu_celular = Celular("Samsung", "S24")
meu_celular.verificar_status()
```


# intro_poo_api_cdt
Este repositório é seu guia completo para os **fundamentos da Programação Orientada a Objetos (POO)** e o **uso prático de APIs**, tudo com a **Python**.

* **Programação Orientada a Objetos (POO):** Explore os pilares da POO – **classes**, **objetos**, **herança**, **polimorfismo** e **encapsulamento**. Aprenda a organizar seu código de forma lógica e eficiente, criando programas mais fáceis de entender, manter e escalar. 

* **Integração com APIs:** Descubra como seu código Python pode "conversar" com outros sistemas na internet. Veja exemplos práticos de como **fazer requisições**, **receber dados** (geralmente em formato JSON) e **utilizá-los** em seus projetos, abrindo um mundo de possibilidades de integração.

* **Fundamentos Sólidos:** Este espaço é perfeito para **iniciantes** que buscam construir uma base robusta em **algoritmos e estruturas de dados essenciais**. Cada projeto é desenhado para ajudar você a pensar como um programador, resolver problemas e implementar soluções eficazes.

Sinta-se à vontade para mergulhar nos códigos, testar as implementações e solidificar seu conhecimento em POO e APIs com Python.
