from ZTRequests import ZTRequests
from TrustDataBuilder import TrustDataBuilder
from ClientAPIConfig import ClientAPIConfig

config = ClientAPIConfig()

# Function to send a request to the edge node
def TestRequests(session, data):
    TrustDataBuilder.sessionToken = session

    # For this to work you will have to set this ip to the ip of the edge node
    print("Posting...")
    response = ZTRequests.post(f"http://192.168.0.212:5005/testPost", json=data)

    print(response.text)

def main():
    session = input("Enter the session you want to spoof:")
    data = {"Test": "Spoofed session test"}
    TestRequests(session, data)

if __name__ == "__main__":
    main()

