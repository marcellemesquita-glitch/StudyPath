# StudyPath - Organizador de Estudos Autodidata

## O que e o app?

Um aplicativo web que ajuda pessoas que estudam por conta propria a organizarem seus estudos. O usuario chega, conta o que quer aprender, e o app monta um plano de estudos personalizado com materiais, cronograma e acompanhamento do progresso.

---

## Funcionalidades Principais

### 1. Primeiro Acesso - Definindo o Objetivo

Quando o usuario entra pela primeira vez, ele responde um questionario simples:

- **O que voce quer aprender?** (ex: programacao, ingles, marketing digital)
- **Por que voce quer aprender isso?** (ex: mudar de carreira, hobby, crescer no trabalho)
- **Qual seu nivel atual?** (nunca estudei / sei o basico / ja tenho experiencia)
- **Quanto tempo por dia voce pode estudar?** (30min / 1h / 2h / mais de 2h)
- **Qual seu prazo?** (sem pressa / 3 meses / 6 meses / 1 ano)

Com essas respostas, o app gera um plano de estudos personalizado.

### 2. Plano de Estudos e Materiais

Depois do questionario, o app entrega:

- **Trilha de aprendizado**: os temas organizados em ordem logica (do basico ao avancado)
- **Materiais sugeridos**: links para videos, artigos, cursos gratuitos e livros sobre cada tema
- **Cronograma semanal**: distribui os estudos nos dias da semana de acordo com o tempo disponivel

O usuario pode ajustar tudo manualmente se quiser.

### 3. Diario de Estudos

Um espaco onde o usuario registra o que estudou no dia:

- **O que estudei hoje?** (campo de texto livre)
- **Quanto tempo estudei?** (em minutos/horas)
- **Como me senti?** (facil / normal / dificil) - pode ser com emojis ou icones
- **Anotacoes livres**: duvidas, insights, links uteis

Funciona como um registro pessoal que ajuda a manter a consistencia.

### 4. Dashboard de Evolucao

Uma tela visual onde o usuario ve seu progresso:

- **Sequencia de dias estudados** (tipo o "streak" do Duolingo)
- **Horas totais de estudo**
- **Porcentagem da trilha concluida** (barra de progresso)
- **Calendario de atividade** (tipo o quadro verde do GitHub - mostra os dias que estudou)
- **Grafico simples**: horas estudadas por semana

---

## Telas do App

| Tela | O que mostra |
|------|-------------|
| **Login/Cadastro** | Entrar com email e senha |
| **Questionario Inicial** | Perguntas para definir o objetivo |
| **Minha Trilha** | O plano de estudos com os temas e materiais |
| **Diario** | Formulario para registrar o estudo do dia + historico |
| **Dashboard** | Graficos e numeros do progresso |
| **Perfil/Config** | Ajustar dados pessoais e preferencias |

---

## Como vai funcionar por tras (Visao Tecnica Simplificada)

### Tecnologias

| Parte do App | Tecnologia | Para que serve |
|-------------|-----------|---------------|
| **Parte visual (frontend)** | HTML + CSS + JavaScript | O que o usuario ve e interage |
| **Logica do app (backend)** | Python com Flask ou Django | Processa as informacoes, monta o plano, salva dados |
| **Inteligencia Artificial** | API da OpenAI (ChatGPT) ou Claude (Anthropic) | Gera trilhas personalizadas, sugere materiais e ajusta o plano |
| **Biblioteca Python p/ IA** | `openai` (para ChatGPT) ou `anthropic` (para Claude) | Pacotes Python que conectam o app com a IA. Instala com pip e chama no codigo |
| **Banco de dados** | SQLite (inicio) ou PostgreSQL | Guarda os dados dos usuarios, diarios, planos |
| **Hospedagem** | Render, Railway ou PythonAnywhere | Deixa o app acessivel na internet |

### Estrutura de Pastas (simplificada)

```
studypath/
├── app.py                  # Arquivo principal do app
├── templates/              # As telas em HTML
│   ├── login.html
│   ├── questionario.html
│   ├── trilha.html
│   ├── diario.html
│   └── dashboard.html
├── static/                 # Estilos e imagens
│   ├── style.css
│   └── imagens/
├── models.py               # Define como os dados sao guardados
├── routes.py               # Define o que acontece em cada pagina
└── requirements.txt        # Lista de pacotes Python necessarios
```

---

## Onde a IA Entra no App

A inteligencia artificial e o coracao do app. Ela atua em varios momentos:

| Momento | O que a IA faz | Como funciona |
|---------|---------------|---------------|
| **Montagem da trilha** | Recebe as respostas do questionario e gera uma trilha de estudos personalizada com topicos em ordem logica | O app manda as respostas do usuario para a API (ChatGPT ou Claude) e recebe de volta a trilha organizada |
| **Sugestao de materiais** | Sugere videos, artigos, livros e cursos gratuitos para cada topico da trilha | A IA recomenda materiais com base no tema e no nivel do usuario |
| **Ajuste do plano** | Se o usuario esta achando facil ou dificil demais, a IA reajusta o ritmo e os materiais | Com base nos registros do diario (dificuldade, tempo), a IA adapta o cronograma |
| **Resumo semanal** | Gera um resumo do que o usuario aprendeu na semana com dicas para a proxima | A IA le as entradas do diario e cria um feedback personalizado |
| **Tirar duvidas** | O usuario pode perguntar duvidas sobre o que esta estudando diretamente no app | Um chat simples integrado com a API da IA |

### Bibliotecas Python para IA

Para conectar o app com a IA, basta instalar um pacote e usar no codigo. Exemplo:

**Opcao 1 - Usando OpenAI (ChatGPT):**
```bash
pip install openai
```
```python
from openai import OpenAI

client = OpenAI(api_key="sua-chave-aqui")

resposta = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Voce e um assistente de estudos."},
        {"role": "user", "content": "Crie uma trilha de estudos de Python para iniciante, 1h por dia, em 3 meses."}
    ]
)

trilha = resposta.choices[0].message.content
```

**Opcao 2 - Usando Anthropic (Claude):**
```bash
pip install anthropic
```
```python
from anthropic import Anthropic

client = Anthropic(api_key="sua-chave-aqui")

resposta = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    system="Voce e um assistente de estudos.",
    messages=[
        {"role": "user", "content": "Crie uma trilha de estudos de Python para iniciante, 1h por dia, em 3 meses."}
    ]
)

trilha = resposta.content[0].text
```

> **Resumo**: sao so 2 passos - instalar o pacote (`pip install`) e chamar no codigo.
> A IA recebe um texto (o pedido) e devolve outro texto (a resposta). Simples assim.

### Como funciona na pratica (simplificado)

```
Usuario responde o questionario
        |
        v
App envia as respostas para a API da IA (ex: ChatGPT ou Claude)
        |
        v
IA retorna uma trilha de estudos personalizada
        |
        v
App salva a trilha no banco de dados e mostra para o usuario
```

> **Custo**: As APIs de IA cobram por uso. No inicio, o custo e baixo (centavos por requisicao).
> Para manter o app gratuito, da para limitar o numero de vezes que a IA e chamada por usuario por dia.

---

## Ordem de Desenvolvimento (Passo a Passo)

### Fase 1 - Base (MVP - versao minima funcional)
1. Criar o cadastro e login do usuario
2. Montar o questionario inicial
3. Gerar uma trilha de estudos simples baseada nas respostas
4. Permitir que o usuario marque topicos como concluidos

### Fase 2 - Diario e Acompanhamento
5. Criar o diario de estudos (formulario + historico)
6. Montar o dashboard com metricas basicas (dias estudados, horas, progresso)

### Fase 3 - Melhorias
7. Sugestao de materiais automatica (integracao com APIs de busca ou curadoria manual)
8. Calendario visual de atividade
9. Notificacoes/lembretes por email
10. Melhorar o visual do app

### Fase 4 - Extras (futuro)
11. Usar inteligencia artificial para sugerir materiais melhores e ajustar o plano
12. Gamificacao (pontos, conquistas, niveis)
13. Comunidade (ver o progresso de outros usuarios, grupos de estudo)
14. App mobile

---

## Dados que o App Precisa Guardar

### Usuario
- Nome, email, senha
- Respostas do questionario
- Data de cadastro

### Trilha de Estudo
- Tema principal
- Lista de topicos (com ordem e status: pendente/concluido)
- Materiais vinculados a cada topico

### Diario
- Data da entrada
- O que estudou (texto)
- Tempo de estudo
- Nivel de dificuldade
- Anotacoes

---

## Diferenciais que Podem Destacar o App

- **Simplicidade**: a maioria dos apps de estudo sao complicados demais. Esse e direto ao ponto.
- **Personalizacao real**: o plano e feito sob medida, nao e generico.
- **Foco no autodidata**: nao e uma plataforma de cursos, e um organizador para quem ja busca conteudo por conta propria.
- **Diario como habito**: o registro diario cria consistencia, que e o maior desafio de quem estuda sozinho.

---

## Proximos Passos Imediatos

1. Decidir se vai usar **Flask** (mais simples, mais liberdade) ou **Django** (mais estruturado, mais coisas prontas)
2. Criar o projeto base com a primeira tela (cadastro/login)
3. Montar o questionario e salvar as respostas
4. Gerar a primeira versao da trilha de estudos

---

*Documento criado em: 15/02/2026*
