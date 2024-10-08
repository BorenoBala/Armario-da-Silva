from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página principal de filiação
@app.route('/filiacao')
def filiacao():
    return render_template('tela_filiacao.html')

# Rota para "Criar um Time"
@app.route('/criar_time', methods=['POST'])
def criar_time():
    # Aqui você pode processar os dados e armazenar no banco de dados
    # Exemplo: nome do time, etc.
    
    # Redireciona para a página específica após a ação
    return redirect(url_for('time_criado'))

# Página exibida após "Criar um Time"
@app.route('/time_criado')
def time_criado():
    return render_template('criar_time.html', mensagem="Time criado com sucesso!")

# Rota para "Unir-se a um Time"
@app.route('/unir', methods=['POST'])
def unir():
    # Aqui você pode processar os dados (e.g., unir-se a um time existente)
    
    # Redireciona para a página específica após a ação
    return redirect(url_for('unido_time'))

# Página exibida após "Unir-se a um Time"
@app.route('/unido_time')
def unido_time():
    return render_template('unir_time.html', mensagem="Unido a um time com sucesso!")

# Rota para "Ser Árbitro"
@app.route('/ser_arbitro', methods=['POST'])
def ser_arbitro():
    # Aqui você pode processar os dados (e.g., registrar-se como árbitro)
    
    # Redireciona para a página específica após a ação
    return redirect(url_for('arbitro_registrado'))

# Página exibida após "Ser Árbitro"
@app.route('/arbitro_registrado')
def arbitro_registrado():
    return render_template('ser_arbitro.html', mensagem="Registrado como árbitro com sucesso!")

if __name__ == '__main__':
    app.run(debug=True)
