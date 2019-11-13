# webcaptioner-stream

A way to stream caption requests from Web Captioner to your terminal.
A really rough POC!

## Environment Set Up

To get started, set up a virtual environment with Python:

    pip install virtualenv [--user (optional)]

    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Once you are in the virtual environment (shell should be prefaced with `(.venv)`)
run `python3 stream.py` to start a Flask server.

## Generating Keypairs

Web Captioner forces HTTPS by default, so Chrome will by default block
all requests to a standard Flask server because it's not running HTTPS!
No worries, as with a certificate and key we can stand up an HTTPS server.

To generate a private key and certificate, use the following command
and follow the prompts:

    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

## Future Plans

[ ] Dockerize app!