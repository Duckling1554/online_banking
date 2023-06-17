# online_banking
The Conceptual Model of the Bank:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Conceptual%20Model.png)

The Logical Model of the Bank:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Logical%20Model.png)

The Physical Model of the Bank:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Physical%20Model.png)

Then, the Data Warehouse was initiated with the following DDL scripts:
https://github.com/Duckling1554/online_banking/blob/main/Bank_DDL.sql

For instance, 

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/DDL%20Example.png)

The result of it was a working database:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/List%20of%20Tables.png)

Then the Data was generated:
https://github.com/Duckling1554/online_banking/blob/main/Bank_Data.xlsx

The example of it uploaded to the database:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Data%20Example.png)

It was decided to create two analytical reports, valuable for the bank:
1. The list of all the digital footprints for each agreement basse on the customer's actions. For example, if a customer has visited an office and then opened a contract, probably, the reason for the new contract was exactly this visit, so that, itt would be interesting for a bank to know these footprints.
The formation script for it: https://github.com/Duckling1554/online_banking/blob/main/Bank_digital_footprints.sql

The example of resulting analytical Data Mart:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Digital%20Footprints%20Example.png)

2. The channel where the contract was most probable attracted. In our case, it is the first digital foootprint for each contract.
The formation script for it: https://github.com/Duckling1554/online_banking/blob/main/Bank_channel.sql

The example of resulting analytical Data Mart:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Channels%20Example.png)


