from flask import Flask, jsonify, request
from database import db
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet"

db.init_app(app)

@app.route('/diet', methods=['GET'])
def test():
    return jsonify({"message": "hello world"})

@app.route('/meals', methods=['POST'])
def create_meal():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    consumed_at = data.get('consumed_at')
    on_diet = data.get('on_diet', False)
    
    if name and description and consumed_at:
        meal = Meal(name=name, description=description, consumed_at=consumed_at, on_diet=on_diet)
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição cadastrada com sucesso."}), 200
    
    return jsonify({"message": "Dados inválidos."}), 400

@app.route('/meals/<int:id_meal>', methods=['PUT'])
def edit_meal(id_meal):
    data = request.json
    meal = Meal.query.get(id_meal)
    
    if meal:
        meal.name = data.get('name')
        meal.description = data.get('description')
        meal.consumed_at = data.get('consumed_at')
        meal.on_diet = data.get('on_diet', False)
        db.session.commit()
        return jsonify({"message": "Refeição atualizada com sucesso."}), 200
    
    return jsonify({"message": "Refeição não encontrada."}), 404

@app.route('/meals/<int:id_meal>', methods=['DELETE'])
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal)
    
    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": f"Refeição {id_meal} deletada com sucesso."}), 200
    
    return jsonify({"message": "Refeição não encontrada."}), 404

@app.route('/meals/<int:id_meal>', methods=['GET'])
def list_meals(id_meal):
    meal = Meal.query.get(id_meal)
    
    if meal:
        return {
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "consumed_at": meal.consumed_at,
            "on_diet": meal.on_diet
        }
    
    return jsonify({"message": "Refeição não encontrada."}), 404

@app.route('/meals', methods=['GET'])
def list_meal():
    meals = Meal.query.all()
    
    if meals:
        print(meals)
        return jsonify([
        {
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "consumed_at": meal.consumed_at,
            "on_diet": meal.on_diet
        } for meal in meals
    ]), 200
    
    return jsonify({"message": "Nenhuma refeição encontrada."}), 404

if __name__ == "__main__":
    app.run(debug=True)