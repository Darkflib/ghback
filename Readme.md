# Set me up

I assume you are on a Linux or Mac box as I have no fscking clue how to do this on Windows.

1. Clone the repo

```bash
git clone https://github.com/darkflib/ghback.git
```

2. Install the dependencies

```bash
cd stars

python3 -m venv venv   # Create a virtual environment

source venv/bin/activate # Activate the virtual environment

pip install -r requirements.txt  # Install the dependencies
```

3. Setup the .env file

```bash
cp .env.example .env
```

Edit the .env file and set the values for the environment variables.

4. Run the app

```bash
python ghback.py
```

You should now be the proud owner of stars backup in json format.


