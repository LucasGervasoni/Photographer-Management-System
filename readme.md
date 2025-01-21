- [Leia esta página em português](readme.pt.md)


![login-page](https://github.com/user-attachments/assets/255afe78-38b6-4988-8049-c992047e3825)


## 📸 Photographer Management System

This project is designed to streamline the workflow of a photography business by centralizing the management of orders, photographers, and editors. The system facilitates the assignment, upload, editing, and tracking of photographic orders, improving efficiency and enhancing collaboration.

---

### 🎯 **Key Features**

1. **File Management**  
   - Upload and download photos seamlessly.
   - Choose between downloading original or edited photos.
   - Ability to select specific photos that do not need to be downloaded.

2. **Order Management**  
   - Import orders via `.xls` files for efficient bulk management.
   - View all photos within an order or filter to display only edited images.

3. **User Management**  
   - Create and manage users with roles: Admins, Photographers, and Editors.

4. **Activity Log**  
   - Keep track of all upload and download actions for improved accountability.

5. **Admin Dashboard**  
   - Monitor system activity, manage orders, and oversee user performance through a centralized dashboard.

---

### 🛠️ **Technologies Used**

- **Frontend:** JavaScript for managing upload and download interactions.
- **Backend:** Python and Django to handle core business logic and APIs.
- **Database:** SQLite for development; PostgreSQL for production.
- **Cloud Services:**  
  - AWS S3 for file storage.  
  - Heroku for deployment.  
  - BunnyCDN for fast content delivery.  
- **Server Management:** Nginx for load balancing and efficient request handling.


### 🚀 **How to Run**

1. Clone the repository:
   ```bash
   git clone https://github.com/LucasGervasoni/Photographer-Management-System.git
   cd photographer-management-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python manage.py runserver
   ```

4. Access the application in your browser:
   ```
   http://127.0.0.1:8000
   ```

---


### 📄 **License**

This project is licensed under the [MIT License](LICENSE).  

---

