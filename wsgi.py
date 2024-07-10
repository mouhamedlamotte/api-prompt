from app import app


from constant import DEBUG

if __name__ == "__main__":
    if DEBUG :
        print("Running in debug mode")
        app.run(debug=DEBUG)
    else :
        print("Running in production mode")
        from waitress import serve
        serve(app, host="0.0.0.0", port=5000)