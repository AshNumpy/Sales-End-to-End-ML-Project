CREATE TYPE "Order_STATUS" AS ENUM (
  'Shipped',
  'Cancelled',
  'Resolved',
  'On Hold',
  'In Process',
  'Disputed'
);

CREATE TYPE "Order_DEALSIZE" AS ENUM (
  'Small',
  'Medium',
  'Large'
);

CREATE TABLE "Customers" (
  "ID" bigint PRIMARY KEY,
  "CUSTOMERNAME" varchar,
  "PHONE" varchar,
  "ADDRESSLINE1" varchar,
  "ADDRESSLINE2" varchar,
  "CITY" varchar,
  "STATE" varchar,
  "POSTALCODE" bigint,
  "COUNTRY" varchar,
  "TERRITORY" varchar,
  "CONTACTLASTNAME" varchar,
  "CONTACTFIRSTNAME" varchar
);

CREATE TABLE "Products" (
  "PRODUCTCODE" varchar PRIMARY KEY,
  "PRODUCTLINE" varchar,
  "MSRP" float
);

CREATE TABLE "Orders" (
  "ORDERNUMBER" bigint PRIMARY KEY,
  "ORDERDATE" datetime,
  "STATUS" Order_STATUS,
  "QTR_ID" varchar,
  "MONTH_ID" varchar,
  "YEAR_ID" varchar,
  "DEALSIZE" Order_DEALSIZE,
  "CUSTOMERNAME" varchar,
  "CUSTOMER_ID" bigint
);

CREATE TABLE "Order_Items" (
  "ORDERNUMBER" bigint,
  "PRODUCTCODE" varchar,
  "QUANTITYORDERED" int,
  "PRICEEACH" float,
  "ORDERLINENUMBER" bigint,
  "SALES" float,
  PRIMARY KEY ("ORDERNUMBER", "PRODUCTCODE")
);

COMMENT ON COLUMN "Products"."MSRP" IS 'Ürünün perakende satış fiyatı';

COMMENT ON COLUMN "Orders"."ORDERDATE" IS 'MM/DD/YYYY HH:MM';

ALTER TABLE "Orders" ADD FOREIGN KEY ("CUSTOMER_ID") REFERENCES "Customers" ("ID");

ALTER TABLE "Order_Items" ADD FOREIGN KEY ("ORDERNUMBER") REFERENCES "Orders" ("ORDERNUMBER");

ALTER TABLE "Order_Items" ADD FOREIGN KEY ("PRODUCTCODE") REFERENCES "Products" ("PRODUCTCODE");
