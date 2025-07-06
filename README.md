## Trabalho prático II - Algoritmos para problemas difíceis

Este trabalho visa implementar e comparar experimentalmente três soluções para o problema da mochila:

- Uma [solução exata](src/bnb.cpp) baseada em *Branch and Bound*.
- Um [FPTAs](src/fptas.cpp) (*Full Polynomial-Time Approximation Scheme*).
- Uma [solução gulosa](src/greedy.cpp) 2-aproximada.

### Instruções de compilação
Para compilar o projeto, basta executar o comando

```sh
make
```

na raiz do projeto. O executável final será gerado em `bin/tp2`.

### Modo de uso

*Modo de uso:*
```sh
./bin/tp2 <solver> [opções]
```

*Solvers:*
```sh
  bnb           Branch and Bound.
  fptas <eps>   Full Polynomial-Time Approximation Scheme.
  greedy        Guloso 2-aproximado.
```

*Opções:*
```sh
  eps           Precisão para o FPTAS (0 < eps <= 1).
```

*Saída: resposta,tempo,memória*
```sh
  resposta      Resposta do solver para a instância.
  tempo         Tempo gasto pelo solver em microssegundos.
  memória       Memória gasta pelo solver em KB.
```