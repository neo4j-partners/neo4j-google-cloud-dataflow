# neo4j-google-cloud-dataflow
Tutorial and resources for setting up Google Cloud Dataflow with Neo4j and BigQuery

# Overview
In this tutorial, you will learn how to set up Google Cloud Dataflow to extract, transform, and load data from Google BigQuery into a Neo4j graph database instance.

## Preparation
In order complete this lab you will need a Google Cloud Platform account with permission and access to deploy the following services:

1. Neo4j Aura: https://console.cloud.google.com/marketplace/product/endpoints/prod.n4gcp.neo4j.io
2. Cloud Storage: https://console.cloud.google.com/storage/
3. Dataflow: https://console.cloud.google.com/dataflow/
4. BigQuery: https://console.cloud.google.com/bigquery

## Datasets
There are some sample templates and demo datasets available in the [datasets directory](datasets/) of this repository.

In this example we will use the [London public transport network](datasets/csv_files/london_transport/) as our test dataset.

This is a cleaned up version of data downloaded from Transport for London represeting various stations in London and the connections between them. 

# Setup

## Deploy your Neo4j Instance

For this lab, we recommend deploying an instance of Aura from Google Cloud Platform. The links below will show you how to deploy an instance of AuraDS from Google Cloud Marketplace, however for this lab you can also deploy AuraDB Free. 

This [tutorial](https://github.com/neo4j-partners/hands-on-lab-neo4j-and-vertex-ai/tree/main/Lab%201%20-%20Deploy%20Neo4j#lab-1---deploy-neo4j) and [this video](https://youtu.be/27PMDtlSP4w) will guide you through the necessary steps. 


## Set up your Google Cloud project

1. [Select or create a Google Cloud project](https://console.cloud.google.com/cloud-resource-manager). When you first create an account, you get a $300 free credit towards your compute/storage costs.

1. [Make sure that billing is enabled for your project](https://cloud.google.com/billing/docs/how-to/modify-project).

1. [Enable the Dataflow API](https://console.cloud.google.com/apis/library/dataflow.googleapis.com).

1. [Enable the BigQuery API](https://console.cloud.google.com/apis/library/bigquery.googleapis.com).

1. If you are running this notebook locally, you will need to install the [Cloud SDK](https://cloud.google.com/sdk).

1. Enter your project ID in the cell below. Then run the cell to make sure the
Cloud SDK uses the right project for all the commands in this notebook.

## Configure and Deploy a Dataflow Job

The Google Cloud to Neo4j Dataflow template currently supports two types of sources: BigQuery and Google Cloud Storage.

The configuration and deployment is mostly the same regardless of which data sources are used. There are, however, a few differences that need to be taken into account in regards to data preparation and job specification configuration. 

The following guides will walk you through the process of each:

1. [Loading data from BigQuery to Neo4j](01-bigquery_to_neo4j/README.md)

2. [Loading data from Google Cloud Storage into Neo4j](02-cloud_storage_to_neo4j/README.md)

At the end of this tutorial you will have a working graph of the London transit network loaded into an instance of Neo4j.

In a future tutorial we will explore the graph further using graph algorithms, analytics, and generative AI. 