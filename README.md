## Install Dependencies

In your Terminal, type:

    pip install -r requirements.txt

Make sure you have Anaconda or Miniconda installed and run the following:

    conda install -c conda-forge cfgrib

## API Documentation

### Base URL

The base URL for all the API endpoints is `https://api.terraqi.com/`

### Endpoints

#### GET /

This endpoint simply returns a welcome message. Use it to test that you have successfully connected to the TerraQi API.

**Parameters:**
None

**Example request:**

```http
GET https://api.terraqi.com/