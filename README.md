# neo4j-google-cloud-dataflow
Tutorial and resources for setting up Google Cloud Dataflow with Neo4j and BigQuery

# Overview
In this tutorial, you will learn how to set up Google Cloud Dataflow to extract, transform, and load data from Google BigQuery into a Neo4j graph database instance.

## Preparation
In order complete this lab you will need the following you will need a Google Cloud Platform account with permission and access to deploy the following services:

1. Neo4j Aura: https://console.cloud.google.com/marketplace/product/endpoints/prod.n4gcp.neo4j.io
2. Cloud Storage: https://console.cloud.google.com/storage/
3. Dataflow: https://console.cloud.google.com/dataflow/
4. BigQuery: https://console.cloud.google.com/bigquery

If you don't have access to Neo4j Aura you can alternatively use any running instance of Neo4j as long as it is accessible from the internet and you can provide the authentication credentials.

## Dataset
For this lab we will use the [Northwind database](https://github.com/Microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs)

The Northwind database is a sample database originally created by Microsoft and used as the basis for tutorials and demos of their own products although it has been commonly used by many in the industry for decades and used for similar purposes. 

The Northwind database contains the sales data for a fictitious company called “Northwind Traders,” which imports and exports specialty foods from around the world. 

# Setup

## Deploy your Neo4j Instance

If you haven't done so already you will need to deploy an instance of Neo4j. This can be running anywhere in the world as long as it is accessible from the Internet. 

For this lab, however, we recommend deploying an instance of Aura from Google Cloud Platform. The links below will show you how to deploy an instance of AuraDS from Google Cloud Marketplace, however for this lab you can also deploy AuraDB Free. 

This [tutorial](https://github.com/neo4j-partners/hands-on-lab-neo4j-and-vertex-ai/tree/main/Lab%201%20-%20Deploy%20Neo4j#lab-1---deploy-neo4j) and [this video](https://youtu.be/27PMDtlSP4w) will guide you through the necessary steps. 


## Set up your Google Cloud project

1. [Select or create a Google Cloud project](https://console.cloud.google.com/cloud-resource-manager). When you first create an account, you get a $300 free credit towards your compute/storage costs.

1. [Make sure that billing is enabled for your project](https://cloud.google.com/billing/docs/how-to/modify-project).

1. [Enable the Dataflow API](https://console.cloud.google.com/apis/library/dataflow.googleapis.com).

1. [Enable the BigQuery API](https://console.cloud.google.com/apis/library/bigquery.googleapis.com).

1. If you are running this notebook locally, you will need to install the [Cloud SDK](https://cloud.google.com/sdk).

1. Enter your project ID in the cell below. Then run the cell to make sure the
Cloud SDK uses the right project for all the commands in this notebook.

**Note**: Jupyter runs lines prefixed with `!` as shell commands, and it interpolates Python variables prefixed with `$` into these commands.

## Prepare your template files

[This notebook]("neo4j_dataflow_bigquery.ipynb") will guide you through the steps of setting up a Google Cloud Storage bucket with the necessary template files uploaded to them. 

## Set up your Dataflow job

Once your template files are uploaded to the storage buckets you can continue on to configure and set up your Dataflow job. 

Detailed steps with screenshots coming soon

1. Go to the Dataflow console
2. Select "Create New Job"
3. Give your job a name and select the region
4. Click on the dropdown menu and type "neo4j"
5. Select the "Google Cloud to Neo4j" template
6. The required fields will appear
    a. Browse to your storage bucket and select your job spec template
    b. Browse to your storage bucket and select your Neo4j connection template
    c. In the Optional "JSON" field just enter empty curly brackets "{}"
7. Click "Run Job" and now wait for the job to finish (~5-10 minutes for this demo)