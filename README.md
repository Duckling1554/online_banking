# online_banking
## Stages of the project:
1. Chosen a company type and developed its business model
2. Created conceptual, logical and physical data models for the company
3. Created a database, generated data and fiiled it in
4. Created role-to-asset CRUD matrix
5. Developed master-data standards
6. Implemented BI platform
7. Developed analytical ML solution

#### Roles:
1. System Architect - Alina Subbotina
2. Data Engineer - Nikita Senyatkin
3. Business Analyst - Danila Yatsenko
4. BI Analyst - Liubov Levchenko

#### Business case description.
Our object of interest is a newly established online bank that serves both individual and corporate clients. With its simplified organizational structure and lower levels of bureaucracy, the bank aims to deliver a seamless, user-friendly experience that caters to the modern customer's needs.
The bank's range of products is extensive, covering 24 types of deposit accounts, 16 kinds of debit cards, credit cards, cash credits, mortgage loans, auto loans, insurance programs, and currency exchange services. Given that online banking is the main operational pathway, digital customer interactions and transactions form the crux of the bank's data collection.
Opportunities:
The innovative approach that the bank aims to adopt revolves around customer clustering. By implementing a robust system of customer segmentation based on collected data, the bank can unlock a multitude of benefits:
1. Personalized Offerings: Clustering customers based on their banking behavior, preferences, and needs can enable the bank to offer tailored products and services. This level of personalization can greatly enhance customer satisfaction, leading to increased customer retention and loyalty.
2. Effective Marketing: With improved customer segmentation, the bank can design and implement targeted marketing campaigns. This can result in a higher return on marketing investment, as promotional efforts would be directed at the right audience with the right offerings.
3. Risk Management: By identifying distinct customer clusters, the bank can more effectively assess and manage risk. For example, customers who frequently engage in high-value transactions may be categorized as higher-risk, prompting closer monitoring or enhanced security measures.
4. Improved Customer Service: Customer segmentation can also aid in providing differentiated customer service. The bank can provide dedicated service representatives or specialized service channels for different customer clusters.
5. Product and Service Development: Insights from customer clustering can inform the development of new products and services. By understanding the needs and preferences of each customer segment, the bank can design products that directly cater to these requirements.
To make these benefits a reality, the bank must prioritize data management and analytical capabilities. It must ensure that data collection is robust and secure, and invest in analytical tools that can perform sophisticated customer segmentation. With such investments, the online bank can fully leverage its digital platform to deliver exceptional value to its customers, setting itself apart in the competitive banking landscape.

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/3.jpg)

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/1.jpg)

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/2.jpg)

![Иллюстрация к проекту](https://github.com/Duckling1554/online_banking/blob/main/pictures/4.png)

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

Then, Spark were used to fill the preprocessed data inside of the Database

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


