import os
from brownie import network
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json


def publish_collectibles():
    number_of_collectibles = 3
    print(f"You have created {number_of_collectibles} collectibles!")
    for token_id in range(number_of_collectibles):
        metadata_file_name = f"./metadata/{token_id}.json"
        collectible_metadata = metadata_template
        print(metadata_file_name)
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = "DOG_" + str(token_id)
            collectible_metadata["description"] = f"A nice dog to be adopted!"
            image_path = f"./img/{token_id}.png"
            image_uri = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)  # we dump the metadata in the json file
            upload_to_ipfs(metadata_file_name)


# upload any file to ipfs
def upload_to_ipfs(filepath):
    # open as binary
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        # upload stuff ...
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]  # ./img/0.png" => "0.png"
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
