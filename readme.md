# Crypto Asset Tracker

The aim of this project is to create a tool which will get all your assets from your favorite exchanges and displays them.
The project uses Python3 for now.

---

**Support:**

-   [x] Binance
    -   [x] Retrieve all assets on spot wallet and displays to console
    -   [ ] Other wallets (margin, etc...)

---

### Use :

1. Clone repository
   `git clone https://github.com/Hugues862/CryptoAssetTracker.git`
2. Create a .env file inside cloned repo

    1. Add api keys (be sure to enable only viewing with the api keys for security)
        ```
        binance_api_key='insertkey'
        bianance_api_secret='insertsecret'
        ```

3. Install requirements.txt using :
    - `pip install -r requirements.txt`
5. Run main.py
    - `cd parent/cryptoassettracker`
    - `python main.py`
