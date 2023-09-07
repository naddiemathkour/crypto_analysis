# kraken_api
Project Scope:
- Automate 2023-2024 Crypto market cycle DCA purchasing
    - Buy relevant tokens on a daily/bi-weekly basis (depending on fees)
- Create a dashboard view of portfolio movement
    - USD spent vs portfolio value
    - Weighted single dollar value
    - Token vs Token ROI (see which token did best)
- Add text notifications that update me on a regular basis with purchase history and portfolio value
    - Purchases made in most recent buy batch
    - Total value of portfolio
    - Total value of money invested
    - ROI percentage

Potential stack for full project:

Back End:
Code: Python
Database: Postgress

Front End:
Framework: Angular (TypeScript + Node)


To do:
    - Create a fetch_data() function in endpoints.executions
        - Build psql statement to dynamically fetch information
        - Convert fetched information into json object
            - To be sent to front end for graphing
    - Integrate front end of project
    - Determine meaningful graphs to display
    - Determine method of creating PostgreSQL fetch statements
        - Check boxes?