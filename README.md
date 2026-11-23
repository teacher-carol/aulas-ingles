# Aulas de inglês: atividades interativas

Atividades de casa dos alunos, publicadas pelo GitHub Pages.

## Padrão de pastas

```
turma-x/AAAA-MM-DD-tema/index.html
```

Exemplo: `turma-a/2026-11-24-verbs-actions/index.html`

**Nunca usar o nome do aluno** em pastas, arquivos ou textos. Cada aluno tem um código de turma (turma-a, turma-b...). Quem é quem fica só com a professora.

**Índice da professora:** `https://teacher-carol.github.io/aulas-ingles/professora/` lista todas as aulas por turma.

Cada aula tem duas páginas:

- `turma-x/AAAA-MM-DD-tema/` → **tarefa de casa** (o link que vai para o aluno)
- `turma-x/AAAA-MM-DD-tema/aula/` → **página da aula** (a professora compartilha a tela)

A pasta `ferramentas/` tem o gerador das páginas (Python). Cada turma tem o seu gerador (`ferramentas/turma_a.py`, `ferramentas/turma_b.py`). Depois de criar aulas novas, rodar `python3 ferramentas/indice.py` para atualizar o índice.

Link que o aluno recebe:

```
https://teacher-carol.github.io/aulas-ingles/turma-a/2026-11-24-verbs-actions/
```

## Regras

- Uma pasta por turma/aluno, com código (turma-a, turma-b), nunca com o nome.
- Uma pasta por atividade, começando pela data da aula (assim fica em ordem).
- O arquivo sempre se chama `index.html`.
- Nunca colocar nome, telefone ou dados pessoais do aluno nos arquivos: o site é público.

## Conteúdo e propriedade intelectual

O site é público, então:

- Todo o conteúdo é **original**: textos, frases, exercícios e histórias escritos para as aulas.
- **Nada externo**: sem fontes da internet, imagens, músicas, vídeos, personagens ou trechos de livros, sites e materiais de outras plataformas. As páginas usam só as fontes do próprio celular e a voz do próprio aparelho.
- Se um dia for indispensável usar algo de fora, só com licença que permita, e com o crédito na seção **Referências** abaixo.

## Referências

Nenhuma. Todo o conteúdo deste repositório é original.

## Progresso do aluno

Cada atividade tem, na tela final:

- **Melhor pontuação**, salva no próprio celular do aluno.
- **Botão "Send my score to the teacher"**, que abre o WhatsApp com a pontuação de cada jogo pronta para enviar.

Para o botão já abrir a conversa com a professora, preencher no fim do arquivo:

```js
var TEACHER_PHONE = '55DDDNUMERO';
```

Vazio, o WhatsApp abre e o aluno escolhe o contato.
