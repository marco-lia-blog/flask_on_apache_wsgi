from application import create_app

# this var needs to be called exactly application or mod_wsgi won't work with it.
application = create_app()

#if __name__ == "__main__":
#    app.run(host='0.0.0.0')
