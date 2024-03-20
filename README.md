##Datasets and Setup Scripts

This project can be set up with docker locally, the image already has the processed data necessary to run the web app locally. 

The author graph data can be found in authorGraphMini.json, and it can be assumed that the keyword graph data is very similar in structure, with the difference being the key used(the keyphrase itself). This dataset is too large to upload but can be viewed within the image if needed. 



## Setup Instructions

1. **Install Docker**

    ```bash
    sudo apt install docker.io
    ```

2. **Clone the Docker image locally**

    ```bash
    docker pull adirx/datavizgraphapp
    ```

3. **Run the Docker image locally**

    ```bash
    sudo docker run -p 3000:3000 adirx/datavizgraphapp:latest
    ```

4. **Open the web app locally by entering the following URL in your browser**

    [http://localhost:3000/](http://localhost:3000/)
