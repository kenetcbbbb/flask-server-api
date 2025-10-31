from flask import Flask, request, jsonify
import git
import os

app = Flask(__name__)

# Пример данных (вместо базы данных)
data = {"message": "Hello, world!"}

# --- GET ---
@app.route("/get", methods=["GET"])
def get_data():
    return jsonify(data), 200

# --- POST ---
@app.route("/post", methods=["POST"])
def post_data():
    new_data = request.json
    data.update(new_data)
    return jsonify({"status": "added", "data": data}), 201

# --- PUT ---
@app.route("/put", methods=["PUT"])
def put_data():
    new_data = request.json
    data.clear()
    data.update(new_data)
    return jsonify({"status": "replaced", "data": data}), 200

# --- PATCH ---
@app.route("/patch", methods=["PATCH"])
def patch_data():
    patch_data = request.json
    data.update(patch_data)
    return jsonify({"status": "patched", "data": data}), 200

# --- DELETE ---
@app.route("/delete", methods=["DELETE"])
def delete_data():
    data.clear()
    return jsonify({"status": "deleted"}), 200


# --- Git пример ---
@app.route("/git/status", methods=["GET"])
def git_status():
    try:
        repo = git.Repo(".")
        return jsonify({"branch": repo.active_branch.name, "is_dirty": repo.is_dirty()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)