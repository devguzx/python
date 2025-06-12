#  Introdução ao Versionamento de Código

Este documento tem como objetivo compartilhar os conceitos e comandos básicos que aprendi sobre **versionamento de código**, utilizando o **Git** e o **GitHub**.  
A ideia é compartilhar o conhecimento adquirido de forma simples, prática e acessível, tanto pra mim quanto pra quem quiser aprender junto!

---

##  O que é Versionamento de Código?

Versionamento de código é uma técnica usada para **registrar todas as alterações feitas em um projeto ao longo do tempo**.  
Com isso, é possível:

- Voltar para versões anteriores do projeto
- Trabalhar em grupo de forma segura
- Criar testes sem afetar o código principal
- Documentar o histórico do projeto

---

##  Git vs GitHub

- **Git** é o programa que a gente instala no PC pra controlar as versões do código. Funciona no terminal.
- **GitHub** é tipo uma “nuvem” onde a gente pode guardar esses códigos e compartilhar com outras pessoas.
- O Git cuida do histórico, o GitHub é onde a gente publica isso online.


---

##  Conceitos que aprendi

- **Repositório (repo)**: local onde o projeto e seu histórico são salvos.
- **Commit**: registro de uma mudança no código.
- **Branch**: linha paralela de desenvolvimento.
- **Merge**: fusão de uma branch com outra.
- **Clone**: cópia de um repositório remoto.
- **Push/Pull**: envio e recebimento de alterações entre local e remoto.
- **.gitignore**: arquivo para ignorar arquivos desnecessários no versionamento.

---

##  Comandos Básicos

```bash
git init

git status

git add .

git commit -m "mensagem"

git remote add origin https://github.com/usuario/repositorio.git

git push -u origin main

git pull
```
## 📚 Referências Oficiais:
- [Documentação git](https://git-scm.com/doc)
- [Ducumentação gitHub](https://docs.github.com/pt)
