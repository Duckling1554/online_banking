# online_banking
The Conceptual Model of the Bank:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Conceptual%20Model.png)

The Logical Model of the Bank:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Logical%20Model.png)

The Physical Model of the Bank:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Physical%20Model.png)

## Data pipeline 
![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Data%20Pipeline.png)

#### Pipeline stages:
- taking raw data from excel
- making MDM and data preparation using Apache Spark
- creating ML clasterization model
- pushing data to PostgreSQL
- making dashboards using Redash

#### Stages 1,2. Raw data extraction, Creating MDM

Apache Spark Session is launched, some tables, such as CUSTOMER comes from several sources, it is necessary to create <b>MDM logic</b> to union tables into one:
1. Range data sources by their credibility. In case of customer, we had two sources:
- branches_customers
- online_banking customers
branches_customers is more reliable source that online banking
2. Data unioning by reliability. If there are rows in both sources related to one person, row, that stores in more reliable source will be left.
3. Removing duplicates
Scheme of MDM from different sources
![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/image.png)



#### Stage 3. ML model creation
<b>KMeans</b> technique was used to claster the data.
Stages of ML pipeline:
1. Data preprocessing:
- data collection
- feature selection
- additional feature creation
- feature scaling
- one-hot encoding
2. Model selection
3. Making predictions
4. Creating data frame with clusters

Features, used for clasterization:
![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Train%20features.png)
#### Stage 4. Data loading to PostgreSQL
Then, the Data Warehouse was initiated with the following DDL scripts:
https://github.com/Duckling1554/online_banking/blob/main/BD/Bank_DDL.sql
For instance, 

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/DDL%20Example.png)

The result of it was a working database:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/List%20of%20Tables.png)

Then the Data was generated:
https://github.com/Duckling1554/online_banking/blob/main/BD/Bank_Data.xlsx

The example of it uploaded to the database:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Data%20Example.png)

The Database: https://github.com/Duckling1554/online_banking/blob/main/BD/dump-Bank-202306170139

#### Stage 5. Data reporting and dashboarding
It was decided to create two analytical reports, valuable for the bank:
1. The list of all the digital footprints for each agreement basse on the customer's actions. For example, if a customer has visited an office and then opened a contract, probably, the reason for the new contract was exactly this visit, so that, itt would be interesting for a bank to know these footprints.
The formation script for it: https://github.com/Duckling1554/online_banking/blob/main/BD/Bank_digital_footprints.sql

The example of resulting analytical Data Mart:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Digital%20Footprints%20Example.png)

2. The channel where the contract was most probable attracted. In our case, it is the first digital foootprint for each contract.
The formation script for it: https://github.com/Duckling1554/online_banking/blob/main/BD/Bank_channel.sql

The example of resulting analytical Data Mart:

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/Channels%20Example.png)


