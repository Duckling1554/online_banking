create table employee (
	EMPLOYEE_ID int,
	EFF_TO_DTTM timestamp,
	BIRTH_DATE date,
	LEAVE_DATE date,
	HIRE_DATE date,
	MANAGER_ID int,
	OFFICE_ID int,
	DEPARTMENT_NAME text,
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	POSITION_NAME text,
	LAST_NAME text,
	FIRST_NAME text,
	primary key (EMPLOYEE_ID, EFF_TO_DTTM)
);

create table account_balance (
	ACCOUNT_ID int,
	EFF_TO_DTTM timestamp,
	BALANCE_AMT decimal(24,4),
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	primary key (ACCOUNT_ID, EFF_TO_DTTM)
);

create table account (
	ACCOUNT_ID int,
	EFF_TO_DTTM timestamp,
	ACCOUNT_NUM text,
	CUSTOMER_ID int,
	OPEN_DATE date,
	CLOSE_DATE date,
	ACCOUNT_STATUS text,
	ACCOUNT_TYPE text,
	OFFICE_ID int,
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	primary key (ACCOUNT_ID, EFF_TO_DTTM)
);

create table insurance (
	INSURANCE_ID int,
	EFF_FROM_DTTM timestamp,
	LOAN_ID int,
	CONTRACT_TYPE text,
	CUSTOMER_ID int,
	INSURANCE_AMT decimal(24,4),
	OPEN_DATE date,
	CLOSE_PLAN_DATE date,
	CLOSE_FACT_DATE date,
	INSURANCE_PROGRAM text,
	INSURANCE_COMPANY text,
	OFFICE_ID int,
	EFF_TO_DTTM timestamp,
	DELETED_FLG int,
	primary key (INSURANCE_ID, EFF_TO_DTTM)
);

create table delinquency (
	LOAN_ID int,
	EFF_TO_DTTM timestamp,
	DELINQUENCY_START_DATE date,
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	primary key (LOAN_ID, EFF_TO_DTTM)
);

create table deposit_contract (
	CONTRACT_ID int,
	EFF_TO_DTTM timestamp,
	CONTRACT_TYPE text,
	CONTRACT_NUM text,
	OPEN_DATE date,
	CLOSE_PLAN_DATE date,
	CLOSE_FACT_DATE date,
	DEPOSIT_TYPE text,
	DEPOSIT_PERIOD int,
	ACCOUNT_ID int,
	INITIAL_BALANCE_AMT decimal(24,4),
	DEPOSIT_RATE decimal(24,4),
	CUSTOMER_ID int,
	OFFICE_ID int,
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	primary key (CONTRACT_ID, EFF_TO_DTTM)
);

create table office (
	OFFICE_ID int,
	EFF_TO_DTTM timestamp,
	OFFICE_NAME text,
	BRANCH_NAME text,
	REGION_NAME text,
	ADDRESS_NAME text,
	CITY_NAME text,
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	primary key (OFFICE_ID, EFF_TO_DTTM)
);

create table loan (
	LOAN_ID int,
	EFF_TO_DTTM timestamp,
	APPLICATION_ID int,
	CLOSE_FACT_DATE date,
	CLOSE_PLAN_DATE date,
	OFFICE_ID int,
	CONTRACT_PERIOD int,
	CONTRACT_STATUS text,
	CONTRACT_TYPE text,
	CREDIT_CLASS text,
	CUSTOMER_ID int,
	DELETED_FLG int,
	INTEREST_RATE decimal(24,4),
	LOAN_AMT decimal(24,4),
	OPEN_DATE date,
	EFF_FROM_DTTM timestamp,
	primary key (LOAN_ID, EFF_TO_DTTM)
);

create table loan_balance (
	LOAN_ID int,
	EFF_TO_DTTM timestamp,
	BALANCE_AMT decimal(24,4),
	OVERDUE_BALANCE_AMT decimal(24,4),
	UNUSED_LIMIT_AMT decimal(24,4),
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	primary key (LOAN_ID, EFF_TO_DTTM)
);

create table application (
	APPLICATION_ID int,
	EFF_TO_DTTM timestamp,
	EFF_FROM_DTTM timestamp,
	CUSTOMER_ID int,
	APPLICATION_DATE date,
	APPLIED_AMT decimal(24,4),
	CREDIT_CLASS text,
	PRODUCT_TYPE text,
	INCREASE_LIMIT_FLG int,
	CONTRACT_PERIOD int,
	INTEREST_RATE decimal(24,4),
	DELETED_FLG int,
	SPEC_DESIGN_FLG int,
	OVERDRAFT_FLG int,
	SALARY_FLG int,
	PLAN_AGREEMENT_DATE date,
	ACCEPT_FLG int,
	REFUSE_FLG int,
	PROCESSING_FLG int,
	PAYMENT_SYSTEM_NAME text,
	primary key (APPLICATION_ID, EFF_TO_DTTM)
);

create table deposit_balance (
	CONTRACT_ID int,
	EFF_TO_DTTM timestamp,
	EFF_FROM_DTTM timestamp,
	BALANCE_AMT decimal(24,4),
	DELETED_FLG int,
	primary key (CONTRACT_ID, EFF_TO_DTTM)
);

create table customer (
	CUSTOMER_ID int,
	EFF_TO_DTTM timestamp,
	CUSTOMER_TYPE text,
	BIRTH_DATE date,
	BIRTH_PLACE text,
	FIRST_NAME text,
	LAST_NAME text,
	GENDER text,
	MARITAL_STATUS text,
	COUNTRY text,
	BLACK_LIST_FLG int,
	REGISTRATION_ADDRESS text,
	CHILDREN_CNT int,
	EDUCATION_LEVEL text,
	VIP_FLG int,
	REGISTRATION_DATE date,
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	IS_EMPLOYEE_FLG int,
	ACTUAL_ADDRESS text,
	primary key (CUSTOMER_ID, EFF_TO_DTTM)
);

create table card (
	CARD_ID int,
	EFF_TO_DTTM timestamp,
	LOAN_ID int,
	OFFICE_ID int,
	CUSTOMER_ID int,
	CARD_TYPE text,
	OPEN_DATE date,
	CLOSE_DATE date,
	OVERDRAFT_FLG int,
	SALARY_FLG int,
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	PAYMENT_SYSTEM_NAME text,
	primary key (CARD_ID, EFF_TO_DTTM)
);

create table internet_activity (
	ACTIVITY_ID int,
	EFF_TO_DTTM timestamp,
	EFF_FROM_DTTM timestamp,
	CUSTOMER_ID int,
	ACTIVITY_DTTM timestamp,
	"ACTION" text,
	DELETED_FLG int,
	"RESULT" text,
	primary key (ACTIVITY_ID, EFF_TO_DTTM)
);

create table terminal (
	TERMINAL_ID int,
	EFF_TO_DTTM timestamp,
	COUNTRY_NAME text,
	CITY_NAME text,
	LOCATION_NAME text,
	OWNER_NAME text,
	"TYPE" text,
	EFF_FROM_DTTM timestamp,
	DELETED_FLG int,
	primary key (TERMINAL_ID, EFF_TO_DTTM)
);

create table "transaction" (
	TRANSACTION_ID int,
	TRANSACTION_DTTM timestamp,
	CARD_ID int,
	CUSTOMER_ID int,
	TRANSACTION_AMT decimal(24,4),
	FEE_AMT decimal(24,4),
	STATUS text,
	MCC_NAME text,
	TERMINAL_ID int,
	WRONG_PIN_FLG int,
	WRONG_CVV_FLG int,
	primary key (TRANSACTION_ID)
);

create table calls (
	CALL_ID int,
	EFF_TO_DTTM timestamp,
	EFF_FROM_DTTM timestamp,
	CUSTOMER_ID int,
	CALL_DTTM timestamp,
	CONTRACT_TYPE text,
	INCOM_OUTCOM text,
	CALL_RESULT text,
	DELETED_FLG int,
	OFFER_PRODUCT text,
	primary key (CALL_ID, EFF_TO_DTTM)
);

create table office_visits (
	VISIT_ID int,
	EFF_TO_DTTM timestamp,
	EFF_FROM_DTTM timestamp,
	CUSTOMER_ID int,
	VISIT_DTTM timestamp,
	OFFICE_ID int,
	DELETED_FLG int,
	VISIT_AIM text,
	primary key (VISIT_ID, EFF_TO_DTTM)
);




