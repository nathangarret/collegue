## Passo a passo das unidades e códigos propostos (Python):

**Unidade 3: Arquivos e Strings**

**Aula 1: Métodos da Classe String**

* **Representação de Strings:** Strings são sequências de caracteres delimitadas por aspas simples (' ') ou duplas (" "). Se as aspas precisam ser incluídas na string, utilize a sequência de escape `\` antes da aspa (e.g., 'I\'m "sick"').  `\n` representa uma quebra de linha.
* **Operador de Indexação:**  `s[i]` acessa o caractere na posição *i*. Fatias podem ser obtidas com `s[i:j]` (do índice *i* até *j-1*), `s[i:]` (do índice *i* até o final) e `s[:j]` (do início até *j-1*). Índices negativos contam do final da string para o início (-1 é o último caractere).
* **Strings são imutáveis:**  Métodos de string retornam *cópias* modificadas, a string original permanece inalterada.  
* **Métodos importantes:** `s.capitalize()`, `s.count(target)`, `s.find(target)`, `s.lower()`, `s.replace(old, new)`, `s.split(sep)`, `s.strip()`, `s.upper()`.
* **Exercício (Aula 1):**
```python
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lst[:4])       # ['a', 'b', 'c', 'd']
print(lst[3:6])      # ['d', 'e', 'f']
print(lst[3])       # d
print(lst[5:7])      # ['f', 'g']
print(lst[3:])       # ['d', 'e', 'f', 'g', 'h']
print(lst[-3:])      # ['f', 'g', 'h']
```

**Aula 2: Saída Formatada**

* **Função `print()`:**  `sep` define o separador entre argumentos (padrão é espaço). `end` define o caractere ao final da saída (padrão é `\n`).
* **Método `format()`:** Permite formatar a saída usando placeholders `{}`. Dentro dos placeholders, é possível especificar largura, tipo de dado (b, c, d, x, e, f) e precisão decimal.
* **f-strings (Python 3.6+):**  Forma mais compacta de formatação.  Incorpore expressões diretamente na string precedidas por `f` e delimitadas por chaves `{}`.  A formatação segue a mesma sintaxe do método `format()`.

**Aula 3: Arquivos**

* **Motivação:** Arquivos permitem persistir dados e superar as limitações de entrada do usuário e dados fixos no programa.
* **Tipos:** Arquivos de texto (sequências de caracteres) e arquivos binários (sequências de bytes).
* **Sistema de Arquivos:** Organizados em árvore com diretórios (pastas) e arquivos. Caminhos absolutos (da raiz) e relativos (do diretório atual).

**Aula 4: Padrões de Leitura de Arquivos**

* **`open(filename, mode)`:** Abre um arquivo. Modos comuns: 'r' (leitura), 'w' (escrita - sobrescreve), 'a' (append), 'r+' (leitura e escrita).
* **`file.close()`:** Fecha o arquivo.
* **Métodos:** `file.read(n)`, `file.read()`, `file.readline()`, `file.readlines()`.
* **Padrões:** Ler como string, lista de palavras, lista de linhas.
* **Exemplo (Aula 4 - numWords):**
```python
def numWords(filename):
  """Retorna o número de palavras em um arquivo."""
  with open(filename, 'r') as infile: #Usando with para garantir o fechamento do arquivo
      content = infile.read()
  wordList = content.split()
  return len(wordList)

#Exemplo de uso
print(numWords("meu_arquivo.txt"))
```


**Aula 5: Escrevendo em Arquivos**

* **`file.write(s)`:** Escreve a string `s` no arquivo.
* **Conversão de tipos:**  Valores não string precisam ser convertidos para string antes de serem escritos em um arquivo texto (e.g., `str(5)` ou usando f-strings/`format()`).


**Aula 6: Exemplo Prático**

* **Registrar acessos a arquivos:** Criar uma função `openLog(fnome, modo)` que registra data e hora de acesso ao arquivo.
* **Módulo `time`:** `time.time()`, `time.localtime()`, `time.strftime()`.
* **Exercício (Aula 6 - openLog - incompleto, precisa do corpo da função):**
```python
import time

def openLog(fnome, modo):
    """Abre um arquivo e registra o acesso em um log."""
    # 1. Abrir o arquivo usando open() com os parâmetros fornecidos
    # 2. Obter a data e hora atuais com time.localtime() e formatar com time.strftime()
    # 3. Escrever a informação de acesso no arquivo de log (e.g., "arquivo aberto em data/hora")
    # 4. Retornar o objeto de arquivo


#Exemplo de Uso (assumindo que o corpo da função foi implementado)
meu_arquivo = openLog("dados/meu_arquivo.txt", "r")

#...seu código que usa meu_arquivo ...

meu_arquivo.close() # Fecha o arquivo após o uso

```

**Observações:**

* Os códigos dos exercícios foram adaptados para maior clareza e para usar boas práticas como o gerenciamento de arquivos com `with`.
* A função `openLog()` da Aula 6 está incompleta. O corpo da função precisa ser implementado seguindo os passos descritos.
* Lembre-se de adaptar os caminhos de arquivo nos exemplos conforme sua estrutura de diretórios.