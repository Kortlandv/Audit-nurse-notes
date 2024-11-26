from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Sample schema for nursing notes
required_fields = ["Patient Name", "Date", "Time", "Note Content", "Signature"]

@app.route('/')
def home():
    return render_template("upload.html")

@app.route('/audit', methods=["POST"])
def audit_notes():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    
    # Read the uploaded file
    try:
        data = pd.read_csv(file)
    except Exception as e:
        return f"Error reading file: {e}", 400

    # Check for missing fields
    missing_fields = [field for field in required_fields if field not in data.columns]
    if missing_fields:
        return f"Missing required fields: {', '.join(missing_fields)}", 400

    # Audit for missing or incomplete entries
    audit_results = []
    for index, row in data.iterrows():
        issues = []
        for field in required_fields:
            if pd.isna(row[field]) or row[field] == "":
                issues.append(f"Missing {field}")
        
        if issues:
            audit_results.append({
                "Row": index + 1,
                "Issues": "; ".join(issues)
            })

    # Render audit results
    if not audit_results:
        return render_template("results.html", results="All notes are complete!")
    else:
        return render_template("results.html", results=audit_results)

if __name__ == '__main__':
    app.run(debug=True)