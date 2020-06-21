# They Will Remember You!

Planejamento de estudos, com prazo de validade no final do tempo de graduação. O que virá após isso, desejo muito saber. Esta ideia foi inspirada no repositório de [@jwashan](https://github.com/jwasham/coding-interview-university)!

![Warriors](https://www.tec.com.pe/wp-content/uploads/2014/09/LoL-Imagine-Dragons-Warrior-2.jpg)

## O que é isso?

Este repositório surgiu da necessidade mental de um cronograma bem definido acerca do trajeto a ser percorrido para alcançar o objetivo de ser um engenheiro de software. O conteúdo teórico descrito pelo cronograma aborda:

- Noções sólidas de matemática pura (Cálculo I, II e III), probabilidade e estatística, necessários para o estudo e aplicação de algoritmos de aprendizado de máquina e construção de redes neurais, além do exercício de ciência de dados;
- Conhecimentos formais em linguagens de programação back-end, como Python, Java e JavaScript (node.js), além de seus principais frameworks e paradigmas.
- Conhecimentos formais em modelagem de estruturas de sistemas de software, primariamente utlizando da notação da UML;
- Conhecimentos sólidos sobre paradigmas de programação, utilizando a linguagem Haskell como exemplo do paradigma funcional e da linguagem Prolog como exemplo do paradigma lógico.
- É importante destacar que o planejamento descrito nesse repositório está sujeito a alterações a qualquer momento.

## O plano diário

O objetivo é estudar 4 horas diárias, intercalando os objetos de estudo. Além disso, não ultrapassar 8 horas diárias, para não sobrecarregar a mente. Também regular com horários de lazer, visando reservar um tempo para processar o conhecimento obtido e descansar a mente. Não estabelecerei um cronograma reservando dias específicos para determinado conteúdo, assim, deixando o espaço flexível para conteúdos à medida que sentir vontade ou necessidade de um aprofundamento maior sobre determinado conteúdo.

## Organização

- No geral, este repositório contará com um index, que listará todos os conteúdos citados acima, desfragmentando-os em tópicos de estudo menores. Junto com o conteúdo, comumente estarão dispostos links que levam ao lugar de onde eu obtive tal conhecimento do assunto. Ao final, existe uma seção de links úteis, onde estarão dispostos links que apontam para conteúdos miscelâneos, como playlists com músicas para relaxar, artigos sobre assuntos variados, etc.

## Reminders

- Não é necessário, tanto quanto é impossível, aprender perfeitamente todos os conteúdos aqui abordados. Um bom programador não é aquele que sabe tudo, mas sim, aquele que sabe aplicar perfeitamente o suficiente que conhece para resolver um problema.
- Existem dias em que não sentirá vontade ou motivação para aprender algo e isto é perfeitamente normal. O importante é jamais desistir, pois cada percentual de progresso é, ainda assim, progresso. Nestes dias, tente aprender outras coisas de áreas diferentes de programação, que ajudarão sua mente a variar o que está aprendendo e facilitar possíveis associações.
- Conhecimento teórico é bom, mas a prática ajuda muito mais no processo de construir bases sólidas sobre o objeto de estudo. Por isso, sempre pratique o que aprendeu.
- "I fear not the man who has practiced 10,000 kicks once, but I fear the man who has practiced one kick 10,000 times."

## Índice
- [O que é isso](#o-que-é-isso)
- [O plano diário](#o-plano-diário)
- [Organização](#organização)
- [Reminders](#reminders)
- [Python](#python)
- [Data Science](#data-science)
    - [Pandas](#pandas)
    - [NumPy](#numpy)
- [Machine Learning](#machine-learning)
- [Deep Learning](#deep-learning)
	- [Redes Neurais](#redes-neurais)
	- [Funções de Ativação](#funções-de-ativação)
		- [Função de Etapa Binária](#função-de-etapa-binária)
		- [Sigmóide](#sigmóide)
		- [Tanh](#tanh)
		- [ReLU](#relu)
		- [Leaky ReLU](#leaky-relu)
- [Apostilas e Documentações](#apostilas-e-documentações)
- [Cursos](#cursos)
- [Links Úteis](#links-úteis)

## Python
- ### Basics
    - É uma linguagem de alto nível, ou seja, desenvolvida para fácil leitura por parte das pessoas;
    - É uma linguagem interpretada, ou seja, o código-fonte não é compilado diretamente código de máquina;
    - É uma linguagem com tipos dinâmicos, ou seja, um mesmo escopo do código pode assumir diferentes tipos de dado;
    - Possui sintaxe ligeiramente diferente de outras linguagens tradicionais, como Java e C, já que utiliza a identação para marcar blocos de código e requer apenas o nome da variável para sua declaração.
    
- ### Funções
    - Funções em Python são definidas pela palavra chave `def`, seguido do nome da função e do conjunto de parâmetros (opcionais) entre parênteses.
    
	<pre><code>
	def sum_numbers(n1, n2): 
	    return n1 + n2
	</code></pre>

    - É possível passar parâmetros default para a função.
 	
	<pre><code>
	# Atribui o valor de n1 e n2 para 0 caso não sejam passados na chamada do método
	def sum_numbers(n1=0, n2=0): 
	    return n1 + n2
	</code></pre>

- ### Funções lambda

- ### Listas
	- Listas são uma sequência mutável de variáveis, denotada por `list()` ou simplesmente `[]`
	- Os elementos da lista podem ser acessados através de indexação `list[index` ou através de um loop `for`
    
		for item in list:
		    do_something()
    
	- Métodos de listas:
	- [ ] list.append(item): adiciona o item passado como parâmetro a lista.
	- [ ] list.append(item): adiciona o item passado como parâmetro a lista.
    
- ### Dicionários
- ### Tuplas
    - Tuplas são uma sequência imutável de variáveis, denotada por `tuple()` ou simplesmente `()`

- ### Built-in Functions

- ### List Comprehension

## Data Science
- ### Pandas
    - Veja a [documentação](https://pandas.pydata.org/docs/)
    
    - Possui duas classes principais: Series, formada por uma coluna e várias linhas, e DataFrame (conjunto de Series), formado por linhas e colunas.
    
    - Criando uma Series:
        serie = pd.Series([1,2,3,4])
    
    - Criando um DataFrame de uma dimensão:
        dataframe = pd.DataFrame([1,2,3,4])
        
    - Criando um DataFrame de mais de uma dimensão:
        dataframe = pd.DataFrame({"Coluna 1": [1,2,3],
                          "Coluna 2": [4,5,6]},
                        index=[1,2,3])
                        
    - Atributos do DataFrame:
        - [ ] dataframe.index: retorna o valor de início e de fim do dataframe, assim como o step.
        - [ ] dataframe.columns: retorna o nome das colunas do dataframe.
        - [ ] dataframe.values: retorna todas as linhas presentes no dataframe.
        - [ ] dataframe.dtype: retorna o tipo de objeto que cada coluna do dataframe armazena.
        - [ ] dataframe.shape: quantidade de linhas e colunas do DataFrame.
        
    - Principais métodos do DataFrame:
        - [ ] dataframe.head(): retorna um resumo com o número de linhas passado como parâmetro (5 por default).
        - [ ] dataframe.describe(): retorna um resumo estatístico dos dados.
        - [ ] dataframe.loc[]: verificação por nome do índice.
        - [ ] dataframe.iloc[]: verificação por posição no índice.
        - [ ] dataframe.mean(): verifica a média dos valores de cada coluna.
        - [ ] dataframe.apply(): aplica um método para cada item do dataframe.
        - [ ] dataframe.drop(): remove a coluna passada como parâmetro.
        - [ ] dataframe.count(): contagem de dados não-nulos.
        - [ ] dataframe.sort_values(): ordenando em ordem crescente.
        - [ ] dataframe.sort_values(ascending=False): ordenando em ordem decrescente.
        - [ ] dataframe[dataframe['columns'] #condição lógica]: retorna os dados seguindo alguma condição lógica.
        - [ ] dataframe.dropna(): retorna as linhas que não contém um NaN.
        - [ ] dataframe.fillna(): preenche todos os valores NaN por um outro específico.
        - [ ] dataframe.isna(): indica quais valores do dataframe são NaN.
      
- ### NumPy
- ### Web Scraping

## Machine Learning
## Deep Learning
- ## Perceptron
    - O que caracteriza um modelo de aprendizagem profunda são redes neurais artificiais com múltiplas camadas ocultas (ou intermediárias).

    - O Perceptron é a arquitetura de redes neurais artificiais mais simples que existe, desenvolvido nas décadas de 50 e 60.

    - O Perceptron é um modelo matemático que recebe várias entradas (x1,x2, ...xn) e produz uma única saída binária.

					x1,x2,x3 -----> O -----> output

    - Para cada uma das entradas, o modelo introduz pesos (w1, w2, ...wn), que são números reais que expressam a importância das respectivas entradas para a saída. A saída do neurônio, 0 ou 1, true ou false, é determinada pela soma ponderada, Σjwjxj, menor ou maior que algum limiar (threshold).

    - Perceptron é uma rede neural de camada única e um Perceptron de várias camadas é chamado de Rede Neural Artificial. O Perceptron é um classificador linear (binário). Além disso, é usado na aprendizagem supervisionada e pode ser usado para classificar os dados de entrada fornecidos.

- ## Redes Neurais
	
	- Reprodução do comportamento do cérebro humano de forma computacional;
	- O cérebro aprende no reconhecimento de padrões com base na experiência;
    	- Redes Neurais Artificiais Profundas constituem o conceito de Deep Learning;
    	- Redes neurais artificiais possuem a capacidade de recriar sinapses do cérebro;
    	- Uma RNA modela a relação entre um conjunto de sinais de entrada e um sinal de saída usando um modelo derivado de nossa compreensão de como um cérebro biológico responde a estímulos de entradas sensoriais.
    	- Devido ao número enorme de neurônios artificiais necessários, entra a importância da computação paralela em GPU.
    - Deep Learning surgiu pelo fato de que é difícil de definir formalmente um problema casual ou comum no dia a dia, como visão ou audição de algo.

- ## Funções de Ativação

	- Os neurônios fazem uma transformação linear na entrada pelos pesos e bias (viés), enquanto a transformação não-linear é feita pela função de ativação.

	- O movimento da informação "da esquerda para a direita" e único é chamado de propagação direta. Caso o resultado gerado seja incompatível com o esperado, atualizamos o bias e os pesos, no processo chamado de backpropagation.

	- Uma pequena mudança no peso ou no bias causam uma pequena mudança no output.

	- Em sistemas Perceptron, uma mudança pequena nos pesos ou no bias podem causar uma mudança inesperada e difícil de controlar, podendo mudar o resultado completamente de 0 para 1. Nesse cenário, entram as funções de ativação.

	- Funções de ativação verificam se a informação que o neurônio está recebendo é pertinente ou não para a tomada de decisão.

					Y = Activation(Σ(weight * input) + bias)
					
	- Função de ativação é a transformação não linear que fazemos ao longo do sinal de entrada.

	- Sem a função de ativação, um modelo de rede neural é basicamente um algoritmo de regressão linear, se tornando incapaz de adaptar-se de forma não-linear e assim, incapaz de realizar tarefas complexas como processamento de linguagem natural ou classificação de imagens.



	- ## Função de Etapa Binária
		- Funções binárias possuem gradiente da derivada = 0, ou seja, são incapazes de se aperfeiçoar através da correção do erro.
		- Classificador simples baseado em decisões binárias (sim ou não), seguindo a regra:
	
					f(x) = 1, x >= 0
					f(x) = 0, x < 0

	- ## Função Linear
  		- A derivada de uma função linear é constante, ou seja, não depende do valor de entrada x. Por isso, toda vez que efetuamos o backpropagation, o gradiente é o mesmo.
		- A função linear é definida como:
			
					f(x) = ax

	- ## Sigmóide
  		- A maior vantagem desta função linear é justamente o fato de que ela não é linear.
  		- A função essencialmente empurra os valores de Y para os extremos, sendo um atributo interessante quando se deseja classificar os valores dentro de uma classe específica.
  		- A função é problemática quando os valores do gradiente são muito próximos a zero, pois assim, a rede não está realmente aprendendo.
		- A função signóide é definida como:
		
					f(x) = 1 / (1 + e ^ -x)
  
 	- ## Tanh
  		- Basicamente, soluciona o nosso problema dos valores, sendo todos do mesmo sinal. Todas as outras propriedades são as mesmas da função sigmoide. É contínuo e diferenciável em todos os pontos. A função não é linear, então podemos fazer o backpropagation facilmente nos erros.
		- A função tanh é uma versão escalonada da sigmóide, sendo descrita como:
			
					tanh(x) = 2 / (1 + e ^ (- 2x)) -1

	- ## ReLU
  		- É a função de ativação mais utilizada atualmente na construção de redes neurais.
  		- Uma de suas vantagens é que ela não ativa todos os neurônios da rede simultâneamente, tornando a rede esparsa, eficiente e fácil para a computação.
		- Significa Unidade Linear Rectificada e pode ser descrita como:
	
					f(x) = max (0, x) 

	- ## Leaky ReLU
  		- A função Leaky ReLU não passa de uma versão melhorada da função ReLU. Na função ReLU, o gradiente é 0 para x < 0, o que fez os neurônios morrerem por ativações nessa região. Leaky ReLU ajuda a resolver este problema. Em vez de definir a função Relu como 0 para x inferior a 0, definimos como um pequeno componente linear de x. Pode ser definido como:

					f(x) = ax, x < 0f(x) = x, x > = 0

## Apostilas e Documentações
- [Apostila de HTML (en-us)](https://www.w3schools.com/html/)
- [Lista de pacotes e arquivos de classe LaTeX](https://pt.overleaf.com/learn/latex/List_of_packages_and_class_files)

## Cursos
- [Curso de Data Science com Python](https://www.datascienceacademy.com.br/path-player?courseid=python-fundamentos&unit=56fa01d947d7ddf1938b456cUnit)
- [Curso de Flutter e Dart](https://www.youtube.com/playlist?list=PL5EmR7zuTn_aX0pG4oWTyKKQT25Hkq2XG)
- [Curso de JavaScript](https://www.youtube.com/playlist?list=PLHz_AreHm4dlsK3Nr9GVvXCbpQyHQl1o1)
- [Curso de Kotlin](https://www.youtube.com/playlist?list=PLxWMYNrPoLoJ6RjjUdpIPm6NE5CiRPG6E)
- [Curso de PHP](https://www.youtube.com/playlist?list=PLHz_AreHm4dm4beCCCmW4xwpmLf6EHY9k)
- [Curso de RPG Maker MV](https://www.youtube.com/playlist?list=PLfpzoTMgIjznBx77qsr05Re4-UclPC7kS)
- [Curso de Ruby e Ruby on Rails](https://jornadadodev.com.br/posts/ruby)
- [Curso de Unity Engine](https://www.youtube.com/playlist?list=PLOFacakspTDKh8wMqF-2soctnLr7i_NEc)

## Links Úteis
- [Sons de chuva](https://www.youtube.com/watch?v=8plwv25NYRo)
- [Minha playlist de OSTs de Naruto para fins motivacionais](https://www.youtube.com/playlist?list=PL5cKPIIsKxtPHiEpvvWM0A4O6agfqK4cq)
