import ngrok

def connect_ngrok():
    forwarder = ngrok.forward("localhost:8085", authtoken_from_env=True, domain="wisdom-deacon-mounted.ngrok-free.dev")
    print(f"Available at: {forwarder.url()}")

connect_ngrok()