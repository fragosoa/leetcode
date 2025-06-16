from flask import Flask, jsonify
from models.models import db, Employee, Student, University

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/employees')
def list_employees():
    employees = Employee.query.all()
    return jsonify([emp.to_dict() for emp in employees])

@app.route('/universities')
def list_universities():
    universities = University.query.all()
    return jsonify([uni.to_dict() for uni in universities])

@app.route('/students')
def list_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Seed Employee data
        if Employee.query.count() == 0:
            emp1 = Employee(name="Alice Smith", email="alice@example.com")
            emp2 = Employee(name="Bob Johnson", email="bob@example.com")
            db.session.add_all([emp1, emp2])
            db.session.commit()
        # Seed University data
        if University.query.count() == 0:
            uni1 = University(id='uni1', name="MIT", location="Cambridge")
            uni2 = University(id='uni2', name="Stanford", location="Stanford")
            db.session.add_all([uni1, uni2])
            db.session.commit()
        # Seed Student data
        if Student.query.count() == 0:
            student1 = Student(name="Charlie Brown", university_id='uni1')
            student2 = Student(name="Dana White", university_id='uni2')
            db.session.add_all([student1, student2])
            db.session.commit()
    app.run(debug=True)
