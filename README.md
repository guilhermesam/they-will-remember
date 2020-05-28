# They Will Remember You!

Planejamento de estudos, com prazo de validade no final do tempo de graduação. O que virá após isso, desejo muito saber. Esta ideia foi inspirada no repositório de [@jwashan](https://github.com/jwasham/coding-interview-university)!

![Warriors](https://www.tec.com.pe/wp-content/uploads/2014/09/LoL-Imagine-Dragons-Warrior-2.jpg)

## O que é isso?

Este repositório surgiu da necessidade mental de um cronograma bem definido acerca do trajeto a ser percorrido para alcançar o objetivo de ser um engenheiro de software ou. O conteúdo teórico descrito pelo cronograma aborda:

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
    - [Pandas](#pandas)
    - [NumPy](#numpy)

## Python
- ### Estruturas
    - ### Listas
    - ### Dicionários
    - ### Tuplas
- ### Built-in Functions
- ### Funções lambda
- ### List Comprehension
- ### Pandas
    - Possui duas classes principais: Series (unidimensional) e DataFrame (pluridimensional).
    
    - Criando um DataFrame de uma dimensão:
        dataframe = pd.DataFrame([1,2,3,4])
        
    - Criando um DataFrame de mais de uma dimensão:
        dataframe = pd.DataFrame({"Coluna 1": [1,2,3],
                          "Coluna 2": [4,5,6]},
                        index=[1,2,3])
                        
    - Atributos do DataFrame:
        -[] dataframe.index: retorna o valor de início e de fim do dataframe, assim como o step.
        -[] dataframe.columns: retorna o nome das colunas do dataframe.
        -[] dataframe.values: retorna todas as linhas presentes no dataframe.
        -[] dataframe.dtype: retorna o tipo de objeto que cada coluna do dataframe armazena.
        
    - Principais métodos do DataFrame:
        -[] dataframe.head(): retorna um resumo com o número de linhas passado como parâmetro (5 por default).
        -[] dataframe.describe(): retorna um resumo estatístico dos dados.
        
      
- ### NumPy
- ### Web Scraping
