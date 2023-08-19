#!/usr/bin/python3

import os
import json
import sys
#import dotenv

def aura_creds(dotenv_file):
    from dotenv import load_dotenv

    load_dotenv(dotenv_file)

    credentials = {}
    credentials['uri'] = os.getenv("NEO4J_URI")
    credentials['user'] = os.getenv("NEO4J_USERNAME")
    credentials['password'] = os.getenv("NEO4J_PASSWORD")
    credentials['instance_name'] = os.getenv("AURA_INSTANCENAME")

    return credentials

def json_connections(aura_creds):
    json_creds = {}
    json_creds['server_url'] = aura_creds['uri']
    json_creds['database'] = 'neo4j' 
    json_creds['auth_type'] = 'basic' 
    json_creds['username'] = aura_creds['user']
    json_creds['pwd'] = aura_creds['password']

    return json.dumps(json_creds, indent=4)

if __name__ == '__main__':
    # Define command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--aura-creds', help="Path to Neo4j Aura credentials file in dotenv format")
    parser.add_argument('-j', '--output-json', help="Output credentials into a JSON connections file")
    args = parser.parse_args()


    if args.aura_creds:
        neo4j_cxn = args.aura_creds
        print('neo4j_cxn:', neo4j_cxn)
        credentials = aura_creds(neo4j_cxn)

        print('aura credentials:')
        print(credentials)

        if args.output_json:
            outfile = args.output_json
            json_creds = json_connections(credentials)
            print('type(json_creds):', type(json_creds))
            print('json_creds:', json_creds)
            f = open(outfile, "w")
            f.write(json_creds)
            f.close()
