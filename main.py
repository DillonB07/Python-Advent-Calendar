from website import create_app


if __name__ == '__main__':
    app = create_app()
    # file deepcode ignore RunWithDebugTrue: <Developing>
    app.run(host='0.0.0.0', port=8080, debug=True)
