# 💄 Lets Glow - Loja de Cosméticos e Beleza

## 📝 Dados do Cliente

- **Título do Projeto:** Lets Glow: uma loja de beleza e cosmético de revenda de produtos, com produtos, checkout de compra, endereço e contato  
- **Cliente:** Sarah Hesed Liima Santana  
- **CNPJ/CPF:** 40109764897  
- **Contato:** (19) 99636-1965  
- **Email:** letsglowmulher@gmail.com  

---

## 👨‍💻 Equipe de Desenvolvimento

| Nome                        | Curso                           | Disciplina                             |
|----------------------------|----------------------------------|----------------------------------------|
| Luan Marcos de Andrade Santos | Análise e Desenvolvimento de Sistemas | Programação Orientada a Objetos em Java |
| Gustavo Henrique dos Anjos | Ciência da Computação            | Programação Orientada a Objetos em Java |
| Murilo Alves de Godoy      | Ciência da Computação            | Programação Orientada a Objetos em Java |

- **Professor Orientador:** Kesed Rodrigues Julio

---

## 📌 Introdução

O problema do cliente é a baixa visibilidade e vendas. A solução proposta é a criação de uma loja online, que permitirá o cadastro de produtos e sua exibição organizada, permitindo futuramente o uso de tráfego pago para alavancar as vendas. O grupo será responsável apenas pela criação da loja.

---

## 🎯 Objetivo

### Objetivo da Loja

Oferecer produtos de beleza e cuidados pessoais de alta qualidade, acessíveis e cuidadosamente selecionados, promovendo autoestima, bem-estar e confiança com foco em tendências modernas e respeito à diversidade e à natureza.

### Finalidade

Criar uma experiência de compra online prática e encantadora, oferecendo não apenas produtos, mas também inspiração e valorização da beleza única de cada cliente.

---

## 📦 Escopo

- Criação de banco de dados com controle de estoque.
- Design visual atrativo para o site e produtos.
- Sistema de cadastro e login de usuários.
- Mecanismo automático de aprovação de compra.
- Interface intuitiva e responsiva.
- Exibição e retirada de produtos conforme estoque.

---

## 📋 Backlog do Produto

### 🔹 Requisitos Funcionais

- Cadastro de Produtos
- Carrinho de Compras
- Sistema de Pagamento (PIX, cartão, boleto)
- Cadastro de Usuários e Login
- Controle de Estoque
- Área Administrativa
- Integração com Frete (Correios/Melhor Envio)

### 🔸 Requisitos Não Funcionais

- Design Responsivo
- Segurança de Dados (HTTPS)
- Facilidade de Uso (UX/UI)

---

## 🗓️ Cronograma

[Jira Board do Projeto (SCRUM)](https://guanjos04.atlassian.net/jira/software/projects/SCRUM/boards/1?atlOrigin=eyJpIjoiNmE1YWU3ODM2Mzg1NDY5NThhMWM5ZDNlNTZmZmJjMGYiLCJwIjoiaiJ9)

---

## 🧪 Materiais e Métodos

### 🔹 Modelagem do Sistema

| Entidade     | Atributos |
|--------------|-----------|
| Usuário      | id, nome, email, senha, endereço, telefone |
| Produto      | id, nome, descrição, preço, imagens, categoria_id, estoque |
| Pedido       | id, usuario_id, data, status, valor_total |
| ItemPedido   | id, pedido_id, produto_id, quantidade, preco_unitario |
| Pagamento    | id, pedido_id, método, status_pagamento, data_pagamento |
| Categoria    | id, nome_categoria |
| Admin        | id, nome, email, senha |

---

## 💻 Tecnologias Utilizadas

### 🔧 Frontend

- HTML5, CSS3, JavaScript
- Framework: React.js ou JS puro com Bootstrap/Tailwind
- Bibliotecas: Axios, Swiper

### 🖥️ Backend

- PHP (Laravel ou PHP puro com MVC)
- Autenticação: JWT ou sessões
- Banco de Dados: MySQL ou PostgreSQL

### 🛠️ Outros

- Git + GitHub
- Hospedagem: Hostinger, Vercel, Heroku
- Pagamento: Mercado Pago, Stripe ou PagSeguro
- Frete: Correios API / Melhor Envio

---

## 🏛️ Arquitetura do Sistema

### MVC - Model View Controller

- **Model:** Acesso e manipulação dos dados
- **View:** Interface do usuário
- **Controller:** Gerenciamento das requisições e lógica de negócio

---

## 🧪 Protótipos das Telas

### 1. Tela Inicial (Home)
- Ver produtos em destaque
- Buscar produtos
- Acessar categorias

### 2. Página de Produto
- Ver detalhes e adicionar ao carrinho

### 3. Carrinho de Compras
- Ajustar quantidades, remover e finalizar compra

### 4. Login/Cadastro
- Criar conta ou autenticar

### 5. Checkout
- Informar endereço e pagamento

### 6. Painel Administrativo
- Gerenciar produtos, usuários e pedidos

---

## ✅ Conclusão

### Impacto do Sistema

- Maior alcance e visibilidade dos produtos
- Facilidade no processo de compra
- Controle administrativo e de estoque centralizado
- Melhoria na experiência de compra do cliente

### 🚀 Melhorias Futuras

- Sistema de avaliações e comentários
- Promoções e cupons de desconto
- Integração com redes sociais e WhatsApp
- Dashboard de vendas com gráficos

---

## ✅ Homologação do MVP

- Reunião realizada com o cliente
- MVP aprovado

**Participantes:**
- Luan Marcos de Andrade Santos
- Gustavo Henrique dos Anjos
- Sarah Hesed Liima Santana

---

## 📣 Divulgação

### LinkedIn do Projeto

> A página do LinkedIn do projeto deve conter:
> - Logo do projeto
> - Título
> - Resumo
> - Nomes dos integrantes e professor
> - Link do repositório no GitHub
> - Artefatos das sprints

**[Inserir aqui link e print da página do LinkedIn]**

---

## 🎥 Eventos e Apresentações

### Seminário de Projetos de Software

> Equipe ausente.

### FENATEC – Feira de Negócios em Tecnologia

**Vídeo de apresentação:**  
> [Inserir link do vídeo]

**Fotos do Evento:**
1. 📸 Time ao lado do pôster  
   _Da esquerda para direita: [nomes]_

2. 📸 Integrante apresentando o sistema  
   _Apresentando: [nome]_

3. 📸 Público assistindo à apresentação  
   _Participantes atentos_

4. 📸 Plano geral da FUNETEC  
   _Ambiente da feira_

**Lista de Visitantes da FUNETEC:**
> Inserir planilha com nomes e e-mails.

---

## 📄 Carta de Apresentação

> Documento assinado pela instituição convidando a cliente a participar do projeto, descrevendo as etapas e responsabilidades.

---

## 📄 Carta de Autorização

> Documento assinado pela cliente autorizando a realização do projeto com a equipe:

**Cliente:** Sarah Hesed Liima Santana  
**Data:** 14 de Março de 2025  
**Email:** letsglowmulher@gmail.com  
**Contato:** (19) 99636-1965  

**Alunos Autorizados:**
- Luan Marcos de Andrade Santos – ADS – 202402410601  
- Gustavo Henrique dos Anjos – CC – 202203873997  
- Murilo Alves de Godoy – CC

---

## ✍️ Relato Individual do Processo

### Gustavo Henrique dos Anjos
> Foi uma experiência intensa e real, envolvendo gestão de projeto, aprendizado de tecnologias como HTML e CSS, uso do Jira e GitHub.

### Murilo Alves de Godoy
> [Inserir relato]

### Luan Marcos de Andrade Santos
> [Inserir relato]
