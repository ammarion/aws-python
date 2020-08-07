import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

# change below this line only 

kwargs = {"Text": "I am Ammar Alim",
          "SourceLanguageCode": "en",
          "TargetLanguageCode": "ar"
}

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()
