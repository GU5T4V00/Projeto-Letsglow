# Lets Glow: Loja de Beleza e Cosméticos

## Dados do Cliente
- **Título do Projeto:** Lets Glow: uma loja de beleza e cosmético de revenda de produtos, com produtos checkout de compra, endereço e contato
- **Cliente:** Sarah Hesed Lima Santana
- **CNPJ/CPF:** 40109764897
- **Contato:** (19) 99636-1965
- **Email do contato:** letsglowmulher@gmail.com

## Equipe de Desenvolvimento
- **Luan Marcos de Andrade Santos**
  - Curso: Análise e Desenvolvimento de Sistemas
  - Disciplina: Programação Orientada a Objetos em Java
- **Caio Rafael Tilli Von Groll**
  - Curso: Análise e Desenvolvimento de Sistemas
  - Disciplina: Programação Orientada a Objetos em Java
- **Gustavo Henrique dos Anjos**
  - Curso: Ciência da Computação
  - Disciplina: Programação Orientada a Objetos em Java
- **Murilo Alves de Godoy**
  - Curso: Ciência da Computação
  - Disciplina: Programação Orientada a Objetos em Java

## Professor Orientador
- **Kessed Rodrigues Julio**

## Introdução
O problema do cliente é simples, mas não tão simples. A cliente tem uma loja de cosméticos e beleza e quer vender mais. Uma das soluções seria fazer tráfego pago, mas ela precisa de uma loja online para vender. Nosso grupo vai criar essa loja para ela, mas a divulgação não é nossa responsabilidade.

## Objetivo
### 🎯 Objetivo da Loja
Oferecer produtos de beleza e cuidados pessoais de alta qualidade, acessíveis e cuidadosamente selecionados, promovendo autoestima, bem-estar e confiança para todas as pessoas, com foco em tendências modernas e valores que respeitam a diversidade e a natureza.

### 🛒 Finalidade
Criar uma experiência de compra online prática e encantadora, onde cada cliente encontre não apenas produtos, mas também inspiração para se cuidar, se expressar e valorizar sua beleza única. A loja busca ser referência em atendimento, qualidade e inovação no universo da beleza.

## Escopo
- **Banco de Dados:** Controle de produtos entre estoque e exibição no site.
- **Design:** Criação de designs para o site e produtos.
- **Sistema de Cadastro/Acesso:** Cada cliente terá sua própria conta.
- **Aprovação Automática:** Identificação de pagamento e liberação para entrega/retirada.

## Backlogs do Produto
### 📌 Resumo dos Requisitos – Loja Virtual de Cosméticos e Beleza
#### Requisitos Funcionais:
- **Cadastro de Produtos:** Nome, descrição, preço, categoria, imagens e estoque.
- **Carrinho de Compras:** Adicionar/remover produtos, calcular total e checkout.
- **Sistema de Pagamento:** Integração com Pix, cartão de crédito/débito e boleto bancário.
- **Cadastro de Usuários:** Criar conta, fazer login e acompanhar pedidos.
- **Controle de Estoque:** Atualização automática conforme vendas.
- **Área Administrativa:** Gerenciamento de produtos, pedidos, usuários e relatórios.
- **Integração com Métodos de Frete:** Cálculo automático de frete via Correios ou Melhor Envio.

#### Requisitos Não Funcionais:
- **Design Responsivo:** Adaptável para desktop, tablets e celulares.
- **Segurança de Dados:** Utilização de protocolos HTTPS e proteção de dados dos usuários.
- **Facilidade de Uso (UX/UI):** Interface intuitiva e agradável.

## Cronograma
- [Link para o cronograma](https://guanjos04.atlassian.net/jira/software/projects/SCRUM/boards/1?atlOrigin=eyJpIjoiNmE1YWU3ODM2Mzg1NDY5NThhMWM5ZDNlNTZmZmJja, endereço, telefone
- **Produto:** id, nome, descrição, preço, imagens, categoria_id, estoque
- **Pedido:** id, usuario_id, data, status, valor_total
- **ItemPedido:** id, pedido_id, produto_id, quantidade, preco_unitario
- **Pagamento:** id, pedido_id, método, status_pagamento, data_pagamento
- **Categoria:** id, nome_categoria
- **Admin:** id, nome, email, senha

### 🛠 Tecnologias Utilizadas
#### Frontend
- HTML5, CSS3, JavaScript
- Framework: React.js ou JS puro com Bootstrap/Tailwind
- Bibliotecas extras: Axios, Swiper

#### Backend
- Linguagem: PHP
- Framework: Laravel ou PHP puro com estrutura MVC
- Autenticação: JWT ou sessão PHP
- Validação: Middleware + filtros de input

#### Banco de Dados
- PostgreSQL ou MySQL

#### Outros
- Controle de versão: Git + GitHub
- Hospedagem: Hostinger, Vercel (frontend) ou Heroku (backend com Postgre)
- Pagamento: Integração com Mercado Pago, Stripe ou PagSeguro
- Frete: Correios API / Melhor Envio

### 🏛️ Arquitetura do Sistema
#### Arquitetura MVC (Model-View-Controller)
1. **Model:** Lógica de acesso ao banco de dados
2. **View:** Camadas visuais com HTML/CSS e scripts JS
3. **Controller:** Controla as requisições e direciona o fluxo entre o model e a view

## Resultados
### 🧪 Protótipo – Telas do Sistema
1. **🏠 Tela Inicial (Home)**
   - Ações do usuário: Ver produtos em destaque, acessar categorias, usar a barra de busca, clicar em um produto para ver detalhes.
   - Reações do sistema: Carrega produtos via banco de dados, redireciona para a página de detalhes do produto ao clicar.

2. **🛒 Página de Produto**
   - Ações do usuário: Ver detalhes do produto, adicionar ao carrinho, escolher quantidade.
   - Reações do sistema: Produto é adicionado ao carrinho e exibe confirmação.

3. **🛍️ Carrinho de Compras**
   - Ações do usuário: Aumentar/diminuir quantidade de itens, remover produto, finalizar compra.
   - Reações do sistema: Atualiza valores em tempo real, encaminha para checkout ao finalizar.

4. **👤 Tela de Login/Cadastro**
   - Ações do usuário: Fazer login ou criar conta.
   - Reações do sistema: Autentica o usuário e redireciona para a loja.

5. **💳 Checkout (Pagamento + Endereço)**
   - Ações do usuário: Informar endereço de entrega, escolher forma de pagamento, confirmar pedido.
   - Reações do sistema: Gera pedido no banco de dados, redireciona para página de confirmação.

6. **🛠️ Painel Administrativo (Admin)**
   - Ações do admin: Cadastrar produtos, editar/deletar produtos, acompanhar pedidos.
   - Reações do sistema: CRUD completo de produtos, atualiza visualmente os pedidos.

## Conclusão
### 💡 Impacto do Sistema
A implementação da loja virtual trouxe uma transformação significativa no processo de vendas e atendimento ao cliente. Antes, o processo de comercialização dos produtos era feito de forma informal ou limitada a redes sociais, o que dificultava a organização dos pedidos, controle de estoque e gestão de clientes.

Com o novo sistema:
- O cliente pode navegar pelos produtos com facilidade e fazer compras de forma autônoma.
- A administração da loja passou a ter controle total sobre o estoque, pedidos e pagamentos.
- O atendimento ficou mais ágil, com notificações automáticas e sistema de pedidos rastreável.
- A visibilidade dos produtos foi ampliada, gerando mais alcance e aumentando o potencial de vendas.

Resultado: O sistema otimizou a operação da loja, reduziu o retrabalho e criou uma experiência de compra mais profissional e confiável para o usuário final.

### 🚀 Melhorias Futuras
- **Sistema de Avaliações e Comentários:** Permitir que clientes avaliem os produtos e deixem comentários.
- **Área de Promoções e Cupons de Desconto:** Funcionalidades específicas para campanhas promocionais.
- **Integração com Redes Sociais e WhatsApp:** Login social e compartilhamento direto de produtos.
- **Dashboard com Gráficos de Vendas:** Painel visual para o administrador acompanhar estatísticas de vendas.

## Homologação do MVP junto ao cliente
Após as entregas parciais, realizadas de acordo com os requisitos do sistema e cronograma, o MVP foi apresentado em uma reunião entre o time de desenvolvedores e o cliente.

## Divulgação
### Linkedin do Projeto
A página do Linkedin do projeto deve ter o logo do LTD, o título do projeto, um breve resumo, o nome dos integrantes e o nome do professor-orientador. Insira também o link do repositório do projeto no GitHub. Neste perfil, deve ser postado a cada Sprint, os artefatos produzidos (diagramas, vídeos explicativos de códigos, artigo sobre determinado tema vinculado ao desenvolvimento do projeto).

### Seminário de Projetos de Software
Grave sua apresentação, poste no Linkedin do projeto e insira aqui o link público do vídeo da apresentação.

## FENATEC: Feira de Negócios em Tecnologia
### Apresentação do projeto
Um vídeo deve ser produzido mostrando o time apresentando seu projeto para algum visitante. Importante que neste vídeo tenha uma tomada do banner e dos integrantes. Insira aqui o link público deste vídeo.

#### Fotos da Apresentação
1. !Foto 1: Time ao lado do poster
   - **Legenda:** Descreva quem está na foto.
2. !Foto 2: Integrante apresentando o sistema
   - **Legenda:** Coloque o nome de quem está apresentando.
3. !Foto 3: Público assistindo a apresentação
   - **Legenda:** Participantes do evento assistindo a apresentação.
4. !Foto 4: Plano geral da FUNETEC
   - **Legenda:** Estandes da FUNETEC.

#### Lista de Presentes na Apresentação
- Cole aqui a lista de presença dos visitantes da FUNETEC com nome e email do visitante. Os próprios times farão um formato contendo no cabeçalho: Lista de Visitantes FUNETEC. Compartilhe a planilha gerada pelo form com todos os times.

## Carta de Apresentação
Vimos por desta apresentar o grupo de acadêmicos do Centro Universitário Uni Metrocamp, localizada à Rua Sales de Oliveira, 1661 - Campinas - SP, a fim de convidá-lo a participar de uma atividade extensionista associada ao componente curricular Programação Orientada a Objetos em Java, sob responsabilidade do orientador Prof. Kesede Rodrigues Julio (profkesede64@gmail.com).

Em consonância ao Plano Nacional de Educação vigente, o Centro Universitário Uni Metrocamp promove o Desenvolvimento de Software que, norteados pela metodologia de Gerenciamento Ágil Scrum, tem por princípios fundantes o diagnóstico dos problemas/demandas/necessidades, a participação ativa dos interessados/públicos participantes, a construção dialógica, coletiva e experiencial de conhecimentos, o planejamento de ações, o desenvolvimento e avaliação das ações, a sistematização dos conhecimentos, a avaliação das ações desenvolvidas.

Nesse contexto, a disciplina acima mencionada tem como principal escopo os temas relacionados à Programação Orientada a Objeto / Padrões de Projetos de Software, no que diz respeito ao desenvolvimento de um software utilizando Programação Orientada a Objeto.

Sendo assim, pedimos o apoio de Sarah Hesed Lima Santana para a realização das seguintes atividades: levantamento de requisitos, validação das entregas parciais, revalidação dos requisitos, homologação do MVP, ou qualquer outra intervenção que auxilie no desenvolvimento das competências de nossos acadêmicos e ao mesmo tempo possa contribuir para a comunidade em que estamos inseridos.

Aproveitamos a oportunidade para solicitarmos, em caso de aceite, que a parceria seja formalizada, mediante assinatura da Carta de Autorização, as atividades e informações que o(s) aluno(s) poderá(ão) ter acesso.

Em tempo, registramos ainda, o convite para a participação de todos os interessados no fórum semestral de acompanhamento e avaliação das atividades realizadas, que está previsto para o final deste semestre, e será comunicado previamente em convite específico.

Desde já nos colocamos à sua disposição para quaisquer esclarecimentos.

Atenciosamente,

Campinas, 12 de abril de 2025.

____________________________________  
Assinatura Direção Acadêmica da IES

____________________________________  
Assinatura Docente

## Carta de Autorização
Eu, Sarah Hesed Lima Santana, (preencher com cargo ocupado), da (nome da empresa, organização, associação, escola, secretaria, etc., situada no endereço – inserir o endereço), autorizo a realização das seguintes atividades acadêmicas do componente extensionista <código e nome da disciplina>, do Centro Universitário Uni Metrocamp, sob orientação do Prof. Kesede Rodrigues Julio.

### Atividades:
- (Descrever atividades)

Conforme combinado em contato prévio, as atividades acima descritas são autorizadas para os seguintes alunos:

| Nome dos/das alunos/as           | Curso                              | Matrícula |
| -------------------------------- | ---------------------------------- | --------- |
| Luan Marcos de Andrade Santos    | Análise e Desenvolvimento de Sistemas |           |
| Caio Rafael Tilli Von Groll      | Análise e Desenvolvimento de Sistemas |           |
| Gustavo Henrique dos Anjos       | Ciência da Computação              |           |
| Murilo Alves de Godoy            | Ciência da Computação              |           |

Declaro que fui informado por meio da Carta de Apresentação sobre as características e objetivos das atividades que serão realizadas na organização/instituição/empresa a qual represento e afirmo estar ciente de tratar-se de uma atividade realizada com intuito exclusivo de ensino de alunos de graduação, sem a finalidade de exercício profissional.

Desta forma, autorizo, em caráter de confidencialidade:
- o acesso a informações e dados que forem necessários à execução da atividade;
- o registro de imagem por meio de fotografias;
- outro: (especificar)

Campinas, __ de __________ de 2025.

___________________________________________________________________  
(Assinatura, nome completo do responsável, email de contato e com carimbo da empresa)

## Relato Individual do Processo
- **Nome do aluno:**  
  Um breve relato pessoal sobre o trabalho extensionista desenvolvido.
- **Nome do aluno:**  
  Um breve relato pessoal sobre o trabalho extensionista desenvolvido.
- **Nome do aluno:**  
  Um breve relato pessoal sobre o trabalho extensionista desenvolvido.
- **Nome do aluno:**  
  Um breve relato pessoal sobre o trabalho extensionista desenvolvido.
- **Nome do aluno:**  
  Um breve relato pessoal sobre o trabalho extensionista desenvolvido.
