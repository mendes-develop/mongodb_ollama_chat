people: list[str] = ['James', 'Ronaldo', "Charlotte", "Stephanie"]

def get_names_under_x_characters():
  return [person for person in people if len(person) >= 8]

def calculate_factorial(number: int): 
  if number == 1:
    return number
  else:
    return number * calculate_factorial(number - 1)
  

def calculate_fibonacci(number: int):
  if number <= 1:
    return number
  else:
    return calculate_fibonacci(number - 1) + calculate_fibonacci(number - 2)
  

def main():
  adicione_seu_nome = input("Adicione Seu Nome: ")
  print(f"Olá, {adicione_seu_nome} voce eh uma bixa!")

  print(calculate_fibonacci(8))
  print(calculate_factorial(8))
  
  print(get_names_under_x_characters())
  
  
if __name__ == "__main__":
  main()
  
  
