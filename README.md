# Aulas de inglês: atividades interativas

Atividades de casa dos alunos, publicadas pelo GitHub Pages.

## Padrão de pastas

```
nome-do-aluno/AAAA-MM-DD-tema/index.html
```

Exemplo: `miguel/2026-11-18-past-simple/index.html`

Link que o aluno recebe:

```
https://<usuario>.github.io/aulas-ingles/miguel/2026-11-18-past-simple/
```

## Regras

- Uma pasta por aluno, em minúsculas e sem acento.
- Uma pasta por atividade, começando pela data da aula (assim fica em ordem).
- O arquivo sempre se chama `index.html`.
- Nunca colocar sobrenome, telefone ou dados pessoais do aluno nos arquivos: o site é público.

## Progresso do aluno

Cada atividade tem, na tela final:

- **Melhor pontuação**, salva no próprio celular do aluno.
- **Botão "Send my score to the teacher"**, que abre o WhatsApp com a pontuação de cada jogo pronta para enviar.

Para o botão já abrir a conversa com a professora, preencher no fim do arquivo:

```js
var TEACHER_PHONE = '55DDDNUMERO';
```

Vazio, o WhatsApp abre e o aluno escolhe o contato.
