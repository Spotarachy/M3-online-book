from website import create_APP

APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)
