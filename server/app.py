from server.modules.app.app import Application


app = Application().create_app()

if __name__ == '__main__':
    app.run(debug=True)
