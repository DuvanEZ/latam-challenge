from flask import Flask, jsonify, request, current_app
import os
from src.q1_time import q1_time
from src.q1_memory import q1_memory
from src.q2_time import q2_time
from src.q2_memory import q2_memory
from src.q3_time import q3_time
from src.q3_memory import q3_memory
import logging
import pandas as pd

app = Flask(__name__)
print("Started.")

@app.route('/')
def home():
    return '''
    <h1>Welcome to the Data Processing API</h1>
   <p>Con esta aplicación hecha en Flask se pretende mostrar los resultados a las preguntas específicas. Para cada pregunta se elaboraron dos soluciones: una memory efficient y otra time efficient. Para ver el detalle del código, por favor ir a este repositorio en GitHub <a href="https://github.com/DuvanEZ/latam-challenge" target="_blank">https://github.com/DuvanEZ/latam-challenge</a>.</p>

    <button onclick="fetchAndDisplayResults()">Run Analysis</button>
    <div id="resultsTable">Click the button to run analysis.</div>
    <script>
        function fetchAndDisplayResults() {
            const resultsTable = document.getElementById('resultsTable');
            resultsTable.innerHTML = 'Processing...';

            fetch('/run')
                .then(response => response.json())
                .then(data => {
                    let tableHTML = '<table><tr><th>Function</th><th>Result</th></tr>';
                    data.forEach(row => {
                        tableHTML += `<tr><td>${row.function}</td><td>${row.result}</td></tr>`;
                    });
                    tableHTML += '</table>';
                    resultsTable.innerHTML = tableHTML;
                })
                .catch(error => {
                    console.error('Error:', error);
                    resultsTable.innerHTML = 'An error occurred. Please try again.';
                });
        }

    </script>
    ''', 200

@app.route('/run', methods=['GET']) 
def process_files():
    with app.app_context():
        # Set up logging
        logging.basicConfig(filename='process_files.log', level=logging.INFO)

        try:
            logging.info("Starting functions...")
            file_path = "farmers-protest-tweets-2021-2-4.json"
            results = [
                {'function': 'q1_time', 'result': q1_time(file_path)},
                {'function': 'q1_memory', 'result': q1_memory(file_path)},
                {'function': 'q2_time', 'result': q2_time(file_path)},
                {'function': 'q2_memory', 'result': q2_memory(file_path)},
                {'function': 'q3_time', 'result': q3_time(file_path)},
                {'function': 'q3_memory', 'result': q3_memory(file_path)}
            ]
            df = pd.DataFrame(results)
            print(df)
            return jsonify(df.to_dict(orient='records')), 200

        except Exception as e:
            logging.error(f"Error: {str(e)}")
            return jsonify({'message': f'Error: {str(e)}'}), 500

if __name__ == "__main__":
    print("Starting API on port 80.")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 80)))