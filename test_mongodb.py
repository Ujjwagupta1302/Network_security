
# Below is the code to check whether my mongoDB is working correctly or not. 
from pymongo.mongo_client import MongoClient

# my uri details are imp so they should not be left as it is. Hence we will use the .env file

uri = "mongodb+srv://<write own username>:<write own password>@cluster0.igy6g4r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)