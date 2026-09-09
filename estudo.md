# Git: explicação de cada comando e passo a passo

## 1) git init
Cria um repositório Git dentro da pasta do projeto.

- Serve para iniciar o controle de versão local.
- Depois disso, o Git começa a monitorar os arquivos da pasta.

Exemplo:
```bash
git init
```

## 2) git add
Adiciona arquivos à área de preparação (staging area), ou seja, marca quais arquivos serão incluídos no próximo commit.

- `git add .` adiciona todos os arquivos da pasta atual.
- `git add nome-do-arquivo.txt` adiciona apenas um arquivo.

Exemplo:
```bash
git add .
```

## 3) git commit
Salva as alterações feitas e adicionadas no repositório com uma mensagem descritiva.

- É como criar um "ponto de salvamento" do projeto.
- A mensagem deve explicar o que foi alterado.

Exemplo:
```bash
git commit -m "Primeiro commit"
```

## 4) git branch
Gerencia ramificações do projeto (branches).

- Permite criar versões diferentes do código ao mesmo tempo.
- Útil para desenvolver features sem mexer na branch principal.

Exemplos:
```bash
git branch
```
Lista as branches existentes.

```bash
git branch feature-nova
```
Cria uma nova branch chamada `feature-nova`.

## 5) git merge
Une alterações de uma branch em outra.

- Normalmente usamos para juntar a branch de desenvolvimento na branch principal.
- Exemplo: depois de terminar uma funcionalidade, você faz o merge dela na branch `main`.

Exemplo:
```bash
git checkout main
git merge feature-nova
```

## 6) git push
Envia os commits locais para um repositório remoto, como GitHub.

- Permite compartilhar o projeto com outras pessoas.
- Geralmente é usado depois de um commit.

Exemplo:
```bash
git push origin main
```

## 7) git pull
Baixa as alterações do repositório remoto para o local.

- Atualiza sua cópia do projeto com o que foi enviado por outras pessoas.
- Geralmente é usado antes de continuar trabalhando.

Exemplo:
```bash
git pull origin main
```

# Passo a passo de uso básico do Git

## Fluxo simples

1. Inicializar o repositório:
```bash
git init
```

2. Criar ou alterar arquivos no projeto.

3. Adicionar arquivos para o estágio:
```bash
git add .
```

4. Fazer o commit:
```bash
git commit -m "Mensagem do commit"
```

5. Ver as branches:
```bash
git branch
```

6. Criar uma branch nova:
```bash
git branch feature-login
```

7. Mudar para essa branch:
```bash
git checkout feature-login
```

8. Trabalhar na feature e fazer mais commits.

9. Voltar para a branch principal:
```bash
git checkout main
```

10. Juntar as alterações com merge:
```bash
git merge feature-login
```

11. Enviar para o GitHub:
```bash
git push origin main
```

12. Atualizar o projeto local com o que está no remoto:
```bash
git pull origin main
```

# Resumo

- `git init`: inicia o repositório local.
- `git add`: prepara arquivos para commit.
- `git commit`: salva uma versão do projeto.
- `git branch`: cria e gerencia branches.
- `git merge`: une branches.
- `git push`: envia para o GitHub/remoto.
- `git pull`: recebe atualizações do remoto.

Esse é o fluxo básico do Git usado em projetos de desenvolvimento.