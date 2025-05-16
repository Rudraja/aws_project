import requests

def get_instance_metadata():
    base_url = "http://169.254.169.254/latest/meta-data/"
    metadata_items = ['instance-id', 'instance-type', 'ami-id', 'public-ipv4', 'placement/availability-zone']
    metadata = {}

    for item in metadata_items:
        url = base_url + item
        response = requests.get(url)
        if response.status_code == 200:
            metadata[item] = response.text
        else:
            metadata[item] = 'Unavailable'

    return metadata

if __name__ == "__main__":
    data = get_instance_metadata()
    for key, value in data.items():
        print(f"{key}: {value}")
