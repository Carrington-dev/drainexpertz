import uuid
from flask import request, jsonify
from src import app, db, User

@app.route("/api")
def api_home():
    """
    Welcome API
    ---
    tags:
      - Basic Views
    responses:
      200:
        description: Returns a feedback message
        schema:
          type: object
          properties:
            message:
              type: string
              example: "You are now subscribed to our newsletter!."
    """
    return jsonify({
        "message": "You are now subscribed to our newsletter!."
    })

@app.route('/api/users', methods=['POST'])
def add_user():
    """
    Creates a new user
    ---
    tags:
      - Users
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - username
            - last_name
            - first_name
            - email
            - is_admin
            - password
          properties:
            first_name:
              type: string
              example: Maanda
            last_name:
              type: string
              example: Muleya
            username:
              type: string
              example: johndoe
            email:
              type: string
              example: johndoe@example.com
            password:
              type: string
              example: #Jopempe2043
            is_admin:
              type: string
              example: false
    responses:
      201:
        description: User registered successfully
      400:
        description: User with this username or email already exists
    """
    # Get data from the incoming POST request
    data = request.get_json()
    id = str(uuid.uuid4())
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin')

    # Check if username and email are provided
    if not username or not email:
        return jsonify({'message': 'Username and email are required'}), 400
        
    if not id:
        return jsonify({"message": 'Id is required'}), 400
    
    if not password:
        return jsonify({"message": 'Password is required'}), 400
        

    # Create a new user and save it to the database
    try:
        new_user = User(username=username, 
                        email=email, 
                        first_name=first_name, 
                        last_name=last_name,
                        is_admin=is_admin,
                        password=password)
        db.session.add(new_user)
        db.session.commit()

        # return jsonify({'message': 'User added successfully'}), 201
        return jsonify(new_user), 201
    except:
        return jsonify({'message': 'User with similar credentials already exists'}), 400

@app.route("/api/subscribe")
def subscribe():
    """
    Simple Subscribe API
    ---
    tags:
      - Basic Views
    responses:
      200:
        description: Returns a feedback message
        schema:
          type: object
          properties:
            message:
              type: string
              example: "You are now subscribed to our newsletter!."
    """
    return jsonify({
        "message": "You are now subscribed to our newsletter!."
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_fast(user_id):
    """
    Get User by ID
    ---
    tags:
      - Users
    summary: Retrieve a user by their unique ID
    notes: Use this endpoint to fetch user details by providing their unique user ID.
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The unique ID of the user
        example: 1
    responses:
      200:
        description: User details retrieved successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            first_name:
              type: string
              example: "Carma"
            last_name:
              type: string
              example: "Mudau"
            username:
              type: string
              example: "can96"
            email:
              type: string
              example: "cr56m@gms.com"
      404:
        description: User not found
    """

    user = User.query.get(user_id)  # Returns None if user not found
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

# Delete User by ID
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete User by ID
    ---
    tags:
      - Users
    summary: Delete a user from the database
    notes: Provide a valid user ID to remove a user from the system.
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The unique ID of the user to be deleted
        example: 1
    responses:
      200:
        description: User deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "User deleted successfully"
      404:
        description: User not found
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted successfully'}), 200

# Update User by ID
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    """
    Update User by ID
    ---
    tags:
      - Users
    summary: Update user details
    notes: Provide the user ID and the updated data to modify a user's details.
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The unique ID of the user to update
        example: 1
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: "new_username"
            email:
              type: string
              example: "new_email@example.com"
            first_name:
              type: string
              example: "Pythongton"
            last_name:
              type: string
              example: "Mudau"
           
    responses:
      200:
        description: User updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "User updated successfully"
      404:
        description: User not found
      400:
        description: Invalid request data
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    last_name = data.get('last_name')
    first_name = data.get('first_name')
    username = data.get('username')
    email = data.get('email')
    is_admin = data.get('is_admin')
    password = data.get('password')

    if username:
        user.username = username
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name

    if password:
        user.password = password
    if is_admin:
        user.is_admin = is_admin

    db.session.commit()
    
    return jsonify({'message': 'User updated successfully', "user": user}), 200

@app.route('/api/users/<int:user_id>', methods=['UPDATE'])
def update_user(user_id):
    """
    Update User by ID
    ---
    tags:
      - Users
    summary: Update user details
    notes: Provide the user ID and the updated data to modify a user's details.
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The unique ID of the user to update
        example: 1
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: "new_username"
            email:
              type: string
              example: "new_email@example.com"
            first_name:
              type: string
              example: "Pythongton"
            last_name:
              type: string
              example: "Mudau"
           
    responses:
      200:
        description: User updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "User updated successfully"
      404:
        description: User not found
      400:
        description: Invalid request data
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    last_name = data.get('last_name')
    first_name = data.get('first_name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin')

    if username:
        user.username = username
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if password:
        user.password = password
    if is_admin:
        user.is_admin = is_admin

    db.session.commit()
    
    return jsonify({'message': 'User updated successfully', "user": user}), 200

@app.route('/api/users/me', methods=['GET'])
def get_my_profile():
    """
    Get my profile
    ---
    tags:
      - Users
    summary: Retrieve details of the currently authenticated user
    responses:
      200:
        description: User profile details
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            username:
              type: string
              example: johndoe
            email:
              type: string
              example: johndoe@example.com
    """
    # In a real app, you'd extract the logged-in user from a JWT token
    # Example: user_id = get_jwt_identity()
    user = User.query.first()  # Simulate getting the logged-in user
    
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})


@app.route('/api/users/search', methods=['GET'])
def search_users():
    """
    Search users by username
    ---
    tags:
      - Users
    summary: Find users by a partial username
    parameters:
      - name: query
        in: query
        type: string
        required: true
        description: Part of the username to search for
        example: john
    responses:
      200:
        description: List of matching users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              username:
                type: string
                example: johndoe
              email:
                type: string
                example: johndoe@example.com
    """
    query = request.args.get('query', '')
    
    users = User.query.filter(User.username.ilike(f"%{query}%")).all()
    
    return jsonify([
        {'id': user.id, 'username': user.username, 'email': user.email} for user in users
    ])

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Get all users with pagination
    ---
    tags:
      - Users
    summary: Retrieve a list of users
    parameters:
      - name: page
        in: query
        type: integer
        required: false
        description: The page number (default is 1)
        example: 1
      - name: limit
        in: query
        type: integer
        required: false
        description: The number of users per page (default is 10)
        example: 10
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              username:
                type: string
                example: johndoe
              email:
                type: string
                example: johndoe@example.com
    """
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    users = User.query.paginate(page=page, per_page=limit, error_out=False)
    
    return jsonify([
        # {'id': user.id, 'username': user.username, 'email': user.email} 
        user for user in users.items
    ])
