import boto3

def translate_text(text, source_language_code, target_language_code): # we define the positional
    # arguments in the () 
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # we remove the hardcoded values
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('الشبكة العالمية انترنيت ويونيكود، حيث ستتم، على الصعيدين الدولي والمحلي على حد','ar','en') # we provide the value for the args when we call
    # the function in the correct position

if __name__=="__main__":
    main()
