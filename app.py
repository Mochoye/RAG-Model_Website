from flask import Flask, request, render_template, redirect, url_for, flash
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/books'
app.secret_key = 'supersecretkey'  # for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and file.filename.endswith('.pdf'):
        file.save('data/books/temp/a.pdf')
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        

        # Call the database.py script
        subprocess.run(['python', 'database.py'])

        flash('Database saved successfully')
        return redirect(url_for('index'))

    flash('Invalid file format. Please upload a PDF.')
    return redirect(url_for('index'))

@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        query_text = request.form['query']
        query_text = f"'{query_text}'"
        print(query_text)
        result = subprocess.run(['python', 'query.py', query_text], capture_output=True, text=True)
        response = result.stdout
        print(response)
        return render_template('query.html', query=query_text, response=response)
    return render_template('query.html')

if __name__ == '__main__':
    app.run(debug=True)
