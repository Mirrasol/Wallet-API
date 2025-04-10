# Wallet API: testing assignment.

A compact webservice to browse wallets and withdraw/deposit funds into them.

## 1) Features

  - check the current balance of a wallet using its UUID;

  - withdraw or deposit a specified amount into a wallet.

## 2) Installation

1) Download the package from GitHub:

`git clone git@github.com:Mirrasol/Wallet-API.git`

2) Create .env file that contains your secret keys and database settings (refer to .env_example)

2) Run the project in a Docker container:

`docker compose up --build`

3) Or install using pip:

`pip install -r requirements.txt`

4) Afterwards, apply initial migration.
