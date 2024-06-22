# dio-twitter-py

Projeto criado durante o living code [Consumindo a API do Twitter com Python](https://docs.google.com/presentation/d/11DkkyQUIloVQLm8i6hN6w3xyUaP4WSRE/edit?usp=sharing&ouid=102662434190974209165&rtpof=true&sd=true). Criar um projeto prático com o objetivo de consumir a API REST do Twitter seguindo uma série de boas práticas e dicas foram apresentadas pelo expert. Entre elas o Tweepy, para reduzir a complexidade no consumo da API do Twitter.

A API do Twitter permite analisar o desempenho orgânico dos Tweets, permitindo ver uma série de métricas associadas a um determinado Tweet. Isso pode ser útil na tomada de decisões baseadas em dados sobre o desempenho de Tweets específicos. A pesquisa de Tweet é um método GET que retorna informações sobre um Tweet ou grupo de Tweets. As métricas estão disponíveis como parte do endpoint de pesquisa do Tweet.

## Índice

- [Tecnologias](#tecnologias)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Rodando a aplicação](#rodando-a-aplicação)
- [Rodando os testes](#rodando-os-testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Tecnologias 📚

- Python 3.12
- MongoDB
- Docker
- FastAPI

## Requisitos ✋

- Docker
- Docker compose

## Instalação 💽

Instale o [Docker](https://www.docker.com) e [Docker compose](https://docs.docker.com/compose/) no seu computador.

## Rodando a aplicação 🛸

```sh
poetry shell
python main.py


## Rodando os testes 

poetry shell
pytest

## Contribuição
Para contribuir com o projeto, por favor, siga as seguintes etapas:

Fork o repositório.
Crie uma branch para sua feature (git checkout -b feature/AmazingFeature).
Commit suas mudanças (git commit -m 'Add some AmazingFeature').
Push para a branch (git push origin feature/AmazingFeature).
Abra um Pull Request.

Relatorio desenvolvido por Cibele Gomes Domingos Moraes Lima