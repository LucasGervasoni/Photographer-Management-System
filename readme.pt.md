## 📸 Sistema de Gerenciamento de Fotógrafos

Este projeto foi projetado para otimizar o fluxo de trabalho de uma empresa de fotografia, centralizando a gestão de pedidos, fotógrafos e editores. O sistema facilita a atribuição, upload, edição e acompanhamento dos pedidos fotográficos, melhorando a eficiência e promovendo a colaboração.

---

### 🎯 **Principais Funcionalidades**

1. **Gestão de Arquivos**  
   - Upload e download de fotos de forma prática.
   - Escolha entre baixar fotos originais ou editadas.
   - Possibilidade de selecionar fotos específicas que não precisam ser baixadas.

2. **Gestão de Pedidos**  
   - Importação de pedidos via arquivos `.xls` para uma gestão em massa eficiente.
   - Visualização de todas as fotos de um pedido ou filtragem para exibir apenas as imagens editadas.

3. **Gestão de Usuários**  
   - Criação e gerenciamento de usuários com papéis: Administradores, Fotógrafos e Editores.

4. **Registro de Atividades**  
   - Acompanhe todas as ações de upload e download para maior responsabilidade.

5. **Painel Administrativo**  
   - Monitore as atividades do sistema, gerencie pedidos e supervisione o desempenho dos usuários através de um painel centralizado.

---

### 🛠️ **Tecnologias Utilizadas**

- **Frontend:** JavaScript para gerenciar interações de upload e download.
- **Backend:** Python e Django para lidar com a lógica de negócios principal e APIs.
- **Banco de Dados:** SQLite para desenvolvimento; PostgreSQL para produção.
- **Serviços em Nuvem:**  
  - AWS S3 para armazenamento de arquivos.  
  - Heroku para deploy.  
  - BunnyCDN para entrega rápida de conteúdo.  
- **Gestão de Servidor:** Nginx para balanceamento de carga e gerenciamento eficiente de requisições.

---

---

### 🚀 **Como Rodar**

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucasGervasoni/Photographer-Management-System.git
   cd sistema-gerenciamento-fotografos
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

4. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:8000
   ```

---


---

### 📄 **Licença**

Este projeto está licenciado sob a [Licença MIT](LICENSE).  

---
