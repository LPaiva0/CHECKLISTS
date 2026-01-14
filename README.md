Sistema de Gestão de Checklists Logísticos
Este repositório contém um módulo completo de auditoria e conformidade para frotas logísticas. O sistema foi desenvolvido para garantir a segurança operacional através de inspeções veiculares detalhadas, monitoramento de falhas e dashboards de indicadores.
Destaques do Projeto
•	Arquitetura Escalável: Uso de Blueprints do Flask para organização de rotas e Herança de Templates (Jinja2) para uma interface unificada.
•	Processamento Assíncrono: Implementação de alertas de reprovação via e-mail utilizando threading, garantindo que o envio de notificações não prejudique a performance da interface.
•	Design Profissional: Interface moderna construída com Bootstrap 5, apresentando um menu lateral fixo (Sidebar) e componentes responsivos.
•	Camada de Demonstração (Mock Data): O projeto foi desacoplado de bancos de dados físicos (MySQL/SQL Server) e utiliza dados simulados, permitindo que recrutadores visualizem todas as funcionalidades imediatamente após a clonagem.

Tecnologias e Bibliotecas
•	Backend: Python 3.13 / Flask.
•	Frontend: HTML5, CSS3 (Flexbox/Grid), Bootstrap 5, Font Awesome.
•	Utilitários: pytz (Gestão de fuso horário), python-dotenv (Variáveis de ambiente).
Estrutura do Repositório
 
Como Executar Localmente
1.	Clone o repositório:
•	git clone https://github.com/LPaiva0/CHECKLISTS.git
•	cd CHECKLISTS
2.	Instale as dependências:
•	pip install -r requirements.txt
3.	Inicie o servidor:
•	python app.py
Acesse no navegador: http://127.0.0.1:5000/checklist/dashboard
Visualização do Módulo
O sistema é dividido em três pilares principais:
1.	Dashboard: Monitoramento de KPIs como Taxa de Aprovação e Top Veículos Críticos.
2.	Gerenciamento: Controle total sobre os modelos de checklist e periodicidades de inspeção.
3.	Histórico: Rastreabilidade completa de todas as inspeções realizadas com filtros de busca.

