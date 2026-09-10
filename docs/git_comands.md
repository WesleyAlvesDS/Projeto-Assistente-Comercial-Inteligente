# Git: comandos e fluxo de trabalho

Guia rápido dos comandos mais usados no projeto. Execute os comandos a partir da pasta do repositório.

## Índice

- [Comandos principais](#comandos-principais)
- [Fluxo básico](#fluxo-básico)
- [Resumo](#resumo)

## Comandos principais

### `git init`
Cria um repositório Git dentro da pasta do projeto.

- Serve para iniciar o controle de versão local.
- Depois disso, o Git começa a monitorar os arquivos da pasta.

Exemplo:
```bash
git init
```

### `git add`
Adiciona arquivos à área de preparação (staging area), ou seja, marca quais arquivos serão incluídos no próximo commit.

- `git add .` adiciona todos os arquivos da pasta atual.
- `git add nome-do-arquivo.txt` adiciona apenas um arquivo.

Exemplo:
```bash
git add .
```

### `git commit`
Salva as alterações feitas e adicionadas no repositório com uma mensagem descritiva.

- É como criar um "ponto de salvamento" do projeto.
- A mensagem deve explicar o que foi alterado.

Exemplo:
```bash
git commit -m "Primeiro commit"
```

### `git branch`
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

### `git merge`
Une alterações de uma branch em outra.

- Normalmente usamos para juntar a branch de desenvolvimento na branch principal.
- Exemplo: depois de terminar uma funcionalidade, você faz o merge dela na branch `main`.

Exemplo:
```bash
git checkout main
git merge feature-nova
```

### `git push`
Envia os commits locais para um repositório remoto, como GitHub.

- Permite compartilhar o projeto com outras pessoas.
- Geralmente é usado depois de um commit.

Exemplo:
```bash
git push origin main
```

### `git pull`
Baixa as alterações do repositório remoto para o local.

- Atualiza sua cópia do projeto com o que foi enviado por outras pessoas.
- Geralmente é usado antes de continuar trabalhando.

Exemplo:
```bash
git pull origin main
```

### Issues (GitHub)
As Issues são tarefas, bugs, melhorias ou dúvidas registradas dentro de um repositório no GitHub.

- Servem para organizar o trabalho do projeto.
- Podem ser usadas para registrar bugs, ideias de funcionalidade ou pendências.
- Cada issue pode ter título, descrição, labels, responsáveis e status.
- É uma forma de acompanhar o que precisa ser feito sem misturar com o código.

Exemplo de uso:
- "Corrigir erro ao cadastrar cliente"
- "Adicionar filtro por data na tabela"
- "Melhorar a interface da página inicial"

Dica:
- Crie uma issue para cada tarefa ou problema.
- Depois, você pode fechar a issue quando a solução for concluída.

## Fluxo básico

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

## Resumo

- `git init`: inicia o repositório local.
- `git add`: prepara arquivos para commit.
- `git commit`: salva uma versão do projeto.
- `git branch`: cria e gerencia branches.
- `git merge`: une branches.
- `git push`: envia para o GitHub/remoto.
- `git pull`: recebe atualizações do remoto.
- `Issues`: organiza tarefas, bugs e melhorias no GitHub.

Esse é o fluxo básico do Git usado em projetos de desenvolvimento.