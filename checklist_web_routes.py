from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, session
from datetime import datetime
import pytz
import os
import threading
from dotenv import load_dotenv

# Blueprint configurado para o módulo de Logística
checklist_web_bp = Blueprint('checklist_web', __name__, template_folder='templates')

load_dotenv()

# --- DADOS SIMULADOS (MOCK DATA) ---
# Estes dados permitem que o projeto rode no GitHub sem um banco de dados real.
MOCK_MODELOS = [
    {"ID": 1, "NOME": "Checklist Caminhão Baú", "PERIODICIDADE": "Diário", "TIPO_VEICULO": "Caminhão", "ATIVO": 1, "EMAILS_NOTIFICACAO": "logistica@exemplo.com"},
    {"ID": 2, "NOME": "Checklist Empilhadeira", "PERIODICIDADE": "Semanal", "TIPO_VEICULO": "Maquinário", "ATIVO": 1, "EMAILS_NOTIFICACAO": "manutencao@exemplo.com"},
]

MOCK_PERGUNTAS = [
    {"ID": 1, "MODELO_ID": 1, "TEXTO_PERGUNTA": "Nível de óleo do motor", "TIPO_MIDIA": "FOTO", "MEDIA_OBRIGATORIA": 1, "ORDEM": 1},
    {"ID": 2, "MODELO_ID": 1, "TEXTO_PERGUNTA": "Luzes de Freio e Seta", "TIPO_MIDIA": "NENHUM", "MEDIA_OBRIGATORIA": 0, "ORDEM": 2},
]

MOCK_REALIZADOS = [
    {
        "ID": 501, 
        "DATA_HORA": datetime.now(), 
        "PLACA_VEICULO": "LOG-2026", 
        "PLACA_2": "CAR-1234", 
        "PLACA_3": "",
        "COD_MOTORISTA": "MOTORISTA_DEMO", 
        "MODELO_NOME": "Checklist Caminhão Baú", 
        "USUARIO_NOME": "Recrutador Demo"
    }
]

# --- FUNÇÕES AUXILIARES ---

def data_hora_brasilia():
    """Retorna a data e hora atual no fuso de São Paulo"""
    timezone = pytz.timezone('America/Sao_Paulo')
    return datetime.now(timezone)

# --- ROTAS DE GERENCIAMENTO ---

@checklist_web_bp.route('/checklist/gerenciar')
def index():
    """Lista os modelos de checklist cadastrados (Simulado)"""
    modelos = [m for m in MOCK_MODELOS if m['ATIVO'] == 1]
    return render_template('Logistica/checklist_gerenciar.html', modelos=modelos)

@checklist_web_bp.route('/checklist/get_perguntas/<int:modelo_id>')
def get_perguntas(modelo_id):
    """API para carregar perguntas dinamicamente via AJAX"""
    perguntas = [p for p in MOCK_PERGUNTAS if p['MODELO_ID'] == modelo_id]
    return jsonify(perguntas)

# --- ROTA: DASHBOARD LOGÍSTICO ---

@checklist_web_bp.route('/checklist/dashboard')
def dashboard():
    """Exibe indicadores de performance e conformidade da frota"""
    data_str = request.args.get('data') or datetime.now().strftime('%Y-%m-%d')
    
    # KPIs Simulados baseados em lógica real de negócio
    total_checklists = 120
    total_nao_conformes = 15
    taxa_aprovacao = 87.5
    
    top_veiculos_problema = [
        {'PLACA_VEICULO': 'LOG-1010', 'COD_MOTORISTA': 'J. SILVA', 'QTD_ERROS': 8},
        {'PLACA_VEICULO': 'LOG-2020', 'COD_MOTORISTA': 'A. OLIVEIRA', 'QTD_ERROS': 4}
    ]

    resumo_por_modelo = [
        {'NOME_MODELO': 'Caminhão Baú', 'PERIODICIDADE': 'Diário', 'QTD': 85},
        {'NOME_MODELO': 'Frota Leve', 'PERIODICIDADE': 'Semanal', 'QTD': 35}
    ]

    data_br = datetime.strptime(data_str, '%Y-%m-%d').strftime('%d/%m/%Y')

    return render_template('Logistica/checklist_dashboard.html',
                           data_selecionada_str=data_str,
                           data_selecionada_str_br=data_br,
                           total_checklists=total_checklists,
                           total_nao_conformes=total_nao_conformes,
                           taxa_aprovacao=taxa_aprovacao,
                           top_veiculos_problema=top_veiculos_problema,
                           resumo_por_modelo=resumo_por_modelo)

# --- ROTA: HISTÓRICO DE CHECKLISTS ---

@checklist_web_bp.route('/checklist/realizados')
def realizados():
    """Lista histórico de checklists realizados com suporte a AJAX para DataTables"""
    checklists = MOCK_REALIZADOS
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        lista_json = [{
            'ID': item['ID'],
            'DATA_FMT': item['DATA_HORA'].strftime('%d/%m/%Y %H:%M'),
            'PLACA_VEICULO': item['PLACA_VEICULO'],
            'USUARIO_NOME': item['USUARIO_NOME'],
            'MODELO_NOME': item['MODELO_NOME'],
            'LINK_DETALHES': "#"
        } for item in checklists]
        return jsonify(lista_json)

    return render_template('Logistica/checklist_realizados.html', checklists=checklists)

# --- VÍNCULOS (EXEMPLO DE INTEGRAÇÃO ERP) ---

@checklist_web_bp.route('/api/checklist-clientes/<int:modelo_id>', methods=['GET'])
def api_get_clientes_vinculo(modelo_id):
    """Demonstra lógica de vinculação entre modelos de checklist e clientes do ERP"""
    return jsonify({
        'disponiveis': [{'val': 'C1', 'text': '[C1] Cliente Alpha'}],
        'vinculados': [{'val': 'C2', 'text': '[C2] Cliente Beta'}]
    })

@checklist_web_bp.route('/checklist/salvar_pergunta', methods=['POST'])
def salvar_pergunta_mock():
    """Endpoint simulado para demonstrar interação de escrita"""
    return jsonify({'sucesso': True, 'msg': 'Operação simulada com sucesso!'})