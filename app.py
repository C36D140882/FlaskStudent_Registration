from flask import Flask, render_template, request, redirect, url_for, flash
from mongodb import collection


app = Flask(__name__)
app.secret_key = 'your_secret_key' 


# Route for the registration form
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        student_id = request.form.get('student_id')
        course = request.form.get('course')
        
        if not all([name, email, age, student_id, course]):
            flash('All fields are required.', 'danger')
            return redirect(url_for('register'))
        
        # Insert data into MongoDB
        collection.insert_one({
            'name': name,
            'email': email,
            'age': age,
            
            'student_id': student_id,
            'course': course
        })
        
        flash('Registration successful!', 'success')  
        return redirect(url_for('register'))

    return render_template('register1.html')

if __name__ == '__main__':
    app.run(debug=True)