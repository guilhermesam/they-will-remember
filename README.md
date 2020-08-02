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
- [Dicionário do Programador](#dicionário-do-programador)
- [Python](#python)
	- [Funções](#funções)
	- [Funções Lambda](#funções-lambda)
	- [Strings](#strings)
	- [Listas](#listas)
	- [Dicionários](#dicionários)
	- [Tuplas](#tuplas)
	- [Funções Built-in](#funções-built-in)
	- [Orientação a Objetos](#orientação-a-objetos)
	- [Date and Time](#date-and-time)
	- [Boas práticas](#boas-práticas)
	
- [Data Science](#data-science)
	- [Importância do uso de dados](#importância-do-uso-de-dados)
- [Ferramentas e técnicas de Data Science](#ferramentas-e-técnicas-de-data-science)
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
- [Git](#git)
- [Apostilas e Documentações](#apostilas-e-documentações)
- [Cursos](#cursos)
- [Links Úteis](#links-úteis)

## Dicionário do Programador

- ### Continuous Integration (CI): 
	- Processo de automatização de builds e testes de códigos que acontece quando um membro do time realiza um commit.
	- Considerada uma metodologia de desenvolvimento moderna.
	- Atua para resolver problemas relacionados a manutenção do projeto.
	- Contribui diretamente na redução do custo do projeto.
	- Práticas como o CI são necessárias dentro de grandes projetos, que compreendem um grande número de pessoas trabalhando em uma mesma feature.
	- É necessário que sejam realizados ao menos um commit por dia, devido ao fato que a atualização e integração devem ser contínuas, evitando que um código muito grande entre em conflito com outro código, dificultando assim a identificação das partes críticas.
	- Automatização de build: sempre que uma nova versão do sistema for gerada, ela deverá ser feita de forma automatizada e sem interferência externa.
	- Testes automáticos durante o período de builds são essenciais.
	- Ferramentas notáveis: Jenkins, TravisCI, GitLabCI, Hudson, CruiseControl, Bamboo.

- ### GraphQL:
	- Relacionado ao desenvolvimento de APIs.
	- Significa Graph Query Language (Linguagem de Consulta em Grafos).
	- Permite que uma API retorne mais ou menos dados, de acordo com a necessidade, performando melhor que modelos de API tradicionais.
	- Modelo semelhante à estrutura da orientação a objetos.

- ### MVC (Model-View-Controller):
	- É um padrão de arquitetura de software utilizado em vários tipos de projetos.
	- Foi desenvolvido em 1979, por Trygve Reenskaug, muito popular atualmente no desenvolvimento web.
	- Consiste em dividir a aplicação nas três camadas que compõem seu nome, possibilitando separar a interface de usuário das regras de negócio e auxiliando na reutilização de código.
	- Sua principal desvantagem é a complexidade na compreensão da estrutura de divisão da aplicação em camadas.
	Model: camada responsável pela manipulação dos dados da aplicação, responsável por questões como acesso a bancos de dados ou consumo de APIs.
	View: responsável pela interface que será exibida ao usuário, que contém, por exemplo, os arquivos HTML e CSS.
	Controller: Responsável pela comunicação entre a camada View e o Model, realizando as requisições do usuário na camada Model para obter os dados e utilizar as Views para exibir de volta ao usuário.
	Router: Elemento responsável por criar as rotas que ligam os endereços.
	- Frameworks que utilizam MVC: Ruby on Rails, Merb, Spring, Struts, Laravel, CodeIgniter, CakePHP, Symfony, React, Backbone, Angular, Asp.Net MVC, Django, CherryPy.
	
	
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

- ### Strings
	- Em Python, objetos do tipo String são listas de caractere, baseadas em Unicode.
	

- ### Listas
	- Listas são uma sequência mutável de variáveis, denotada por `list()` ou simplesmente `[]`
	- Os elementos da lista podem ser acessados através de indexação `list[index]` ou através de um loop `for`;
	
	<pre><code>
	for item in list:
		do_something()
	</code></pre>
	
	- É possível criar uma lista através da multiplicação de uma outra lista;
    
	<pre><code>
	[1] * 3
	Output: [1,1,1]
	</code></pre>
    	
	- É possível concatenar duas listas através do operador `+`;
	- É possível verificar a existência de um elemento dentro de uma lista através da sintaxe ` element in list`, que retorna um valor booleano;
  	- É possível realizar o fatiamento (slicing) em uma lista, através da sinxate `list[start:end]`;  
	- Métodos de listas:
		- list.append(item): adiciona o item passado como parâmetro a lista.
		- list.append(item): adiciona o item passado como parâmetro a lista.
    
- ### Dicionários
	- Dicionários são estruturas de dados que armazenam uma coleção de elementos ordenados através de chave e valor, declarados por `dict()` ou `{}`;
	- Métodos de dicionários:
		- `clear()`: Remove todos os itens do dicionário;
		- `copy()`: Retorna uma cópia do dicionário;
		- `fromkeys()`: Retorna uma cópia do dicionário com as chaves especificadas;
		- `get(key)`: Retorna o valor correspondente à chave especificada;
		- `items()`: Retorna uma lista contendo uma tupla para cada par chave-valor;
		- `keys()`: Retorna uma lista contendo as chaves do dicionário;
		- `pop(key)`: Remove o elemento com a chave especificada;
		- `popitem()`: Remove o último par chave-valor inserido;
		- `setdefault()`: Retorna o valor da chave especificada. Se a chave não existe: insere a chave com o valor especificado;
		- `update({key:value})`: Atualiza o dicionário com o par chave-valor especificado;
		- `values()`: Retorna uma lista com todos os valores do dicionário;
		
- ### Tuplas
	- Tuplas são uma sequência imutável de variáveis, denotada por `tuple()` ou simplesmente `()`. Possuem os mesmos métodos de listas, porém, seus elementos não podem mudar, ou seja, não é possível executar métodos inerentes à listas, tais como append() ou clear().

- ### Funções Built-in
	- `abs()`: Retorna o valor absoluto do número. Útil para calcular notações científicas, na forma de, por exemplo, `3e3`, resultando em 3000.
	- `all()`: Retorna True caso todos os itens de um iterável são True, caso contrário, retorna False. A função sem parâmetros retorna True.
	- `any()`: Retorna True caso qualquer item dentro de um iterável for True, caso contrário, retorna False.
	- `ascii()`: Retorna uma versão legível do objeto, transformando caracteres non-ascii em caracteres de escape.
	- `bin()`: Retorna a versão binária de um número.
	- `bool()`: Retorna a versão booleana do objeto especificado.
	- `bytearray(x,encoding,error)`: Retorna um array de bytes.
	- `callable()`: Retorna True se o objeto é chamável.
	- `chr()`: Retorna o caractere Unicode correspondente ao caractere passado.
	- `complex()`: Retorna um número complexo.
	- `delattr(class, attr)`: Deleta o atributo do objeto passado como parâmetro.
	- `dict()`: Instancia um dicionário.
 	- `dir(object)`: Retorna uma lista com as propriedades e métodos do objeto recebido como parâmetro.
	- `enumerate(iterable, start)`: Retorna uma lista como objeto enumerável.
	- `eval(expression)`: Efetua uma operação e retorna o valor resultante desta.
	- `exec(object)`: Executa o código ou objeto passado como parâmetro.
	- `filter(function, iterable)`: Retorna os itens de um objeto iterável que satisfaçam a condição que a função passada como parâmetro determina.
	- `float()`: Retorna a versão float do objeto especificado.
	- `format(object, pattern)`: Formata o objeto especificado de acordo com determinado padrão.
	- `getattr(class, attr)`: Retorna o atributo do objeto passado como parâmetro.
	- `hasattr`: Retorna true se o objeto passado como parâmetro possui o atributo passado como parâmetro.
	- `hash(object)`: Retorna o valor hash para o objeto especificado.
	- `help(object)`: Retorna informações acerca da utilização da propriedade ou método passado como parâmetro.
	- `hex(number)`: Converte um número em um valor hexadecimal.
	- `id(object)` : Retorna o endereço de memória local do objeto passado como parâmetro.
	- `input(message)` : Permite que o sistema solicite informações para o usuário.
	- `int()` : Retorna um inteiro correspondente ao objeto especificado.
	- `isinstance(object, object)` : Retorna true se o objeto especificado é uma instância do objeto especificado.
	- `issubclass(object, object)`:  Retorna true se o objeto especificado é uma subclasse do objeto especificado.
	- `iter()`: Retorna um objeto iterável.
	- `len(object)` : Retorna o tamanho de um objeto.
	- `list(object)` : Retorna uma lista a partir do objeto passado como parâmetro ou instancia uma nova.
	- `map(function, iterable)` : Aplica uma função em cada item de um objeto iterável e devolve um novo objeto.
	- `max()`: Retorna o maior valor dentro de um iterável.
	- `memoryview(object)` : Retorna um objeto como ponto de vista da memória a partir de um objeto passado como parâmetro. 
	- `min()` : Retorna o menor valor dentro de um iterável.
	- `next(iterable)` : Retorna o próximo item de um objeto iterável, iniciando no índice 0 por padrão.
	- `object()`: Instancia um novo objeto.
	- `oct(number)` : Converte um número para um objeto do sistema [octal](https://pt.wikipedia.org/wiki/Sistema_octal).
	- `open(filepath, method)` : Abre um arquivo de acordo com o método de leitura (w: write, r: read).
	- `pow(x,y)` : Retorna o valor de x elevado a y.
	- `print()` : Imprime um objeto na tela.
	- `range(start, end, step)` : Gera uma sequência de números, iniciando em 0 e incrementando em 1, por padrão.
	- `reversed(iterable)` : Retorna um iterador, porém revertido.
	- `round(number, param)` : Retorna um número decimal arredondado, de acordo com o número de casas decimais passado como parâmetro.
	- `set()` : Retorna um novo objeto setável.
	- `setattr(class, attr, new_value)` : Altera algum atributo de uma classe com um novo valor.
	- `sorted(iterable, key, reverse)` : Organiza uma lista a partir de determinado critério. É possível alterar a ordenação da lista passando um valor booleano para a propriedade reverse.
	- `str()` : Instancia um novo objeto do tipo String.
	- `sum(iterable)` : Soma todos os itens de um objeto iterável.
	- `super()` : Retorna um objeto que representa a classe-pai.
	- `tuple()` : Instancia um novo objeto do tipo tupla.
	- `type(object)` : Retorna o tipo do objeto especificado.
	- `vars(object)` : Retorna um dicionário contendo as propriedades de um objeto.
	- `zip(iterables..)` : Retorna um objeto iterável contendo tuplas, agrupando na mesma tupla os itens com os mesmos índices nos iteráveis originais.

- ### Orientação a Objetos:
	- **Sintaxe básica:**
		<pre><code>
		class Dog:
		    def __init__(self, name, age):
		        self.name = name
			self.age = age
		    def noise(self):
		    	return "Au Au"
		</code></pre>
		
	- A palavra chave `self` faz referência a uma instância da classe, assim, variando de objeto para objeto.
	- Os atributos precisam ser passados diretamente através da instanciação de um objeto.
	- O método `__init__(self)` representa o método construtor.
		<pre><code>
		class People:
			# atributo de classe
			this_year = 2020
			def __init__(self, name, age):
				self.name = name
				self.age = age
			def get_born_year(self):
				return self.this_year - self.age
		</code></pre>
	- Após isso, um objeto desta classe pode ser instanciado como: `people = People('Guilherme', 18)`.
	- É possível, assim como um atributo de classe, criar um método de classe, que será referenciado pela própria classe, e não por uma instância dela, através do decorator `@classmethod`. Ao invés da keyword `self` usa-se, por convenção, a keyword `cls`, que faz referência a própria classe.
	
		
	- **Métodos Estáticos**
		- Recebe um decorator `@staticmethod`. Não requer uma instância de classe nem a classe em si. Altera algum comportamento interno da classe ou provê utilitários que serão consumidos pela classe, como por exemplo, gerando um código identificador para uma classe Pessoa.
		- Por mais que não seja possível usar `self` nem `cls` em sua definição, um método estático pode ser invocado tanto como método de classe quanto como método de instância.
		
	- **Métodos Getters e Setters**
		- Métodos que interagem diretamente com atributos de classe.
		- Getters são definidos através do decorator `@property` e Setters através do decorator `@<nome_do_atributo>.setter`.
		- Por convenção, usa-se o nome do atributo com underscore (_) no retorno do getter.
		<pre><code>
		class People:
			# atributo de classe
			this_year = 2020
			def __init__(self, name, age):
				self.name = name
				self.age = age
			@property
			def get_name(self):
				return self._name
			@property
			def get_age(self):
				return self._age
			@name.setter
			def set_name(self, new_name):
				self._name = new_name
		</code><</pre>
		
	- **Encapsulamento**
		- Oculta partes do código para proteção contra interferência externa;
		- Diferentemente de outras linguagens de programação que suportam OO, como Java, C++, PHP, etc., Python não tem uma declaração explícita para encapsulamento, como as keywords `private`, `public`, `protected`. Ao invés disso, usam-se algumas convenções para definir a visibilidade dos métodos e atributos, que utilizam o underscore(_).
		- Para explicitar que determinado método ou atributo é protegido, usa-se um underscore (_) na frente do nome.
		- Para explicitar fortemente que determinado método ou atributo é privado, usa-se dois underscore (_) na frente do nome.
		- Ainda assim, é possível utilizá-lo em qualquer lugar do código, entretanto, não é uma prática recomendada.
	
	- **Associação**
		- Tipo de relacionamento onde uma classe está associada com outra, porém, nenhuma das duas classes tem dependência entre si.
		<pre><code>
		class Writer:
			def __init__(self, name):
				self.__name = name
				self.__tool = None
			@property
			def get_name(self):
				return self.__name
			@property
			def get_tool(self)
				return self.__tool
			@tool.setter
			def set_tool(self, tool):
				self.__tool = tool
		class Pen:
			def __init__(self, color):
				self.__color = color
			@property
			def get_color(self):
				return self.__color	
			def write(self):
				return 'writing...'
		writer = Writer('John')
		pen = Pen('blue')
		writer.tool = pen
		writer.tool.write()
		Output: 'writing...'
		</code><</pre>
	
	- **Agregação**
		- Tipo de relacionamento onde um objeto possui outros objetos, e ele não depende desses objetos para existir.
		- Por exemplo, uma Gaveta pode conter Meias, mas a Gaveta não é feita de Meias. Ou seja, mesmo sem Meias a Gaveta ainda existirá.
		<pre><code>
		class Cart:
			def __init__(self):
				self.products = []
			def insert_product(self, product):
				self.products.append(product)
			def list_products(self):
				for product in self.products:
					print(product.name)
		class Product:
			def __init__(self, name, value):
				self.__name = name
				self.__value = value
		cart = Cart()
		p1 = Product('t-shirt', 30)
		p2 = Product('shoes', 200)
		cart.insert_product(p1)
		</code><</pre>
		
	- **Composição**
		- Relação que ocorre quando um objeto é formado por outros objetos. Ou seja, suas partes o compõem, sem elas o objeto não existe.
		<pre><code>
		class Customer:
			def __init__(self, name):
				self.name = name
				self.address = []
			def insert_address(self, city):
				self.address.append(Address(city))
		class Address:
			def __init__(self, city):
				self.city = city
		</code><</pre>
		
- ### Date and Time
	- Para utilizar essas funcionalidades, deve-se realizar a importação do módulo `datetime` ou do módulo `time`.
	- Ao utilizar o método `time()` do módulo time, o retorno será o número de segundos que se passaram desde a Epoch, ou seja, 1 de janeiro de 1970.
	- Após obter esse número, utilizado em um grande número de sistemas legado, é possível convertê-lo para um padrão "legível", passando-o como parâmetro para o método `fromtimestamp()` do módulo `datetime`.
	- O método `fromtimestamp` retorna um objeto de data com uma série de atributos, sendo eles: dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second.
	- Com o método `timedelta(days=)`, é possível criar um objeto comparativo de datas.
	- O método `today()` do módulo `datetime` retorna o ano, mês e dia atuais, no momento da execução do código.

- ### Boas práticas
	Saber construir código e fazê-lo funcionar perfeitamente não são skills suficientes para ser um bom desenvolvedor; é preciso desenvolver um código dentro dos padrões reconhecidos pela linguagem, para que o processo de manutenção seja facilitado. Em Python, a convenção de escrita de código é chamada [PEP8](https://www.python.org/dev/peps/pep-0008/).
	- #### Estruturas de Projetos
		Um código bem estruturado é aquele que é limpo, de fácil compreensão, com a lógica explícita e consisa e bem organizado, com seus arquivos e pastas devidamente organizados. Assim, aos olhos de outros programadores, é fácil compreender o que cada trecho do código faz, o porquê de ele estar ali, como o faz, etc. Uma dica primordial é nomear arquivos com nomes significativos, como por exemplo, multiplicacao.py, para um script que executa multiplicações; se criarmos vários arquivos que executam operações matemáticas, por que não criar uma pasta chamada matematica?
	
	- #### Organização de módulos
		Uma boa prática para definição de módulos é **jamais** misturar nomes de arquivos com namespace (pasta onde se encontra o arquivo), evitando uma redundância na hora de invocar o módulo, do tipo: namespace.namespace_nome. Além de melhorar a visibilidade, o nome da pasta em si ganha maior importância.
	
	- #### Organização de pacotes
		É importante destacar que **módulos** são os arquivos Python únicos (com extensão .py), enquanto seu conjunto recebe o nome de **pacote**. Por definição, toda pasta que contenha o arquivo de inicialização nomeado como `__init__.py` é considerado um pacote, sendo esse arquivo o primeiro a ser iniciado. Uma boa prática é deixar este arquivo em branco dentro do pacote, dessa forma, não haverá nenhum código nele a ser executado ao se fazer uma chamada para qualquer módulo dentro desse pacote.
		
	- #### Estrutura de um repositório Git
		O Python é, atualmente, uma das linguagens mais utilizadas pelos desesnvolvedores ao redor do mundo, por fatores como facilidades no desenvolvimento e bom poder de processamento; porém, muitos apontam o principal motivo como sendo o fato de que Python é uma linguagem de código aberto, ou seja, qualquer desenvolvedor no mundo pode colaborar com o lançamento de novos pacotes e o aperfeiçoamento da linguagem em si, se tornando desnecessário "reinventar a roda". A tecnologia mais popular atualmente para código aberto é o Git, sendo a plataforma mais popular o GitHub.
		
		Os repositórios Git são geralmente organizados da seguinte forma:
		1. Título do projeto
		2. Descrição do projeto
		3. Arquivos do projeto
		4. README.md (leia-me)
		
		Essa descrição facilita a compreensão do projeto por parte de qualquer desenvolvedor que deseje colaborar; quanto maior o projeto, mais complexa a compreensão se torna e mais importante é a organização da estrutura.
	- #### Arquivos
		**README.md**: é o arquivo principal do projeto, que irá fornecer a qualquer um que esteja visitando o repositório o que está sendo feito, dicas de como utilizar, quais os objetivos, ou seja, as principais informações a respeito do projeto.
		
		**LICENSE.md**: é o arquivo que define quais são as licenças para a utilização do código. Por se tratar de código aberto, é importante definir a licença mais liberal possível, para explicitar que qualquer um está autorizado a utilizar seu projeto e eventualmente melhorá-lo.
		
		**setup.py**: é o arquivo de instalação do projeto.
		
		**requirements.txt**: Eventualmente, enquanto trabalhamos com Python, estaremos também utilizando código escrito por terceiros em pacotes. Assim, com esse arquivo, estamos explicitando quais são os requisitos para utilizar nosso código.
		
	- #### Pastas
		**docs**: Em projetos de médio e grande porte, é importante dispôr de uma documentação robusta, que irá informar ao usuário do projeto acerca do funcionamento do mesmo, ou mesmo servir de guia para auxiliar na manutenção. Nesta pasta, toda documentação será armazenada.
		
		**tests**: Um erro de sintaxe é diferente de um erro de semântica, ou seja, um código que roda não é sinônimo de código que funciona. Por isso, o desenvolvedor deve testá-lo, a fim de garantir que a saída produzida é igual a esperada. Nesta pasta, caso existam arquivos de teste automatizado, os mesmos são armazenados.
		
		**nome_do_pacote**: É a pasta que contém os módulos propriamente ditos. Um bom exemplo de repositório pode ser visto nesse [link](https://github.com/navdeep-G/samplemod).
		
		
## Data Science
- ### Importância do uso de dados
	Nos dias atuais, o conceito de Big Data está mais presente do que nunca; cada vez mais um volume imenso de dados é gerado pelos usuários de todos os tipos de plataformas digitais, como Facebook, Twitter, Tinder, Google, YouTube, etc., porém, estes dados por si só não nos dizem nada, se não forem tratados corretamente, não fornecerão nenhum insight e não possuirão valor algum. É importante que o cientista de dados saiba tratar esses dados corretamente, seja limpando-os, verificando se estão consistentes, tratando valores faltantes, etc.; além disso, nem sempre os dados estarão dispostos em uma estrutura bem definida, como tabelas de bancos de dados relacionais ou arquivos do Excel, eles também podem ser arquivos de áudio, vídeo, texto em linguagem natural, etc.
	
	O processo de ciência de dados, todavia, vai muito além de tratar esses dados em uma forma "legível" de visualização, seja para obter algum dado ou valor, também envolve fazer as perguntas corretas aos dados, elaborar as hipóteses e as validar. Algumas perguntas bastante válidas nesse processo são: "o que eu quero aprender com esses dados?", "que tipo de problema eu quero solucionar com o processamento desses dados?", "que ações ou decisões serão feitas a partir dos insights obtidos?".
	
- ### Principais conceitos de Data Science
	- Data Science é uma interseção entre três grandes áreas: matemática, tecnologia e negócios, além também de conhecimento especializado;
	- É o processo de descoberta de padrões ocultos em grandes volumes de dados, sejam eles estruturados ou não. Estes dados são organizados em modelos que são capazes de explicar o passado ou prever o futuro;
	- **Data Mining**: Processo de analisar padrões ocultos de dados de acordo com diferentes perspectivas para categorizar em informações úteis;
	- Processos de análise de dados: envolve extração, transformação, limpeza, modelagem e visualização de dados.
	
- ### Objetivos específicos de Data Science
	- Explicar o passado, normalmente associado a técnicas de BI (Business Inteligence) e utilização de dados estruturados, focado em análise exploratória de dados para descoberta de novos padrões usando ferramentas estatísticas e visualização por meio de dashboards;
	- Prever o futuro, utilizando tećnicas estatísticas tradicionais ou algoritmos de Machine Learning, com o objetivo de extrair insights de dados, sejam eles estruturados ou não, identificando tendências ou fazendo previsões.

## Ferramentas e técnicas de Data Science
- ### Pandas
	- Veja a [documentação](https://pandas.pydata.org/docs/)
    
	- Possui duas classes principais: Series, formada por uma coluna e várias linhas, e DataFrame (conjunto de Series), formado por linhas e colunas.
    
	- Criando uma Series:
        `series = pd.Series([1,2,3,4])`. Para realizar consultas em uma Series, é possível utilizar os atributos `loc[]` e `iloc[]`, que retornam baseado no nome do label e na posição no índice do elemento, respectivamente.
    
	- Criando um DataFrame de uma dimensão:
       `dataframe = pd.DataFrame([1,2,3,4])`
        
	- Criando um DataFrame de mais de uma dimensão:
        `dataframe = pd.DataFrame({"Coluna 1": [1,2,3], "Coluna 2": [4,5,6]}, index=[1,2,3])`
                        
	#### Atributos do DataFrame:
	` dataframe.index` : retorna o valor de início e de fim do dataframe, assim como o step.
	` dataframe.columns` : retorna o nome das colunas do dataframe.
	` dataframe.values` : retorna todas as linhas presentes no dataframe.
	` dataframe.dtypes` : retorna o tipo de objeto que cada coluna do dataframe armazena.
	` dataframe.shape` : quantidade de linhas e colunas do DataFrame.

	#### Principais métodos do DataFrame:
		- `dataframe.apply()` : aplica um método para cada item do dataframe.
		- `dataframe.count()` : contagem de dados não-nulos.
	 	- `dataframe.describe()` : retorna um resumo estatístico dos dados.
		- `dataframe.drop()` : remove a coluna passada como parâmetro.
		- `dataframe.dropna()` : retorna as linhas que não contém um NaN.
		- `dataframe.fillna()` : preenche todos os valores NaN por um outro específico.
		- `dataframe.iloc[]` : verificação por posição no índice.
		- `dataframe.isna()` : indica quais valores do dataframe são NaN.
		- `dataframe.head()` : retorna um resumo com o número de linhas passado como parâmetro (5 por default).
		- `dataframe.loc[]` : verificação por nome do índice.
		- `dataframe.mean()` : verifica a média dos valores de cada coluna.
		- `dataframe.sort_values()` : ordenando em ordem crescente.
		- `dataframe.sort_values(ascending=False)` : ordenando em ordem decrescente.
		- `dataframe[dataframe['columns'] #condição lógica] ` : retorna os dados seguindo alguma condição lógica.
      	
	- Como tornar o código "pandorable"?
		- É uma prática ruim utilizar encadeamento de indexação, como df.loc["Washtenaw"]["Total Population"], porque o pandas irá trazer uma cópia de uma view do DataFrame, ocupando mais memória do que deveria;
		- Ao contrário do encadeamento de indexação, é uma boa prática aplicar encadeamento de métodos, possibilitando condensar várias operações em um DataFrame em uma única sentença;
      
- ### NumPy
	- Veja a [documentação](https://numpy.org/doc/stable/)
	
	- NumPy fornece uma estrutura semelhante às listas built-in do Python, porém, são muito mais eficientes computacionalmente, chamadas de array.
	
	- É utilizado para efetuar cálculos em arrays multidimensionais, sendo empregado em áreas como machine learning, data science, visão computacional, tarefas matemáticas complexas, etc.
	
	- Geralmente, o numpy é importado com o allias **np**.
	
	- #### Arrays NumPy
		- É a estrutura de dados mais importante fornecida pelo numpy. Consiste em uma tabela de elementos (geralmente números), sendo todos do mesmo tipo, e que são indexados por uma tupla de inteiros positivos. As dimensões são conhecidas como **eixos**, constituindo em uma lista de coordenadas, *e.g.*, `[1,2,1]`, sendo esta lista a posição de um ponto em um espaço tridimensional, como esse eixo tem 3 elementos, diz-se que possui um comprimento de 3. 
		
	- #### Criando um array
		`array = np.array([1,2,3])`.
		- Arrays podem ter várias dimensões, podendo representar, por exemplo, uma matriz, através de um array de duas dimensões. É possível definir o número de dimensões de um array através do atributo `ndim`.
		
			`array = np.array([1,2,3,4], ndim=5)`
			
			`output: array([[[[[1, 2, 3, 4]]]]])`
			
	- #### Indexação
		Assim como em listas, é possível acessar um elemento de um array passando diretamente o número do seu índice, por exemplo, `array[0]`. É importante, porém, atentar à indexação quando trabalhando com arrays de mais de uma dimensão, pois uma indexação simples, da mesma maneira da anterior, iŕa retornar a primeira linha da matriz, e não o primeiro elemento, sendo necessário especificar a coluna desejada também. Caso seja necessário retornar o primeiro elemento da primeira coluna, utiliza-se `array[0][0]` ou `array[0,0]`.
		
	- #### Slicing com arrays
		Podemos fragmentar um array atribuindo o início e o fim da partição, da seguinte forma: `new_array = array[0:10]`, ou seja, o array resultante terá todos os elementos do array original partindo do índice 0 e parando no índice 10, dando um step de 1. Podemos alterar o step para, ao invés de pegar todo elemento subsequente, capturar os elementos "pulando" de 2 em 2, por exemplo: `new_array = array[0:10:2]`. Para fazer o slicing em um array de duas dimensões, precisamos especificar qual será a linha pertencente ao array que queremos efetuar o slicing, por exemplo: se temos um array do tipo `np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])`, podemos escrever `arr[1, 1:4]` para obter todos os elementos do índice 1 até o índice 4, percorrendo a segunda linha do array.
		 
	- #### Tipos de dados
		- i - integer
		- b - boolean
		- u - unsigned integer
		- f - float
		- c - complex float
		- m - timedelta
		- M - datetime
		- O - object
		- S - string
		- U - unicode string
		- V - fixed chunk of memory for other type ( void )
		
		Podemos checar o tipo do dado através do atributo dtype. Além disso, esse atributo também pode ser usado para inicializar um array com um tipo arbitrário de dado, por exemplo: `np.array([1, 2, 3, 4], dtype='S')`, onde o array será criado contendo strings de números. Para os tipos i, u, f, S e U, nós podemos definir o tamanho em bytes, como por exemplo, ` np.array([1, 2, 3, 4], dtype='i4')`, criando um array de inteiros com 4 bytes de tamanho. Se quisermos converter o tipo de dado de um array já existente, podemos utilizar o método `astype(type)`, especificando o novo tipo de dado. 
		 
	- #### Métodos e atributos do array:
		- `np.empty(shape, dtype)` : Cria um array não-inicializado com shape e dtype especificados.
		- `np.floor` : Retorna uma versão arredondada do parâmetro, podendo ser um array ou apenas um número flutuante.
		- `np.ones(length)` : Retorna uma matriz quadrada, com tamanho definido, preenchida com uns.
		- `np.random.random((num_rows, num_columns))` : Retorna uma matriz, com formato especificado, preenchida com número aleatórios.
		- `array.reshape((new_format))` : Retorna um novo array formatado, baseado no array original. O formato do novo array deve ter relação com o formato do array original, de modo a evitar que existam valores em branco. Por exemplo, se o array original possuía formato (6,0), o novo formato deve abranger todos os valores sem possuir espaços não preenchidos, podendo ser, por exemplo, (3,2).
		- `array.shape` : Retorna as dimensões do array.
		- `np.zeros(length)` : Retorna uma matriz quadrada, com tamanho definido, preenchida com zeros.
		- É possível atribuir diretamente um valor ao array, através do seu índice. Por exemplo, em uma matriz 3x3, `matriz[0][0] = 4` irá atribuir 4 para o valor na posição (0,0).
		
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



	- ### Função de Etapa Binária
		- Funções binárias possuem gradiente da derivada = 0, ou seja, são incapazes de se aperfeiçoar através da correção do erro.
		- Classificador simples baseado em decisões binárias (sim ou não), seguindo a regra:
	
					f(x) = 1, x >= 0
					f(x) = 0, x < 0

	- ### Função Linear
  		- A derivada de uma função linear é constante, ou seja, não depende do valor de entrada x. Por isso, toda vez que efetuamos o backpropagation, o gradiente é o mesmo.
		- A função linear é definida como:
			
					f(x) = ax

	- ### Sigmóide
  		- A maior vantagem desta função linear é justamente o fato de que ela não é linear.
  		- A função essencialmente empurra os valores de Y para os extremos, sendo um atributo interessante quando se deseja classificar os valores dentro de uma classe específica.
  		- A função é problemática quando os valores do gradiente são muito próximos a zero, pois assim, a rede não está realmente aprendendo.
		- A função signóide é definida como:
		
					f(x) = 1 / (1 + e ^ -x)
  
 	- ### Tanh
  		- Basicamente, soluciona o nosso problema dos valores, sendo todos do mesmo sinal. Todas as outras propriedades são as mesmas da função sigmoide. É contínuo e diferenciável em todos os pontos. A função não é linear, então podemos fazer o backpropagation facilmente nos erros.
		- A função tanh é uma versão escalonada da sigmóide, sendo descrita como:
			
					tanh(x) = 2 / (1 + e ^ (- 2x)) -1

	- ### ReLU
  		- É a função de ativação mais utilizada atualmente na construção de redes neurais.
  		- Uma de suas vantagens é que ela não ativa todos os neurônios da rede simultâneamente, tornando a rede esparsa, eficiente e fácil para a computação.
		- Significa Unidade Linear Rectificada e pode ser descrita como:
	
					f(x) = max (0, x) 

	- ### Leaky ReLU
  		- A função Leaky ReLU não passa de uma versão melhorada da função ReLU. Na função ReLU, o gradiente é 0 para x < 0, o que fez os neurônios morrerem por ativações nessa região. Leaky ReLU ajuda a resolver este problema. Em vez de definir a função Relu como 0 para x inferior a 0, definimos como um pequeno componente linear de x. Pode ser definido como:

					f(x) = ax, x < 0f(x) = x, x > = 0
					
## Git
- Comandos básicos:
	- git init: inicia um repositório local;
	- git status: verifica o estado do contâiner de mudanças;
	- git add: adiciona um arquivo ou diretório ao contâiner;
		- O comando git add se faz necessário não apenas ao adicionar um arquivo novo ao git, mas também para atualizar o arquivo com novas mudanças.
	- git commit -m "mensagem": realiza o commit da mudança efetuada;
	- git push: envia as mudanças locais commitadas para o repositório remoto;
	- git remote add origin <link do repositório remoto>: adiciona um origin para o repositório se não existe nenhum. Isso é útil quando se deseja iniciar um repositório localmente com "git init" e, em seguida, é necessário enviá-lo para um repositório remoto mais tarde;
	- git branch: verifica onde está o HEAD e em qual branch do git;
	- git diff: verifica a diferença entre a última mudança e as mudanças atuais;
	- git remote -v: retorna informações do repositório remoto;

- Controle de versões:
	- git log: retorna uma lista, identificando os commits efetuados através do retorno de um hash, o autor e a data, bem como a branch;
	- Ao efetuar uma mudança, o git rastreia esta mudança através da identificação dos contêineres dos commits, armazenando apenas as mudanças que foram feitas e tornando possível reverter o código para um estado passado;
	- Para recuperar uma versão passada, devemos apontar o HEAD (estado atual) para o respectivo commit, dessa maneira: `git checkout <código do commit>`;
	- Para retornar ao último commit, usa-se `git checkout master`.
	- Se quisermos descartar as mudanças feitas no arquivo, usa-se `git checkout <nome do arquivo>`.
	- Se, após adicionarmos as mudanças ao git, quisermos desfazer essas mudanças, podemos usar `git reset HEAD <nome do arquivo>` para desfazê-las;
	- Para voltar a um commit anterior, excluindo o atual, usa-se `git reset --hard <código do commit>`;
	
- Criando branches e merges:
	- Criar uma branch (ou ramificação) permite que testes e modificações sejam feitas sem interferir na branch principal (master);
	- Para criar uma nova branch, usa-se `git checkout -b <nome da branch>`;
	- A branch criada herda todos os commits da branch master;
	- É importante destacar que, antes de ser feito o merge, se retornarmos a branch master, todas as mudanças feitas nas outras branchs irão "sumir".
	- Para retornar à branch master, usa-se `git checkout master`.
	- Para efetuar a junção do branch criado com o branch master, é necessário estar na master. Após isso, usa-se `git merge <nome da branch>` para fazer o merge;

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
