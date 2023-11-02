/*
System Security
In this section, we will want you to demonstrate your knowledge of security best practices. Write your answer to this question in security_question.md either in English or Spanish.
Suppose you are the head of Engineering for an exciting new tech startup that installs solar panels via an app. It's Uber for Solar Panels! You are doing a security audit of your app's infrastructure. You are using the OWASP Top 10 for 2021 as a guide for what security issues might be a problem for you.
Your infrastructure is deployed in Kubernetes containers on Amazon Web Services. It has these components:
•	A mobile app for Android and iOS.
•	A web frontend that the customer can use instead of the mobile app. This is written in Javascript with Next.js.
•	A MySQL database that stores customer information, including passwords, home addresses, telephone numbers, etc. It
also contains customer order information.
•	A Python backend implemented in FastAPI. This talks to the database and serves data to both the web frontend and the mobile apps.
You have 12 software engineer employees who have full access to the system, 3 customer support employees who can view customer information and make changes to orders and accounts, and one sales employee.
Using the OWASP Top 10, what would you look for to make your system secure?
*/

/* SOLUCION

Para asegurar la seguridad de la infraestructura de su aplicación de instalación de paneles solares, considerando la implementación en contenedores de Kubernetes en Amazon Web Services y utilizando la OWASP Top 10 para 2021 como guía, aquí hay áreas críticas en las que debe enfocarse durante la auditoría de seguridad:
1.	Injection Attacks (Inyecciones):
•	Implementar consultas preparadas y validación de datos para evitar ataques de inyección, especialmente en las consultas a la base de datos MySQL. Evitar la ejecución de comandos maliciosos.
2.	Authentication and Session Management (Autenticación y Gestión de Sesiones):
•	Implementar autenticación segura, preferiblemente mediante métodos de autenticación de un solo sentido (como bcrypt).
•	Garantizar una gestión de sesiones adecuada para evitar el robo de sesiones y el acceso no autorizado a cuentas de usuarios.
3.	Sensitive Data Exposure (Exposición de Datos Sensibles):
•	Encriptar datos sensibles en reposo y en tránsito, incluyendo contraseñas y cualquier otra información del cliente almacenada en la base de datos MySQL.
4.	XML External Entity (XXE) Attacks (Ataques de Entidades XML Externas):
•	Deshabilitar el procesamiento de entidades XML externas para prevenir ataques XXE en cualquier entrada XML recibida.
5.	Security Misconfigurations (Configuraciones de Seguridad Incorrectas):
•	Revisar y asegurar adecuadamente la configuración de Kubernetes, asegurando que no haya configuraciones inseguras o predeterminadas que puedan ser explotadas.
6.	Broken Access Control (Control de Acceso Roto):
•	Implementar un control de acceso adecuado para asegurar que los empleados tengan solo los privilegios necesarios para llevar a cabo sus funciones.
•	Garantizar que las acciones sensibles, como los cambios en los pedidos y cuentas, estén adecuadamente autorizadas y registradas.
7.	Using Components with Known Vulnerabilities (Uso de Componentes con Vulnerabilidades Conocidas):
•	Regularmente actualizar todos los componentes, bibliotecas y frameworks utilizados para evitar vulnerabilidades conocidas.
8.	Insufficient Logging and Monitoring (Registros y Monitoreo Insuficientes):
•	Establecer registros detallados y monitoreo en tiempo real para detectar y responder a actividades inusuales o intentos de intrusión.
9.	Cross-Site Scripting (XSS) Attacks (Ataques de Scripting entre Sitios):
•	Validar y sanitizar todas las entradas del usuario para evitar ataques XSS en la aplicación web y en la interfaz móvil.
10.	Insecure Deserialization (Deserialización Insegura):
•	Evitar la deserialización de datos no confiables. Validar y autenticar los datos deserializados para prevenir la manipulación maliciosa de objetos.
Al centrarse en estas áreas, puede fortalecer la seguridad de su aplicación de instalación de paneles solares, protegiendo los datos del cliente y garantizando una experiencia segura para los usuarios y empleados.
