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

```
./bin/tp2 <solver> [opções]

Solvers:
  bnb           Branch and Bound.
  fptas <eps>   Full Polynomial-Time Approximation Scheme.
  greedy        Guloso 2-aproximado.

Opções:
  eps           Precisão para o FPTAS (0 < eps <= 1).
```
